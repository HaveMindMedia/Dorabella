"""
Dorabella Waltz — Polyphonic MIDI Generator
Creates a full waltz arrangement from the cipher melody:
  - Right hand: the decoded cipher melody
  - Left hand: waltz accompaniment (bass + chord pattern)
Outputs MIDI at both 108 BPM and 87 BPM (the cipher number).
"""
from midiutil import MIDIFile
import os

OUTPUT_DIR = os.path.expanduser("~/Downloads")

# ── Cipher Data ──────────────────────────────────────────────────────────
# The 87 cipher values from Elgar's 1897 Dorabella Cipher
S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21,22,21,6,5,17]
S1 = [18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,16,7,19,17,15,3]
S2 = [21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,17,6,2,14,6,17,7,2,3,21,2]
FLAT = S0 + S1 + S2  # 87 values

# Pitch mapping: value // 3 -> scale degree in G major
# 0=G3, 1=A3, 2=B3, 3=C4, 4=D4, 5=E4, 6=F#4, 7=G4
G_MAJOR_SCALE = [55, 57, 59, 60, 62, 64, 66, 67]  # MIDI note numbers

# Duration mapping: value % 3
# 0=half (2 beats), 1=quarter (1 beat), 2=eighth (0.5 beats)
DUR_MAP = {0: 2.0, 1: 1.0, 2: 0.5}

def get_pitch(val):
    return G_MAJOR_SCALE[val // 3]

def get_dur(val):
    return DUR_MAP[val % 3]

# ── Harmony Analysis ─────────────────────────────────────────────────────
# G major chords (MIDI note numbers for left hand)
CHORDS = {
    'G':  {'bass': 43, 'chord': [55, 59]},     # G2 bass, G3+B3
    'Am': {'bass': 45, 'chord': [57, 60]},     # A2 bass, A3+C4
    'Bm': {'bass': 47, 'chord': [59, 62]},     # B2 bass, B3+D4
    'C':  {'bass': 48, 'chord': [60, 64]},     # C3 bass, C4+E4
    'D':  {'bass': 50, 'chord': [62, 66]},     # D3 bass, D4+F#4
    'Em': {'bass': 52, 'chord': [55, 64]},     # E3 bass, G3+E4 (inv)
    'D7': {'bass': 50, 'chord': [60, 66]},     # D3 bass, C4+F#4
}

def analyze_bar_harmony(bar_pitches):
    """Determine the best chord for a bar based on melody notes."""
    pitch_set = set(p % 12 for p in bar_pitches)  # pitch classes

    # Score each chord by how many melody notes are chord tones
    best_chord = 'G'
    best_score = -1

    chord_pcs = {
        'G':  {7, 11, 2},   # G B D
        'Am': {9, 0, 4},    # A C E
        'Bm': {11, 2, 6},   # B D F#
        'C':  {0, 4, 7},    # C E G
        'D':  {2, 6, 9},    # D F# A
        'Em': {4, 7, 11},   # E G B
        'D7': {2, 6, 9, 0}, # D F# A C
    }

    for name, pcs in chord_pcs.items():
        score = len(pitch_set & pcs)
        # Bonus for G on first/last bar
        if score > best_score:
            best_score = score
            best_chord = name

    return best_chord


def create_waltz_midi(tempo, filename):
    """Create a polyphonic waltz MIDI file."""
    midi = MIDIFile(2)  # 2 tracks: melody + accompaniment

    # Track 0: Melody (right hand)
    midi.addTrackName(0, 0, "Melody")
    midi.addTempo(0, 0, tempo)
    midi.addProgramChange(0, 0, 0, 0)  # Acoustic Grand Piano

    # Track 1: Accompaniment (left hand)
    midi.addTrackName(1, 0, "Accompaniment")
    midi.addTempo(1, 0, tempo)
    midi.addProgramChange(1, 1, 0, 0)  # Acoustic Grand Piano

    # ── Build melody ──
    # Group into bars of 3 notes each
    bars = []
    for i in range(0, len(FLAT), 3):
        bar_vals = FLAT[i:i+3]
        bars.append(bar_vals)

    # Write melody notes and collect bar data for harmony
    beat_pos = 0.0
    bar_data = []  # (bar_start, bar_pitches, bar_end)

    for bar_idx, bar_vals in enumerate(bars):
        bar_start = beat_pos
        bar_pitches = []
        for val in bar_vals:
            pitch = get_pitch(val)
            dur = get_dur(val)
            # Melody velocity: moderate, with slight accent on beat 1
            vel = 85
            midi.addNote(0, 0, pitch, beat_pos, dur, vel)
            bar_pitches.append(pitch)
            beat_pos += dur
        bar_data.append((bar_start, bar_pitches, beat_pos))

    # ── Build accompaniment ──
    for bar_idx, (bar_start, bar_pitches, bar_end) in enumerate(bar_data):
        chord_name = analyze_bar_harmony(bar_pitches)

        # First bar: G major, last bar: G major (tonic framing)
        if bar_idx == 0 or bar_idx == len(bar_data) - 1:
            chord_name = 'G'
        # Penultimate bar: D7 (dominant preparation)
        if bar_idx == len(bar_data) - 2:
            chord_name = 'D7'

        chord = CHORDS[chord_name]
        bar_dur = bar_end - bar_start

        # Waltz pattern: bass on beat 1, chord on beats 2 & 3
        # Scale to actual bar duration
        if bar_dur >= 2.5:
            # Full waltz pattern
            # Beat 1: bass note (duration depends on bar length)
            bass_dur = min(1.0, bar_dur / 3)
            midi.addNote(1, 1, chord['bass'], bar_start, bass_dur, 65)

            # Beat 2: chord
            chord_start = bar_start + bass_dur
            chord_dur = min(1.0, (bar_dur - bass_dur) / 2)
            for note in chord['chord']:
                midi.addNote(1, 1, note, chord_start, chord_dur, 50)

            # Beat 3: chord (lighter)
            chord2_start = chord_start + chord_dur
            chord2_dur = bar_dur - bass_dur - chord_dur
            if chord2_dur > 0.1:
                for note in chord['chord']:
                    midi.addNote(1, 1, note, chord2_start, chord2_dur, 45)
        else:
            # Short bar: just bass + one chord
            midi.addNote(1, 1, chord['bass'], bar_start, bar_dur * 0.5, 60)
            for note in chord['chord']:
                midi.addNote(1, 1, note, bar_start + bar_dur * 0.5, bar_dur * 0.5, 45)

    # Write MIDI file
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'wb') as f:
        midi.writeFile(f)
    print(f"  Created: {filepath}")
    return filepath


def main():
    print("Dorabella Waltz — Polyphonic MIDI Generator")
    print(f"Output: {OUTPUT_DIR}\n")

    # Generate at both tempos
    print("1. Waltz at 108 BPM (standard waltz tempo)")
    f1 = create_waltz_midi(108, "dorabella_waltz_polyphonic_108bpm_v1.0_03-16-2026.mid")

    print("\n2. Waltz at 87 BPM (the cipher number — 87 symbols)")
    f2 = create_waltz_midi(87, "dorabella_waltz_polyphonic_87bpm_v1.0_03-16-2026.mid")

    print("\nDone. Use FluidSynth to render to WAV:")
    print(f"  fluidsynth -ni <soundfont.sf2> {f1} -F output_108.wav -r 44100")
    print(f"  fluidsynth -ni <soundfont.sf2> {f2} -F output_87.wav -r 44100")


if __name__ == "__main__":
    main()

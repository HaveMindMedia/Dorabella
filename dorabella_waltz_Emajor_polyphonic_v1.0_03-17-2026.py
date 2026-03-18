"""
Dorabella Waltz — E Major Transposition (for Salut d'Amour comparison)
Transpose down minor 3rd: G major → E major
"""
from midiutil import MIDIFile
import os

OUTPUT_DIR = os.path.expanduser("~/Downloads/Dorabella")

# Cipher values
S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21,22,21,6,5,17]
S1 = [18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,16,7,19,17,15,3]
S2 = [21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,17,6,2,14,6,17,7,2,3,21,2]
FLAT = S0 + S1 + S2

# E major scale (transposed down minor 3rd from G major)
# G3→E3, A3→F#3, B3→G#3, C4→A3, D4→B3, E4→C#4, F#4→D#4, G4→E4
E_MAJOR_SCALE = [52, 54, 56, 57, 59, 61, 63, 64]  # MIDI: E3 F#3 G#3 A3 B3 C#4 D#4 E4

DUR_MAP = {0: 2.0, 1: 1.0, 2: 0.5}

# E major chords for accompaniment
CHORDS = {
    'E':   {'bass': 40, 'chord': [52, 56]},     # E2, E3+G#3
    'F#m': {'bass': 42, 'chord': [54, 57]},     # F#2, F#3+A3
    'G#m': {'bass': 44, 'chord': [56, 59]},     # G#2, G#3+B3
    'A':   {'bass': 45, 'chord': [57, 61]},     # A2, A3+C#4
    'B':   {'bass': 47, 'chord': [59, 63]},     # B2, B3+D#4
    'C#m': {'bass': 49, 'chord': [52, 61]},     # C#3, E3+C#4
    'B7':  {'bass': 47, 'chord': [57, 63]},     # B2, A3+D#4
}

def get_pitch(val):
    return E_MAJOR_SCALE[val // 3]

def get_dur(val):
    return DUR_MAP[val % 3]

def analyze_harmony(pitches):
    pitch_set = set(p % 12 for p in pitches)
    chord_pcs = {
        'E':   {4, 8, 11},
        'F#m': {6, 9, 1},
        'G#m': {8, 11, 3},
        'A':   {9, 1, 4},
        'B':   {11, 3, 6},
        'C#m': {1, 4, 8},
        'B7':  {11, 3, 6, 9},
    }
    best, best_s = 'E', -1
    for name, pcs in chord_pcs.items():
        s = len(pitch_set & pcs)
        if s > best_s:
            best_s = s
            best = name
    return best

def create_midi(tempo, filename):
    midi = MIDIFile(2)
    midi.addTrackName(0, 0, "Melody")
    midi.addTempo(0, 0, tempo)
    midi.addProgramChange(0, 0, 0, 0)
    midi.addTrackName(1, 0, "Accompaniment")
    midi.addTempo(1, 0, tempo)
    midi.addProgramChange(1, 1, 0, 0)

    bars = [FLAT[i:i+3] for i in range(0, len(FLAT), 3)]
    beat_pos = 0.0
    bar_data = []

    for bar_vals in bars:
        bar_start = beat_pos
        bar_pitches = []
        for val in bar_vals:
            p = get_pitch(val)
            d = get_dur(val)
            midi.addNote(0, 0, p, beat_pos, d, 85)
            bar_pitches.append(p)
            beat_pos += d
        bar_data.append((bar_start, bar_pitches, beat_pos))

    for i, (start, pitches, end) in enumerate(bar_data):
        ch = analyze_harmony(pitches)
        if i == 0 or i == len(bar_data) - 1:
            ch = 'E'
        if i == len(bar_data) - 2:
            ch = 'B7'
        c = CHORDS[ch]
        dur = end - start
        if dur >= 2.5:
            bd = min(1.0, dur / 3)
            midi.addNote(1, 1, c['bass'], start, bd, 65)
            cd = min(1.0, (dur - bd) / 2)
            for n in c['chord']:
                midi.addNote(1, 1, n, start + bd, cd, 50)
            cd2 = dur - bd - cd
            if cd2 > 0.1:
                for n in c['chord']:
                    midi.addNote(1, 1, n, start + bd + cd, cd2, 45)
        else:
            midi.addNote(1, 1, c['bass'], start, dur * 0.5, 60)
            for n in c['chord']:
                midi.addNote(1, 1, n, start + dur * 0.5, dur * 0.5, 45)

    fp = os.path.join(OUTPUT_DIR, filename)
    with open(fp, 'wb') as f:
        midi.writeFile(f)
    print(f"Created: {fp}")
    return fp

if __name__ == "__main__":
    print("Dorabella Waltz — E Major (Salut d'Amour key)\n")
    create_midi(87, "dorabella_waltz_Emajor_87bpm_v1.0_03-17-2026.mid")
    create_midi(108, "dorabella_waltz_Emajor_108bpm_v1.0_03-17-2026.mid")

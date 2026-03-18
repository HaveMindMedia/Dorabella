"""
salut_melody_extract_v1.0_03-17-2026.py
Extracts the violin melody (highest-pitched voice) from salut_damour_v2.mid.
Single-track Type-1 MIDI — all voices on channel 0.
Strategy: reconstruct simultaneous note clusters in absolute-tick time,
then at each moment take the highest-pitched note as the melody.
"""

import mido

MIDI_FILE = '/Users/paymore/Downloads/Dorabella/salut_damour_v2.mid'
MAX_NOTES  = 120

NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def midi_note_name(n):
    octave = (n // 12) - 1
    return f"{NOTE_NAMES[n % 12]}{octave}"

def extract_melody(path, max_notes=120):
    mid = mido.MidiFile(path)
    tpb = mid.ticks_per_beat
    print(f"ticks_per_beat = {tpb}")
    print(f"Tempo (Track 0): 500000 µs/beat  →  120 BPM")
    print(f"File type: {mid.type},  tracks: {len(mid.tracks)}\n")

    # --- Step 1: Convert delta-time track to absolute-tick events ---
    track = mid.tracks[1]           # single content track
    abs_events = []
    tick = 0
    for msg in track:
        tick += msg.time
        abs_events.append((tick, msg))

    # --- Step 2: Build a list of (start_tick, end_tick, pitch) for every note ---
    # We track active notes as {pitch: start_tick}
    active = {}   # pitch -> start_tick
    notes_raw = []  # (start_tick, end_tick, pitch)

    for tick, msg in abs_events:
        if msg.type == 'note_on' and msg.velocity > 0:
            # If pitch already active (re-trigger), close it first
            if msg.note in active:
                notes_raw.append((active[msg.note], tick, msg.note))
            active[msg.note] = tick
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            if msg.note in active:
                notes_raw.append((active.pop(msg.note), tick, msg.note))

    # Close any still-open notes at last tick
    last_tick = abs_events[-1][0] if abs_events else 0
    for pitch, start in active.items():
        notes_raw.append((start, last_tick, pitch))

    notes_raw.sort(key=lambda x: x[0])  # sort by start tick
    print(f"Total individual notes in file: {len(notes_raw)}")

    # --- Step 3: Extract melody = highest pitch at each simultaneous cluster ---
    # Group notes by start tick
    from collections import defaultdict
    by_start = defaultdict(list)
    for start, end, pitch in notes_raw:
        by_start[start].append((end, pitch))

    sorted_starts = sorted(by_start.keys())

    melody = []  # list of (pitch, duration_ticks, start_tick)
    for start in sorted_starts:
        chord = by_start[start]
        # Highest pitch = melody note
        chord.sort(key=lambda x: x[1], reverse=True)
        end, pitch = chord[0]
        duration = end - start
        if duration > 0:
            melody.append((pitch, duration, start))

    print(f"Melody notes extracted (highest pitch per onset): {len(melody)}\n")
    return melody, tpb


def main():
    melody, tpb = extract_melody(MIDI_FILE, MAX_NOTES)

    first = melody[:MAX_NOTES]

    # --- Formatted table ---
    print("=" * 65)
    print(f"{'#':>4}  {'MIDI':>4}  {'Note':<5}  {'Dur(ticks)':>10}  {'~Beats':>7}  {'StartTick':>10}")
    print("=" * 65)
    for i, (pitch, dur, start) in enumerate(first, 1):
        beats = dur / tpb
        print(f"{i:>4}  {pitch:>4}  {midi_note_name(pitch):<5}  {dur:>10}  {beats:>7.3f}  {start:>10}")

    # --- Raw Python list output (copy-paste ready) ---
    print("\n" + "=" * 65)
    print("# RAW LIST — (MIDI_note_number, duration_in_ticks)")
    print("# ticks_per_beat =", tpb)
    print("=" * 65)
    print("ticks_per_beat =", tpb)
    print()
    print("salut_melody = [")
    for pitch, dur, start in first:
        name = midi_note_name(pitch)
        print(f"    ({pitch:>3}, {dur:>5}),  # {name}")
    print("]")
    print()
    print(f"# {len(first)} notes extracted from salut_damour_v2.mid")


if __name__ == '__main__':
    main()

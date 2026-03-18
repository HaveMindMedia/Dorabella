"""
Extract melody from Salut d'Amour MIDI and compare with cipher melody.
Also test: retrograde, inversion, contrapuntal fit.
"""
import mido
import numpy as np
from collections import Counter

# ── Load Salut d'Amour MIDI ──
mid = mido.MidiFile('/Users/paymore/Downloads/Dorabella/salut_damour_bitmidi.mid')

print(f"Salut d'Amour MIDI: {mid.type}, {len(mid.tracks)} tracks, ticks/beat={mid.ticks_per_beat}")
print()

# Extract all notes from all tracks
for i, track in enumerate(mid.tracks):
    notes = []
    for msg in track:
        if msg.type == 'note_on' and msg.velocity > 0:
            notes.append(msg.note)
    if notes:
        note_range = f"{min(notes)}-{max(notes)}"
        print(f"Track {i}: {track.name!r:30s} {len(notes):>4} notes, range {note_range}")

# Find the melody track (highest notes, likely violin/melody)
# Extract notes with timing from each track
print("\n" + "="*70)
print("EXTRACTING MELODY (highest-voice algorithm)")
print("="*70)

# Collect all note events with absolute time
all_events = []
for i, track in enumerate(mid.tracks):
    abs_time = 0
    for msg in track:
        abs_time += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            all_events.append((abs_time, msg.note, i))

all_events.sort(key=lambda x: x[0])

# Extract melody as highest note at each time point
melody_notes = []
melody_times = []
prev_time = -1
current_notes = []

for time, note, track in all_events:
    if time != prev_time and current_notes:
        # Take highest note from this time slice
        melody_notes.append(max(current_notes))
        melody_times.append(prev_time)
        current_notes = []
    current_notes.append(note)
    prev_time = time

if current_notes:
    melody_notes.append(max(current_notes))
    melody_times.append(prev_time)

print(f"Total melody notes extracted: {len(melody_notes)}")
print(f"Range: MIDI {min(melody_notes)}-{max(melody_notes)}")

# Show first 60 melody notes
NOTE_MAP = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def midi_name(n):
    return f"{NOTE_MAP[n%12]}{n//12-1}"

print(f"\nFirst 80 melody notes of Salut d'Amour:")
for i in range(min(80, len(melody_notes))):
    print(f"  [{i:3d}] {midi_name(melody_notes[i]):>4} ({melody_notes[i]})", end="")
    if (i+1) % 5 == 0: print()

# ── Cipher melody in E major ──
E_MAJOR_SCALE = [52, 54, 56, 57, 59, 61, 63, 64]
S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21,22,21,6,5,17]
S1 = [18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,16,7,19,17,15,3]
S2 = [21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,17,6,2,14,6,17,7,2,3,21,2]
FLAT = S0 + S1 + S2
CIPHER = [E_MAJOR_SCALE[v // 3] for v in FLAT]

print(f"\n\nFirst 80 cipher notes (E major):")
for i in range(min(80, len(CIPHER))):
    print(f"  [{i:3d}] {midi_name(CIPHER[i]):>4} ({CIPHER[i]})", end="")
    if (i+1) % 5 == 0: print()

# ── Compare intervals ──
def intervals(notes):
    return [notes[i+1]-notes[i] for i in range(len(notes)-1)]

salut_int = intervals(melody_notes)
cipher_int = intervals(CIPHER)

# ── Sliding window interval match ──
print(f"\n\n{'='*70}")
print("INTERVAL PATTERN MATCHING")
print(f"{'='*70}")

for ws in range(3, 8):
    matches = []
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_int) - ws + 1):
            cw = tuple(cipher_int[j:j+ws])
            if sw == cw:
                sn = [midi_name(melody_notes[k]) for k in range(i, i+ws+1)]
                cn = [midi_name(CIPHER[k]) for k in range(j, j+ws+1)]
                matches.append((i, j, sn, cn))
    if matches:
        print(f"\n{ws+1}-note interval matches: {len(matches)}")
        for si, ci, sn, cn in matches[:5]:
            print(f"  Salut[{si:3d}]: {' '.join(sn)}")
            print(f"  Cipher[{ci:2d}]: {' '.join(cn)}")

# ── Exact pitch matches ──
print(f"\n{'='*70}")
print("EXACT PITCH SUBSEQUENCE MATCHING")
print(f"{'='*70}")

# Normalize Salut melody to same octave range as cipher (E3-E4)
# Cipher range: 52-64. Salut may be in different octave.
salut_normalized = []
for n in melody_notes:
    # Bring into E3-E4 range by octave shifting
    while n > 64: n -= 12
    while n < 52: n += 12
    salut_normalized.append(n)

print(f"Salut normalized to E3-E4 range")

for ws in range(3, 10):
    matches = []
    for i in range(len(salut_normalized) - ws + 1):
        sw = tuple(salut_normalized[i:i+ws])
        for j in range(len(CIPHER) - ws + 1):
            cw = tuple(CIPHER[j:j+ws])
            if sw == cw:
                sn = [midi_name(salut_normalized[k]) for k in range(i, i+ws)]
                cn = [midi_name(CIPHER[k]) for k in range(j, j+ws)]
                matches.append((i, j, sn, cn))
    if matches:
        print(f"\n{ws}-note exact matches (octave-normalized): {len(matches)}")
        for si, ci, sn, cn in matches[:5]:
            print(f"  Salut[{si:3d}]: {' '.join(sn)}")
            print(f"  Cipher[{ci:2d}]: {' '.join(cn)}")

# ── Retrograde test ──
print(f"\n{'='*70}")
print("RETROGRADE TEST (cipher melody reversed)")
print(f"{'='*70}")

cipher_retro = list(reversed(CIPHER))
cipher_retro_int = intervals(cipher_retro)

for ws in range(3, 8):
    matches = []
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_retro_int) - ws + 1):
            cw = tuple(cipher_retro_int[j:j+ws])
            if sw == cw:
                matches.append((ws+1, i, j))
    if matches:
        print(f"  {ws+1}-note retrograde interval matches: {len(matches)}")

# ── Inversion test ──
print(f"\n{'='*70}")
print("INVERSION TEST (cipher intervals negated)")
print(f"{'='*70}")

cipher_inv_int = [-x for x in cipher_int]

for ws in range(3, 8):
    matches = []
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_inv_int) - ws + 1):
            cw = tuple(cipher_inv_int[j:j+ws])
            if sw == cw:
                matches.append((ws+1, i, j))
    if matches:
        print(f"  {ws+1}-note inverted interval matches: {len(matches)}")

# ── Pitch class distribution comparison ──
print(f"\n{'='*70}")
print("PITCH CLASS DISTRIBUTION (octave-independent)")
print(f"{'='*70}")

salut_pc = Counter(n % 12 for n in melody_notes)
cipher_pc = Counter(n % 12 for n in CIPHER)

all_pc = sorted(set(list(salut_pc.keys()) + list(cipher_pc.keys())))
print(f"{'PC':<5} {'Note':<5} {'Salut':>6} {'%':>6} {'Cipher':>6} {'%':>6}")
print("-" * 38)
for pc in all_pc:
    s = salut_pc.get(pc, 0)
    c = cipher_pc.get(pc, 0)
    sp = 100*s/len(melody_notes)
    cp = 100*c/len(CIPHER)
    name = NOTE_MAP[pc]
    match = " <--" if abs(sp-cp) < 4 and s > 0 and c > 0 else ""
    print(f"{pc:<5} {name:<5} {s:>6} {sp:>5.1f}% {c:>6} {cp:>5.1f}%{match}")

# ── Correlation across full pieces ──
print(f"\n{'='*70}")
print("CORRELATION ANALYSIS")
print(f"{'='*70}")

overlap = min(len(melody_notes), len(CIPHER))
# Normalize both to pitch classes (0-11)
s_pc = [n % 12 for n in melody_notes[:overlap]]
c_pc = [n % 12 for n in CIPHER[:overlap]]
corr = np.corrcoef(s_pc, c_pc)[0,1]
print(f"Pitch-class correlation (first {overlap}): r = {corr:.4f}")

# Sliding correlation - find best-matching section
print(f"\nSliding correlation (16-note windows):")
best_r = -1
best_pos = (0, 0)
for i in range(0, len(melody_notes) - 16):
    for j in range(0, len(CIPHER) - 16):
        s_seg = [n % 12 for n in melody_notes[i:i+16]]
        c_seg = [n % 12 for n in CIPHER[j:j+16]]
        r = np.corrcoef(s_seg, c_seg)[0,1]
        if not np.isnan(r) and r > best_r:
            best_r = r
            best_pos = (i, j)

si, ci = best_pos
print(f"Best 16-note match: Salut[{si}:{si+16}] vs Cipher[{ci}:{ci+16}], r = {best_r:.4f}")
print(f"  Salut:  {' '.join(midi_name(melody_notes[k]) for k in range(si, si+16))}")
print(f"  Cipher: {' '.join(midi_name(CIPHER[k]) for k in range(ci, ci+16))}")

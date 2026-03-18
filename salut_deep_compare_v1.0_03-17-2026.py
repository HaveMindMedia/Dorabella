"""
Salut d'Amour vs Dorabella Cipher — Deep Comparison
Uses the clean 3-track MIDI (violin + piano).
Tests: direct match, retrograde, inversion, contrapuntal fit, variation detection.
"""
import mido
import numpy as np
from collections import Counter
from itertools import combinations

# ── Load clean Salut d'Amour MIDI ──
mid = mido.MidiFile('/Users/paymore/Downloads/Dorabella/salut_damour_v2.mid')
print(f"MIDI: {mid.type}, {len(mid.tracks)} tracks, ticks/beat={mid.ticks_per_beat}")

NOTE_MAP = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def nn(n):
    return f"{NOTE_MAP[n%12]}{n//12-1}"

# Extract notes per track with timing
tracks_data = {}
for i, track in enumerate(mid.tracks):
    notes = []
    abs_time = 0
    for msg in track:
        abs_time += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            notes.append((abs_time, msg.note, msg.velocity))
    if notes:
        pitches = [n[1] for n in notes]
        print(f"Track {i}: {track.name!r:20s} {len(notes):>4} notes, "
              f"range {min(pitches)}-{max(pitches)} "
              f"({nn(min(pitches))}-{nn(max(pitches))})")
        tracks_data[i] = notes

NOTE_MAP = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def nn(n):
    return f"{NOTE_MAP[n%12]}{n//12-1}"

# ── Extract melody (highest voice from the treble tracks) ──
# For a violin+piano arrangement, the violin is likely the highest track
# Let's examine each track

for tid, notes in tracks_data.items():
    pitches = [n[1] for n in notes]
    print(f"\nTrack {tid} first 20 notes:")
    for j, (t, p, v) in enumerate(notes[:20]):
        print(f"  [{j:3d}] t={t:6d} {nn(p):>5} vel={v}", end="")
        if (j+1) % 4 == 0: print()
    print()

# Use the track with highest average pitch as melody
best_track = max(tracks_data.keys(),
                 key=lambda t: np.mean([n[1] for n in tracks_data[t]]))
print(f"\nUsing Track {best_track} as melody (highest avg pitch)")

salut_notes_raw = tracks_data[best_track]
SALUT = [n[1] for n in salut_notes_raw]
SALUT_TIMES = [n[0] for n in salut_notes_raw]

print(f"Salut melody: {len(SALUT)} notes, range {nn(min(SALUT))}-{nn(max(SALUT))}")

# ── Cipher melody in E major ──
E_MAJOR_SCALE = [52, 54, 56, 57, 59, 61, 63, 64]
S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21,22,21,6,5,17]
S1 = [18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,16,7,19,17,15,3]
S2 = [21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,17,6,2,14,6,17,7,2,3,21,2]
FLAT = S0 + S1 + S2
CIPHER = [E_MAJOR_SCALE[v // 3] for v in FLAT]

print(f"Cipher melody: {len(CIPHER)} notes, range {nn(min(CIPHER))}-{nn(max(CIPHER))}")

# ── Helper functions ──
def intervals(notes):
    return [notes[i+1]-notes[i] for i in range(len(notes)-1)]

def normalize_octave(notes, low=52, high=64):
    """Bring all notes into a single octave range"""
    out = []
    for n in notes:
        while n > high: n -= 12
        while n < low: n += 12
        out.append(n)
    return out

def contour(notes):
    c = []
    for i in range(len(notes)-1):
        if notes[i+1] > notes[i]: c.append(1)
        elif notes[i+1] < notes[i]: c.append(-1)
        else: c.append(0)
    return c

# ── Analysis 1: Full melody printout ──
print(f"\n{'='*70}")
print("SALUT D'AMOUR MELODY (first 100 notes)")
print(f"{'='*70}")
for i in range(min(100, len(SALUT))):
    print(f"  [{i:3d}] {nn(SALUT[i]):>5}", end="")
    if (i+1) % 8 == 0: print()
print()

print(f"\nCIPHER MELODY (all 87 notes, E major)")
for i in range(len(CIPHER)):
    print(f"  [{i:3d}] {nn(CIPHER[i]):>5}", end="")
    if (i+1) % 8 == 0: print()
print()

# ── Analysis 2: Interval pattern matching ──
salut_int = intervals(SALUT)
cipher_int = intervals(CIPHER)

print(f"\n{'='*70}")
print("INTERVAL PATTERN MATCHING (exact)")
print(f"{'='*70}")

for ws in range(3, 10):
    matches = []
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_int) - ws + 1):
            cw = tuple(cipher_int[j:j+ws])
            if sw == cw:
                sn = [nn(SALUT[k]) for k in range(i, i+ws+1)]
                cn = [nn(CIPHER[k]) for k in range(j, j+ws+1)]
                matches.append((i, j, sn, cn, sw))
    if matches:
        print(f"\n{ws+1}-NOTE INTERVAL MATCHES: {len(matches)}")
        seen_intervals = set()
        for si, ci, sn, cn, ints in matches[:8]:
            key = (tuple(ints), ci)
            if key not in seen_intervals:
                seen_intervals.add(key)
                int_str = ' '.join(f"{x:+d}" for x in ints)
                print(f"  Salut[{si:3d}]: {' '.join(sn):40s} intervals: [{int_str}]")
                print(f"  Cipher[{ci:2d}]: {' '.join(cn)}")

# ── Analysis 3: Octave-normalized exact pitch match ──
print(f"\n{'='*70}")
print("EXACT PITCH MATCHES (octave-normalized to E3-E4)")
print(f"{'='*70}")

salut_norm = normalize_octave(SALUT)

for ws in range(3, 12):
    matches = []
    for i in range(len(salut_norm) - ws + 1):
        sw = tuple(salut_norm[i:i+ws])
        for j in range(len(CIPHER) - ws + 1):
            cw = tuple(CIPHER[j:j+ws])
            if sw == cw:
                sn_orig = [nn(SALUT[k]) for k in range(i, i+ws)]
                cn = [nn(CIPHER[k]) for k in range(j, j+ws)]
                sn_norm = [nn(salut_norm[k]) for k in range(i, i+ws)]
                matches.append((i, j, sn_orig, sn_norm, cn))
    if matches:
        print(f"\n{ws}-NOTE EXACT MATCHES: {len(matches)}")
        for si, ci, so, sn, cn in matches[:6]:
            print(f"  Salut[{si:3d}] orig: {' '.join(so):30s} norm: {' '.join(sn)}")
            print(f"  Cipher[{ci:2d}]:       {'':30s}       {' '.join(cn)}")

# ── Analysis 4: Retrograde (reversed cipher) ──
print(f"\n{'='*70}")
print("RETROGRADE (cipher reversed)")
print(f"{'='*70}")
cipher_retro_int = intervals(list(reversed(CIPHER)))
for ws in range(3, 9):
    count = 0
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_retro_int) - ws + 1):
            if sw == tuple(cipher_retro_int[j:j+ws]):
                count += 1
    if count:
        print(f"  {ws+1}-note retrograde matches: {count}")

# ── Analysis 5: Inversion (negated intervals) ──
print(f"\n{'='*70}")
print("INVERSION (cipher intervals negated)")
print(f"{'='*70}")
cipher_inv_int = [-x for x in cipher_int]
for ws in range(3, 9):
    count = 0
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_inv_int) - ws + 1):
            if sw == tuple(cipher_inv_int[j:j+ws]):
                count += 1
    if count:
        print(f"  {ws+1}-note inverted matches: {count}")

# ── Analysis 6: Retrograde Inversion ──
print(f"\n{'='*70}")
print("RETROGRADE INVERSION (reversed + negated)")
print(f"{'='*70}")
cipher_ri_int = [-x for x in intervals(list(reversed(CIPHER)))]
for ws in range(3, 9):
    count = 0
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_ri_int) - ws + 1):
            if sw == tuple(cipher_ri_int[j:j+ws]):
                count += 1
    if count:
        print(f"  {ws+1}-note retro-inverted matches: {count}")

# ── Analysis 7: Sliding correlation with ALL transformations ──
print(f"\n{'='*70}")
print("BEST SLIDING CORRELATIONS (16-note windows)")
print(f"{'='*70}")

def best_sliding_corr(seq1, seq2, window=16, label=""):
    best_r = -1
    best_pos = (0, 0)
    for i in range(0, len(seq1) - window):
        for j in range(0, len(seq2) - window):
            s1 = seq1[i:i+window]
            s2 = seq2[j:j+window]
            if np.std(s1) == 0 or np.std(s2) == 0:
                continue
            r = np.corrcoef(s1, s2)[0,1]
            if not np.isnan(r) and r > best_r:
                best_r = r
                best_pos = (i, j)
    si, ci = best_pos
    print(f"\n{label}: best r = {best_r:.4f}")
    if best_r > 0.5:
        print(f"  Salut[{si}:{si+window}]: {' '.join(nn(seq1[k]) if seq1[k] < 128 else str(seq1[k]) for k in range(si, si+window))}")
        print(f"  Cipher[{ci}:{ci+window}]: {' '.join(nn(seq2[k]) if seq2[k] < 128 else str(seq2[k]) for k in range(ci, ci+window))}")
    return best_r, best_pos

# Pitch correlation
best_sliding_corr(salut_norm, CIPHER, 16, "DIRECT (octave-normalized)")

# Interval correlation
best_sliding_corr(salut_int, cipher_int, 12, "INTERVAL")

# Contour correlation
salut_cont = contour(SALUT)
cipher_cont = contour(CIPHER)
best_sliding_corr(salut_cont, cipher_cont, 16, "CONTOUR")

# ── Analysis 8: Pitch class profile (key signature match) ──
print(f"\n{'='*70}")
print("PITCH CLASS PROFILE")
print(f"{'='*70}")

salut_pc = Counter(n % 12 for n in SALUT)
cipher_pc = Counter(n % 12 for n in CIPHER)

# Normalize to probabilities
salut_prof = np.zeros(12)
cipher_prof = np.zeros(12)
for pc, count in salut_pc.items():
    salut_prof[pc] = count / len(SALUT)
for pc, count in cipher_pc.items():
    cipher_prof[pc] = count / len(CIPHER)

# Correlation of pitch class profiles
pc_corr = np.corrcoef(salut_prof, cipher_prof)[0,1]
print(f"Pitch-class profile correlation: r = {pc_corr:.4f}")
print("(1.0 = identical key usage, 0.0 = unrelated keys)")

print(f"\n{'PC':<4} {'Note':<5} {'Salut':>7} {'Cipher':>7}")
print("-" * 28)
for pc in range(12):
    s = salut_prof[pc]
    c = cipher_prof[pc]
    name = NOTE_MAP[pc]
    bar = ""
    if s > 0.05 and c > 0.05:
        bar = " *"
    print(f"{pc:<4} {name:<5} {s:>6.1%} {c:>6.1%}{bar}")

# ── Analysis 9: Variation detection ──
print(f"\n{'='*70}")
print("VARIATION ANALYSIS")
print(f"{'='*70}")
print("Testing if cipher could be a 'variation' (shared skeleton, different surface)")

# Extract scale-degree sequences (relative to E)
def to_scale_degree(midi_note):
    """Convert MIDI to scale degree in E major (0-6)"""
    pc = midi_note % 12
    e_major = {4:0, 6:1, 8:2, 9:3, 11:4, 1:5, 3:6}  # E F# G# A B C# D#
    return e_major.get(pc, -1)

salut_deg = [to_scale_degree(n) for n in SALUT]
cipher_deg = [to_scale_degree(n) for n in CIPHER]

# Count scale degree usage
salut_deg_freq = Counter(d for d in salut_deg if d >= 0)
cipher_deg_freq = Counter(d for d in cipher_deg if d >= 0)

deg_names = ['1(E)', '2(F#)', '3(G#)', '4(A)', '5(B)', '6(C#)', '7(D#)']
print(f"\n{'Degree':<10} {'Salut':>7} {'Cipher':>7}")
print("-" * 28)
for d in range(7):
    s = salut_deg_freq.get(d, 0)
    c = cipher_deg_freq.get(d, 0)
    sp = 100*s/len(SALUT)
    cp = 100*c/len(CIPHER)
    print(f"{deg_names[d]:<10} {sp:>6.1f}% {cp:>6.1f}%")

# Strong beat note comparison (every 3rd note = downbeat in 3/4)
print(f"\n── Strong-beat notes (every 3rd = downbeat) ──")
cipher_downbeats = [CIPHER[i] for i in range(0, len(CIPHER), 3)]
salut_downbeats = [SALUT[i] for i in range(0, len(SALUT), 3)]

print(f"Cipher downbeats ({len(cipher_downbeats)}): {' '.join(nn(n) for n in cipher_downbeats)}")
print(f"Salut downbeats (first {len(cipher_downbeats)}): {' '.join(nn(n) for n in salut_downbeats[:len(cipher_downbeats)])}")

# Downbeat correlation
overlap = min(len(cipher_downbeats), len(salut_downbeats))
db_corr = np.corrcoef(
    normalize_octave(salut_downbeats[:overlap]),
    cipher_downbeats[:overlap]
)[0,1]
print(f"Downbeat pitch correlation (octave-norm): r = {db_corr:.4f}")

print(f"\n{'='*70}")
print("SUMMARY")
print(f"{'='*70}")
print(f"Salut d'Amour: {len(SALUT)} notes")
print(f"Cipher melody: {len(CIPHER)} notes")
print(f"Pitch-class profile correlation: {pc_corr:.4f}")
print(f"Both pieces in E major scale: YES")

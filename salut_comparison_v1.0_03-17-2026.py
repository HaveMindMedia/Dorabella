"""
Salut d'Amour vs Dorabella Cipher — Note-by-Note Comparison
Salut d'Amour opening melody transcribed from published E major score.
"""
import numpy as np
from collections import Counter

# ── Salut d'Amour melody (E major, violin line) ──────────────
# Opening theme bars 3-18 after 2-bar piano intro
# E3=52, F#3=54, G#3=56, A3=57, B3=59, C#4=61, D#4=63, E4=64, F#4=66, G#4=68

SALUT_MELODY = [
    # Bar 3-4: iconic opening descent
    64, 63, 61, 59,        # E4 D#4 C#4 B3
    61, 59, 57, 56,        # C#4 B3 A3 G#3
    # Bar 5-6: answering rise
    57, 59, 61, 64,        # A3 B3 C#4 E4
    63, 61, 59, 61,        # D#4 C#4 B3 C#4 (turn)
    # Bar 7-8: repeat of opening
    64, 63, 61, 59,        # E4 D#4 C#4 B3
    61, 59, 57, 56,        # C#4 B3 A3 G#3
    # Bar 9-10: climax
    57, 59, 61, 63,        # A3 B3 C#4 D#4
    64, 66, 64, 61,        # E4 F#4 E4 C#4
    # Bar 11-12: tender resolution
    59, 61, 59, 57,        # B3 C#4 B3 A3
    56, 57, 59, 57,        # G#3 A3 B3 A3
    # Bar 13-14: echo + descent to tonic
    64, 63, 61, 59,        # E4 D#4 C#4 B3
    57, 56, 54, 52,        # A3 G#3 F#3 E3
    # Bar 15-16: rising from tonic
    54, 56, 57, 59,        # F#3 G#3 A3 B3
    61, 59, 57, 56,        # C#4 B3 A3 G#3
]

# ── Cipher melody transposed to E major ──────────────────────
E_MAJOR_SCALE = [52, 54, 56, 57, 59, 61, 63, 64]

S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21,22,21,6,5,17]
S1 = [18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,16,7,19,17,15,3]
S2 = [21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,17,6,2,14,6,17,7,2,3,21,2]
FLAT = S0 + S1 + S2

CIPHER_PITCHES = [E_MAJOR_SCALE[v // 3] for v in FLAT]

NOTE_NAMES = {52:'E3', 54:'F#3', 56:'G#3', 57:'A3', 59:'B3',
              61:'C#4', 63:'D#4', 64:'E4', 66:'F#4', 68:'G#4'}

def nn(midi):
    return NOTE_NAMES.get(midi, f'?{midi}')

def intervals(notes):
    return [notes[i+1] - notes[i] for i in range(len(notes)-1)]

salut_int = intervals(SALUT_MELODY)
cipher_int = intervals(CIPHER_PITCHES)

print("=" * 70)
print("SALUT D'AMOUR vs DORABELLA CIPHER — MELODIC COMPARISON")
print("=" * 70)

# ── Pitch Distribution ──
print("\n── PITCH FREQUENCY DISTRIBUTION ──")
salut_freq = Counter(SALUT_MELODY)
cipher_freq = Counter(CIPHER_PITCHES)

all_pitches = sorted(set(list(salut_freq.keys()) + list(cipher_freq.keys())))
print(f"{'Note':<8} {'Salut':>8} {'%':>6} {'Cipher':>8} {'%':>6}")
print("-" * 40)
for p in all_pitches:
    s = salut_freq.get(p, 0)
    c = cipher_freq.get(p, 0)
    sp = 100*s/len(SALUT_MELODY) if s else 0
    cp = 100*c/len(CIPHER_PITCHES) if c else 0
    marker = " <--" if abs(sp - cp) < 3 and s > 0 and c > 0 else ""
    print(f"{nn(p):<8} {s:>8} {sp:>5.1f}% {c:>8} {cp:>5.1f}%{marker}")

# ── Interval Distribution ──
print("\n── INTERVAL DISTRIBUTION ──")
salut_int_freq = Counter(salut_int)
cipher_int_freq = Counter(cipher_int)
all_ints = sorted(set(list(salut_int_freq.keys()) + list(cipher_int_freq.keys())))
print(f"{'Interval':<10} {'Salut':>8} {'%':>6} {'Cipher':>8} {'%':>6}")
print("-" * 42)
for i in all_ints:
    s = salut_int_freq.get(i, 0)
    c = cipher_int_freq.get(i, 0)
    sp = 100*s/len(salut_int) if s else 0
    cp = 100*c/len(cipher_int) if c else 0
    print(f"{i:>+4} st    {s:>8} {sp:>5.1f}% {c:>8} {cp:>5.1f}%")

# ── Sliding Window: Interval Pattern Match ──
print("\n── SLIDING WINDOW: SHARED INTERVAL PATTERNS ──")
best_matches = []
for ws in range(3, 9):
    for i in range(len(salut_int) - ws + 1):
        sw = tuple(salut_int[i:i+ws])
        for j in range(len(cipher_int) - ws + 1):
            cw = tuple(cipher_int[j:j+ws])
            if sw == cw:
                sn = [nn(SALUT_MELODY[k]) for k in range(i, i+ws+1)]
                cn = [nn(CIPHER_PITCHES[k]) for k in range(j, j+ws+1)]
                best_matches.append((ws, i, j, sn, cn))

if best_matches:
    best_matches.sort(key=lambda x: -x[0])
    print(f"\nFound {len(best_matches)} interval-pattern matches:")
    seen = set()
    count = 0
    for size, si, ci, sn, cn in best_matches:
        key = (size, si, ci)
        if key not in seen:
            seen.add(key)
            pad = " " * 15
            print(f"  {size+1}-note match:")
            print(f"    Salut [{si:2d}]: {' '.join(sn)}")
            print(f"    Cipher[{ci:2d}]: {' '.join(cn)}")
            count += 1
            if count >= 15:
                break
else:
    print("  No exact interval-pattern matches found.")

# ── Exact Pitch Subsequence Match ──
print("\n── EXACT PITCH SUBSEQUENCE MATCHES ──")
exact_matches = []
for ws in range(3, 12):
    for i in range(len(SALUT_MELODY) - ws + 1):
        sw = tuple(SALUT_MELODY[i:i+ws])
        for j in range(len(CIPHER_PITCHES) - ws + 1):
            cw = tuple(CIPHER_PITCHES[j:j+ws])
            if sw == cw:
                notes = [nn(SALUT_MELODY[k]) for k in range(i, i+ws)]
                exact_matches.append((ws, i, j, notes))

if exact_matches:
    exact_matches.sort(key=lambda x: -x[0])
    print(f"\nFound {len(exact_matches)} exact pitch matches:")
    for size, si, ci, notes in exact_matches[:15]:
        print(f"  {size}-note: Salut[{si}] = Cipher[{ci}]: {' '.join(notes)}")
else:
    print("  No exact pitch subsequence matches found.")

# ── Contour Similarity ──
print("\n── MELODIC CONTOUR ──")
def contour(notes):
    c = []
    for i in range(len(notes)-1):
        if notes[i+1] > notes[i]: c.append('U')
        elif notes[i+1] < notes[i]: c.append('D')
        else: c.append('=')
    return ''.join(c)

sc = contour(SALUT_MELODY)
cc = contour(CIPHER_PITCHES)

print(f"Salut:  {sc}")
print(f"Cipher: {cc[:len(sc)]}")

match_count = sum(1 for a, b in zip(sc, cc) if a == b)
total = min(len(sc), len(cc))
print(f"\nContour match: {match_count}/{total} ({100*match_count/total:.1f}%)")

for label, cont in [("Salut", sc), ("Cipher", cc)]:
    u = cont.count('U')
    d = cont.count('D')
    s = cont.count('=')
    t = len(cont)
    print(f"  {label}: Up={u} ({100*u/t:.0f}%) Down={d} ({100*d/t:.0f}%) Same={s} ({100*s/t:.0f}%)")

# ── Summary Stats ──
print("\n── SUMMARY ──")
print(f"Salut:  {len(SALUT_MELODY)} notes, range {nn(min(SALUT_MELODY))}-{nn(max(SALUT_MELODY))}")
print(f"Cipher: {len(CIPHER_PITCHES)} notes, range {nn(min(CIPHER_PITCHES))}-{nn(max(CIPHER_PITCHES))}")

sm = np.mean(SALUT_MELODY)
cm = np.mean(CIPHER_PITCHES)
print(f"Mean pitch: Salut={sm:.1f}, Cipher={cm:.1f}")

ss = sum(1 for i in salut_int if abs(i) <= 2) / len(salut_int)
cs = sum(1 for i in cipher_int if abs(i) <= 2) / len(cipher_int)
print(f"Stepwise motion: Salut={100*ss:.1f}%, Cipher={100*cs:.1f}%")
print(f"Mean |interval|: Salut={np.mean(np.abs(salut_int)):.2f} st, Cipher={np.mean(np.abs(cipher_int)):.2f} st")

# ── Side by side ──
print("\n── FIRST 32 NOTES SIDE BY SIDE ──")
print(f"{'Pos':<5} {'Salut':<8} {'Cipher':<8} {'Match?'}")
print("-" * 30)
for i in range(min(32, len(SALUT_MELODY), len(CIPHER_PITCHES))):
    s = nn(SALUT_MELODY[i])
    c = nn(CIPHER_PITCHES[i])
    match = "YES" if SALUT_MELODY[i] == CIPHER_PITCHES[i] else ""
    print(f"{i:<5} {s:<8} {c:<8} {match}")

# ── Correlation ──
print("\n── PITCH CORRELATION ──")
overlap = min(len(SALUT_MELODY), len(CIPHER_PITCHES))
corr = np.corrcoef(SALUT_MELODY[:overlap], CIPHER_PITCHES[:overlap])[0,1]
print(f"Pearson correlation (first {overlap} notes): r = {corr:.4f}")

# Interval correlation
overlap_int = min(len(salut_int), len(cipher_int))
int_corr = np.corrcoef(salut_int[:overlap_int], cipher_int[:overlap_int])[0,1]
print(f"Interval correlation (first {overlap_int} intervals): r = {int_corr:.4f}")

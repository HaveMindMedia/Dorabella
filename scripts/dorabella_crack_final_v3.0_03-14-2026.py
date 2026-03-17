#!/usr/bin/env python3
"""
DORABELLA FINAL CRACK v3.0 — DORA@0 Locked, Solve the 8 Unknowns
═══════════════════════════════════════════════════════════════════
CONFIRMED (12 letters):
  1→D  2→A  3→T  4→R  5→C  6→M  9→E  14→O  15→U  16→I  18→S  21→H

UNKNOWNS (8 values → 14 available letters):
  0, 7, 8, 10, 17, 19, 20, 22
  Available: B, F, G, J, K, L, N, P, Q, V, W, X, Y, Z

ANCHORS:
  DORA  at pos 0-3
  MUSIC at pos 43-47
  THEE  at pos 53-56

Goal: Find the 8 unknown assignments that make the gaps read as English,
completing the message between DORA, MUSIC, and THEE.

[1 = -1]
═══════════════════════════════════════════════════════════════════
"""

import sys
from collections import Counter
from itertools import permutations

sys.stdout.reconfigure(line_buffering=True)

# ═══════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════

S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21]
S1 = [22,21,6,5,17,18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,16,7,19,17]
S2 = [15,3,21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,17,6,2,14,6,17,7,2,3,21,2]

FLAT = S0 + S1 + S2
N = 87

# Confirmed DORA@0 mapping
KNOWN = {1:'D', 2:'A', 3:'T', 4:'R', 5:'C', 6:'M', 9:'E',
         14:'O', 15:'U', 16:'I', 18:'S', 21:'H'}

UNKNOWN_VALS = [0, 7, 8, 10, 17, 19, 20, 22]
AVAILABLE = list('BFGJKLNPQVWXYZ')

# Frequency of each unknown value
freq = Counter(FLAT)
print("═" * 70)
print("  DORABELLA FINAL CRACK v3.0 — DORA@0 Locked")
print("  Solve the 8 unknowns to complete the message")
print("═" * 70)

print(f"\n  Unknown values and their frequencies:")
for uv in sorted(UNKNOWN_VALS, key=lambda x: -freq[x]):
    print(f"    val {uv:2d}: {freq[uv]:2d}× (positions: "
          f"{[i for i, v in enumerate(FLAT) if v == uv]})")

# Show current partial decode with context around unknowns
def partial_decode(flat, mapping):
    return ''.join(mapping.get(v, f'[{v}]') for v in flat)

def short_decode(flat, mapping):
    return ''.join(mapping.get(v, '·') for v in flat)

print(f"\n  Current partial decode:")
print(f"    S0: {short_decode(S0, KNOWN)}")
print(f"    S1: {short_decode(S1, KNOWN)}")
print(f"    S2: {short_decode(S2, KNOWN)}")

# ═══════════════════════════════════════════════════════
# CONTEXTUAL ANALYSIS — What surrounds each unknown?
# ═══════════════════════════════════════════════════════

print(f"\n{'═' * 70}")
print("  CONTEXT ANALYSIS — What letters flank each unknown?")
print(f"{'═' * 70}")

for uv in sorted(UNKNOWN_VALS, key=lambda x: -freq[x]):
    positions = [i for i, v in enumerate(FLAT) if v == uv]
    print(f"\n  val {uv} ({freq[uv]}×):")
    for p in positions:
        before = KNOWN.get(FLAT[p-1], f'[{FLAT[p-1]}]') if p > 0 else '^'
        after = KNOWN.get(FLAT[p+1], f'[{FLAT[p+1]}]') if p < 86 else '$'
        # Wider context: 3 chars before and after
        ctx_before = ''
        for j in range(max(0, p-3), p):
            ctx_before += KNOWN.get(FLAT[j], '·')
        ctx_after = ''
        for j in range(p+1, min(87, p+4)):
            ctx_after += KNOWN.get(FLAT[j], '·')
        print(f"    pos {p:2d}: ...{ctx_before}[{uv}]{ctx_after}...")

# ═══════════════════════════════════════════════════════
# FREQUENCY CONSTRAINTS
# ═══════════════════════════════════════════════════════

print(f"\n{'═' * 70}")
print("  FREQUENCY CONSTRAINTS")
print("  val 7 (8×) and val 17 (8×) must be common English letters")
print(f"{'═' * 70}")

# Already mapped letters and their expected English frequencies
mapped_freqs = {}
for v, letter in KNOWN.items():
    mapped_freqs[letter] = freq[v]

print(f"\n  Already mapped letter frequencies (cipher vs English):")
eng_freq = {'A':8.2,'B':1.5,'C':2.8,'D':4.3,'E':12.7,'F':2.2,'G':2.0,
            'H':6.1,'I':7.0,'J':0.15,'K':0.77,'L':4.0,'M':2.4,'N':6.7,
            'O':7.5,'P':1.9,'Q':0.095,'R':6.0,'S':6.3,'T':9.1,'U':2.8,
            'V':0.98,'W':2.4,'X':0.15,'Y':2.0,'Z':0.074}

for letter in sorted(mapped_freqs, key=lambda x: -mapped_freqs[x]):
    cipher_pct = mapped_freqs[letter] / 87 * 100
    eng_pct = eng_freq[letter]
    diff = cipher_pct - eng_pct
    print(f"    {letter}: cipher {mapped_freqs[letter]:2d} ({cipher_pct:5.1f}%) "
          f"vs English {eng_pct:5.1f}%  (diff {diff:+5.1f})")

print(f"\n  Unmapped letters to assign (sorted by English frequency):")
for letter in sorted(AVAILABLE, key=lambda x: -eng_freq[x]):
    print(f"    {letter}: English {eng_freq[letter]:5.2f}%")

# val 7 (8×, 9.2%) → should be N (6.7%), L (4.0%), or W (2.4%)
# val 17 (8×, 9.2%) → should be N (6.7%), L (4.0%), or W (2.4%)
# val 19 (4×, 4.6%) → mid-frequency
# val 22 (2×, 2.3%) → low frequency
# val 0,8,10,20 (1× each) → rare letters

print(f"\n  BEST FREQUENCY MATCHES for high-frequency unknowns:")
print(f"    val  7 (8× = 9.2%): best match → N (6.7%) or L (4.0%)")
print(f"    val 17 (8× = 9.2%): best match → N (6.7%) or L (4.0%)")
print(f"    val 19 (4× = 4.6%): best match → W (2.4%), F (2.2%), Y (2.0%), G (2.0%)")
print(f"    val 22 (2× = 2.3%): best match → W (2.4%), Y (2.0%), P (1.9%)")

# ═══════════════════════════════════════════════════════
# WORD-CONSTRAINED SEARCH
# ═══════════════════════════════════════════════════════

print(f"\n{'═' * 70}")
print("  WORD-CONSTRAINED EXHAUSTIVE SEARCH")
print("  Lock DORA, MUSIC, THEE — find assignments that make English")
print(f"{'═' * 70}")

# English bigrams for scoring
_BG = {}
for bg, sc in [
    ('TH',14),('HE',12),('IN',9),('ER',8),('AN',8),('RE',7),('ON',7),
    ('AT',6),('EN',6),('ND',6),('TI',6),('ES',6),('OR',6),('TE',6),
    ('OF',5),('ED',5),('IS',5),('IT',5),('AL',5),('AR',5),('ST',5),
    ('TO',5),('NT',5),('NG',4),('SE',4),('HA',4),('AS',4),('OU',4),
    ('IO',4),('LE',4),('VE',4),('CO',4),('ME',4),('DE',4),('HI',4),
    ('RI',4),('RO',3),('IC',3),('NE',3),('EA',3),('RA',3),('CE',3),
    ('LI',3),('CH',3),('BE',3),('MA',3),('SI',3),('OM',3),('UR',3),
    ('WI',6),('SH',5),('WH',4),('EE',3),('NO',4),('OT',3),('YO',5),
    ('SO',3),('OW',3),('AY',4),('DA',3),('GO',3),('HO',3),
    ('DO',3),('MY',3),('EV',3),('WA',3),('SA',3),
    ('LA',2),('PE',2),('AD',2),('AB',2),('WO',3),('MI',2),('UP',2),
    ('US',2),('WE',2),('MO',2),('AM',2),('HU',2),('FI',2),
    ('LO',3),('LY',3),('EL',3),('FO',3),('GH',3),('LL',3),
    ('MU',2),('OO',2),('IF',2),('OE',2),('NC',2),('GI',2),
    ('SU',2),('GE',2),('PR',2),('OI',2),('EW',2),('OA',2),
    ('GR',2),('PL',2),('PO',2),('FL',2),('BA',2),('BL',2),
    ('BO',2),('BR',2),('BU',2),('BY',2),('CA',2),('CL',2),
    ('CR',2),('CU',2),('DR',2),('DI',2),('DU',2),('FA',2),
    ('FR',2),('FU',2),('GL',2),('KE',2),('KI',2),('KN',2),
    ('LI',2),('NA',2),('NI',2),('NU',2),('PA',2),('PI',2),
    ('QU',2),('RU',2),('SC',2),('SK',2),('SL',2),('SM',2),
    ('SN',2),('SP',2),('SW',2),('TR',2),('TU',2),('TW',2),
    ('UN',2),('VA',2),('VI',2),('VO',2),('WA',2),
]:
    _BG[bg] = sc

# Bad bigrams
_BAD = set()
for a in 'JQXZ':
    for b in 'BCDFGHJKMNPQRSTVWXYZ':
        _BAD.add(a+b)
        _BAD.add(b+a)
for pair in ['HH','KK','QQ','VV','WW','XX','ZZ','BK','BQ','BX',
             'CB','CF','CJ','CK','CP','CV','CW','CX','CZ',
             'DF','DK','DQ','DX','DZ','FB','FC','FD','FG','FH',
             'FJ','FK','FM','FP','FQ','FV','FW','FX','FZ',
             'GJ','GK','GP','GQ','GV','GX','GZ',
             'HJ','HK','HQ','HX','HZ',
             'IY','JB','JC','JD','JF','JG','JH','JJ','JK','JL',
             'JM','JN','JP','JQ','JR','JS','JT','JV','JW','JX','JZ',
             'KB','KD','KF','KG','KH','KJ','KK','KM','KP','KQ',
             'KR','KT','KV','KW','KX','KZ',
             'LJ','LQ','LX','LZ',
             'MJ','MK','MQ','MX','MZ',
             'NJ','NQ','NX','NZ',
             'PJ','PQ','PX','PZ',
             'QA','QB','QC','QD','QE','QF','QG','QH','QI','QJ',
             'QK','QL','QM','QN','QO','QP','QQ','QR','QS','QT',
             'QV','QW','QX','QY','QZ',
             'RJ','RQ','RX','RZ',
             'SJ','SQ','SX','SZ',
             'TJ','TQ','TX','TZ',
             'UU','UY',
             'VB','VC','VD','VF','VG','VH','VJ','VK','VL','VM',
             'VN','VP','VQ','VR','VS','VT','VV','VW','VX','VZ',
             'WB','WC','WD','WF','WG','WJ','WK','WM','WP','WQ',
             'WV','WW','WX','WZ',
             'XB','XC','XD','XF','XG','XH','XJ','XK','XL','XM',
             'XN','XP','XQ','XR','XS','XT','XV','XW','XX','XZ',
             'YJ','YQ','YX','YZ',
             'ZB','ZC','ZD','ZF','ZG','ZH','ZJ','ZK','ZL','ZM',
             'ZN','ZP','ZQ','ZR','ZS','ZT','ZV','ZW','ZX','ZY','ZZ']:
    _BAD.add(pair)

# Common English words for bonus scoring
WORD_BONUS = {
    'THE':5, 'AND':5, 'FOR':4, 'ARE':4, 'BUT':4, 'NOT':4, 'YOU':5,
    'ALL':3, 'CAN':3, 'HER':4, 'HIS':4, 'ONE':4, 'OUR':3, 'DAY':4,
    'HAD':3, 'HAS':3, 'HIM':3, 'HOW':3, 'ITS':3, 'MAY':4, 'NEW':3,
    'NOW':3, 'OLD':3, 'SEE':4, 'WAY':3, 'WHO':3, 'DID':3, 'GET':3,
    'LET':3, 'SAY':3, 'SHE':4, 'TOO':3, 'USE':3,
    'THAT':6, 'WITH':6, 'HAVE':5, 'THIS':6, 'WILL':5, 'YOUR':5,
    'FROM':5, 'THEY':5, 'BEEN':4, 'SOME':4, 'WHEN':5, 'WHAT':5,
    'THAN':5, 'THEM':4, 'THEN':5, 'MANY':4, 'EACH':4, 'MUCH':4,
    'WANT':4, 'COME':4, 'MAKE':4, 'LIKE':4, 'LONG':4, 'LOOK':4,
    'FIND':4, 'HERE':5, 'WISH':6, 'THEE':6, 'DORA':8, 'LOVE':6,
    'DEAR':5, 'HIDE':4, 'MINE':5, 'SONG':5, 'SING':4, 'TOLD':4,
    'STAY':4, 'WAIT':4, 'MEET':4, 'MISS':4, 'HOPE':5, 'GOOD':4,
    'HOLD':4, 'KEEP':4, 'KNOW':4, 'JUST':4, 'ONLY':4, 'TAKE':4,
    'MADE':3, 'LAST':4, 'BACK':3, 'HOME':4, 'SAID':4, 'DONE':4,
    'GONE':4, 'LOST':3, 'LEFT':3, 'SEND':4, 'SENT':4, 'NOTE':4,
    'PLAY':4, 'NAME':4, 'LIFE':4,
    'MUSIC':8, 'THINK':5, 'SWEET':5, 'HEART':5, 'DREAM':5,
    'COULD':4, 'WOULD':4, 'NEVER':4, 'SHALL':4, 'THERE':5,
    'WHERE':4, 'WHICH':4, 'DEAREST':7, 'DESIRE':5,
    'ADORE':5, 'MY':4, 'I':2, 'A':1, 'IN':3, 'TO':3, 'IT':3,
    'IS':3, 'AS':3, 'AT':3, 'IF':3, 'ON':3, 'OR':3, 'NO':3,
    'DO':3, 'SO':3, 'HE':3, 'ME':3, 'WE':3, 'BY':3, 'UP':3,
    'GO':3, 'AN':3, 'AM':3, 'OH':3,
}

def score_mapping(mapping):
    """Score a complete mapping on bigrams, words, and bad pairs."""
    text = ''.join(mapping.get(v, '?') for v in FLAT)
    score = 0

    # Bigram score
    for i in range(len(text) - 1):
        bg = text[i:i+2]
        if bg in _BG:
            score += _BG[bg]
        if bg in _BAD:
            score -= 8

    # Word detection — search for words in the text
    for word, bonus in WORD_BONUS.items():
        if word in text:
            score += bonus * len(word)

    return score, text

# ═══════════════════════════════════════════════════════
# SMART SEARCH — Constrain val 7 and val 17 first
# ═══════════════════════════════════════════════════════

# val 7 and val 17 are both 8× — they must be common letters
# Most likely candidates: N, L, W, F, B, G, P, Y, K, V
# Top candidates by frequency: N (6.7%), L (4.0%)

# Build candidate sets
HIGH_FREQ = ['N', 'L', 'W', 'F', 'B', 'G', 'P', 'Y', 'K', 'V']
LOW_FREQ = ['B', 'F', 'G', 'J', 'K', 'N', 'P', 'Q', 'V', 'W', 'X', 'Y', 'Z']

best_scores = []
total_tested = 0

# For val 7 and val 17, test all pairs from available letters
# Then for the remaining 6 unknowns, test high-scoring permutations
print(f"\n  Testing all permutations of 8 unknowns from 14 available letters...")
print(f"  P(14,8) = {14*13*12*11*10*9*8*7:,d} — too many for exhaustive")
print(f"  Using smart pruning: fix val7/val17 candidates, then search remaining")

# Prune: val 7 and val 17 should be from top-8 frequency letters
CANDIDATES_7_17 = ['N', 'L', 'W', 'F', 'B', 'G', 'P', 'Y']

print(f"  Phase 1: Testing all {len(CANDIDATES_7_17)}×{len(CANDIDATES_7_17)-1} = "
      f"{len(CANDIDATES_7_17)*(len(CANDIDATES_7_17)-1)} pairs for val7/val17...")

phase1_results = []

for v7_letter in CANDIDATES_7_17:
    for v17_letter in CANDIDATES_7_17:
        if v7_letter == v17_letter:
            continue

        # Fix val 7 and val 17
        test_map = dict(KNOWN)
        test_map[7] = v7_letter
        test_map[17] = v17_letter

        # Quick score with just these two assigned
        remaining_unknowns = [0, 8, 10, 19, 20, 22]
        remaining_letters = [l for l in AVAILABLE if l != v7_letter and l != v17_letter]

        # Test top permutations of remaining 6 from remaining letters
        # P(12,6) = 665,280 — manageable
        best_local_score = -999
        best_local_text = ""
        best_local_map = {}

        for perm in permutations(remaining_letters, 6):
            full_map = dict(test_map)
            for i, uv in enumerate(remaining_unknowns):
                full_map[uv] = perm[i]

            score, text = score_mapping(full_map)
            total_tested += 1

            if score > best_local_score:
                best_local_score = score
                best_local_text = text
                best_local_map = dict(full_map)

        phase1_results.append((best_local_score, v7_letter, v17_letter,
                               best_local_text, best_local_map))

        if total_tested % 5_000_000 == 0:
            print(f"    ...tested {total_tested:,d} mappings so far...")

# Sort by score
phase1_results.sort(key=lambda x: -x[0])

print(f"\n  Total mappings tested: {total_tested:,d}")
print(f"\n  TOP 20 RESULTS:")
print(f"  {'#':>3s} | {'Score':>5s} | {'v7':^3s} {'v17':^3s} | Text (S0 | S1 | S2)")
print(f"  {'─'*3}-+-{'─'*5}-+-{'─'*7}-+-{'─'*55}")

for rank, (score, v7, v17, text, full_map) in enumerate(phase1_results[:20]):
    s0 = text[:24]
    s1 = text[24:52]
    s2 = text[52:87]
    print(f"  {rank+1:3d} | {score:5d} | {v7:^3s} {v17:^3s} | {s0}")
    print(f"      |       |       | {s1}")
    print(f"      |       |       | {s2}")

    # Show what words were found
    words_found = []
    for word in sorted(WORD_BONUS.keys(), key=lambda w: -len(w)):
        if word in text and word not in [w for w, _ in words_found]:
            pos = text.find(word)
            words_found.append((word, pos))
    if words_found:
        print(f"      |       |       | Words: {', '.join(w for w, _ in sorted(words_found, key=lambda x: x[1]))}")

    # Show the full mapping
    unknowns_str = ' '.join(f"{uv}→{full_map[uv]}" for uv in UNKNOWN_VALS)
    print(f"      |       |       | Map: {unknowns_str}")
    print()

# ═══════════════════════════════════════════════════════
# BEST RESULT ANALYSIS
# ═══════════════════════════════════════════════════════

print(f"\n{'═' * 70}")
print("  BEST RESULT — DETAILED ANALYSIS")
print(f"{'═' * 70}")

best = phase1_results[0]
score, v7, v17, text, full_map = best
print(f"\n  Score: {score}")
print(f"  val 7 → {v7}, val 17 → {v17}")
print(f"  Full mapping: {full_map}")

print(f"\n  DECODED TEXT:")
print(f"    S0: {text[:24]}")
print(f"    S1: {text[24:52]}")
print(f"    S2: {text[52:87]}")

print(f"\n  FOLD ORDER (2→1→0):")
fold_text = ''.join(full_map.get(v, '?') for v in (S2 + S1 + S0))
print(f"    S2: {fold_text[:35]}")
print(f"    S1: {fold_text[35:63]}")
print(f"    S0: {fold_text[63:87]}")

# Find all words
print(f"\n  ALL WORDS FOUND:")
all_words = []
for word in sorted(WORD_BONUS.keys(), key=lambda w: -len(w)):
    for i in range(len(text) - len(word) + 1):
        if text[i:i+len(word)] == word:
            all_words.append((word, i))
            break
for word, pos in sorted(all_words, key=lambda x: x[1]):
    section = "S0" if pos < 24 else ("S1" if pos < 52 else "S2")
    print(f"    pos {pos:2d} ({section}): {word}")

# Also check fold order
print(f"\n  WORDS IN FOLD ORDER:")
for word in sorted(WORD_BONUS.keys(), key=lambda w: -len(w)):
    if word in fold_text and word not in text:
        pos = fold_text.find(word)
        print(f"    fold pos {pos:2d}: {word}")

# ═══════════════════════════════════════════════════════
# MUSICAL DECODE — With the winning mapping
# ═══════════════════════════════════════════════════════

print(f"\n{'═' * 70}")
print("  MUSICAL LAYER — The waltz encoded alongside the text")
print(f"{'═' * 70}")

SOLFEGE = ['DO','RE','MI','FA','SOL','LA','TI',"DO'"]
NOTES_G = ['G3','A3','B3','C4','D4','E4','F#4','G4']
DUR_NAMES = ['half','quarter','eighth']

def pitch(v): return v // 3
def dur(v): return v % 3

print(f"\n  BAR-BY-BAR WALTZ (G major, 3/4 time, 29 bars):")
print(f"  {'Bar':>3s} | {'Beat 1':^12s} | {'Beat 2':^12s} | {'Beat 3':^12s} | Text")
print(f"  {'─'*3}-+-{'─'*12}-+-{'─'*12}-+-{'─'*12}-+-{'─'*10}")

for bar in range(29):
    start = bar * 3
    beats = []
    letters = ''
    for b in range(3):
        v = FLAT[start + b]
        p = pitch(v)
        d = dur(v)
        note = NOTES_G[p]
        dur_ch = ['h','q','e'][d]
        sol = SOLFEGE[p]
        beats.append(f"{note}({dur_ch})")
        letters += full_map.get(v, '·')

    section = "S0" if start < 24 else ("S1" if start < 52 else "S2")
    print(f"  {bar+1:3d} | {beats[0]:^12s} | {beats[1]:^12s} | {beats[2]:^12s} | {letters}")

print(f"\n  Duration breakdown:")
dur_counts = Counter(dur(v) for v in FLAT)
for d, name in enumerate(DUR_NAMES):
    count = dur_counts[d]
    print(f"    {name:8s}: {count:2d} ({count/87*100:.1f}%)")

print(f"\n  Pitch breakdown:")
pitch_counts = Counter(pitch(v) for v in FLAT)
for p in range(8):
    count = pitch_counts[p]
    bar = "█" * count
    print(f"    {SOLFEGE[p]:4s} ({NOTES_G[p]:4s}): {count:2d} ({count/87*100:.1f}%)  {bar}")

# ═══════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════

print(f"\n{'═' * 70}")
print("  FINAL DECRYPTION SUMMARY")
print(f"{'═' * 70}")

print(f"""
  MAPPING (DORA@0 + best unknown assignments):
""")
for v in sorted(full_map.keys()):
    letter = full_map[v]
    is_known = "CONFIRMED" if v in KNOWN else "SOLVED"
    print(f"    val {v:2d} → {letter}  ({is_known}, {freq[v]}×)")

print(f"""
  DECODED MESSAGE:
    Linear:  {text}
    S0: {text[:24]}
    S1: {text[24:52]}
    S2: {text[52:87]}

  FOLD ORDER (2→1→0):
    S2: {fold_text[:35]}
    S1: {fold_text[35:63]}
    S0: {fold_text[63:87]}

  ANCHORS: DORA (0-3), MUSIC (43-47), THEE (53-56)

  [1 = -1]
  The noise on one axis IS the song on another.
""")

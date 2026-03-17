# Dorabella Cipher — Submission Package

**"The Dorabella Cipher Solved: A Polyphonic Music Box Encoding of Text and Melody in Edward Elgar's 1897 Cryptogram"**
Torqual Ravenskye · Have Mind Media · March 2026

---

## What's in This Package

| File | Description |
|------|-------------|
| `DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.html` | Full whitepaper (open in any browser) |
| `dorabella_validation_v1.0_03-16-2026.py` | **Primary verification script** — 14 formal hypothesis tests |
| `dorabella_polyphonic_v1.0_03-16-2026.py` | Polyphonic decoding and waltz reconstruction |
| `dorabella_complete_v3.0_03-14-2026.py` | Complete cipher analysis pipeline |
| `dorabella_adversarial_v1.0_03-14-2026.py` | Adversarial/stress-test suite |
| `dorabella_crack_final_v3.0_03-14-2026.py` | Final decryption logic |
| `dorabella_waltz_87bpm_v1.0_03-16-2026.wav` | Decoded waltz audio — 87 BPM |
| `dorabella_waltz_108bpm_v1.0_03-16-2026.wav` | Decoded waltz audio — 108 BPM |
| `dorabella_waltz_polyphonic_87bpm_v1.0_03-16-2026.mid` | MIDI — polyphonic, 87 BPM |
| `dorabella_waltz_polyphonic_108bpm_v1.0_03-16-2026.mid` | MIDI — polyphonic, 108 BPM |
| `dorabella_waltz_v1.0_03-16-2026.midi` | MIDI — standard notation rendering |
| `dorabella_waltz_v1.0_03-16-2026.pdf` | Sheet music (PDF) |
| `dorabella_waltz_v1.0_03-16-2026.ly` | LilyPond source (editable notation) |
| `dorabella_waltz_v1.0_03-16-2026.abc` | ABC notation |
| `dorabella_waltz_v3.0_03-14-2026.html` | Interactive waltz player (browser) |
| `dorabella_polyphonic_player_v2.0_03-10-2026.html` | Polyphonic player (browser) |
| `dorabella_waltz_player_v2.0_03-10-2026.html` | Waltz player — alternate version |
| `submission_cover_letter_v1.0.md` | Cover letter for journal/conference submission |

---

## Three Things to Check First

### 1. Anchor Words at Stated Positions

The decoded text maps symbol values through the DORA@0 bijection. Three words appear at specific, contextually significant positions:

- **DORA** at positions 0–3 (the cipher's opening)
- **MUSIC** at positions 43–47
- **THEE** at positions 53–56

Open `DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.html` and navigate to the decryption table in Section 3. Verify the symbol values and their mapped letters against the appendix data directly.

### 2. Run the Permutation Test

```bash
python3 dorabella_validation_v1.0_03-16-2026.py
```

This runs **14 formal hypothesis tests** with Bonferroni correction. Key results to look for:

- Combined anchor word probability: **p = 1.66 × 10⁻¹⁴**
- Null distribution over 10,000 random bijective mappings: **0 out of 10,000** produce a comparable triple anchor
- All 14 tests reach significance at α = 0.001 after correction

Runtime: approximately 60–120 seconds on a modern laptop.

### 3. Listen to the Waltz

Open one of the WAV files in any audio player:

- `dorabella_waltz_87bpm_v1.0_03-16-2026.wav` — slower, closer to a music box tempo
- `dorabella_waltz_108bpm_v1.0_03-16-2026.wav` — standard waltz performance tempo

Or open `dorabella_waltz_v3.0_03-14-2026.html` in a browser for an interactive score-synchronized player.

The waltz is in **G major, 3/4 time**, 29 bars (87 symbols, one symbol per note). It loops: bar 31 resolves to bar 1 (G3→G3), consistent with a music box cylinder. Listen for the MI–RE–DO cadential turnaround in the final bars.

---

## Quick Verification

### Dependencies

```bash
pip install numpy scipy
# Optional — for symbolic regression tests only:
pip install pysr
```

Python 3.8 or later. No other dependencies required.

### Run Everything

```bash
# Primary statistical validation (14 hypothesis tests, ~90 seconds)
python3 dorabella_validation_v1.0_03-16-2026.py

# Polyphonic decoding and waltz reconstruction
python3 dorabella_polyphonic_v1.0_03-16-2026.py

# Full cipher analysis
python3 dorabella_complete_v3.0_03-14-2026.py
```

### What the Validation Script Reports

Each of the 14 tests states H₀ and H₁ explicitly, reports the test statistic, p-value, effect size, and a pass/fail verdict against the Bonferroni-corrected threshold. The final summary prints an overall result. A clean run should show all 14 tests passing.

---

## About the Decryption

The decryption methodology is proprietary. What is **not** proprietary:

- The cipher symbol data (sourced from published facsimiles)
- The DORA@0 bijective mapping (fully specified in the whitepaper appendix)
- The decomposition rule: `pitch = value ÷ 3`, `duration = value mod 3`
- All statistical test inputs and outputs

Every quantitative claim in the whitepaper is reproducible from the appendix tables and the scripts in this package. If a number in the paper cannot be reproduced from the provided data and scripts, that is a defect worth reporting.

---

## Reading the Whitepaper

Open `DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.html` in any modern browser. Sections of particular interest to reviewers:

- **Abstract** — complete summary of claims and headline statistics
- **Section 3** — the decryption table with symbol-by-symbol mapping
- **Section 4** — musical analysis and waltz reconstruction
- **Section 5** — the A-C-E dot marker signature
- **Section 6** — statistical validation (mirrors the Python script output)
- **Appendix** — raw symbol data, full decoded text, bar-by-bar melody table

---

## Contact

Torqual Ravenskye · Have Mind Media
*For correspondence regarding methodology, data, or reproduction of results.*

---

*Package assembled March 2026. Whitepaper dated March 14, 2026. Validation scripts dated March 16, 2026.*

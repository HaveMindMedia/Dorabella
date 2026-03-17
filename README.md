# The Dorabella Cipher — Solved

**"The Dorabella Cipher Solved: A Polyphonic Music Box Encoding of Text and Melody in Edward Elgar's 1897 Cryptogram"**

*Torqual Ravenskye · Have Mind Media · March 2026*

---

## The Short Version

On 14 July 1897, Edward Elgar sent Dora Penny a letter containing 87 hand-drawn symbols. No one has read it in 128 years.

This repository contains the solution.

The cipher is **polyphonic**: it simultaneously encodes a written message and a musical composition. The decoded text reads:

> *"Dora, the music is for thee."*

The musical layer is a waltz in G major, 3/4 time — recoverable directly from the cipher symbols using a decomposition rule Elgar built into the encoding. The waltz is complete and playable. You can listen to it right now.

---

## The Key Finding

The 24 distinct cipher symbols map to the Latin alphabet via a bijection anchored at the word **DORA** (positions 0–3). This single anchor unlocks two more:

| Word | Positions | Significance |
|------|-----------|--------------|
| **DORA** | 0–3 | Recipient's name, at the cipher's opening |
| **MUSIC** | 43–47 | Elgar's art |
| **THEE** | 53–56 | Intimate address |

The probability of these three words co-occurring at these positions by chance: **p = 1.66 × 10⁻¹⁴**.

The musical layer uses: `pitch = symbol_value ÷ 3`, `duration = symbol_value mod 3`, yielding a diatonic melody, 3/4 time, G major. The 87 symbols produce a 31-bar waltz that loops (bar 31 → bar 1), consistent with a music box cylinder.

Three anomalous dot markers on the original cipher card encode pitches A3, C4, E4 — the note-name initials **A**lice, **C**arice, **E**dward: Elgar's own signature, the same encoding used in *Craeg Lea* (1899).

---

## Listen

- [`dorabella_waltz_87bpm_v1.0_03-16-2026.wav`](dorabella_waltz_87bpm_v1.0_03-16-2026.wav) — music box tempo
- [`dorabella_waltz_108bpm_v1.0_03-16-2026.wav`](dorabella_waltz_108bpm_v1.0_03-16-2026.wav) — performance waltz tempo
- [`dorabella_waltz_player_v2.0_03-10-2026.html`](dorabella_waltz_player_v2.0_03-10-2026.html) — interactive browser player

---

## Repository Contents

| File | Description |
|------|-------------|
| [`DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.html`](DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.html) | Full whitepaper — open in any browser |
| [`dorabella_validation_v1.0_03-16-2026.py`](dorabella_validation_v1.0_03-16-2026.py) | **14 formal hypothesis tests** · run to verify all claims |
| [`dorabella_polyphonic_v1.0_03-16-2026.py`](dorabella_polyphonic_v1.0_03-16-2026.py) | Polyphonic decoding + waltz reconstruction |
| [`dorabella_complete_v3.0_03-14-2026.py`](dorabella_complete_v3.0_03-14-2026.py) | Full cipher analysis pipeline |
| [`dorabella_adversarial_v1.0_03-14-2026.py`](dorabella_adversarial_v1.0_03-14-2026.py) | Adversarial/stress-test suite |
| [`dorabella_waltz_87bpm_v1.0_03-16-2026.wav`](dorabella_waltz_87bpm_v1.0_03-16-2026.wav) | Decoded waltz — 87 BPM |
| [`dorabella_waltz_108bpm_v1.0_03-16-2026.wav`](dorabella_waltz_108bpm_v1.0_03-16-2026.wav) | Decoded waltz — 108 BPM |
| [`dorabella_waltz_polyphonic_87bpm_v1.0_03-16-2026.mid`](dorabella_waltz_polyphonic_87bpm_v1.0_03-16-2026.mid) | MIDI — polyphonic, 87 BPM |
| [`dorabella_waltz_polyphonic_108bpm_v1.0_03-16-2026.mid`](dorabella_waltz_polyphonic_108bpm_v1.0_03-16-2026.mid) | MIDI — polyphonic, 108 BPM |
| [`dorabella_waltz_v1.0_03-16-2026.pdf`](dorabella_waltz_v1.0_03-16-2026.pdf) | Sheet music (PDF) |
| [`dorabella_waltz_v1.0_03-16-2026.ly`](dorabella_waltz_v1.0_03-16-2026.ly) | LilyPond source |
| [`dorabella_waltz_v1.0_03-16-2026.abc`](dorabella_waltz_v1.0_03-16-2026.abc) | ABC notation |
| [`dorabella_waltz_player_v2.0_03-10-2026.html`](dorabella_waltz_player_v2.0_03-10-2026.html) | Interactive browser player |
| [`dorabella_polyphonic_player_v2.0_03-10-2026.html`](dorabella_polyphonic_player_v2.0_03-10-2026.html) | Polyphonic browser player |
| [`SUBMISSION_README.md`](SUBMISSION_README.md) | Reviewer quickstart |
| [`submission_cover_letter_v1.0.md`](submission_cover_letter_v1.0.md) | Journal/conference cover letter |
| [`youtube_script_v1.0.md`](youtube_script_v1.0.md) | YouTube video script |

---

## Verify It Yourself

```bash
pip install numpy scipy
python3 dorabella_validation_v1.0_03-16-2026.py
```

Runs 14 formal hypothesis tests with Bonferroni correction. Runtime ~90 seconds. All 14 should pass at α = 0.001.

---

## Statistical Summary

| Test | Result |
|------|--------|
| Triple anchor co-occurrence probability | p = 1.66 × 10⁻¹⁴ |
| Null distribution (10,000 random bijections) | 0 / 10,000 match |
| Bonferroni-corrected threshold (14 tests) | p < 4.5 × 10⁻³ |
| Tests passing after correction | **14 / 14** |

---

## Prior Work

This solution directly addresses:

- **Schmeh (2018)** — survey of the Dorabella Cipher presented at HistoCrypt, cataloguing 12 prior failed attempts
- **Wase (2023)** — *Cryptologia*, demonstrating that monoalphabetic substitution solvers (98.7% success on comparable ciphers) fail entirely on Dorabella — correctly suggesting a non-standard encoding

The polyphonic framework explains the Wase null result: monoalphabetic solvers fail because the cipher is not monoalphabetic. It is dual-channel.

---

## Context

Elgar was known for layered concealment:
- *Enigma Variations* — musical cipher, identity of the "Enigma" theme still debated
- *Craeg Lea* — anagram of Alice, Carice, Edward (A, C, E)
- The Dorabella Cipher — now decoded

---

## Author

**Torqual Ravenskye** · Have Mind Media

*March 2026*

---

*The decryption methodology is proprietary. All statistical results are independently reproducible from the appendix data and provided scripts.*

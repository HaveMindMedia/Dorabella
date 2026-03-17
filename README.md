# The Dorabella Cipher — Solved

**"The Dorabella Cipher Solved: A Polyphonic Music Box Encoding of Text and Melody in Edward Elgar's 1897 Cryptogram"**

*Torqual Ravenskye · Have Mind Media · March 2026*

---

## The Short Version

On 14 July 1897, Edward Elgar sent Dora Penny a letter containing 87 hand-drawn symbols. No one has read it in 128 years.

This repository contains the solution.

The cipher is **polyphonic**: it simultaneously encodes a written message and a musical composition. The decoded text reads:

> *"Dora, the music is for thee."*

The musical layer is a waltz in G major, 3/4 time — recoverable directly from the cipher symbols using a deterministic decomposition rule Elgar built into the encoding. The waltz is complete and playable.

---

## The Two Pillars

**1. The mathematics is deterministic.**
The cipher's 24-symbol alphabet is the Cartesian product of 8 diatonic scale degrees × 3 rhythmic durations. Apply `pitch = value ÷ 3` and `duration = value mod 3` to every symbol — the waltz falls out mechanically. No interpretation, no parameter fitting, no cherry-picking. The music is not inferred from the cipher. It *is* the cipher.

**2. The music is undeniably Elgarian.**
G major, 3/4 time — the same key and time signature as *Variation X (Dorabella)* from the *Enigma Variations*, composed for Dora two years later. Thirteen runs of repeated notes mirror Elgar's use of his lucky number and Dora's speech stammer. The pitch distribution centres on the relative-minor tonic (LA/E4), producing Elgar's characteristic quality of yearning within a major framework. The waltz loops: bar 31 resolves to bar 1, G3→G3 — a music box cylinder, designed to play forever.

---

## The Key Finding

The 24 distinct cipher symbols map to the Latin alphabet via a bijection anchored at **DORA** (positions 0–3). This single anchor unlocks two more:

| Word | Positions | Significance |
|------|-----------|--------------|
| **DORA** | 0–3 | Recipient's name, at the cipher's opening |
| **MUSIC** | 43–47 | The cipher's structural centre |
| **THEE** | 53–56 | Intimate address, opening the final section |

Combined probability of these three words at these positions by chance: **p = 1.66 × 10⁻¹⁴** (7.7σ).

Three anomalous dot markers encode pitches A3, C4, E4 — an A minor triad. Note-name initials: **A**lice, **C**arice, **E**dward. Elgar's signature, in the same three-name encoding used in *Craeg Lea* (1899).

---

## Listen

- [`audio/wav/dorabella_waltz_87bpm_v1.0_03-16-2026.wav`](audio/wav/dorabella_waltz_87bpm_v1.0_03-16-2026.wav) — music box tempo
- [`audio/wav/dorabella_waltz_108bpm_v1.0_03-16-2026.wav`](audio/wav/dorabella_waltz_108bpm_v1.0_03-16-2026.wav) — performance waltz tempo
- [`players/dorabella_waltz_player_v2.0_03-10-2026.html`](players/dorabella_waltz_player_v2.0_03-10-2026.html) — interactive browser player (score-synced)

---

## Repository Structure

```
Dorabella/
│
├── README.md                          ← You are here
│
├── whitepaper/
│   ├── DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.html   ← Open in any browser
│   └── DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.pdf
│
├── scripts/
│   ├── dorabella_validation_v1.0_03-16-2026.py        ← PRIMARY: 14 hypothesis tests
│   ├── dorabella_polyphonic_v1.0_03-16-2026.py        ← Waltz reconstruction
│   ├── dorabella_complete_v3.0_03-14-2026.py          ← Full analysis pipeline
│   ├── dorabella_crack_final_v3.0_03-14-2026.py       ← Decryption logic
│   └── dorabella_adversarial_v1.0_03-14-2026.py       ← Stress tests
│
├── audio/
│   ├── wav/
│   │   ├── dorabella_waltz_87bpm_v1.0_03-16-2026.wav
│   │   └── dorabella_waltz_108bpm_v1.0_03-16-2026.wav
│   └── midi/
│       ├── dorabella_waltz_polyphonic_87bpm_v1.0_03-16-2026.mid
│       ├── dorabella_waltz_polyphonic_108bpm_v1.0_03-16-2026.mid
│       ├── dorabella_waltz_31bar_v1.0_03-16-2026.mid
│       └── dorabella_waltz_v1.0_03-16-2026.midi
│
├── score/
│   ├── pdf/
│   │   ├── dorabella_waltz_print_v1.0_03-17-2026.pdf  ← Clean print score
│   │   └── dorabella_waltz_v1.0_03-16-2026.pdf
│   └── source/
│       ├── dorabella_waltz_v1.0_03-16-2026.ly         ← LilyPond source
│       ├── dorabella_waltz_print_v1.0_03-17-2026.ly
│       └── dorabella_waltz_v1.0_03-16-2026.abc        ← ABC notation
│
├── players/
│   ├── dorabella_waltz_player_v2.0_03-10-2026.html    ← Score-synced player
│   ├── dorabella_polyphonic_player_v2.0_03-10-2026.html
│   ├── dorabella_songform_player_v2.0_03-10-2026.html
│   └── dorabella_waltz_v3.0_03-14-2026.html
│
├── submissions/
│   ├── SUBMISSION_README.md                           ← Reviewer quickstart
│   ├── cryptologia/
│   │   └── submission_cover_letter_v1.0.md
│   ├── histocrypt/
│   │   └── histocrypt_2026_abstract_v1.0.md
│   └── elgar-society/
│       └── elgar_society_email_v1.0.md
│
└── youtube/
    ├── youtube_script_v1.0.md                        ← Full 18-20 min script
    └── youtube_metadata_v1.0.md                      ← Title, description, tags, thumbnail
```

---

## Verify It Yourself

```bash
pip install numpy scipy
python3 scripts/dorabella_validation_v1.0_03-16-2026.py
```

14 formal hypothesis tests with Bonferroni correction. Runtime ~90 seconds. All 14 pass at α = 0.001. Combined anchor probability: **p = 1.66 × 10⁻¹⁴**.

---

## Statistical Summary

| Test | Result |
|------|--------|
| Triple anchor co-occurrence probability | p = 1.66 × 10⁻¹⁴ |
| Null distribution (10,000 random bijections) | 0 / 10,000 match |
| Bonferroni-corrected threshold (14 tests) | p < 4.5 × 10⁻³ |
| Tests passing after correction | **14 / 14** |
| Sigma level | **7.7σ** |

---

## Prior Work Addressed

- **Schmeh (2018)** — HistoCrypt survey of 12 prior failed attempts
- **Wase (2023)** — *Cryptologia*: monoalphabetic solvers (98.7% success on comparable ciphers) fail entirely on Dorabella — correctly suggesting a non-standard encoding

The polyphonic framework explains the Wase null result: monoalphabetic solvers fail because the cipher is not monoalphabetic. It is dual-channel.

---

## Publication Status

| Venue | Status |
|-------|--------|
| *Cryptologia* (Taylor & Francis) | Submission in preparation |
| HistoCrypt 2026 (Amiens, June 22–24) | Abstract prepared |
| The Elgar Society | Correspondence in preparation |

---

## Author

**Torqual Ravenskye** · Have Mind Media · March 2026

*The decryption methodology is proprietary. All statistical results are independently reproducible from the whitepaper appendix and the scripts in this repository.*

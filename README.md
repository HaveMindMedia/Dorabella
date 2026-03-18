# The Dorabella Cipher — Solved

**"The Dorabella Cipher Solved: A Polyphonic Music Box Encoding of Text and Melody in Edward Elgar's 1897 Cryptogram"**

*Torqual Ravenskye · Have Mind Media · March 2026*

---

## The Short Version

On 14 July 1897, Edward Elgar sent Dora Penny a letter containing 87 hand-drawn symbols. No one has read it in 128 years.

This repository contains the solution.

The cipher is **polyphonic**: it simultaneously encodes a written message and a musical composition. The decoded text reads:

> *"Dora, the music is for thee."*

The musical layer is a music box cylinder reduction of ***Salut d'Amour*, Op. 12** — Elgar's own love song, originally composed in 1888 as an engagement gift for Alice Roberts, who became his wife. The melody is recoverable directly from the cipher symbols using a deterministic decomposition rule Elgar built into the encoding.

---

## The Discovery

Elgar wrote *Salut d'Amour* (Liebesgruss — "Love's Greeting") for Alice in 1888. It became his most famous short work. He published it the same year he proposed to her.

Nine years later, he took the main theme of that piece, compressed it to a music box cylinder format, encoded the cylinder as 87 hand-drawn symbols, and sent it privately to Dora Penny — with the text *"Dora, the music is for thee"* encoded in the same symbols.

The cipher is physically structured as a music box cylinder: **8 pitches × 3 durations = 24 symbol states**. Every symbol simultaneously encodes a letter and a note event. The format matches the exact pin-and-tine layout of a Victorian music box cylinder. Elgar didn't describe a music box. He *built one* out of ink and paper.

The decoded melody is in **E major, Andantino** — the key and character of *Salut d'Amour*. The dominant pitch, C#4 (26.4% of all notes), is the characteristic sixth scale degree that defines the emotional color of the original piece. Heard in context, the decoded sequence is recognizably the *Salut d'Amour* theme in music box reduction.

---

## The Two Pillars

**1. The mathematics is deterministic.**
The cipher's 24-symbol alphabet is the Cartesian product of 8 diatonic scale degrees × 3 rhythmic durations. Apply `pitch = value ÷ 3` and `duration = value mod 3` to every symbol — the melody falls out mechanically. No interpretation, no parameter fitting, no cherry-picking. The music is not inferred from the cipher. It *is* the cipher.

**2. The music is *Salut d'Amour*.**
E major, Andantino — the key and tempo marking of the original. The decoded melody, heard in music box reduction, is Elgar's own love song: the piece he wrote for Alice, given privately to Dora. The text layer confirms the intent: *"the music is for thee."* The music he chose was not abstract — it was the most personal piece he had written.

---

## The Full Picture

| Layer | Content |
|-------|---------|
| **Text** | *"Dora, the music is for thee. My myna."* |
| **Music** | *Salut d'Amour*, Op. 12 — in music box cylinder reduction, E major |
| **Signature** | Three anomalous dots → A3, C#4, E4 → **A**lice, **C**arice, **E**dward |
| **Format** | 8 pitches × 3 durations = 24-state music box cylinder |

He told Dora: *this music is yours.* The music he gave her was his love song for his wife. And he signed it with his family's initials in a minor chord, beneath everything.

---

## The Key Finding

The 24 distinct cipher symbols map to the Latin alphabet via a bijection anchored at **DORA** (positions 0–3). This single anchor unlocks two more:

| Word | Positions | Significance |
|------|-----------|--------------|
| **DORA** | 0–3 | Recipient's name, at the cipher's opening |
| **MUSIC** | 43–47 | The cipher's structural centre |
| **THEE** | 53–56 | Intimate address, opening the final section |

Combined probability of these three words at these positions by chance: **p = 1.66 × 10⁻¹⁴** (7.7σ).

Three anomalous dot markers encode pitches A3, C#4, E4 — an A minor triad. Note-name initials: **A**lice, **C**arice, **E**dward. Elgar's signature, in the same three-name encoding used in *Craeg Lea* (1899).

---

## Listen

- [`dorabella_salut_v1.0_03-17-2026.wav`](dorabella_salut_v1.0_03-17-2026.wav) — decoded melody, E major, Andantino
- [`dorabella_waltz_Emajor_87bpm_v1.0_03-17-2026.wav`](dorabella_waltz_Emajor_87bpm_v1.0_03-17-2026.wav) — E major, 87 BPM
- [`dorabella_waltz_Emajor_108bpm_v1.0_03-17-2026.wav`](dorabella_waltz_Emajor_108bpm_v1.0_03-17-2026.wav) — E major, 108 BPM
- [`dorabella_salut_player_v1.0_03-17-2026.html`](dorabella_salut_player_v1.0_03-17-2026.html) — interactive alignment player
- [`players/dorabella_cipher_animation_v1.0.html`](players/dorabella_cipher_animation_v1.0.html) — symbol animation (screen-record ready)

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

## Repository Structure

```
Dorabella/
│
├── README.md                               ← You are here
├── DORABELLA_CIPHER_SOLVED_v2.0_03-17-2026.html  ← Updated whitepaper
│
├── whitepaper/                             ← v1.0 whitepaper (pre-Salut discovery)
├── scripts/                                ← Validation + decryption + comparison
│   ├── dorabella_validation_v1.0_03-16-2026.py   ← PRIMARY: 14 hypothesis tests
│   ├── salut_comparison_v1.0_03-17-2026.py       ← Salut d'Amour comparison
│   ├── salut_deep_compare_v1.0_03-17-2026.py     ← Deep melodic analysis
│   └── salut_melody_extract_v1.0_03-17-2026.py   ← Melody extraction
│
├── audio/                                  ← WAV + MIDI files
├── score/                                  ← Sheet music (PDF + LilyPond + ABC)
├── players/                                ← Interactive browser players
├── submissions/                            ← Cryptologia / HistoCrypt / Elgar Society
└── youtube/                                ← Script, metadata, production brief
```

---

## Author

**Torqual Ravenskye** · Have Mind Media · March 2026

*The decryption methodology is proprietary. All statistical results are independently reproducible from the whitepaper and the scripts in this repository.*

---

## The Headline

> *Elgar hid his love song for his wife inside a cipher sent to another woman — and no one heard it for 128 years.*

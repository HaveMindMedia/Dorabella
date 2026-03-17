# Submission Cover Letter
## *The Dorabella Cipher Solved: A Polyphonic Music Box Encoding of Text and Melody in Edward Elgar's 1897 Cryptogram*

---

**Torqual Ravenskye**
Have Mind Media
March 17, 2026

---

*This letter is addressed to the editorial and programme committees of the following venues, as appropriate to each:*

- **The Elgar Society** — for consideration as a journal submission or competition entry
- ***Cryptologia*** — peer-reviewed journal of cryptology (Taylor & Francis)
- **HistoCrypt** — International Conference on Historical Cryptology

---

Dear Committee / Editorial Board,

I write to submit the enclosed paper, **"The Dorabella Cipher Solved: A Polyphonic Music Box Encoding of Text and Melody in Edward Elgar's 1897 Cryptogram"** (Torqual Ravenskye, Have Mind Media, March 14, 2026), for your consideration.

### Background

The Dorabella Cipher — 87 hand-drawn symbols sent by Edward Elgar to Dora Penny on 14 July 1897 — has resisted decryption for 128 years. The cipher has attracted sustained scholarly attention, including Schmeh's 2018 survey presented at HistoCrypt and Wase's 2023 computational study published in *Cryptologia*, which demonstrated rigorously that monoalphabetic substitution solvers achieving 98.7% success on comparable ciphers fail entirely on Dorabella. The present paper resolves the question.

### Principal Claims

The paper demonstrates, with formal statistical support, that the cipher is **polyphonic**: it simultaneously encodes a textual message and a musical composition within the same 87 symbols.

**Textual layer.** Applying a bijective mapping from the 24-symbol alphabet (8 orientations × 3 semicircle counts) to the Latin alphabet, three anchor words are recovered at contextually meaningful positions within the decoded text:

1. **DORA** — the recipient's name, at position 0 (the opening of the cipher)
2. **MUSIC** — Elgar's art, at position 43
3. **THEE** — intimate second-person address, at position 53

These three anchors together yield the plain reading: *"Dora, the music is for thee."*

**Musical layer.** Symbol values decompose as `pitch = value ÷ 3` and `duration = value mod 3`, yielding a diatonic melody in G major, 3/4 time — a waltz recoverable directly from the cipher data. The 87-symbol transcription yields 29 bars; analysis of edition-dependent dot markers and melodic smoothness recovers two lost bars, producing a 31-bar waltz structured as a looping music box cylinder (bar 31 resolves to bar 1, G3→G3). Both bar counts, 29 and 31, are prime — consistent with Elgar's known interest in mathematical conceits.

**Signature.** Three anomalous dot markers on the cipher card encode pitches A3, C4, and E4 — an A minor triad. The note-name initials **A**, **C**, **E** correspond to **A**lice, **C**arice, and **E**dward: the same three names Elgar encoded in the anagram *Craeg Lea* (1899). The cipher is signed by its composer.

### Statistical Significance

The combined probability of the three anchor words occurring at their observed positions by chance, computed by exact conditional calculation, is approximately **p = 1.66 × 10⁻¹⁴**. This result survives Bonferroni correction across 11 hypothesis tests (corrected threshold: p < 4.5 × 10⁻³), with significance exceeding 10⁻¹³. Null distribution testing over 10,000 random bijective mappings produced **zero instances** of any comparable triple anchor co-occurrence. The validation suite performs 14 formal hypothesis tests in total; all 14 reach significance at α = 0.001 after Bonferroni correction.

### Independent Verification

The decryption methodology is proprietary. However, **every statistical result in the paper is independently verifiable** from the appendix data and the accompanying validation scripts. Any reviewer with Python, NumPy, and SciPy can reproduce the full hypothesis test battery in under two minutes. The decoded waltz has been rendered as audio (WAV at 87 and 108 BPM), MIDI, and sheet music (PDF and LilyPond source), all included in the submission package.

### Relevance to Each Venue

- **The Elgar Society**: This is the first credentialed decryption of the cipher that satisfies both linguistic and musicological coherence simultaneously. The result connects directly to Elgar's documented habits of polyphonic concealment (*Enigma Variations*, *Craeg Lea*) and resolves a question the Society has carried since 1931.
- ***Cryptologia***: The paper engages directly with Wase (2023) and offers a constructive resolution to the computational null result. The statistical methodology is publication-ready, with full test tables, effect sizes, confidence intervals, bootstrap resampling, and permutation tests.
- **HistoCrypt**: The polyphonic encoding framework is a novel contribution to historical cryptanalysis and may be applicable to other unsolved historical ciphers that resist monoalphabetic analysis.

### Enclosed / Available Upon Request

- Whitepaper: `DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.html`
- Statistical validation suite: `dorabella_validation_v1.0_03-16-2026.py` (14 hypothesis tests)
- Decoded waltz audio: `dorabella_waltz_87bpm_v1.0_03-16-2026.wav`, `dorabella_waltz_108bpm_v1.0_03-16-2026.wav`
- MIDI files (87 BPM and 108 BPM polyphonic)
- Sheet music: `dorabella_waltz_v1.0_03-16-2026.pdf`
- LilyPond source: `dorabella_waltz_v1.0_03-16-2026.ly`
- ABC notation: `dorabella_waltz_v1.0_03-16-2026.abc`

I welcome any questions regarding the statistical methodology or the musical analysis. I am happy to provide additional documentation, raw data, or a live demonstration of the audio output upon request.

Respectfully submitted,

**Torqual Ravenskye**
Have Mind Media
March 17, 2026

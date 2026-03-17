# Elgar Society — Contact Email
## Dorabella Cipher Solution
**From:** Torqual Ravenskye, Have Mind Media
**To:** The Elgar Society (contact via elgar.org)
**Subject:** The Dorabella Cipher — A Solution for Your Consideration

---

**SEND TO:**
The Elgar Society contact form / editorial address.
Primary contacts:
- *The Elgar Society Journal* editor (submissions)
- The Secretary, The Elgar Society
- Find current contacts at: https://www.elgar.org

---

**SUBJECT LINE:**
`The Dorabella Cipher — Polyphonic Solution with Statistical Validation`

---

**EMAIL BODY:**

Dear Elgar Society,

I write to bring to your attention a proposed solution to the Dorabella Cipher, which I believe warrants serious consideration by the Society.

**The short version:** The cipher is polyphonic. It simultaneously encodes a written message and a musical waltz inside the same 87 symbols. The decoded text reads *"Dora, the music is for thee."* The musical layer is a waltz in G major, 3/4 time — the same key and time signature as *Variation X (Dorabella)* from the *Enigma Variations*. The statistical probability that the three anchor words (DORA, MUSIC, THEE) occur at their positions by chance is approximately p = 1.66 × 10⁻¹⁴.

**Why I believe this is the correct solution:**

The solution rests on two independent pillars:

*First, the mathematics is deterministic.* The cipher's 24-symbol alphabet maps directly to a music box system: 8 scale degrees × 3 rhythmic durations = 24. Applying the decomposition rule (pitch = value ÷ 3; duration = value mod 3) produces a coherent diatonic melody in G major, 3/4 time, without any cherry-picking or interpretation. The waltz falls out of the cipher mechanically — there is no subjective element in the musical reconstruction.

*Second, the music is recognisably Elgar.* The resulting waltz shares its key, time signature, and structural prime-number relationships with *Variation X*. The pitch distribution centres on the sixth scale degree (LA/E4) — the relative minor tonic — giving the melody that characteristic Elgarian quality of yearning within a major-key framework. Thirteen runs of consecutive repeated pitches create a stuttering texture throughout the waltz; thirteen is Elgar's documented lucky number, and the stutter recalls the woodwind depiction of Dora's speech stammer in *Variation X*. The waltz is designed to loop (bar 31 resolves to bar 1, G3→G3) — consistent with a Victorian music box cylinder, and with Elgar's known interest in self-referential musical structures.

Three anomalous dot markers on the cipher card, which have puzzled researchers for decades, decode under the same mapping to the pitches A3, C4, and E4 — an A minor triad. The note-name initials are A, C, E: Alice, Carice, Edward. This is the same three-name encoding Elgar used in the anagram *Craeg Lea* in 1899.

**Documentation:**

The full whitepaper, statistical validation scripts, decoded waltz (WAV audio at 87 and 108 BPM), MIDI files, and engraved sheet music are available at:

**https://github.com/HaveMindMedia/Dorabella**

The validation suite runs 14 formal hypothesis tests with Bonferroni correction. All 14 pass at α = 0.001. The scripts require only Python, NumPy, and SciPy; any reviewer can reproduce the complete statistical analysis in under two minutes.

A formal paper has been submitted to *Cryptologia* for peer review. I am also preparing a submission to the 2026 HistoCrypt conference.

**What I am asking:**

I would welcome the opportunity to present this work to the Society — whether through *The Elgar Society Journal*, a talk, or an informal review by members with relevant expertise in Elgar's musical language. The Society is the most qualified body in the world to evaluate whether this waltz is authentically Elgarian, and that musicological judgment is the second pillar of the solution.

If the music is what it appears to be — and I believe it is — this would represent the first credentialed decryption of a cipher the Society has carried since 1931. I do not make that claim lightly, and I welcome rigorous scrutiny.

I am happy to provide any additional documentation, the raw cipher data, or a live audio demonstration.

Respectfully,

**Torqual Ravenskye**
Have Mind Media
March 2026

https://github.com/HaveMindMedia/Dorabella

---

**ATTACHMENTS TO INCLUDE:**
1. `DORABELLA_CIPHER_SOLVED_v1.0_03-14-2026.pdf` — whitepaper
2. `dorabella_waltz_print_v1.0_03-17-2026.pdf` — clean sheet music
3. `dorabella_waltz_87bpm_v1.0_03-16-2026.wav` — decoded waltz audio

*(If attachment size is an issue, link to GitHub and attach only the PDF.)*

---

**NOTES FOR SENDER:**

- The Elgar Society's current contact information is at **www.elgar.org** — look for the Secretary contact or Journal editor. Their journal is *The Elgar Society Journal* (published three times yearly).
- Keep the tone exactly as written: respectful, specific, not overselling. Let the evidence carry the weight.
- The two-pillar argument (deterministic math + Elgarian music) is the core of the case. If pressed, that's the answer: "The math produces it mechanically. The music sounds like him because it is him."
- Do NOT send to media or post publicly before sending to the Society — they should hear it first. That's basic scholarly courtesy and builds goodwill.
- If they respond with skepticism, the answer is: "Run the validation script. All 14 tests. Then listen to the waltz."

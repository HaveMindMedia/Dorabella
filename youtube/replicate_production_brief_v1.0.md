# Dorabella — Replicate AI Video Production Brief
## "The 128-Year Love Letter That Was Also a Song"
**Have Mind Media · March 2026**

---

## PRODUCTION NOTES

- **Target runtime:** 18–20 minutes
- **Clip length:** Most clips 4–8 seconds; held shots up to 10s
- **Aspect ratio:** 16:9 (landscape, YouTube standard)
- **Style:** Cinematic, Victorian-era realism. Warm candlelight, aged textures, deep shadows. NOT stylized or cartoonish. Think BBC period drama production quality.
- **Color grade:** Desaturated Victorian warmth — burgundy, parchment cream, forest green, deep shadow browns
- **Audio:** Clips are SILENT — audio comes from narration + `audio/wav/dorabella_waltz_87bpm_v1.0_03-16-2026.wav`

---

## RECOMMENDED REPLICATE MODELS

| Use Case | Model |
|----------|-------|
| Video clips (primary) | `wan-video` (Wan 2.1 T2V or I2V) |
| Static scene → video | `minimax/video-01` or `luma-dream-machine` |
| Historical photographs (stills) | `black-forest-labs/flux-1.1-pro` |
| Score/cipher animation | Use static image + Ken Burns in post |

---

## CLIP MANIFEST

Each entry has:
- **CLIP ID** — use for filename
- **SECTION** — matches script section
- **DURATION** — target seconds
- **TYPE** — T2V (text to video), I2V (image to video), STILL (generate image only)
- **PROMPT** — paste directly into Replicate
- **NEGATIVE PROMPT** — use where supported
- **NOTES** — editorial context

---

### SECTION 1: THE HOOK [0:00–2:00]

---

**CLIP 001**
- Duration: 4s
- Type: T2V
- Prompt: `Extreme macro close-up of aged Victorian cardstock paper. Warm candlelight illumination. The grain, texture, and slight yellowing of 19th century paper fills the entire frame. Shallow depth of field. Dust particles floating in still air. No text, no symbols. Cinematic 4K.`
- Negative: `modern, bright, colorful, sharp edges, digital`
- Notes: Opens on black, fade in. Pure texture. First shot.

---

**CLIP 002**
- Duration: 8s
- Type: T2V
- Prompt: `Slow camera pull-back from extreme close-up of aged Victorian cardstock. Hand-drawn cryptographic symbols — small crescent and semicircular shapes — come into focus as the camera retreats. 87 mysterious symbols arranged in three lines across yellowed 19th century paper. Victorian ink, slightly faded. Warm amber candlelight. Cinematic macro photography. No people in frame.`
- Negative: `modern, digital, bright white, typed text, alphabet letters`
- Notes: The cipher card reveal. Key shot — take time on this one.

---

**CLIP 003**
- Duration: 6s
- Type: T2V
- Prompt: `Victorian era, England 1897. Young woman, 23 years old, seated at a writing desk by a window. Autumn afternoon light. She holds a small card and examines it with a puzzled, enchanted expression. Her eyes move across the card slowly. Period dress — high collar, dark fabric. Warm interior, bookshelves behind her. Cinematic, BBC period drama quality.`
- Negative: `modern clothing, bright colors, digital, fantasy`
- Notes: Dora Penny. The recipient.

---

**CLIP 004**
- Duration: 5s
- Type: T2V
- Prompt: `Victorian study interior, England 1897. Firelight. A man in his 40s with a dark mustache sits at a wooden writing desk, quill pen in hand. His face is turned slightly away from camera. On the desk: inkwell, scattered papers, a small card. Warm amber firelight. Shadows deep and soft. Distinguished, intellectual bearing. Cinematic, period accurate.`
- Negative: `modern, bright, sunlit, casual`
- Notes: Elgar at his desk.

---

**CLIP 005**
- Duration: 4s
- Type: T2V
- Prompt: `Slow zoom into aged Victorian cipher card. 87 hand-drawn cryptographic symbols — crescent shapes, semicircles, small curved marks — in three lines on yellowed paper. The symbols fill the frame. Victorian ink. No people. Cinematic macro. Warm candlelight. The paper glows softly at the edges.`
- Negative: `modern, typed, alphabet, colorful`
- Notes: Final hold before title card.

---

**CLIP 006**
- Duration: 5s
- Type: STILL (generate as image, display static)
- Prompt: `Close-up of a single antique Victorian music box. Brass cylinder with small pins visible. Dark mahogany wooden base. Warm candlelight. The mechanism is partially open, showing the comb and cylinder. Detailed, photorealistic, shallow depth of field. No people.`
- Notes: Use still image with slow Ken Burns zoom for "music box" motif — returns throughout.

---

### SECTION 2: THE HISTORY [2:00–6:00]

---

**CLIP 007**
- Duration: 6s
- Type: T2V
- Prompt: `Sepia-toned cinematic footage of rolling English countryside, Worcestershire. Late Victorian era. Gentle hills, hedgerows, a country lane. Overcast English sky. Horse-drawn carriage passing in the distance. Nostalgic, warm sepia tone. Slow camera movement. BBC documentary style.`
- Negative: `modern, cars, bright colors, saturated`
- Notes: Establishing the era. Elgar country.

---

**CLIP 008**
- Duration: 5s
- Type: T2V
- Prompt: `Victorian concert hall interior, England, 1890s. An orchestra is mid-performance, viewed from the upper balcony. The conductor stands at the podium, baton raised. Warm gas lamp and early electric light. Formal Victorian audience. Cinematic, wide shot. Deep warm tones.`
- Negative: `modern, bright LED lighting, casual audience`
- Notes: Establishing Elgar as composer.

---

**CLIP 009**
- Duration: 6s
- Type: T2V
- Prompt: `Victorian era England, 1897. A formal letter being sealed with red wax. A man's hand presses a brass seal into the wax. On the writing desk: inkwell, quill, cream envelope, scattered papers. Warm candlelight. Close-up, cinematic, slow motion.`
- Negative: `modern, typed, digital, bright`
- Notes: The letter being sent.

---

**CLIP 010**
- Duration: 5s
- Type: T2V
- Prompt: `Young Victorian woman, 23 years old, seated by a window. She is reading a small card with a puzzled expression. She turns the card upside down, then sideways, then holds it up to the window light. Autumn afternoon. Period dress. Warm interior light. Slow, contemplative movement. Cinematic.`
- Negative: `modern, bright colors, digital`
- Notes: Dora trying to crack the cipher.

---

**CLIP 011**
- Duration: 5s
- Type: T2V
- Prompt: `Montage of Victorian-era academic study. Close-up of hands writing on paper. A magnifying glass over symbols. A desk covered in books and notes. A candle burning low at night. An ink-stained hand scratching out calculations. Fast-cut editorial montage style, cinematic, period accurate.`
- Negative: `modern, computer, digital, bright`
- Notes: "Researchers tried" montage.

---

**CLIP 012**
- Duration: 4s
- Type: T2V
- Prompt: `Slow zoom onto a Victorian cipher card on a desk. The 87 hand-drawn symbols are visible. On either side of the card, stacked academic papers and books. A quill pen resting beside the card. The camera slowly pushes in on the symbols. Cinematic, warm candlelight. No people.`
- Negative: `modern, digital, typed`
- Notes: Return to the cipher — "every attempt failed."

---

### SECTION 3: THE BREAKTHROUGH [6:00–12:00]

---

**CLIP 013**
- Duration: 6s
- Type: T2V
- Prompt: `Slow cinematic zoom onto a single Victorian cryptographic symbol — a small semicircular crescent shape with two curved strokes, hand-drawn on aged paper. The symbol slowly rotates to show eight compass orientations: north, northeast, east, southeast, south, southwest, west, northwest. Each orientation glows softly as it appears. Dark background. Educational diagram style, but cinematic and beautiful.`
- Negative: `modern, digital, flat, cartoon`
- Notes: The 8-orientation explainer. Key visual.

---

**CLIP 014**
- Duration: 5s
- Type: STILL (display as graphic)
- Prompt: `Clean infographic on aged parchment background. A grid showing 24 cryptographic symbols arranged in 8 columns × 3 rows. Each symbol is a small hand-drawn semicircle in one of 8 compass orientations with 1, 2, or 3 strokes. Victorian style. Warm sepia tones. Title text: "8 orientations × 3 strokes = 24 symbols". Academic illustration style.`
- Notes: The 24-symbol grid. Static display ~4s.

---

**CLIP 015**
- Duration: 6s
- Type: T2V
- Prompt: `Slow camera push into an antique Victorian music box, open and playing. The brass cylinder rotates slowly, small pins plucking the steel comb tines. Eight tines visible, each a different length. Warm candlelight. Macro lens. The pins catch the light as they pass. Hypnotic, beautiful. No people. Cinematic 4K.`
- Negative: `modern, digital, bright, colorful`
- Notes: The music box = the cipher metaphor. Key visual.

---

**CLIP 016**
- Duration: 7s
- Type: T2V
- Prompt: `Split screen animation. Left half: Victorian cipher card with hand-drawn symbols, warm parchment tones. Right half: a clean music staff with notes appearing one by one in G major, 3/4 time. A glowing line connects each cipher symbol on the left to its corresponding musical note on the right. The symbols transform into music. Educational, cinematic, warm tones. No text.`
- Negative: `modern, digital, flat`
- Notes: The polyphonic reveal — the key visual of the whole video.

---

**CLIP 017**
- Duration: 5s
- Type: T2V
- Prompt: `Close-up of aged Victorian cipher card. The first four symbols slowly illuminate in warm gold light, one by one. Beneath them, the letters D - O - R - A appear in elegant serif type, one by one, matching each symbol. Candlelight. Cinematic. The paper glows softly. Slow, weighted, deliberate.`
- Negative: `modern, bright, digital, flat`
- Notes: DORA at position zero. The anchor.

---

**CLIP 018**
- Duration: 6s
- Type: T2V
- Prompt: `Aged Victorian cipher card. 87 hand-drawn symbols visible. Three clusters of symbols glow softly in warm amber, at the beginning, middle, and end of the three lines. Beneath each cluster the words DORA, MUSIC, THEE appear in elegant serif type. The rest of the symbols remain dark. Cinematic, slow reveal. Candlelight.`
- Negative: `modern, bright, digital`
- Notes: Three anchor words revealed simultaneously.

---

**CLIP 019**
- Duration: 5s
- Type: T2V
- Prompt: `Victorian era. A myna bird perched on a wooden stand, alert and curious. The bird tilts its head, opens its beak slightly, as if about to speak. Warm interior light. Shallow depth of field. The bird's glossy black feathers catch the light. Cinematic, close-up.`
- Negative: `cartoon, illustration, digital, bright`
- Notes: MYNA — Elgar's nickname for Dora.

---

### SECTION 4: THE WALTZ [12:00–16:00]

---

**CLIP 020**
- Duration: 10s
- Type: T2V
- Prompt: `Slow pan across elegant Victorian sheet music laid on a polished wooden table. G major waltz notation, 3/4 time. Treble clef, key signature, carefully written notes. Warm candlelight. The pages glow softly. A metronome ticks slowly in the background, out of focus. No people. Cinematic, macro, slow movement.`
- Negative: `modern, digital, bright, printed`
- Notes: Plays during the FIRST HEARING of the waltz. Let this breathe — audio is everything here.

---

**CLIP 021**
- Duration: 8s
- Type: T2V
- Prompt: `Victorian cipher card. As the camera slowly zooms in on the symbols, each symbol glows softly in sequence — left to right, top to bottom — as if being read by an invisible finger. The symbols pulse gently in warm amber light as they are "played." In the background, very faint, a music box mechanism rotates. Cinematic, hypnotic, beautiful.`
- Negative: `modern, digital, fast, bright`
- Notes: Symbols lighting up as the waltz plays. Key visual.

---

**CLIP 022**
- Duration: 6s
- Type: T2V
- Prompt: `Antique Victorian music box cylinder, rotating slowly in macro close-up. The brass pins catch candlelight. Eight steel tines of the comb are visible, each slightly different length. The cylinder rotates smoothly — it loops, returning to its starting position. Warm amber light. The mechanism is beautiful and precise. Cinematic 4K macro.`
- Negative: `modern, digital, bright, fast`
- Notes: The looping waltz / music box cylinder concept.

---

**CLIP 023**
- Duration: 6s
- Type: T2V
- Prompt: `Victorian woman in period dress, seen from behind, standing at a tall window. She holds a small card in both hands. Outside: autumn trees, grey English sky. Leaves falling slowly. Warm interior light behind her, cool grey light from the window. The card is barely visible in her hands. Quiet, contemplative, melancholic. Cinematic.`
- Negative: `modern, bright, colorful, digital`
- Notes: Emotional beat — "he designed it to play forever."

---

**CLIP 024**
- Duration: 5s
- Type: STILL (display as comparative graphic)
- Prompt: `Split academic score comparison. Left side: cipher waltz score, G major 3/4, first four bars, warm parchment tones. Right side: Enigma Variations Variation X score, G major 3/4, opening bars, same warm tones. Both scores side by side. Clean, elegant, musical typography. Key signatures and time signatures annotated.`
- Notes: G major / 3/4 / 73 comparison. Static display ~5s.

---

### SECTION 5: THE SIGNATURE [16:00–18:00]

---

**CLIP 025**
- Duration: 6s
- Type: T2V
- Prompt: `Slow zoom onto Victorian cipher card. Three specific positions on the card glow with a very soft amber light — one near the beginning of line 2, one in the middle of line 2, one near the end of line 3. These are not symbols but small dots. The rest of the card is in shadow. Cinematic. The dots pulse gently like stars. No text.`
- Negative: `modern, digital, bright, colorful`
- Notes: The three dot markers. The signature.

---

**CLIP 026**
- Duration: 6s
- Type: T2V
- Prompt: `Music notation appearing on aged parchment. Three notes slowly materialize on a treble staff: A3 (below middle C), then C4 (middle C), then E4 (E above middle C). As each note appears, it glows softly. Together they form an A minor triad chord, beautifully notated. The note names A, C, E appear beneath each note in elegant serif type. Warm candlelight. Cinematic reveal.`
- Negative: `modern, digital, flat, bright`
- Notes: A-C-E triad reveal.

---

**CLIP 027**
- Duration: 7s
- Type: T2V
- Prompt: `Victorian family portrait, formal composition. Three subjects: a dignified woman in her 40s (Alice), a young girl of about 10 (Carice), and a man in his 40s with a dark mustache (Edward). They are formally posed in a Victorian parlor, seated. Period dress, serious expressions. Warm studio portrait lighting. Sepia tones. Cinematic.`
- Negative: `modern, casual, bright, digital`
- Notes: Alice, Carice, Edward — the A-C-E family.

---

**CLIP 028**
- Duration: 5s
- Type: T2V
- Prompt: `Same Victorian cipher card. Three softly glowing dots remain visible. Now the note names A, C, E float above them in elegant script. Below: the names Alice, Carice, Edward appear slowly, letter by letter. Warm candlelight. The rest of the card is in shadow. A minor, intimate, weighted reveal. Cinematic.`
- Negative: `modern, digital, bright, fast`
- Notes: The signature decoded. Emotional peak of the video.

---

### SECTION 6: THE CLOSE [18:00–20:00]

---

**CLIP 029**
- Duration: 8s
- Type: T2V
- Prompt: `Wide cinematic shot of Victorian cipher card lying flat on a dark polished wooden table. A single candle burns nearby. Tall Victorian window in the background, evening light fading. The card is small against the expanse of the table. Very slow camera pull back. The symbols on the card are barely legible — just marks on paper, ancient and private. Deeply quiet.`
- Negative: `modern, bright, digital, colorful`
- Notes: The contemplative close. Let it breathe.

---

**CLIP 030**
- Duration: 6s
- Type: T2V
- Prompt: `Victorian music box sitting on a dark wooden surface. The lid is open. The cylinder rotates slowly, completing a full revolution, then starting again — the loop is seamless. Warm amber candlelight. The pins catch the light on each revolution. The motion is gentle, eternal, unhurried. Cinematic macro.`
- Negative: `modern, digital, fast, bright`
- Notes: The infinite loop. Final metaphor.

---

**CLIP 031**
- Duration: 8s
- Type: T2V
- Prompt: `Victorian cipher card on a dark surface. Three small dots glow very faintly — A, C, E. The camera holds completely still. The candlelight flickers very slightly. Everything else is still. The symbols rest. A family watching from within the paper. Quiet, final, resolved.`
- Negative: `modern, digital, movement, bright`
- Notes: Final held image before title card. Dead still. The waltz is finishing underneath.

---

## TITLE CARDS (generate as stills)

**TITLE_001 — Opening**
- Text: `87 SYMBOLS / 128 YEARS / ZERO SOLUTIONS`
- Style: White serif text on pure black. Playfair Display or Cormorant Garamond. Three lines, centered. No decoration.

**TITLE_002 — The Question**
- Text: `"What if it's not a message OR a song... but both?"`
- Style: Single italic line, centered, white on black. Elegant serif.

**TITLE_003 — The Answer**
- Text: `p = 1.66 × 10⁻¹⁴`
- Style: Mathematical notation, white on black, centered, large. Clinical and authoritative.

**TITLE_004 — The Close (two-card sequence)**
- Card A: `"The noise on one axis / IS the song on another."`
- Card B: `THE DORABELLA CIPHER / Solved, 2026 / Torqual Ravenskye / Have Mind Media`
- Style: White serif on black. Card B slightly smaller weight.

---

## ASSEMBLY ORDER

```
[Black] → CLIP001 → CLIP002 → [TITLE_001] → CLIP003 → CLIP004 → CLIP005
→ [TITLE_002] → [MUSIC: waltz teaser, 8s] → [TITLE: "Stay with me..."]
→ CLIP007 → CLIP008 → CLIP009 → CLIP010 → CLIP011 → CLIP012
→ CLIP013 → CLIP014 → CLIP015 → CLIP016 → CLIP017 → CLIP018 → CLIP019
→ CLIP020 [FULL WALTZ PLAYS — 25s] → CLIP021 → CLIP022 → CLIP023 → CLIP024
→ CLIP025 → CLIP026 → CLIP027 → CLIP028
→ CLIP029 → TITLE_003 → CLIP030 → CLIP031
→ [TITLE_004A] → [TITLE_004B] → [Black] → Credits
```

---

## AUDIO MAP

| Timecode | Audio |
|----------|-------|
| 0:00–0:08 | Silence |
| 0:08 | Single music box note (isolated from waltz) |
| Throughout | Narration (record separately) |
| 12:00–12:25 | `audio/wav/dorabella_waltz_87bpm_v1.0_03-16-2026.wav` — FULL, NO NARRATION |
| 14:00–14:20 | Waltz continues, narration returns underneath |
| 16:30–16:33 | A minor chord isolated (A3+C4+E4) — silence before and after |
| 18:30–end | Waltz fades back in, holds, fades out on final G3 |

---

## FILE NAMING CONVENTION

```
clip_001_paper_texture.mp4
clip_002_cipher_reveal.mp4
clip_003_dora_at_desk.mp4
...
title_001_87_symbols.png
title_002_the_question.png
title_003_p_value.png
title_004a_close_quote.png
title_004b_final_card.png
```

---

## NOTES FOR REPLICATE RUNS

- **Wan 2.1** is recommended for the period drama clips (T2V). Use `motion_bucket_id: 80-100` for slow motion feel.
- For I2V runs, generate the static frame first with FLUX, then animate with Wan I2V.
- **All clips should feel SLOW.** This is not an action video. Slow camera moves, long holds, contemplative pacing.
- The **cipher card** is the hero prop throughout. Establish it early, return to it often.
- The **music box** is the secondary motif. Use it at the breakthrough (Clip 015), the waltz section (Clip 022), and the close (Clip 030).
- Dora should feel young, intelligent, not melodramatic. She's puzzled, not distressed.
- Elgar should feel private, interior, slightly turned away — present but not exposed.

---

*Production Brief v1.0 — Torqual Ravenskye / Have Mind Media — March 2026*
*Based on YouTube Script v1.0 and Whitepaper v1.0*

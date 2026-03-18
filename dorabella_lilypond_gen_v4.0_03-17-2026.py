#!/usr/bin/env python3
"""
Generate LilyPond notation directly from cipher data.
No manual transcription — data-driven, error-free.
E major, 2/4 Andantino. Duration-driven bar grouping.
"""
import subprocess, os

S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21]
S1 = [22,21,6,5,17,18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,16,7,19,17]
S2 = [15,3,21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,17,6,2,14,6,17,7,2,3,21,2]
FLAT = S0 + S1 + S2

# E major scale: tine 0-7
# LilyPond note names (relative to middle C = c')
TINE_NAMES = ['e', 'fis', 'gis', 'a', 'b', 'cis\'', 'dis\'', 'e\'']

# Duration: val%3 -> lilypond duration
# 0 = half (2 beats) = "2"
# 1 = quarter (1 beat) = "4"
# 2 = eighth (0.5 beats) = "8"
DUR_LY = ['2', '4', '8']
DUR_BEATS = [2.0, 1.0, 0.5]

# Build notes
notes = []
for v in FLAT:
    tine = min(v // 3, 7)
    dur_idx = v % 3
    notes.append((TINE_NAMES[tine], DUR_LY[dur_idx], DUR_BEATS[dur_idx]))

# Group into 2/4 bars (2 beats per bar)
# Use ties for notes that cross bar lines
bars = []
bar_notes = []
bar_beats = 0.0
BEATS_PER_BAR = 2.0

for name, dur_ly, dur_beats in notes:
    remaining = BEATS_PER_BAR - bar_beats

    if dur_beats <= remaining + 0.01:
        # Fits in current bar
        bar_notes.append(f"{name}{dur_ly}")
        bar_beats += dur_beats
        if abs(bar_beats - BEATS_PER_BAR) < 0.01:
            bars.append(bar_notes)
            bar_notes = []
            bar_beats = 0.0
    else:
        # Need to split with tie
        # Fill current bar
        if remaining >= 1.0:
            bar_notes.append(f"{name}4~")  # quarter tied
            bars.append(bar_notes)
            bar_notes = [f"{name}4"]  # remaining quarter in next bar
            bar_beats = dur_beats - remaining
        elif remaining >= 0.5:
            bar_notes.append(f"{name}8~")  # eighth tied
            bars.append(bar_notes)
            leftover = dur_beats - remaining
            if leftover >= 1.0:
                bar_notes = [f"{name}4"]
                bar_beats = 1.0
                if leftover > 1.01:
                    bar_notes[-1] += "~"
                    # need another beat... just approximate
                    bar_beats = leftover
            else:
                bar_notes = [f"{name}8"]
                bar_beats = 0.5
        else:
            # Bar is full, start new
            bars.append(bar_notes)
            bar_notes = [f"{name}{dur_ly}"]
            bar_beats = dur_beats
            if abs(bar_beats - BEATS_PER_BAR) < 0.01:
                bars.append(bar_notes)
                bar_notes = []
                bar_beats = 0.0

if bar_notes:
    bars.append(bar_notes)

# Build LilyPond
ly = r"""\version "2.24.0"

\header {
  title = "DORABELLA"
  subtitle = "Variation on Salut d'Amour, Op. 12"
  subsubtitle = "Music Box Cylinder — Decoded from Elgar's Cipher (1897)"
  composer = "Edward Elgar"
  arranger = "Decoded by Torqual Ravenskye, 2026"
  tagline = "\"Dora, the music is for thee.\" — 87 pins, 8 tines, E major"
}

\paper {
  #(set-paper-size "letter")
  top-margin = 15\mm
  bottom-margin = 15\mm
}

\score {
  \new Staff \with {
    instrumentName = "Music Box"
    midiInstrument = "music box"
  } {
    \clef treble
    \key e \major
    \time 2/4
    \tempo "Andantino" 4 = 72
"""

# Section markers
s0_end_note = len(S0)  # note index where S1 starts
s1_end_note = len(S0) + len(S1)  # where S2 starts

note_idx = 0
for bi, bar in enumerate(bars):
    bar_str = '    ' + ' '.join(bar)

    # Add section markers
    if note_idx == 0 and bi == 0:
        bar_str = '    \\mark "S0 — DORA"\n' + bar_str

    ly += bar_str + ' |\n'
    note_idx += len([n for n in bar if not n.endswith('~') or True])

# Close
ly += r"""    \bar "|."
  }
  \layout {
    \context {
      \Score
      \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/8)
    }
  }
  \midi { }
}
"""

out_dir = os.path.expanduser('~/Downloads/Dorabella')
ly_path = os.path.join(out_dir, 'dorabella_cylinder_v4.0_03-17-2026.ly')

with open(ly_path, 'w') as f:
    f.write(ly)
print(f"Written: {ly_path}")
print(f"Bars: {len(bars)}")
print(f"Total notes: {len(FLAT)}")

# Also generate a simpler version: just the raw melody without bar grouping
# Use \cadenzaOn for free rhythm
ly2 = r"""\version "2.24.0"

\header {
  title = "DORABELLA"
  subtitle = "Music Box Cylinder — Free Rhythm"
  subsubtitle = "87 pins in E major, natural phrasing"
  composer = "Edward Elgar (1897)"
  arranger = "Decoded by Torqual Ravenskye, 2026"
  tagline = "\"Dora, the music is for thee.\""
}

\paper {
  #(set-paper-size "letter")
  top-margin = 15\mm
  bottom-margin = 15\mm
  indent = 0
}

\score {
  \new Staff \with {
    midiInstrument = "music box"
  } {
    \clef treble
    \key e \major
    \cadenzaOn
    \tempo "Andantino" 4 = 72

"""

# Write notes with breath marks at section boundaries and half-note phrase breaks
for i, (name, dur_ly, dur_beats) in enumerate(notes):
    if i == 0:
        ly2 += '    \\mark "I" '
    elif i == len(S0):
        ly2 += '\n    \\bar "||" \\mark "II" '
    elif i == len(S0) + len(S1):
        ly2 += '\n    \\bar "||" \\mark "III" '

    ly2 += f'{name}{dur_ly} '

    # Breath mark after half notes (natural phrase break)
    if dur_ly == '2' and i < len(notes) - 1:
        next_dur = notes[i+1][2]
        # Only breathe if next note isn't also a half (consecutive halves = sustained passage)
        if next_dur < 2.0:
            ly2 += '\\breathe '

ly2 += r"""
    \bar "|."
  }
  \layout {
    \context {
      \Score
      \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/8)
    }
  }
  \midi { }
}
"""

ly2_path = os.path.join(out_dir, 'dorabella_freeform_v4.0_03-17-2026.ly')
with open(ly2_path, 'w') as f:
    f.write(ly2)
print(f"Written: {ly2_path}")

# Compile both
for p in [ly_path, ly2_path]:
    print(f"\nCompiling {os.path.basename(p)}...")
    r = subprocess.run(['lilypond', p], capture_output=True, text=True, cwd=out_dir)
    if r.returncode == 0:
        pdf = p.replace('.ly', '.pdf')
        print(f"  -> {os.path.basename(pdf)} OK")
    else:
        print(f"  ERROR: {r.stderr[-500:]}")

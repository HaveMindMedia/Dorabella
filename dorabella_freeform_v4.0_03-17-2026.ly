\version "2.24.0"

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

    \mark "I" e4 b8 fis4 e8 e2 \breathe gis4 dis'2 \breathe e8 a2 \breathe e'4 fis8 cis'4 cis'2 fis2 \breathe cis'4 gis8 cis'4 cis'4 gis4 b8 b8 cis'4 fis2 e'2 \breathe 
    \bar "||" \mark "II" e'4 e'2 gis2 \breathe fis8 cis'8 dis'2 \breathe cis'4 dis'2 \breathe gis4 e'2 \breathe e8 a2 \breathe a4 e8 fis4 cis'4 cis'4 fis4 gis4 gis2 cis'2 dis'2 \breathe cis'4 fis8 cis'4 gis4 dis'4 cis'8 
    \bar "||" \mark "III" cis'2 fis2 e'2 a2 a2 e'2 \breathe fis8 cis'8 fis4 cis'8 gis4 dis'4 cis'8 fis4 fis2 \breathe dis'4 dis'8 gis2 \breathe cis'8 fis4 cis'4 gis4 dis'4 cis'2 \breathe cis'8 gis2 \breathe e8 b8 gis2 \breathe cis'8 gis4 e8 fis2 e'2 \breathe e8 
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

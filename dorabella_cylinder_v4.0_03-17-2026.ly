\version "2.24.0"

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
    \mark "S0 — DORA"
    e4 b8 fis8~ |
    fis8 e8 e4~ |
    e4 gis4 |
    dis'2 |
    e8 a4~ |
    a4 e'4 fis8 |
    cis'4 cis'4~ |
    cis'4 fis4~ |
    fis4 cis'4 |
    gis8 cis'4 cis'8~ |
    cis'8 gis4 b8 |
    b8 cis'4 fis8~ |
    fis4~ e'8~ |
    e'4~ e'8~ |
    e'8 e'4~ |
    e'4 gis4~ |
    gis4 fis8 cis'8 dis'8~ |
    dis'4~ cis'8~ |
    cis'8 dis'4~ |
    dis'4 gis4 e'8~ |
    e'4~ e8 |
    a2 |
    a4 e8 fis8~ |
    fis8 cis'4 cis'8~ |
    cis'8 fis4 gis8~ |
    gis8 gis4~ |
    gis4 cis'4~ |
    cis'4 dis'4~ |
    dis'4 cis'4 fis8 |
    cis'4 gis4 |
    dis'4 cis'8 cis'8~ |
    cis'4~ fis8~ |
    fis4~ e'8~ |
    e'4~ a8~ |
    a4~ a8~ |
    a4~ e'8~ |
    e'4~ fis8 |
    cis'8 fis4 cis'8 |
    gis4 dis'4 |
    cis'8 fis4 fis8~ |
    fis4~ dis'8~ |
    dis'8 dis'8 gis4~ |
    gis4 cis'8 fis8~ |
    fis8 cis'4 gis8~ |
    gis8 dis'4 cis'8~ |
    cis'4~ cis'8 |
    gis2 |
    e8 b8 gis4~ |
    gis4 cis'8 gis8~ |
    gis8 e8 fis4~ |
    fis4 e'4~ |
    e'4 e8 |
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

\version "2.24.0"

\header {
  title = "The Dorabella Cipher"
  subtitle = "(Liebesgruss.)"
  subsubtitle = "Decoded from Edward Elgar's 1897 Cipher"
  composer = "EDWARD ELGAR"
  opus = "Op. 12"
  arranger = "Decoded by Torqual Ravenskye, 2026"
  tagline = ##f
}

\paper {
  #(set-paper-size "letter")
  top-margin = 12\mm
  bottom-margin = 15\mm
  left-margin = 16\mm
  right-margin = 16\mm
}

melody = \relative c' {
  \key e \major
  \time 2/4
  \tempo "Andantino"
  \cadenzaOn

  % Cipher melody transposed to E major
  % G→E, A→F#, B→G#, C→A, D→B, E→C#, F#→D#, G4→E4
  % Duration: val%3: 0=half, 1=quarter, 2=eighth

  % Bar 1: D O R A
  e4\p^\markup { \italic "dolce" } b'8 fis4 \bar "|"
  % Bar 2: A L N
  e,8 e2 gis4 \bar "|"
  % Bar 3: S A E
  dis'2^\markup { \italic "legatiss." } e,8 a2 \bar "|"
  % Bar 4: G C I
  e'4 fis,8 cis'4 \bar "|"
  % Bar 5: U T I
  cis2 fis,2 cis'4 \bar "|"
  % Bar 6: F I I
  gis8 cis4 cis4 \bar "|"
  % Bar 7: N O O
  gis4 b8 b8 \bar "|"
  % Bar 8: I T H
  cis4 fis,2 e'2 \bar "|"
  % Bar 9: G H M
  e4 e2 gis,2 \bar "|"
  % Bar 10: C Y S
  fis8 cis'8 dis2 \bar "|"
  % Bar 11: I S N
  cis4 dis2 gis,4 \bar "|"
  % Bar 12: H A E
  e'2 e,8 a2 \bar "|"
  % Bar 13: V A R
  a4 e8 fis4 \bar "|"
  % Bar 14: I I R
  cis'4 cis4 fis,4 \bar "|"
  % Bar 15: N M U
  gis4 gis2 cis2 \bar "|"
  % Bar 16: S I C
  dis2 cis4 fis,8 \bar "|"
  % Bar 17: I N B
  cis'4 gis4 dis'4 \bar "|"
  % Bar 18: Y U T
  cis8 cis2 fis,2 \bar "|"
  % Bar 19: H E E
  e'2 a,2 a2 \bar "|"
  % Bar 20: H C Y
  e'2 fis,8 cis'8 \bar "|"
  % Bar 21: R Y N
  fis,4 cis'8 gis4 \bar "|"
  % Bar 22: B Y R
  dis'4 cis8 fis,4 \bar "|"
  % Bar 23: T B P
  fis2 dis'4 dis8 \bar "|"
  % Bar 24: M Y R
  gis,2 cis8 fis,4 \bar "|"
  % Bar 25: I N B
  cis'4 gis4 dis'4 \bar "|"
  % Bar 26: U Y M
  cis2 cis8 gis2 \bar "|"
  % Bar 27: A O M
  e8 b'8 gis2 \bar "|"
  % Bar 28: Y N A
  cis8 gis4 e8 \bar "|"
  % Bar 29: T H A
  fis2 e'2 e,8 \bar "|."
}

\score {
  \new Staff \with {
    instrumentName = \markup { \smallCaps "Violon." }
  } {
    \melody
  }
  \layout {
    \context {
      \Score
      \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/8)
    }
  }
}

\score {
  \unfoldRepeats \melody
  \midi {
    \tempo 4 = 76
  }
}

\version "2.24.0"

\header {
  title = "The Dorabella Waltz — Transposed to E Major"
  subtitle = "For comparison with Salut d'Amour (Op. 12)"
  composer = "Edward Elgar (1857–1934)"
  arranger = "Decoded by Torqual Ravenskye, 2026"
  tagline = ##f
}

\paper {
  #(set-paper-size "letter")
  top-margin = 15\mm
  bottom-margin = 15\mm
  left-margin = 18\mm
  right-margin = 18\mm
}

melody = \relative c' {
  \key e \major
  \time 3/4
  \tempo "Waltz" 4 = 108
  \cadenzaOn

  % Original G major transposed down minor 3rd to E major
  % G3→E3, A3→F#3, B3→G#3, C4→A3, D4→B3, E4→C#4, F#4→D#4, G4→E4

  % Bar 1: DORA
  e4 b'8 fis4 \bar "|"
  % Bar 2
  e,8 e2 gis4 \bar "|"
  % Bar 3
  dis'2 e,8 a2 \bar "|"
  % Bar 4
  e'4 fis,8 cis'4 \bar "|"
  % Bar 5
  cis2 fis,2 cis'4 \bar "|"
  % Bar 6
  gis8 cis4 cis4 \bar "|"
  % Bar 7
  gis4 b8 b8 \bar "|"
  % Bar 8
  cis4 fis,2 e'2 \bar "|"
  % Bar 9
  e4 e2 gis,2 \bar "|"
  % Bar 10
  fis8 cis'8 dis2 \bar "|"
  % Bar 11
  cis4 dis2 gis,4 \bar "|"
  % Bar 12
  e'2 e,8 a2 \bar "|"
  % Bar 13
  a4 e8 fis4 \bar "|"
  % Bar 14
  cis'4 cis4 fis,4 \bar "|"
  % Bar 15: MUSIC begins
  gis4 gis2 cis2 \bar "|"
  % Bar 16
  dis2 cis4 fis,8 \bar "|"
  % Bar 17
  cis'4 gis4 dis'4 \bar "|"
  % Bar 18: THEE begins
  cis8 cis2 fis,2 \bar "|"
  % Bar 19
  e'2 a,2 a2 \bar "|"
  % Bar 20
  e'2 fis,8 cis'8 \bar "|"
  % Bar 21
  fis,4 cis'8 gis4 \bar "|"
  % Bar 22
  dis'4 cis8 fis,4 \bar "|"
  % Bar 23
  fis2 dis'4 dis8 \bar "|"
  % Bar 24
  gis,2 cis8 fis,4 \bar "|"
  % Bar 25
  cis'4 gis4 dis'4 \bar "|"
  % Bar 26
  cis2 cis8 gis2 \bar "|"
  % Bar 27
  e8 b'8 gis2 \bar "|"
  % Bar 28
  cis8 gis4 e8 \bar "|"
  % Bar 29
  fis2 e'2 e,8 \bar "|."
}

\score {
  \new Staff { \melody }
  \layout { }
}

\score {
  \unfoldRepeats \melody
  \midi { }
}

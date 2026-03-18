\version "2.24.0"

\header {
  title = "DORABELLA"
  subtitle = "Variation on Salut d'Amour, Op. 12"
  subsubtitle = "Decoded from Elgar's Dorabella Cipher (1897)"
  composer = "Edward Elgar"
  opus = "Music Box Cylinder"
  arranger = "Cipher decoded by Torqual Ravenskye, 2026"
  tagline = "\"Dora, the music is for thee.\""
}

\paper {
  #(set-paper-size "letter")
  top-margin = 15\mm
  bottom-margin = 15\mm
  left-margin = 15\mm
  right-margin = 15\mm
}

global = {
  \key e \major
  \time 2/4
  \tempo "Andantino" 4 = 72
}

melody = \relative c' {
  \global
  \clef treble

  %% Section I (S0) — "DORA" at opening
  %% 24 pins, 27.5 beats
  %% val: 1,14,4,2,  0,7,18,2,  9,22,5,16,  15,3,16,8,  16,16,7,14,  14,16,3,21
  %% pitch(val//3): 0,4,1,0, 0,2,6,0, 3,7,1,5, 5,1,5,2, 5,5,2,4, 4,5,1,7
  %% E major: E3,B3,F#3,E3, E3,G#3,D#4,E3, A3,E4,F#3,C#4, C#4,F#3,C#4,G#3, C#4,C#4,G#3,B3, B3,C#4,F#3,E4
  %% dur(val%3): 1,2,1,2, 0,1,0,2, 0,1,2,1, 0,0,1,2, 1,1,1,2, 2,1,0,0

  e4 b'8 fis
  e2~ e4 gis
  dis'2~ dis4 e,8
  a4 e'8 fis,4
  cis'2~ cis2~
  cis4 fis,8 cis'4 gis8
  cis4 cis gis8 b
  b8 cis fis,2~ fis2

  \bar "||"

  %% Section II (S1) — "MUSIC" embedded
  %% 28 pins, 34 beats
  %% val: 22,21,6,5, 17,18,16,18, 7,21,2,9, 10,2,4,16, 16,4,7,6, 15,18,16,5, 16,7,19,17
  %% pitch: 7,7,2,1, 5,6,5,6, 2,7,0,3, 3,0,1,5, 5,1,2,2, 5,6,5,1, 5,2,6,5
  %% E4,E4,G#3,F#3, C#4,D#4,C#4,D#4, G#3,E4,E3,A3, A3,E3,F#3,C#4, C#4,F#3,G#3,G#3, C#4,D#4,C#4,F#3, C#4,G#3,D#4,C#4
  %% dur: 1,0,0,2, 2,0,1,0, 1,0,2,0, 1,2,1,1, 1,1,1,0, 0,0,1,2, 1,1,1,2

  e'4 e2~ e2 gis,8 fis
  cis'8 dis2~ dis4 cis dis2~ dis4
  gis,4 e2~ e4 a
  a4 e8 fis4 cis'
  cis4 fis, gis gis
  cis2~ cis2~ cis2~ cis4 fis,8
  cis'4 gis dis' cis8

  \bar "||"

  %% Section III (S2) — "THEE" embedded
  %% 35 pins, 42 beats
  %% val: 15,3,21,9, 9,21,5,17, 4,17,7,19, 17,4,3,19, 20,6,17,4, 16,7,19,15, 17,6,2,14, 6,17,7,2, 3,21,2
  %% pitch: 5,1,7,3, 3,7,1,5, 1,5,2,6, 5,1,1,6, 6,2,5,1, 5,2,6,5, 5,2,0,4, 2,5,2,0, 1,7,0
  %% C#4,F#3,E4,A3, A3,E4,F#3,C#4, F#3,C#4,G#3,D#4, C#4,F#3,F#3,D#4, D#4,G#3,C#4,F#3, C#4,G#3,D#4,C#4, C#4,G#3,E3,B3, G#3,C#4,G#3,E3, F#3,E4,E3
  %% dur: 0,0,0,0, 0,0,2,2, 1,2,1,1, 2,1,0,1, 2,0,2,1, 1,1,1,0, 2,0,2,2, 0,2,1,2, 0,0,2

  cis2~ cis2 fis,2 e'2
  a,2 e'2 fis,8 cis'8
  fis,4 cis'8 gis4 dis'
  cis8 fis, fis2~ fis4 dis'
  dis8 gis,2~ gis4 cis8 fis,
  cis'4 gis dis' cis2~ cis4
  gis8 e2~ e4 b
  gis8 cis gis8 e
  fis2 e'2 e8

  \bar "|."
}

\score {
  \new Staff \with {
    instrumentName = "Violin"
    midiInstrument = "music box"
  } {
    \melody
  }
  \layout {
    \context {
      \Score
      \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/8)
    }
  }
  \midi { }
}

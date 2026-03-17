\version "2.24.0"

\header {
  title = "The Dorabella Waltz"
  subtitle = "Decoded from Edward Elgar's 1897 Cipher"
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
  \key g \major
  \time 3/4
  \tempo "Waltz" 4 = 108
  \cadenzaOn

  % Bar 1: D O R A — DORA
  g4 d'8 a4 \bar "|"
  % Bar 2: A L N
  g8 g2 b4 \bar "|"
  % Bar 3: S A E
  fis'2 g,8 c2 \bar "|"
  % Bar 4: G C I
  g'4 a,8 e'4 \bar "|"
  % Bar 5: U T I
  e2 a,2 e'4 \bar "|"
  % Bar 6: F I I
  b8 e4 e4 \bar "|"
  % Bar 7: N O O
  b4 d8 d8 \bar "|"
  % Bar 8: I T H
  e4 a,2 g'2 \bar "|"
  % Bar 9: G H M
  g4 g2 b,2 \bar "|"
  % Bar 10: C Y S
  a8 e'8 fis2 \bar "|"
  % Bar 11: I S N
  e4 fis2 b,4 \bar "|"
  % Bar 12: H A E
  g'2 g,8 c2 \bar "|"
  % Bar 13: V A R
  c4 g8 a4 \bar "|"
  % Bar 14: I I R
  e'4 e4 a,4 \bar "|"
  % Bar 15: N M U — MUSIC begins
  b4 b2 e2 \bar "|"
  % Bar 16: S I C
  fis2 e4 a,8 \bar "|"
  % Bar 17: I N B
  e'4 b4 fis'4 \bar "|"
  % Bar 18: Y U T — THEE begins
  e8 e2 a,2 \bar "|"
  % Bar 19: H E E
  g'2 c,2 c2 \bar "|"
  % Bar 20: H C Y
  g'2 a,8 e'8 \bar "|"
  % Bar 21: R Y N
  a,4 e'8 b4 \bar "|"
  % Bar 22: B Y R
  fis'4 e8 a,4 \bar "|"
  % Bar 23: T B P
  a2 fis'4 fis8 \bar "|"
  % Bar 24: M Y R
  b,2 e8 a,4 \bar "|"
  % Bar 25: I N B
  e'4 b4 fis'4 \bar "|"
  % Bar 26: U Y M
  e2 e8 b2 \bar "|"
  % Bar 27: A O M
  g,8 d'8 b2 \bar "|"
  % Bar 28: Y N A
  e'8 b4 g,8 \bar "|"
  % Bar 29: T H A
  a2 g'2 g,8 \bar "|."
}

\score {
  \new Staff \with {
    instrumentName = ""
    \override StaffSymbol.line-count = #5
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
  \midi { }
}

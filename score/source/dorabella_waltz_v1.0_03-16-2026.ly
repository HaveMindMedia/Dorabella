\version "2.24.0"

\header {
  title = "The Dorabella Waltz"
  subtitle = "Decoded from Edward Elgar's 1897 Cipher"
  composer = "Edward Elgar (1897), decoded by Torqual Ravenskye (2026)"
  tagline = "Epoch Geometry [1 = -1] — The cipher is the music."
}

\paper {
  #(set-paper-size "letter")
  top-margin = 15\mm
  bottom-margin = 15\mm
  left-margin = 15\mm
  right-margin = 15\mm
}

% ============================================================================
% DORABELLA CIPHER WALTZ — 29 bars, 87 notes, G major, 3/4
% ============================================================================
%
% Cipher decomposition:
%   pitch(v) = v // 3 → 0=G3, 1=A3, 2=B3, 3=C4, 4=D4, 5=E4, 6=F#4, 7=G4
%   dur(v)   = v %  3 → 0=half, 1=quarter, 2=eighth
%
% FLAT = S0 ++ S1 ++ S2 (87 values)
% S0 = [1,14,4,2,0,7,18,2,9,22,5,16,15,3,16,8,16,16,7,14,14,16,3,21]
% S1 = [22,21,6,5,17,18,16,18,7,21,2,9,10,2,4,16,16,4,7,6,15,18,16,5,
%        16,7,19,17]
% S2 = [15,3,21,9,9,21,5,17,4,17,7,19,17,4,3,19,20,6,17,4,16,7,19,15,
%        17,6,2,14,6,17,7,2,3,21,2]
%
% The cipher's dual-encoding (text + music sharing the same integer)
% means bar durations rarely sum to exactly 3 beats. Only 6 of 29 bars
% are metrically regular. We use \cadenzaOn to honor the cipher values
% exactly, with explicit barlines at every 3-note grouping.
%
% Decoded plaintext:
%   DORA LNS AEG CIU TIF IIN OOI THG HMC YSI SNH AEV ARI
%   IRN MUS ICI NBY UTH EEH CYR YNB YRT BPM YRI NBU YMA OMY NAT HA
% ============================================================================

melody = {
  \clef treble
  \key g \major
  \time 3/4
  \cadenzaOn
  \set Staff.midiInstrument = "acoustic grand"

  % ==== SECTION S0 (bars 1-8) ====

  % Bar 1: vals [1,14,4] → D O R — "DORA" begins
  g4^\markup { \bold \italic "DORA" }  d'8  a4
  \bar "|"

  % Bar 2: vals [2,0,7] → A L N
  g8  g2  b4
  \bar "|"

  % Bar 3: vals [18,2,9] → S A E
  fis'2  g8  c'2
  \bar "|"

  % Bar 4: vals [22,5,16] → G C I
  g'4  a8  e'4
  \bar "|"

  % Bar 5: vals [15,3,16] → U T I
  e'2  a2  e'4
  \bar "|"

  % Bar 6: vals [8,16,16] → F I I
  b8  e'4  e'4
  \bar "|"

  % Bar 7: vals [7,14,14] → N O O
  b4  d'8  d'8
  \bar "|"

  % Bar 8: vals [16,3,21] → I T H
  e'4  a2  g'2
  \bar "|"

  % ==== SECTION S1 (bars 9-17, S0/S1 boundary at bar 9 note 1) ====

  % Bar 9: vals [22,21,6] → G H M
  g'4  g'2  b2
  \bar "|"

  % Bar 10: vals [5,17,18] → C Y S
  a8  e'8  fis'2
  \bar "|"

  % Bar 11: vals [16,18,7] → I S N
  e'4  fis'2  b4
  \bar "|"

  % Bar 12: vals [21,2,9] → H A E
  g'2  g8  c'2
  \bar "|"

  % Bar 13: vals [10,2,4] → V A R
  c'4  g8  a4
  \bar "|"

  % Bar 14: vals [16,16,4] → I I R
  e'4  e'4  a4
  \bar "|"

  % Bar 15: vals [7,6,15] → N M U — "MUSIC" begins at M (note 2)
  b4  b2^\markup { \bold \italic "MUSIC" }  e'2
  \bar "|"

  % Bar 16: vals [18,16,5] → S I C
  fis'2  e'4  a8
  \bar "|"

  % Bar 17: vals [16,7,19] → I N B
  e'4  b4  fis'4
  \bar "|"

  % ==== SECTION S2 (bars 18-29, S1/S2 boundary at bar 18 note 1) ====

  % Bar 18: vals [17,15,3] → Y U T — "THEE" begins at T (note 3)
  e'8  e'2  a2^\markup { \bold \italic "THEE" }
  \bar "|"

  % Bar 19: vals [21,9,9] → H E E
  g'2  c'2  c'2
  \bar "|"

  % Bar 20: vals [21,5,17] → H C Y
  g'2  a8  e'8
  \bar "|"

  % Bar 21: vals [4,17,7] → R Y N
  a4  e'8  b4
  \bar "|"

  % Bar 22: vals [19,17,4] → B Y R
  fis'4  e'8  a4
  \bar "|"

  % Bar 23: vals [3,19,20] → T B P
  a2  fis'4  fis'8
  \bar "|"

  % Bar 24: vals [6,17,4] → M Y R
  b2  e'8  a4
  \bar "|"

  % Bar 25: vals [16,7,19] → I N B
  e'4  b4  fis'4
  \bar "|"

  % Bar 26: vals [15,17,6] → U Y M
  e'2  e'8  b2
  \bar "|"

  % Bar 27: vals [2,14,6] → A O M
  g8  d'8  b2
  \bar "|"

  % Bar 28: vals [17,7,2] → Y N A
  e'8  b4  g8
  \bar "|"

  % Bar 29: vals [3,21,2] → T H A
  a2  g'2  g8
  \bar "|."
}

% Decoded cipher letters as lyrics (one per note)
decodedText = \lyricmode {
  D O R
  A L N
  S A E
  G C I
  U T I
  F I I
  N O O
  I T H
  G H M
  C Y S
  I S N
  H A E
  V A R
  I I R
  N M U
  S I C
  I N B
  Y U T
  H E E
  H C Y
  R Y N
  B Y R
  T B P
  M Y R
  I N B
  U Y M
  A O M
  Y N A
  T H A
}

\score {
  <<
    \new Staff \with {
      \override VerticalAxisGroup.staff-staff-spacing.basic-distance = #12
    } {
      \new Voice = "mel" { \melody }
    }
    \new Lyrics \lyricsto "mel" { \decodedText }
  >>
  \layout {
    \context {
      \Score
      \override BarNumber.break-visibility = ##(#f #f #f)
    }
  }
}

\score {
  <<
    \new Staff { \melody }
  >>
  \midi {
    \tempo 4 = 108
  }
}

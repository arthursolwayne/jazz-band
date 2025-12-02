
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (D2, F#2, G2, A2)
    (38, 1.5), (40, 1.875), (43, 2.25), (45, 2.625),
    # Bar 3 (A2, B2, C#3, D3)
    (45, 3.0), (47, 3.375), (50, 3.75), (52, 4.125),
    # Bar 4 (D3, F#3, G3, A3)
    (52, 4.5), (54, 4.875), (57, 5.25), (59, 5.625)
]

for note, time in bass_notes:
    b = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(b)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, A, C#)
piano_notes = [
    # Bar 2
    (50, 1.5), (52, 1.5), (55, 1.5), (58, 1.5),
    # Bar 3: Bm7 (B, D, F#, A)
    (59, 3.0), (62, 3.0), (65, 3.0), (69, 3.0),
    # Bar 4: G7 (G, B, D, F)
    (57, 4.5), (62, 4.5), (67, 4.5), (69, 4.5)
]

for note, time in piano_notes:
    p = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(p)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (D), E4 (E), F#4 (F#), D4 (D)
sax_notes = [
    (62, 1.5), (64, 1.5), (67, 1.5), (62, 1.5),
    (62, 3.0), (64, 3.0), (67, 3.0), (62, 3.0)
]

for note, time in sax_notes:
    s = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.5)
    sax.notes.append(s)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F (F2, A2, C3, D3)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=82, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=80, pitch=84, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=80, pitch=85, start=2.625, end=3.0),  # D3
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=84, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=80, pitch=82, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=80, pitch=80, start=4.125, end=4.5),  # G2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=80, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=80, pitch=78, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=82, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=80, pitch=84, start=5.625, end=6.0),  # C3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comping: open voicings, different chords each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=87, start=1.5, end=2.0),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.5),  # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=87, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=89, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=5.0),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: a short motif, one phrase, make it sing
# Motif: G (87) Bb (81) A (82) F (84)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=2.5),  # F
    # Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=87, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=4.25, end=4.5),  # F
    # And one final note to stretch the tension
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=5.0),   # G again
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=40, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=44, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=40, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.5),  # F
    # Bar 4 continuation
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.75, end=6.0),  # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),  # G7
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=46, start=2.75, end=3.0),  # Bb7
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=49, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=52, start=2.75, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # G7
    pretty_midi.Note(velocity=90, pitch=46, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody in Fm, one short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=3.25, end=3.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5),  # F
    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=5.75, end=6.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

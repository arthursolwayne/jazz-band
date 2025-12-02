
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=5.75, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=2.0),  # F7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),  # A7 (A C# E G)
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.5),  # F7
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),  # A7
    pretty_midi.Note(velocity=90, pitch=68, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back to finish
# F G Ab Bb (motif), played on 1, 2, 3, and 4 of bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("jazz_intro.mid")

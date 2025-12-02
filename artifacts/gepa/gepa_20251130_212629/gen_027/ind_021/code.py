
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet

# Bass line - Marcus (walking line in Fm, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),   # Ab
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=66, start=5.625, end=6.0),   # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante (one short motif, starts and ends on a question, no scale runs)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),  # hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75),  # Fm7 root
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=2.0),  # Fm7 b9
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.25),  # Fm7 3rd
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.5),  # Fm7 5th
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=90, pitch=39, start=3.0, end=3.25),  # Fm7 b7
    pretty_midi.Note(velocity=90, pitch=40, start=3.25, end=3.5),  # Fm7 5th
    pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=3.75),  # Fm7 3rd
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),  # Fm7 root
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.75),  # Fm7 b9
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # Fm7 #9
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.25),  # Fm7 root
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),  # Fm7 5th
    pretty_midi.Note(velocity=90, pitch=39, start=5.5, end=5.75),  # Fm7 b7
    pretty_midi.Note(velocity=90, pitch=41, start=5.75, end=6.0),  # Fm7 3rd
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (7th chords on 2 and 4)
piano_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # G
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),  # G
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (melody)
sax_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=110, pitch=59, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=58, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # A
    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=58, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # A
    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=110, pitch=59, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=58, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=59, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

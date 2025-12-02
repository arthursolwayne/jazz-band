
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=36, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=35, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # G

    # Bar 3: Fm7
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=37, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=35, start=4.125, end=4.5),   # D

    # Bar 4: Fm7
    pretty_midi.Note(velocity=80, pitch=35, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),   # G
    pretty_midi.Note(velocity=80, pitch=37, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),   # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: Fm7 - comp on beat 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.0),  # D

    # Bar 3: Fm7 - comp on beat 4
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),  # D

    # Bar 4: Fm7 - comp on beat 2
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=5.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=5.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=5.875),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - short motif, starts at 1.5s
# Motif: F - Ab - Bb - D (Fm7) in 4th position, then resolves on D (beat 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # D (return)
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),  # D (return)
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.125),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.625),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

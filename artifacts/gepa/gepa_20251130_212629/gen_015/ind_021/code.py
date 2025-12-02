
import pretty_midi

# Create a PrettyMIDI object with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)      # Alto saxophone
bass = pretty_midi.Instrument(program=33)     # Double bass
piano = pretty_midi.Instrument(program=0)     # Acoustic piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Acoustic drum kit

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    # Bar 1: 0.0 - 1.5s
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),

    # Bar 2: 1.5 - 3.0s
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),

    # Bar 3: 3.0 - 4.5s
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),

    # Bar 4: 4.5 - 6.0s
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Bass (Marcus): Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.25),   # E
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),   # Gb
    pretty_midi.Note(velocity=100, pitch=39, start=2.75, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.5),   # Gb
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.75),   # E
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25),   # Gb
    pretty_midi.Note(velocity=100, pitch=39, start=4.25, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.25),   # E
    pretty_midi.Note(velocity=100, pitch=37, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.75),   # Gb
    pretty_midi.Note(velocity=100, pitch=39, start=5.75, end=6.0),   # Ab
]

bass.notes.extend(bass_notes)

# Piano (Diane): Comping with Fm7 and Eb7 chords on beats 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # Fm7: F (65)
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # Ab (71)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # C (69)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Eb (67)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Eb7: Eb (62)
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb (69)
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # D (64)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # Fm7: F
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Eb
]

piano.notes.extend(piano_notes)

# Sax (Dante): Lyrical motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),   # E

    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),   # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # E

    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),   # E

    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.125),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25),  # E

    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),   # E
]

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_jazz_quartet.mid")

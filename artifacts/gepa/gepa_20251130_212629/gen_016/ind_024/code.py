
import pretty_midi

# Initialize a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key signature to F minor (key number 20) - F minor = F, Ab, Bb
midi.key_signature = pretty_midi.KeySignature(key_number=20)

# Instrumens
sax = pretty_midi.Instrument(program=66)       # Soprano Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Grand Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]

drums.notes.extend(drum_notes)

# Bass line in Fm: walking line with chromatic motion
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=39, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=36, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=37, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=39, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=37, start=4.75, end=5.0),  # F
]

bass.notes.extend(bass_notes)

# Piano: comping with 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # D
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # F
    # Bar 4: F7
    pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.75, end=5.0),  # D
]

piano.notes.extend(piano_notes)

# Sax: short melodic motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=3.875, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.0, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=5.375, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=5.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=5.75, end=6.0),   # Bb
]

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_jazz_quartet.mid")

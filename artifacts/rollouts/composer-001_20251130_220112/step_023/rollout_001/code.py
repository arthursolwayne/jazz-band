
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full Quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # F# (chromatic)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875),  # D (return)
]
sax.notes.extend(sax_notes)

# Bass line (chromatic walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=46, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.1875),  # G
]
bass.notes.extend(bass_notes)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    # Bar 2, beat 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),
    # Bar 2, beat 4: D7 (same chord)
    pretty_midi.Note(velocity=90, pitch=62, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=66, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=69, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=67, start=2.1875, end=2.375),
]
piano.notes.extend(piano_notes)

# Drums for bar 2 (same pattern as bar 1)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Full Quartet (3.0 - 4.5s)
# Sax melody (variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.5625, end=3.75),  # A (return)
]
sax.notes.extend(sax_notes)

# Bass line (chromatic walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.5625, end=3.75),  # D
]
bass.notes.extend(bass_notes)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    # Bar 3, beat 2: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5625),
    # Bar 3, beat 4: A7 (same chord)
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=65, start=3.875, end=4.0625),
]
piano.notes.extend(piano_notes)

# Drums for bar 3 (same pattern as bar 1)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full Quartet (4.5 - 6.0s)
# Sax melody (variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # D (return)
]
sax.notes.extend(sax_notes)

# Bass line (chromatic walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=90, pitch=46, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.0625), # E
    pretty_midi.Note(velocity=90, pitch=49, start=5.0625, end=5.25),  # G
]
bass.notes.extend(bass_notes)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    # Bar 4, beat 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625),
    # Bar 4, beat 4: D7 (same chord)
    pretty_midi.Note(velocity=90, pitch=62, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=90, pitch=66, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.375, end=5.5625),
]
piano.notes.extend(piano_notes)

# Drums for bar 4 (same pattern as bar 1)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif (D, F#, B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
]
sax.notes.extend(sax_notes)

# Bass line (walking line in D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # F#
]
bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Saxophone continues (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # B
]
sax.notes.extend(sax_notes)

# Bar 3: Bass continues (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=4.25, end=4.5),  # D#
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues (3.0 - 4.5s)
piano_notes = [
    # Bar 3: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # G
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Saxophone continues (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Bar 4: Bass continues (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # B
]
bass.notes.extend(bass_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

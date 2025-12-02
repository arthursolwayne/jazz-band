
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Dm7 - G - C - Dm7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # Dm7 (D)
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # Dm7 (D)
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.6875),  # D (root)
    pretty_midi.Note(velocity=80, pitch=58, start=1.6875, end=1.875), # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),   # F (3rd)
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.125),  # G (5th)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.6875),  # D
    # F7 on 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0),   # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif variation, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # Dm7 (D)
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # Dm7 (D)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.9375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.9375, end=4.125), # Dm7 (D)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic passes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875),  # G (5th)
    pretty_midi.Note(velocity=80, pitch=63, start=3.1875, end=3.375), # Ab (chromatic)
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.5625), # Bb (3rd)
    pretty_midi.Note(velocity=80, pitch=67, start=3.5625, end=3.75),  # B (chromatic)
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),  # C (root)
    pretty_midi.Note(velocity=80, pitch=71, start=3.9375, end=4.125), # D
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with subtle variation
piano_notes = [
    # Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.1875),  # D
    # F7 on 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5625), # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.5625), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.3125), # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # Dm7 (D)
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # Dm7 (D)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.4375, end=5.625), # Dm7 (D)
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.6875),  # E (chromatic)
    pretty_midi.Note(velocity=80, pitch=65, start=4.6875, end=4.875), # F (3rd)
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0625), # G (5th)
    pretty_midi.Note(velocity=80, pitch=69, start=5.0625, end=5.25),  # A (chromatic)
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.4375),  # B (chromatic)
    pretty_midi.Note(velocity=80, pitch=72, start=5.4375, end=5.625), # C (root)
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with subtle variation
piano_notes = [
    # Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.6875),  # D
    # F7 on 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.0625), # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.0625), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=60, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=5.8125), # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=60, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=60, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

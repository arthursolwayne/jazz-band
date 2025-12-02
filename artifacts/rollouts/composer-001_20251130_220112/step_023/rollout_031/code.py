
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full band enters
# Sax: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),   # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=48, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=70, pitch=50, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=70, pitch=47, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=70, pitch=52, start=2.0, end=2.1875),  # F
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.6875, end=1.875), # D7
    pretty_midi.Note(velocity=80, pitch=67, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.375, end=2.5625), # D7
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.375, end=2.5625), # A
    pretty_midi.Note(velocity=80, pitch=71, start=2.375, end=2.5625), # C
]
piano.notes.extend(piano_notes)

# Bar 3: Continue motif
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=2.1875, end=2.375), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5625, end=2.75),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=52, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=70, pitch=53, start=2.1875, end=2.375), # F#
    pretty_midi.Note(velocity=70, pitch=51, start=2.375, end=2.5625), # E
    pretty_midi.Note(velocity=70, pitch=48, start=2.5625, end=2.75),  # D
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=2.1875, end=2.375), # D7
    pretty_midi.Note(velocity=80, pitch=67, start=2.1875, end=2.375), # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=80, pitch=71, start=2.1875, end=2.375), # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.0625), # D7
    pretty_midi.Note(velocity=80, pitch=67, start=2.875, end=3.0625), # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.875, end=3.0625), # A
    pretty_midi.Note(velocity=80, pitch=71, start=2.875, end=3.0625), # C
]
piano.notes.extend(piano_notes)

# Bar 4: Finish the motif
# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.9375),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=2.9375, end=3.125), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.3125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.3125, end=3.5),   # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=51, start=2.75, end=2.9375),  # E
    pretty_midi.Note(velocity=70, pitch=48, start=2.9375, end=3.125), # D
    pretty_midi.Note(velocity=70, pitch=50, start=3.125, end=3.3125), # Eb
    pretty_midi.Note(velocity=70, pitch=52, start=3.3125, end=3.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: Final comping
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=2.9375, end=3.125), # D7
    pretty_midi.Note(velocity=80, pitch=67, start=2.9375, end=3.125), # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.9375, end=3.125), # A
    pretty_midi.Note(velocity=80, pitch=71, start=2.9375, end=3.125), # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.6875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

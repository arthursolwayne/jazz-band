
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

# Bar 2: Sax enters with motif
# Dm7: D F A C (Dm7 = D, F, A, C)
# Motif: D - F# (chromatic approach to G) - A - F# (leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.25),  # F#
]
sax.notes.extend(sax_notes)

# Bar 2: Marcus (walking bass line in Dm)
# Dm walking line: D - C - Bb - A - G - F - Eb - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=60, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=57, start=2.0625, end=2.25),
]
bass.notes.extend(bass_notes)

# Bar 2: Diane (comping Dm7 on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (repeat motif with variation)
# Sax: D - F# - A - D (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.4375, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.8125, end=3.0),    # D
]
sax.notes.extend(sax_notes)

# Bar 3: Marcus (walking bass line in Dm)
# Dm walking line: D - C - Bb - A - G - F - Eb - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=60, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=57, start=2.8125, end=3.0),
]
bass.notes.extend(bass_notes)

# Bar 3: Diane (comping Dm7 on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),   # C
]
piano.notes.extend(piano_notes)

# Bar 3: Drums (same pattern as Bar 1)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (finish the intro)
# Sax: D - F# - A - G (a step down from A, leading to the next section)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.5625, end=3.75),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Marcus (walking bass line in Dm)
# Dm walking line: D - C - Bb - A - G - F - Eb - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=60, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=57, start=3.5625, end=3.75),
]
bass.notes.extend(bass_notes)

# Bar 4: Diane (comping Dm7 on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # C
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (same pattern as Bar 1)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

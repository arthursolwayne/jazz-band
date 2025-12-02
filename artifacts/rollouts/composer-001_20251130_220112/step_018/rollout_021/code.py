
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm7 - G7 - Cm7 - F7
# Motif: D, F, G, Eb (Dm7), G, Bb, C, B (G7), C, Eb, F, D (Cm7), F, A, Bb, G (F7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0), # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.1875, end=2.375), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.5625, end=2.75), # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0), # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.1875), # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.9375), # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.9375, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.3125, end=4.5), # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
# D - Eb - F - G - A - Bb - C - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=60, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=69, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=72, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=60, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=67, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=62, start=4.3125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (bar 2), G7 on 4 (bar 2), Cm7 on 2 (bar 3), F7 on 4 (bar 3)
piano_notes = []
# Dm7 on 2 (bar 2)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0), # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0), # C
])
# G7 on 4 (bar 2)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5625), # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.375, end=2.5625), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=2.375, end=2.5625), # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5625), # F
])
# Cm7 on 2 (bar 3)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.1875), # C
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.1875), # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.1875), # G
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.1875), # Bb
])
# F7 on 4 (bar 3)
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=77, start=3.5625, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=79, start=3.5625, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=81, start=3.5625, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=77, start=3.5625, end=3.75), # E
])
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

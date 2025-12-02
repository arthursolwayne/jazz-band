
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D (D, F#, A, B, D, F#, A, B, D, F#, A, B, D, F#, A, B)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),   # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),    # B
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),   # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),    # B
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),   # F#
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),    # B
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, simple comping
# Bar 2: D7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),    # F#
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),    # A
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),    # C#
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),    # F#
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),    # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),    # C#
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),    # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),    # F#
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),    # A
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),    # C#
]
piano.notes.extend(piano_notes)

# Dante: Motif in D, short and haunting
# D (62), F# (67), A (69), B (71)
# Start at 1.5s, leave it hanging, come back at 3.0s
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=105, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=105, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=105, pitch=71, start=2.0625, end=2.25),
    # Come back at bar 3
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=105, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=105, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=105, pitch=71, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=105, pitch=69, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Fill in the rest of the drum pattern for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

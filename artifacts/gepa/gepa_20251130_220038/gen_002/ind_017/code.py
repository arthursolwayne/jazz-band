
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
    pretty_midi.Note(
        velocity=100, pitch=36, start=0.0, end=0.375
    ),
    pretty_midi.Note(
        velocity=100, pitch=36, start=1.125, end=1.5
    ),
    # Snare on 2 and 4
    pretty_midi.Note(
        velocity=100, pitch=38, start=0.75, end=0.875
    ),
    pretty_midi.Note(
        velocity=100, pitch=38, start=1.875, end=2.0
    ),
    # Hihat on every eighth
    pretty_midi.Note(
        velocity=90, pitch=42, start=0.0, end=0.1875
    ),
    pretty_midi.Note(
        velocity=90, pitch=42, start=0.1875, end=0.375
    ),
    pretty_midi.Note(
        velocity=90, pitch=42, start=0.375, end=0.5625
    ),
    pretty_midi.Note(
        velocity=90, pitch=42, start=0.5625, end=0.75
    ),
    pretty_midi.Note(
        velocity=90, pitch=42, start=0.75, end=0.9375
    ),
    pretty_midi.Note(
        velocity=90, pitch=42, start=0.9375, end=1.125
    ),
    pretty_midi.Note(
        velocity=90, pitch=42, start=1.125, end=1.3125
    ),
    pretty_midi.Note(
        velocity=90, pitch=42, start=1.3125, end=1.5
    )
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line, chromatic approaches, no repeated notes
bass_notes = [
    # Fm7 = F, Ab, C, Eb
    # Walking line in Fm
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F (70)
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25), # Eb (69)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # D (67) chromatic
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),  # F again

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # G (71) chromatic
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.125), # D#
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),  # F

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comping on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),  # D#
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # C

    # Bar 2: Bb7 on beat 3 (chromatic approach to Bb)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125), # A#
    pretty_midi.Note(velocity=90, pitch=68, start=2.8125, end=3.0),  # Bb

    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # D#
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # C

    # Bar 3: Bb7 on beat 4 (chromatic approach to Bb)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625), # A#
    pretty_midi.Note(velocity=90, pitch=68, start=5.0625, end=5.25),  # Bb

    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=5.375, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=5.375, end=5.75),  # D#
    pretty_midi.Note(velocity=90, pitch=65, start=5.375, end=5.75),  # C

    # Bar 4: Bb7 on beat 4 (chromatic approach to Bb)
    pretty_midi.Note(velocity=90, pitch=67, start=5.875, end=6.0),  # A#
    pretty_midi.Note(velocity=90, pitch=68, start=6.0, end=6.1875),  # Bb
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax intro (Bar 2: start the motif, leave it hanging)
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
# Motif: F (70), Gb (69), G (71), leave it hanging on G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

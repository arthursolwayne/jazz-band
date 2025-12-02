
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
# Sax motif: F7 -> Ab7 -> Bb7 -> D7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=80, start=1.6875, end=1.875), # Ab7
    pretty_midi.Note(velocity=100, pitch=82, start=1.875, end=2.0625), # Bb7
    pretty_midi.Note(velocity=100, pitch=85, start=2.0625, end=2.25), # D7
]
sax.notes.extend(sax_notes)

# Bass: Walking line - F -> G -> Ab -> A -> Bb -> C -> Db -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=56, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=2.0625, end=2.25), # A
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.4375), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.4375, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=61, start=2.625, end=2.8125), # Db
    pretty_midi.Note(velocity=80, pitch=62, start=2.8125, end=3.0), # D
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0),  # F
    # Bar 2, beat 4: Ab7
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.8125),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=2.8125),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: F7 -> Ab7 -> Bb7 -> D7 (repeat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.1875),  # F7
    pretty_midi.Note(velocity=100, pitch=80, start=3.1875, end=3.375), # Ab7
    pretty_midi.Note(velocity=100, pitch=82, start=3.375, end=3.5625), # Bb7
    pretty_midi.Note(velocity=100, pitch=85, start=3.5625, end=3.75), # D7
]
sax.notes.extend(sax_notes)

# Bass: Walking line - F -> G -> Ab -> A -> Bb -> C -> Db -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=3.5625, end=3.75), # A
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.9375, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.3125), # Db
    pretty_midi.Note(velocity=80, pitch=62, start=4.3125, end=4.5), # D
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.875, end=4.0),  # F
    # Bar 3, beat 4: Ab7
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.8125),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=4.625, end=4.8125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.625, end=4.8125),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=4.625, end=4.8125),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: F7 -> Ab7 -> Bb7 -> D7 (repeat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=80, start=4.6875, end=4.875), # Ab7
    pretty_midi.Note(velocity=100, pitch=82, start=4.875, end=5.0625), # Bb7
    pretty_midi.Note(velocity=100, pitch=85, start=5.0625, end=5.25), # D7
]
sax.notes.extend(sax_notes)

# Bass: Walking line - F -> G -> Ab -> A -> Bb -> C -> Db -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=5.0625, end=5.25), # A
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=61, start=5.625, end=5.8125), # Db
    pretty_midi.Note(velocity=80, pitch=62, start=5.8125, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=5.375, end=5.5),  # F
    # Bar 4, beat 4: Ab7
    pretty_midi.Note(velocity=90, pitch=67, start=6.125, end=6.3125),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=6.125, end=6.3125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=6.125, end=6.3125),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=6.125, end=6.3125),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
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

midi.write("dante_intro.mid")

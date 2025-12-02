
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
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # Dm7: D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.1875),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.1875),  # F
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),  # F
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5625, end=3.75),  # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=48, start=3.5625, end=3.75),  # C
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),  # F
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.3125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.3125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.3125),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.1875),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.6875),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=48, start=5.0, end=5.1875),  # C
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),   # F
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.8125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125),  # F
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.1875),   # Snare on 4
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=2.8125),
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.6875),   # Snare on 4
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.1875),   # Snare on 4
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=5.8125),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

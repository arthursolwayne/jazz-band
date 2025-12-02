
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
    # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Play a short motif that ends on a rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.5),   # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=39, start=2.125, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=37, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.5),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s): F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.0),  # C
    # Bar 3 (2.5 - 3.0s): F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.75),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Rhythmic tension, use rests
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.375, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=41, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.5),   # D
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=100, pitch=39, start=3.625, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=100, pitch=36, start=3.875, end=4.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.25),  # F#
    pretty_midi.Note(velocity=100, pitch=41, start=4.25, end=4.375),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=4.375, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.5s): F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.5),   # G
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.5),   # C
    # Bar 4 (4.5 - 5.0s): F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.0),   # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End on a question, a rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.5),  # A
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=41, start=4.75, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.125),  # C
    pretty_midi.Note(velocity=100, pitch=39, start=5.125, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=37, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.5),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 5.0s): F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.0),   # C
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),  # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat 5
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat 6
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat 7
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat 8
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")

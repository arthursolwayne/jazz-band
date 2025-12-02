
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 1 and 3
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D
    # Bar 2: Dm7 on 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.95),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.95),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.95),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.95),  # D
]
piano.notes.extend(piano_notes)

# Bar 2: Little Ray continues
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Dm7 on 1 and 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D
    # Bar 3: Dm7 on 3
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.45),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.45),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.45),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.45),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Little Ray continues
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Dm7 on 1 and 3
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
    # Bar 4: Dm7 on 3
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.95),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.95),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.95),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.95),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Little Ray continues
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),  # Hihat on 3 & 4
]
drums.notes.extend(drum_notes)

# Sax: Motif
# Bar 2 (1.5 - 3.0s)
# Start the motif on bar 2, 1st beat
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")

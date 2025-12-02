
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625),  # D
    # Bar 2, beat 4
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Dante: Motif in Fm, starts on beat 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.5),   # E (Fm7)
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.75),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.125),  # D
    # Bar 3, beat 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5),   # D
]
piano.notes.extend(piano_notes)

# Dante: Continue motif, build tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=63, start=4.25, end=4.5),   # E
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.625),  # D
    # Bar 4, beat 4
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=56, start=5.625, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Dante: End the motif — a cry, not a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=63, start=5.5, end=5.75),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

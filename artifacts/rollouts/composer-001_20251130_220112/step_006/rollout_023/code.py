
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass (Marcus): Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),   # F (root)
    pretty_midi.Note(velocity=100, pitch=46, start=1.75, end=2.0),   # G (up a half step)
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.25),   # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.5),   # A (up a half step)
    pretty_midi.Note(velocity=100, pitch=48, start=2.5, end=2.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=2.75, end=3.0),   # B
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.75),   # F7: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.5),   # F7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Sax (Dante): Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # A (start motif)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # Bb (up a half step)
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),   # G (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # A (repeat)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),   # Bb (up a half step)
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),   # G (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # A (finish motif)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass (Marcus): Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.25),   # B
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=100, pitch=48, start=3.5, end=3.75),   # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.0),   # C#
    pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.25, end=4.5),   # Eb
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25),   # F7: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),   # F7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax (Dante): Continuation motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # A
]
sax.notes.extend(sax_notes)

# Drums (Bar 3)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass (Marcus): Walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=100, pitch=52, start=5.0, end=5.25),   # D (chromatic)
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.5),   # F#
    pretty_midi.Note(velocity=100, pitch=56, start=5.5, end=5.75),   # G
    pretty_midi.Note(velocity=100, pitch=57, start=5.75, end=6.0),   # Ab
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.75),   # F7: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5),   # F7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Sax (Dante): Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),   # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.25),   # A
]
sax.notes.extend(sax_notes)

# Drums (Bar 4)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.1875), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")

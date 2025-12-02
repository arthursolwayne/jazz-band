
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),     # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),     # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),    # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),     # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),     # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),     # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2 (1.875s) - Dm7: D, F, A, C
    pretty_midi.Note(velocity=85, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    
    # Bar 2, beat 4 (2.625s) - Dm7 (same chord)
    pretty_midi.Note(velocity=85, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=3.0),
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: motif - whisper -> cry
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (whisper)
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # G (builds)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A (peak)
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # G (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line (chromatic approach to F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # E (approach)
]
bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with 7th chords (F7)
piano_notes = [
    # Bar 3, beat 2 (3.375s) - F7: F, A, C, E
    pretty_midi.Note(velocity=85, pitch=59, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.75),
    
    # Bar 3, beat 4 (4.125s) - F7 (same chord)
    pretty_midi.Note(velocity=85, pitch=59, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.5),
    pretty_midi.Note(velocity=85, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: continuation of motif (builds on emotion)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D (echo)
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D (resolve)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),     # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),     # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),    # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.999),   # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),     # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.1875),     # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with 7th chords (Dm7)
piano_notes = [
    # Bar 4, beat 2 (5.25s) - Dm7: D, F, A, C
    pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    
    # Bar 4, beat 4 (5.625s) - Dm7 (same chord)
    pretty_midi.Note(velocity=85, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),
    pretty_midi.Note(velocity=85, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: final resolution, emotional clarity
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D (echo)
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # G (build)
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A (peak)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # G (resolve)
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D (resolve)
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # C (final breath)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_moment.mid')

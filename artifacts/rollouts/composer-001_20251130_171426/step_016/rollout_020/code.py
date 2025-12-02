
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1&
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2&
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3&
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875)  # Hihat on 4&
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),   # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),   # G#
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=3.0),   # A#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),   # F7 - B
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),   # F7 - E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # F7 - B
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),   # F7 - E
]
piano.notes.extend(piano_notes)

# Sax: motif in F, short and haunting
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),   # A (start of motif)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),   # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),   # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),   # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.5, end=3.75),   # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.0),   # B#
    pretty_midi.Note(velocity=100, pitch=56, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.25, end=4.5),   # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # F7 - B
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),   # F7 - E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),   # F7 - B
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),   # F7 - E
]
piano.notes.extend(piano_notes)

# Sax: continue motif, resolve and leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # B
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),   # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 1&
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375), # Hihat on 2&
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125), # Hihat on 3&
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.1875)  # Hihat on 4&
]
drums.notes.extend(drum_notes)

# Bass line: walking with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),   # C#
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.25),   # D#
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),   # E
    pretty_midi.Note(velocity=100, pitch=61, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),   # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),   # F7 - B
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),   # F7 - E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),   # F7 - F
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),   # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # F7 - B
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),   # F7 - E
]
piano.notes.extend(piano_notes)

# Sax: resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),   # A (resolve motif)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),   # B
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),   # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

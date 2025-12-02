
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

bar_duration = 1.5  # seconds per bar
beat_duration = bar_duration / 4  # 0.375s per beat

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=bar_duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
]

# Sax: motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # E
]

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line
bass_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # F
bass_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))  # D
bass_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125))  # C
bass_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5))   # D

# Piano: 7th chords
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
])

# Sax: motif variation
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # E
])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line
bass_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875))  # F
bass_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25))  # D
bass_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625))  # C
bass_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0))   # D

# Piano: 7th chords
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
])

# Sax: motif variation
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # E
])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))

# Add all notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

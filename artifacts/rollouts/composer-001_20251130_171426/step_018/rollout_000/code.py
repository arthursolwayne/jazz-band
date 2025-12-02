
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
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),  # A
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),
]

piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # G#
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # G
]

sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Drums: same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

drums.notes.extend(drum_notes)

# Bass: continue walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # C#
]

bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # F7
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),
]

piano.notes.extend(piano_notes)

# Sax: continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # G#
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # G#
]

sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
# Drums: same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Bass: continue walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # F#
]

bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # F7
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),
]

piano.notes.extend(piano_notes)

# Sax: complete motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # G#
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

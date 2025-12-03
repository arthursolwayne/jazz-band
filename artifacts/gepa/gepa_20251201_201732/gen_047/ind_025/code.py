
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

# Bass: Walking line in F minor, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # G (fifth)
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # A (chromatic approach)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F minor 7 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Ab
])

# Bar 4: E7 (E, G#, B, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
])

piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax: Bar 2, starts with a short motif, leaves it hanging
# F (65), Ab (60), Bb (62), rests
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),
]

# Bar 3: Wait a beat, then resolve
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),
])

# Bar 4: End on a suspended note with space
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')

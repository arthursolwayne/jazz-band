
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
# Sax motif: Fm - Ab - Bb - C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=84, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=86, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=89, start=2.625, end=3.0)   # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0)    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=87, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=90, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=89, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=86, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=89, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=87, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=84, start=2.25, end=2.625),
    # Bar 4: F7 again
    pretty_midi.Note(velocity=90, pitch=87, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=90, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=89, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=84, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=84, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=86, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=89, start=4.125, end=4.5)   # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5)    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=86, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=89, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=87, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.375),
    # Bar 4: F7
    pretty_midi.Note(velocity=90, pitch=87, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=90, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=89, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=84, start=3.75, end=4.125)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=84, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=86, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=89, start=5.625, end=6.0)   # C
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0)    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7
    pretty_midi.Note(velocity=90, pitch=87, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=90, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=89, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875),
    # Bar 5: Bb7 (Bar 4's 2 and 4)
    pretty_midi.Note(velocity=90, pitch=86, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=89, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=87, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=84, start=5.25, end=5.625)
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')


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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare 4
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),     # Hihat 1-4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches, Fm7 chord (F, Ab, C, Db)
# Bar 2: F - Gb - Ab - A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Bar 3: Bb - B - Db - C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Bar 4: F - Gb - Ab - F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Db)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=54, start=1.5, end=1.875),  # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, haunting but incomplete
# Bar 2: F, Ab, Gb, rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # Gb
]
sax.notes.extend(sax_notes)

# Bar 3: D, C, rest, rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # C
]
sax.notes.extend(sax_notes)

# Bar 4: F, Ab, Gb, rest (repeat motif but leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # Gb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick 3
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),   # Snare 4
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=3.0),     # Hihat 1-4
]
drums.notes.extend(drum_notes)

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),   # Snare 4
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5),     # Hihat 1-4
]
drums.notes.extend(drum_notes)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),   # Snare 4
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=6.0),     # Hihat 1-4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

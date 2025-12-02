
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F (F2, C3, G3, Bb3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.625), # G3
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),  # Bb3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, F7, Bb7, Cm7, D7
piano_notes = [
    # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),
    # Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=75, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75),
    # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
]
drums.notes.extend(drum_notes)

# Sax: Start motif in F (F, G#, Bb, B)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=73, start=1.875, end=2.125), # G#
    pretty_midi.Note(velocity=110, pitch=77, start=2.125, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=78, start=2.5, end=2.875),   # B
    # Rest until bar 4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F (F2, C3, G3, Bb3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75), # C3
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125), # G3
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),  # Bb3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, Fm7, D7, Cm7, F7
piano_notes = [
    # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.375),
    # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=81, start=3.375, end=3.75),
    # Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.125),
    # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F (F2, C3, G3, Bb3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # C3
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),  # Bb3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, Bb7, Cm7, D7, F7
piano_notes = [
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),
    # Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=75, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=78, start=4.875, end=5.25),
    # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625),
    # F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax: Finish the motif in F (F, G#, Bb, B)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=110, pitch=73, start=5.875, end=6.0),     # G#
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")


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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax melody (1.5 - 3.0s)
# Sax: Fm7 -> Bb7 -> Eb7 -> Am7
sax_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0), # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (1.5 - 3.0s)
bass_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0), # F#
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.125), # A
    pretty_midi.Note(velocity=80, pitch=44, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.375), # F#
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5), # F
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=2.75), # C
    pretty_midi.Note(velocity=80, pitch=41, start=2.75, end=2.875), # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4 (1.5 - 3.0s)
piano_notes = [
    # Bar 2 (1.5s - 3.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=1.625, end=1.75), # F7 (F, Ab, C, E)
    pretty_midi.Note(velocity=80, pitch=50, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=52, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=55, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.125), # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=55, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=52, start=2.375, end=2.5), # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=80, pitch=54, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=57, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=59, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=54, start=2.75, end=2.875), # Am7 (A, C, E, G)
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=2.875),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.25), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.375), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5), # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.125, end=3.25), # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=3.25, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.5), # F#
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.625), # A
    pretty_midi.Note(velocity=80, pitch=44, start=3.625, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=3.875), # F#
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0), # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.0, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.25), # C
    pretty_midi.Note(velocity=80, pitch=41, start=4.25, end=4.375), # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5), # F
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4 (3.0 - 4.5s)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.125, end=3.25), # F7
    pretty_midi.Note(velocity=80, pitch=50, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=52, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=55, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.625), # Bb7
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=52, start=3.875, end=4.0), # Eb7
    pretty_midi.Note(velocity=80, pitch=54, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=57, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=59, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=54, start=4.25, end=4.375), # Am7
    pretty_midi.Note(velocity=80, pitch=57, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.375),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=5.875), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0), # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.0), # F#
    pretty_midi.Note(velocity=80, pitch=45, start=5.0, end=5.125), # A
    pretty_midi.Note(velocity=80, pitch=44, start=5.125, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.375), # F#
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5), # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.5, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=5.75), # C
    pretty_midi.Note(velocity=80, pitch=41, start=5.75, end=5.875), # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 and 4 (4.5 - 6.0s)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.625, end=4.75), # F7
    pretty_midi.Note(velocity=80, pitch=50, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=52, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=55, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.125), # Bb7
    pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=57, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=52, start=5.375, end=5.5), # Eb7
    pretty_midi.Note(velocity=80, pitch=54, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=57, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=59, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=54, start=5.75, end=5.875), # Am7
    pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=5.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3 (3.0s, 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on 2 and 4 (3.75s, 5.25s)
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth (3.0s to 4.5s)
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

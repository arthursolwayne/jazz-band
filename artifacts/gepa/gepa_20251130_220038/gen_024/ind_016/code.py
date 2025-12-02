
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, sparse comping
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=82, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=84, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=87, start=1.875, end=2.25),
    # Bar 2, beat 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=84, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: 4-note motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # B#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, sparse comping
piano_notes = [
    # Bar 3, beat 2: C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.75),
    # Bar 3, beat 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=81, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=84, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Rest for the first half of the bar, then repeat the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, sparse comping
piano_notes = [
    # Bar 4, beat 2: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=84, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=87, start=4.875, end=5.25),
    # Bar 4, beat 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=84, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=87, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro_wayne.mid")


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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths, chromatic approaches
# Bar 2: F - G - A - Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # F (D2)
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),   # A
]
# Bar 3: Bb - C - D - Eb
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=81, start=4.125, end=4.5),   # Eb
])
# Bar 4: F - G - A - Bb
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),   # A
])
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),
])
# Bar 4: F7 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
])
piano.notes.extend(piano_notes)

# Sax: Short motif, sing it, leave it hanging, come back to finish it
# Melody: F - G - A - Bb (Bar 2), then repeat (Bar 3), then resolve with C (Bar 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=79, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('wayne_meets_dante.mid')

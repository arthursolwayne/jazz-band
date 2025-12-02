
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.0),  # Gb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=75, pitch=70, start=1.5, end=1.75),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=75, pitch=69, start=2.25, end=2.5),  # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=85, pitch=70, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=75, pitch=67, start=3.0, end=3.25),  # Bb
]
piano.notes.extend(piano_notes)

# Dante: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif - F, Ab, Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # Bb
    # Bar 4: Come back and finish it - F, Ab, Bb, Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=75, pitch=69, start=3.0, end=3.25),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=85, pitch=70, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=75, pitch=67, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # Hi-hat
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hi-hat
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # Hi-hat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full Quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # F (1.5s)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),
    # Bb (1.625s)
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),
    # D (1.75s)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),
    # F (1.875s)
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),
    # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),
    # Bb (2.125s)
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),
    # D (2.25s)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),
    # F (2.375s)
    pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2 (2.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.125),
    # F7 on 4 (3.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.125),
]
piano.notes.extend(piano_notes)

# Sax: Melody - a short motif, sing, leave it hanging
sax_notes = [
    # First note: F (1.5s)
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.6875),
    # Second note: Ab (1.6875s)
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875),
    # Third note: D (1.875s)
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.125),
    # Leave it hanging on D
    pretty_midi.Note(velocity=110, pitch=69, start=2.125, end=2.375),
]
sax.notes.extend(sax_notes)

# Bar 3: Full Quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # F (3.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.125),
    # Bb (3.125s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),
    # D (3.25s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),
    # F (3.375s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.5),
    # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),
    # Bb (3.625s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),
    # D (3.75s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875),
    # F (3.875s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.875, end=4.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2 (3.5s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.625),
    # F7 on 4 (4.5s)
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.625),
]
piano.notes.extend(piano_notes)

# Sax: Melody continues
sax_notes = [
    # Continue from last note (D) at 2.375
    pretty_midi.Note(velocity=110, pitch=69, start=2.375, end=2.5),
    # Next note: Ab (2.5s)
    pretty_midi.Note(velocity=110, pitch=68, start=2.5, end=2.6875),
    # Next note: F (2.6875s)
    pretty_midi.Note(velocity=110, pitch=70, start=2.6875, end=2.875),
    # Next note: D (2.875s)
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),
    # Next note: Eb (3.0s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875),
    # Next note: D (3.1875s)
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375),
    # Next note: C (3.375s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),
    # Leave it hanging on C
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),
]
sax.notes.extend(sax_notes)

# Bar 4: Full Quartet (4.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # F (4.5s)
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.625),
    # Bb (4.625s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),
    # D (4.75s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),
    # F (4.875s)
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),
    # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125),
    # Bb (5.125s)
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.25),
    # D (5.25s)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),
    # F (5.375s)
    pretty_midi.Note(velocity=100, pitch=70, start=5.375, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2 (5.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=77, start=5.0, end=5.125),
    # F7 on 4 (6.0s)
    pretty_midi.Note(velocity=100, pitch=70, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=74, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=77, start=6.0, end=6.125),
]
piano.notes.extend(piano_notes)

# Sax: Melody continues and ends with a question
sax_notes = [
    # Continue from last note (C) at 3.75
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875),
    # Next note: Eb (3.875s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.875, end=4.0),
    # Next note: D (4.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.1875),
    # Next note: F (4.1875s)
    pretty_midi.Note(velocity=110, pitch=70, start=4.1875, end=4.375),
    # Next note: Ab (4.375s)
    pretty_midi.Note(velocity=110, pitch=68, start=4.375, end=4.5),
    # Next note: D (4.5s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.6875),
    # Next note: C (4.6875s)
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),
    # End with a question on C
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),
]
sax.notes.extend(sax_notes)

# Drums: Continue full pattern with same timing
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

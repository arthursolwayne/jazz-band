
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

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Dm7 (D F A C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    # G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),
]
piano.notes.extend(piano_notes)

# Sax: Main motif, make it sing
sax_notes = [
    # Motif: D (62) -> Eb (63) -> F (65) -> D (62) -> Eb (63)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=63, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Continue the motif with variation
# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords
piano_notes = [
    # F7 (F A C Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Drums: Same pattern but shifted
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
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

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords
piano_notes = [
    # G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),
    # Cmaj7 (C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Save the MIDI file
midi.write("dante_intro.mid")

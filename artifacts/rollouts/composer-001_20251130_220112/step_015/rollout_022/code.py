
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=54, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.0),  # D#
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # G#
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),  # A#
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=5.5, end=5.75),  # C#
    pretty_midi.Note(velocity=80, pitch=72, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
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

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full band enters (1.5 - 3.0s)
# Sax motif: F7 -> A7 -> Bb7 -> D7
# Rhythm: 8th notes, short and punchy
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=100, pitch=93, start=1.75, end=2.0),  # A7
    pretty_midi.Note(velocity=100, pitch=91, start=2.0, end=2.25),  # Bb7
    pretty_midi.Note(velocity=100, pitch=89, start=2.25, end=2.5),  # D7
]
sax.notes.extend(sax_notes)

# Bass: walking line starting on F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=87, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=93, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=89, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=91, start=1.75, end=2.0),  # Bb
    # Bar 3: A7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=93, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=99, start=2.75, end=3.0),  # C#
    pretty_midi.Note(velocity=80, pitch=96, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=98, start=2.75, end=3.0),  # G
    # Bar 4: Bb7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=91, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=97, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=94, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=96, start=3.75, end=4.0),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full band (3.0 - 4.5s)
# Sax: repeat the motif but slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=100, pitch=93, start=3.25, end=3.5),  # A7
    pretty_midi.Note(velocity=100, pitch=91, start=3.5, end=3.75),  # Bb7
    pretty_midi.Note(velocity=100, pitch=89, start=3.75, end=4.0),  # D7
]
sax.notes.extend(sax_notes)

# Bass: walking line starting on A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: A7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=93, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=99, start=3.25, end=3.5),  # C#
    pretty_midi.Note(velocity=80, pitch=96, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=98, start=3.25, end=3.5),  # G
    # Bar 4: Bb7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=91, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=97, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=94, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=96, start=4.25, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full band (4.5 - 6.0s)
# Sax: repeat the motif but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=100, pitch=93, start=4.75, end=5.0),  # A7
    pretty_midi.Note(velocity=100, pitch=91, start=5.0, end=5.25),  # Bb7
    pretty_midi.Note(velocity=100, pitch=89, start=5.25, end=5.5),  # D7
]
sax.notes.extend(sax_notes)

# Bass: walking line starting on Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Bb7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=91, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=97, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=94, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=96, start=4.75, end=5.0),  # G
    # Bar 4: Bb7 on 2 and 4
    pretty_midi.Note(velocity=80, pitch=91, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=97, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=80, pitch=94, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=96, start=5.75, end=6.0),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
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

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

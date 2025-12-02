
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax starts with a motif: F - Bb - D - F#
note1 = pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75)  # F
note2 = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0)  # Bb
note3 = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)  # D
note4 = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5)  # F#
sax.notes.extend([note1, note2, note3, note4])

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=46, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues the motif (end of phrase)
note5 = pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25)  # F
note6 = pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5)  # Bb
note7 = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75)  # D
note8 = pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0)  # F#
sax.notes.extend([note5, note6, note7, note8])

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=46, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.375),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes the motif and resolves
note9 = pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75)  # F
note10 = pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0)  # Bb
note11 = pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25)  # D
note12 = pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5)  # F#
note13 = pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75)  # F (resolution)
note14 = pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0)  # A (resolution)
sax.notes.extend([note9, note10, note11, note12, note13, note14])

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=46, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")

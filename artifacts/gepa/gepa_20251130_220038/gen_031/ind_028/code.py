
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F major
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C
    # Second beat
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif, start on F, short and singing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Chromatic approach to F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # C
    # Second beat
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif variation, build tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),   # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

# Bass: Chromatic approach to F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # C
    # Second beat
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),  # C
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=77, start=5.0, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=75, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

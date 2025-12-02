
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
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax melody (Dante)
sax_notes = [
    # Bar 2, 1st beat: F (beat 1)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Bar 2, 2nd beat: A (beat 2)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    # Bar 2, 3rd beat: C (beat 3)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    # Bar 2, 4th beat: E (beat 4)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),
]

sax.notes.extend(sax_notes)

# Bass line (Marcus)
bass_notes = [
    # Walking line in F
    # Bar 2, beat 1: F (root)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    # Bar 2, beat 2: A (3rd)
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),
    # Bar 2, beat 3: Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625),
    # Bar 2, beat 4: C (5th)
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),
]

bass.notes.extend(bass_notes)

# Piano comp (Diane)
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=54, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    # Bar 2, beat 4: F7 again
    pretty_midi.Note(velocity=100, pitch=54, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]

piano.notes.extend(piano_notes)

# Bar 3: (3.0 - 4.5s)
# Sax, bass, piano continue

# Sax: Repeat the motif, but start on A (shift up a third)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5),
]

sax.notes.extend(sax_notes)

# Bass line (Marcus)
bass_notes = [
    # Bar 3, beat 1: C (5th)
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),
    # Bar 3, beat 2: E (7th)
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),
    # Bar 3, beat 3: D (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),
    # Bar 3, beat 4: F (root)
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5),
]

bass.notes.extend(bass_notes)

# Piano comp (Diane)
piano_notes = [
    # Bar 3, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    # Bar 3, beat 4: F7 again
    pretty_midi.Note(velocity=100, pitch=54, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
]

piano.notes.extend(piano_notes)

# Bar 4: (4.5 - 6.0s)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
]

sax.notes.extend(sax_notes)

# Bass line (Marcus)
bass_notes = [
    # Bar 4, beat 1: F (root)
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
    # Bar 4, beat 2: A (3rd)
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),
    # Bar 4, beat 3: Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625),
    # Bar 4, beat 4: C (5th)
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)

# Piano comp (Diane)
piano_notes = [
    # Bar 4, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=54, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),
    # Bar 4, beat 4: F7 again
    pretty_midi.Note(velocity=100, pitch=54, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]

piano.notes.extend(piano_notes)

# Drums for Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # E
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # E
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # E
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # A#
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # E
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: continue motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=80, pitch=56, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # E
]
piano.notes.extend(piano_notes)

# Sax: resolution of the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

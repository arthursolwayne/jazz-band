
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
    # Hihat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approach to Fm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=2.25, end=2.375),  # C#
    pretty_midi.Note(velocity=90, pitch=57, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 1: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),
    # Bar 2, beat 2: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),
    # Bar 2, beat 3: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),
    # Bar 2, beat 4: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Sax: Introduce a short motif, leave it hanging
sax_notes = [
    # Bar 2, beat 1: F (48) to Ab (50) to C (52)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=50, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=52, start=1.75, end=1.875),
    # Bar 2, beat 2: Bb (57) to D (59)
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.125),
    # Bar 2, beat 3: Rest
    # Bar 2, beat 4: F (48) to Ab (50) to C (52) again
    pretty_midi.Note(velocity=100, pitch=48, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=2.75),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approach to Fm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=3.125, end=3.25),  # C#
    pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.875, end=4.0),  # G#
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.375),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.375, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 1: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),
    # Bar 3, beat 2: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),
    # Bar 3, beat 3: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),
    # Bar 3, beat 4: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif from bar 2, build on it
sax_notes = [
    # Bar 3, beat 1: C (52) to Eb (55) to F (53)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=55, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.375),
    # Bar 3, beat 2: G (62) to Bb (57) to Ab (50)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=50, start=3.625, end=3.75),
    # Bar 3, beat 3: D (57) to F (48)
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=48, start=3.875, end=4.0),
    # Bar 3, beat 4: Rest
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line, chromatic approach to Fm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0),  # C#
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=5.125, end=5.25),  # D#
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.375),  # E
    pretty_midi.Note(velocity=90, pitch=81, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=83, start=5.5, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=84, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=86, start=5.75, end=5.875),  # G#
    pretty_midi.Note(velocity=90, pitch=88, start=5.875, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 1: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),
    # Bar 4, beat 2: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),
    # Bar 4, beat 3: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),
    # Bar 4, beat 4: Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve it
sax_notes = [
    # Bar 4, beat 1: Ab (50) to C (52)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=52, start=4.625, end=4.75),
    # Bar 4, beat 2: Bb (57) to D (59)
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.0),
    # Bar 4, beat 3: Rest
    # Bar 4, beat 4: Ab (50) to C (52) again
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=52, start=5.375, end=5.5),
]
sax.notes.extend(sax_notes)

# Bar 4, Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

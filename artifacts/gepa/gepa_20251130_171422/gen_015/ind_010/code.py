
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
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - Marcus: walking line, chromatic approaches
bass_notes = [
    # F (1st beat)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Bb (2nd beat)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    # Ab (3rd beat)
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),
    # D (4th beat)
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax - Dante: short motif (start at 1.5s), leave it hanging, come back
sax_notes = [
    # Bar 2: sax motif
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    # Bar 3: silence
    # Bar 4: repeat motif
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line - Marcus: walking line, chromatic approaches
bass_notes = [
    # F (1st beat)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    # Bb (2nd beat)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    # Ab (3rd beat)
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),
    # D (4th beat)
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
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
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line - Marcus: walking line, chromatic approaches
bass_notes = [
    # F (1st beat)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    # Bb (2nd beat)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    # Ab (3rd beat)
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),
    # D (4th beat)
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

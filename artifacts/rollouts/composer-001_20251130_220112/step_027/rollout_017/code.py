
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Fm root (F) on beat 1
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    # Bb (11th) on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),
    # Eb (5th) on beat 3
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    # Ab (b7) on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    # Chromatic approach to F on beat 1
    pretty_midi.Note(velocity=70, pitch=64, start=2.625, end=2.75),
    pretty_midi.Note(velocity=70, pitch=65, start=2.75, end=2.875)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Fm7 on beat 1 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),
    # Bb7 on beat 2 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    # Fm7 on beat 3 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),
    # Eb7 on beat 4 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=66, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: Short motif, starts on beat 1 of bar 2, leaves it hanging
sax_notes = [
    # Start on F (65) with a quarter note
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=2.25),
    # Chromatic run up to Ab (67)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # F on beat 1
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    # Bb on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),
    # Eb on beat 3
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    # Ab on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    # Chromatic approach to F on beat 1
    pretty_midi.Note(velocity=70, pitch=64, start=4.125, end=4.25),
    pretty_midi.Note(velocity=70, pitch=65, start=4.25, end=4.375)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Fm7 on beat 1 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    # Bb7 on beat 2 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    # Fm7 on beat 3 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),
    # Eb7 on beat 4 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.5)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve it
sax_notes = [
    # Continue the motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    # Resolve down to F
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # F on beat 1
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
    # Bb on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),
    # Eb on beat 3
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),
    # Ab on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    # Chromatic approach to F on beat 1
    pretty_midi.Note(velocity=70, pitch=64, start=5.625, end=5.75),
    pretty_midi.Note(velocity=70, pitch=65, start=5.75, end=5.875)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Fm7 on beat 1 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),
    # Bb7 on beat 2 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    # Fm7 on beat 3 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),
    # Eb7 on beat 4 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=66, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Sax: Complete the motif, end on F
sax_notes = [
    # Continue the motif
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

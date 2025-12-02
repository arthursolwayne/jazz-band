
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Kick on 1 and 3 (beat 0 and 2)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    # Snare on 2 and 4 (beat 1 and 3)
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    # Hi-hat on every eighth (8 notes per bar)
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bass: Walking line in F minor, chromatic approach
# Fm7 = F, Ab, C, Eb. Walking line: F, Gb, Ab, A, Bb, B, C, Db, Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F (71)
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # Gb (70)
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),  # Ab (68)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A (69)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: 2nd beat (1.875 - 2.25) -> Fm7 (F, Ab, C, Eb)
# Bar 2: 4th beat (2.625 - 3.0) -> Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),   # Eb
]
piano.notes.extend(piano_notes)

# Sax: Melody (Dante's moment)
# Short motif: F, Ab, Bb, F (hanging on the last note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=3.0),   # F (hanging)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bass: Continue the walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # Bb (66)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # B (67)
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C (72)
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # F (71)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3: 2nd beat (3.375 - 3.75) -> Fm7
# Bar 3: 4th beat (4.125 - 4.5) -> Fm7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),   # Eb
]
piano.notes.extend(piano_notes)

# Sax: Leave it hanging, then return with a resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=4.5),  # F (resting on the unresolved note)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bass: Continue the walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # Eb (65)
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # Bb (66)
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # B (67)
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # F (71)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4: 2nd beat (4.875 - 5.25) -> Fm7
# Bar 4: 4th beat (5.625 - 6.0) -> Fm7
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # Eb
]
piano.notes.extend(piano_notes)

# Sax: Resolution on the last beat (5.625 - 6.0)
# F -> Ab -> C -> Eb (the resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=5.875, end=6.0),    # Ab
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

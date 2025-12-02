
import pretty_midi

# Create a MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Upright Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42
# Bar = 1.5s, beat = 0.375s, 160 BPM, 4/4 time

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on beat 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on beat 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on beat 4 (out of range)
]

# Only include notes within the first bar (0.0 - 1.5)
drum_notes_filtered = [note for note in drum_notes if note.start < 1.5 and note.end <= 1.5]
drums.notes.extend(drum_notes_filtered)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody (Fm - F, Ab, Bb, Db)
# Motif: F, Ab, Bb, Db (Fm7), then F, Eb, Ab (chromatic approach to F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),   # F (71)
    pretty_midi.Note(velocity=100, pitch=68, start=1.625, end=1.75),   # Ab (68)
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),   # Bb (70)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),    # Db (67)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),    # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25),   # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.375),   # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5),    # F (resolution)
]

sax.notes.extend(sax_notes)

# Bass: Walking line in Fm, chromatic approaches
# F - Gb - G - Ab - Bb - B - C - Db (Fm7, Bbm7)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.625),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.625, end=1.75),   # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=1.875),   # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),    # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.125),    # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=2.125, end=2.25),   # B
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.375),   # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.375, end=2.5),    # Db
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Fm7 on beat 2 (1.75s), Bbm7 on beat 4 (2.375s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),   # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875),   # Db
    pretty_midi.Note(velocity=90, pitch=57, start=2.375, end=2.5),    # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=2.375, end=2.5),    # D
    pretty_midi.Note(velocity=90, pitch=59, start=2.375, end=2.5),    # F
    pretty_midi.Note(velocity=90, pitch=56, start=2.375, end=2.5),    # G
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s) - repeat motif with chromatic variation
# Sax: F, Ab, Bb, Db, F, Eb, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.125, end=3.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),    # Db
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),    # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.625, end=3.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=3.875),   # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0),    # F
]

sax.notes.extend(sax_notes)

# Bass: Walking line in Fm, chromatic approaches
# F - Gb - G - Ab - Bb - B - C - Db
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.125),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.125, end=3.25),   # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.5),    # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.625),    # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=3.625, end=3.75),   # B
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=3.875),   # C
    pretty_midi.Note(velocity=80, pitch=50, start=3.875, end=4.0),    # Db
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Fm7 on beat 2 (3.25s), Bbm7 on beat 4 (3.875s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375),   # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.375),   # Db
    pretty_midi.Note(velocity=90, pitch=57, start=3.875, end=4.0),    # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.875, end=4.0),    # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.875, end=4.0),    # F
    pretty_midi.Note(velocity=90, pitch=56, start=3.875, end=4.0),    # G
]

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),     # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 4 (out of range)
]

# Only include notes within the bar (3.0 - 4.5)
drum_notes_filtered = [note for note in drum_notes if note.start < 4.5 and note.end <= 4.5]
drums.notes.extend(drum_notes_filtered)

# Bar 4: Full quartet (4.5 - 6.0s) - resolution, repeat motif with variation
# Sax: F, Ab, Bb, Db, F, Eb, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.625, end=4.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=4.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),    # Db
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125),    # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.375),   # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.5),    # F
]

sax.notes.extend(sax_notes)

# Bass: Walking line in Fm, chromatic approaches
# F - Gb - G - Ab - Bb - B - C - Db
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.625, end=4.75),   # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=4.875),   # G
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.0),    # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.125),    # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=5.125, end=5.25),   # B
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.375),   # C
    pretty_midi.Note(velocity=80, pitch=50, start=5.375, end=5.5),    # Db
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Fm7 on beat 2 (4.75s), Bbm7 on beat 4 (5.375s)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=4.875),   # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=4.875),   # Db
    pretty_midi.Note(velocity=90, pitch=57, start=5.375, end=5.5),    # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=5.375, end=5.5),    # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.375, end=5.5),    # F
    pretty_midi.Note(velocity=90, pitch=56, start=5.375, end=5.5),    # G
]

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),     # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4 (out of range)
]

# Only include notes within the bar (4.5 - 6.0)
drum_notes_filtered = [note for note in drum_notes if note.start < 6.0 and note.end <= 6.0]
drums.notes.extend(drum_notes_filtered)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' has been created.")


import pretty_midi

# Initialize the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: Time 0.0 to 1.5s
bar_duration = 1.5  # 1.5 seconds per bar at 160 BPM

# Drums in Bar 1
# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=0.75, end=1.125))

# Snare on 2 and 4 (beat 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=1.125, end=1.5))

# Hihat on every eighth note
for i in range(8):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): Walking line in F minor, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: F, Gb, G, Ab (walking line in F minor)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F (71)
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Gb (69)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G (71)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Ab (69)
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4 (beat 1 and 3)
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    # Beat 1: F7
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # Eb
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif starts here. One short phrase.
# F - Ab - Bb - F (with slight bends and space)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.125, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.875),    # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F minor, continuing from previous bar
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (beat 1 and 3)
# Bar 3: F7 again
piano_notes = [
    # Beat 1: F7
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Repeat the motif but end it with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.625, end=3.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.375),    # F (slightly delayed for tension)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: same pattern as Bar 1
# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=5.25, end=5.625))

# Snare on 2 and 4 (beat 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=5.625, end=6.0))

# Hihat on every eighth note
for i in range(8):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=start, end=end))

# Bass: Walking line in F minor, continuing from previous bar
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (beat 1 and 3)
# Bar 4: F7 again
piano_notes = [
    # Beat 1: F7
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Resolving the motif, resolving to F with a slight space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=5.125, end=5.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.875),    # F (resolved)
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

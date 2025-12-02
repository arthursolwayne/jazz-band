
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Time per bar in seconds (160 BPM, 4/4 time)
bar_length = 1.5

# Bar 1: Little Ray (drums) alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (kick, 0.0),   # Kick on beat 1
    (snare, 0.75), # Snare on beat 2
    (hihat, 0.0),  # Hihat on 1
    (hihat, 0.375),
    (hihat, 0.75),
    (hihat, 1.125),
    (kick, 1.5),   # Kick on beat 3 (next bar)
    (snare, 2.25), # Snare on beat 4 (next bar)
    (hihat, 1.5),
    (hihat, 1.875),
    (hihat, 2.25),
    (hihat, 2.625)
]

for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Start the motif
# F7 -> G7 -> A7 -> Bb7 (descending line)
# F (65), G (67), A (69), Bb (70)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6),
    pretty_midi.Note(velocity=100, pitch=67, start=1.6, end=1.7),
    pretty_midi.Note(velocity=100, pitch=69, start=1.7, end=1.8),
    pretty_midi.Note(velocity=100, pitch=70, start=1.8, end=1.9)
]
sax.notes.extend(sax_notes)

# BASS: Walking line in F, chromatic approach to each chord
# F -> Gb -> G -> A -> Bb -> B -> C -> Db -> D -> Eb -> E -> F
# F (65), Gb (66), G (67), A (69), Bb (70), B (71), C (60), Db (61), D (62), Eb (63), E (64), F (65)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.5 + 0.25),
    pretty_midi.Note(velocity=70, pitch=66, start=1.75, end=1.75 + 0.25),
    pretty_midi.Note(velocity=70, pitch=67, start=2.0, end=2.0 + 0.25),
    pretty_midi.Note(velocity=70, pitch=69, start=2.25, end=2.25 + 0.25),
    pretty_midi.Note(velocity=70, pitch=70, start=2.5, end=2.5 + 0.25),
    pretty_midi.Note(velocity=70, pitch=71, start=2.75, end=2.75 + 0.25),
    pretty_midi.Note(velocity=70, pitch=60, start=3.0, end=3.0 + 0.25),
    pretty_midi.Note(velocity=70, pitch=61, start=3.25, end=3.25 + 0.25),
    pretty_midi.Note(velocity=70, pitch=62, start=3.5, end=3.5 + 0.25),
    pretty_midi.Note(velocity=70, pitch=63, start=3.75, end=3.75 + 0.25),
    pretty_midi.Note(velocity=70, pitch=64, start=4.0, end=4.0 + 0.25),
    pretty_midi.Note(velocity=70, pitch=65, start=4.25, end=4.25 + 0.25)
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4, comp on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),

    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=70, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=68, start=4.0, end=4.25)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Repeat the motif but delay the end to leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1),
    pretty_midi.Note(velocity=100, pitch=67, start=3.1, end=3.2),
    pretty_midi.Note(velocity=100, pitch=69, start=3.2, end=3.3),
    pretty_midi.Note(velocity=100, pitch=70, start=3.3, end=3.5)  # End a bit later
]
sax.notes.extend(sax_notes)

# BASS: Walking line again, same pattern
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=70, pitch=66, start=3.5, end=3.75),
    pretty_midi.Note(velocity=70, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=70, pitch=69, start=4.25, end=4.5)
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=68, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),

    # Bb7 on beat 4
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.75)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: End the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6),
    pretty_midi.Note(velocity=100, pitch=67, start=4.6, end=4.7),
    pretty_midi.Note(velocity=100, pitch=69, start=4.7, end=4.8),
    pretty_midi.Note(velocity=100, pitch=70, start=4.8, end=5.0)
]
sax.notes.extend(sax_notes)

# BASS: Walking line again, same pattern
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=70, pitch=66, start=5.0, end=5.25),
    pretty_midi.Note(velocity=70, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=70, pitch=69, start=5.75, end=6.0)
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=68, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),

    # Bb7 on beat 4
    pretty_midi.Note(velocity=80, pitch=70, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=67, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=65, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=68, start=6.0, end=6.25)
]
piano.notes.extend(piano_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

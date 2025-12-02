
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar_length = 1.5
time = 0.0

# Drums - Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length))  # Hihat on every eighth

# Bar 2: Full quartet (1.5 - 3.0s)

time = 1.5

# Drums - Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length))  # Hihat on every eighth

# Bass - Bar 2
# Walking line, chromatic approaches, Dm7 chord

# Dm7: D F A C
# Walking line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach)

bass_notes = [62, 63, 65, 67, 69, 70, 71, 72, 62]
for i, pitch in enumerate(bass_notes):
    start = time + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano - Bar 2: 7th chords on 2 and 4
# Dm7 on 2, G7 on 4

# Dm7: D F A C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 0.375, end=time + 0.75))

# G7: G B D F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 1.5, end=time + 1.875))

# Sax - Bar 2
# Motif: D -> Eb -> F -> D (with slight delay on the last note)

sax_notes = [62, 63, 65, 62]
for i, pitch in enumerate(sax_notes):
    start = time + i * 0.375
    if i == 3:
        end = start + 0.75  # Hold the last note
    else:
        end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)

time = 3.0

# Drums - Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length))  # Hihat on every eighth

# Bass - Bar 3
# Walking line, chromatic approaches, Dm7 chord

# Dm7: D F A C
# Walking line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach)

bass_notes = [62, 63, 65, 67, 69, 70, 71, 72, 62]
for i, pitch in enumerate(bass_notes):
    start = time + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano - Bar 3: 7th chords on 2 and 4
# Dm7 on 2, G7 on 4

# Dm7: D F A C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 0.375, end=time + 0.75))

# G7: G B D F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 1.5, end=time + 1.875))

# Sax - Bar 3
# Motif: D -> Eb -> F -> D (with slight delay on the last note)

sax_notes = [62, 63, 65, 62]
for i, pitch in enumerate(sax_notes):
    start = time + i * 0.375
    if i == 3:
        end = start + 0.75  # Hold the last note
    else:
        end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)

time = 4.5

# Drums - Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length))  # Hihat on every eighth

# Bass - Bar 4
# Walking line, chromatic approaches, Dm7 chord

# Dm7: D F A C
# Walking line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach)

bass_notes = [62, 63, 65, 67, 69, 70, 71, 72, 62]
for i, pitch in enumerate(bass_notes):
    start = time + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano - Bar 4: 7th chords on 2 and 4
# Dm7 on 2, G7 on 4

# Dm7: D F A C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 0.375, end=time + 0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 0.375, end=time + 0.75))

# G7: G B D F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 1.5, end=time + 1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 1.5, end=time + 1.875))

# Sax - Bar 4
# Motif: D -> Eb -> F -> D (with slight delay on the last note)

sax_notes = [62, 63, 65, 62]
for i, pitch in enumerate(sax_notes):
    start = time + i * 0.375
    if i == 3:
        end = start + 0.75  # Hold the last note
    else:
        end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

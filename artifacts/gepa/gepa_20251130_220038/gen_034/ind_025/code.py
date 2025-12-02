
import pretty_midi

# Initialize the MIDI file with tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray's groove: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(0, 4):  # 4 beats in a bar
    time = beat * 0.375  # 160 BPM => 0.375s per beat
    if beat % 2 == 0:  # kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
        drums.notes.append(note)
    if beat % 2 == 1:  # snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(note)
    # hihat on every eighth
    for eighth in [0.0, 0.1875]:
        note = pretty_midi.Note(velocity=60, pitch=HIHAT, start=time + eighth, end=time + eighth + 0.05)
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Start of the sax motif: a simple, expressive phrase that sings

# Sax: Dm7 chord (D, F, A, C) but with a rubato feel
# Motif: D -> F -> A -> G (descending with a touch of tension)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)  # D
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 0.375, end=1.5 + 0.75)  # F
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)  # A
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.125, end=1.5 + 1.5)  # G
sax.notes.append(note)

# Bass: Walking line in Dm, chromatic approach to D
# Dm: D F A C
# Walking line: C -> D -> F -> E -> D -> C -> B -> A
notes = [60, 62, 65, 66, 62, 60, 61, 67]  # C D F E D C B A
for i, pitch in enumerate(notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (bar 2 and 4)
# Bar 2: Playing Dm7 on beat 2 (time 2.25s)
note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.25 + 0.1)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.25 + 0.1)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25 + 0.1)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.1)  # C
piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but shift slightly to evoke a memory or idea

note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375)  # D
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=65, start=3.0 + 0.375, end=3.0 + 0.75)  # F
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=69, start=3.0 + 0.75, end=3.0 + 1.125)  # A
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=67, start=3.0 + 1.125, end=3.0 + 1.5)  # G
sax.notes.append(note)

# Bass: Continue walking line
notes = [67, 64, 62, 60, 62, 64, 65, 69]  # A G F E D C B D
for i, pitch in enumerate(notes):
    start = 3.0 + i * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (beat 2 and 4)
note = pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.25 + 0.1)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.25 + 0.1)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.25 + 0.1)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.25 + 0.1)  # C
piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a resolution or a question

note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375)  # D
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=65, start=4.5 + 0.375, end=4.5 + 0.75)  # F
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=69, start=4.5 + 0.75, end=4.5 + 1.125)  # A
sax.notes.append(note)

note = pretty_midi.Note(velocity=100, pitch=67, start=4.5 + 1.125, end=4.5 + 1.5)  # G
sax.notes.append(note)

# Bass: Walking line continues
notes = [67, 69, 65, 62, 60, 62, 64, 65]  # A D F E D C B D
for i, pitch in enumerate(notes):
    start = 4.5 + i * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (beat 2 and 4)
note = pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=5.75 + 0.1)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=5.75 + 0.1)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=5.75 + 0.1)  # A
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=5.75 + 0.1)  # C
piano.notes.append(note)

# Drums: Bar 4 (4.5-6.0s)
for beat in range(0, 4):  # 4 beats in a bar
    time = 4.5 + beat * 0.375
    if beat % 2 == 0:  # kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
        drums.notes.append(note)
    if beat % 2 == 1:  # snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(note)
    # hihat on every eighth
    for eighth in [0.0, 0.1875]:
        note = pretty_midi.Note(velocity=60, pitch=HIHAT, start=time + eighth, end=time + eighth + 0.05)
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

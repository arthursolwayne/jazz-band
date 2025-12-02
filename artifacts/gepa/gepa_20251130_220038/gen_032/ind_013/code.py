
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Time per bar at 160 BPM = 60 / 160 * 4 = 1.5 seconds
bar_duration = 1.5

# -----------------------------
# Bar 1: Little Ray (0.0 - 1.5s)
# Drums only: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# -----------------------------

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.0))

# Hihat on every eighth note
for i in range(8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start, end=end))

# -----------------------------
# Bar 2: Full quartet (1.5 - 3.0s)
# -----------------------------

# Marcus (bass): walking line, Dm7 chord, chromatic approach
# Dm7: D F A C
# Chromatic approach: C# -> D
bass_notes = [
    (1.5, 59),   # C# (chromatic approach to D)
    (1.75, 62),  # D
    (2.0, 64),   # F (Dm7)
    (2.25, 67),  # A
    (2.5, 69),   # C (Dm7)
    (2.75, 64),  # F
    (3.0, 62),   # D
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.25))

# Diane (piano): comp on 2 and 4 with Dm7 chords
# Dm7: D F A C
# On 2 (beat 2) and 4 (beat 4)
piano_notes = [
    (2.0, 62),  # D
    (2.0, 65),  # F
    (2.0, 69),  # A
    (2.0, 72),  # C
    (3.0, 62),  # D
    (3.0, 65),  # F
    (3.0, 69),  # A
    (3.0, 72),  # C
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Dante (sax): short motif, Dm7, sing it
# Dm7: D F A C
# Motif: D -> F -> A -> C on the first beat, then leave it hanging
sax_notes = [
    (1.5, 62),  # D
    (1.75, 65), # F
    (2.0, 69),  # A
    (2.25, 72), # C
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25))

# -----------------------------
# Bar 3: Full quartet (3.0 - 4.5s)
# -----------------------------

# Marcus (bass): walking line, Dm7 chord, chromatic approach
# Dm7: D F A C
# Chromatic approach: C# -> D
bass_notes = [
    (3.5, 59),   # C#
    (3.75, 62),  # D
    (4.0, 64),   # F
    (4.25, 67),  # A
    (4.5, 69),   # C
    (4.75, 64),  # F
    (5.0, 62),   # D
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.25))

# Diane (piano): comp on 2 and 4 with Dm7 chords
# Dm7: D F A C
# On 2 (beat 2) and 4 (beat 4)
piano_notes = [
    (4.0, 62),  # D
    (4.0, 65),  # F
    (4.0, 69),  # A
    (4.0, 72),  # C
    (5.0, 62),  # D
    (5.0, 65),  # F
    (5.0, 69),  # A
    (5.0, 72),  # C
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Little Ray (drums): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.125, end=4.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.0))

# Hihat on every eighth note
for i in range(8):
    start = 3.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start, end=end))

# -----------------------------
# Bar 4: Full quartet (4.5 - 6.0s)
# -----------------------------

# Marcus (bass): walking line, Dm7 chord, chromatic approach
# Dm7: D F A C
# Chromatic approach: C# -> D
bass_notes = [
    (5.5, 59),   # C#
    (5.75, 62),  # D
    (6.0, 64),   # F
    (6.25, 67),  # A
    (6.5, 69),   # C
    (6.75, 64),  # F
    (7.0, 62),   # D
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.25))

# Diane (piano): comp on 2 and 4 with Dm7 chords
# Dm7: D F A C
# On 2 (beat 2) and 4 (beat 4)
piano_notes = [
    (6.0, 62),  # D
    (6.0, 65),  # F
    (6.0, 69),  # A
    (6.0, 72),  # C
    (7.0, 62),  # D
    (7.0, 65),  # F
    (7.0, 69),  # A
    (7.0, 72),  # C
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Little Ray (drums): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=6.375, end=6.5))

# Hihat on every eighth note
for i in range(8):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start, end=end))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

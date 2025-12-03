
import pretty_midi

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum definitions
KICK = 36
SNARE = 38
HIHAT = 42

# Define the time per bar (160 BPM, 4/4 time)
bar_length = 1.5  # seconds per bar
note_length = 0.375  # quarter note = 0.375s

# Bar 1: Little Ray alone (Drums only)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    time = bar * bar_length
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + note_length))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=time + 2 * note_length, end=time + 3 * note_length))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time + note_length, end=time + 2 * note_length))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time + 3 * note_length, end=time + 4 * note_length))
    # Hi-hats on every eighth note (8 notes per bar)
    for i in range(8):
        start = time + i * note_length
        end = start + note_length
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Bar 2: Full quartet (Everyone plays)
# Time starts at 1.5s
time = 1.5

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, time, time + note_length),  # D2
    (40, time + note_length, time + 2 * note_length),  # F2 (chromatic approach)
    (43, time + 2 * note_length, time + 3 * note_length),  # A2
    (38, time + 3 * note_length, time + 4 * note_length)  # D2
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
# Bar 3: Gm7 (G-Bb-D-F)
# Bar 4: Am7 (A-C-E-G)
# Comp on 2 and 4 (beat 2 and 4 of each bar)

# Bar 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time + note_length, end=time + 2 * note_length))  # F4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + note_length, end=time + 2 * note_length))  # A4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + note_length, end=time + 2 * note_length))  # C5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time + note_length, end=time + 2 * note_length))  # D4

# Bar 3
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time + 3 * note_length, end=time + 4 * note_length))  # G4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=time + 3 * note_length, end=time + 4 * note_length))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 3 * note_length, end=time + 4 * note_length))  # D4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 3 * note_length, end=time + 4 * note_length))  # F4

# Bar 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time + 5 * note_length, end=time + 6 * note_length))  # A4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 5 * note_length, end=time + 6 * note_length))  # C5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=time + 5 * note_length, end=time + 6 * note_length))  # E5
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=time + 5 * note_length, end=time + 6 * note_length))  # G4

# Sax: Short motif, make it sing — start, leave it hanging, come back and finish it
# Dm: D, F, A, C — but not scales, just a melodic idea

# Bar 2: D (62), F (65), D (62) — leave it hanging
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=time, end=time + note_length))
sax.notes.append(pretty_midi.Note(velocity=105, pitch=65, start=time + note_length, end=time + 2 * note_length))
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=time + 2 * note_length, end=time + 3 * note_length))

# Bar 3: Rest — let the silence speak
# Bar 4: A (69), C (72), D (62) — resolve the motif
sax.notes.append(pretty_midi.Note(velocity=105, pitch=69, start=time + 3 * note_length, end=time + 4 * note_length))
sax.notes.append(pretty_midi.Note(velocity=105, pitch=72, start=time + 4 * note_length, end=time + 5 * note_length))
sax.notes.append(pretty_midi.Note(velocity=105, pitch=62, start=time + 5 * note_length, end=time + 6 * note_length))

# Drums: Bar 2-4
for bar in [1, 2, 3]:
    time = bar * bar_length
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + note_length))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=time + 2 * note_length, end=time + 3 * note_length))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time + note_length, end=time + 2 * note_length))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time + 3 * note_length, end=time + 4 * note_length))
    # Hi-hats on every eighth note
    for i in range(8):
        start = time + i * note_length
        end = start + note_length
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled


import pretty_midi

# Initialize MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Bar 1: Only drums (0.0 - 1.5 seconds)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar length = 1.5 seconds (60 / 160 * 4 = 1.5)
bar_length = 1.5

# Kick on beats 0 and 2 (beats 1 and 3 of the bar)
drums.notes.append(pretty_midi.Note(
    velocity=80, pitch=drum_kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(
    velocity=80, pitch=drum_kick, start=0.75, end=1.125))

# Snare on beats 1 and 3
drums.notes.append(pretty_midi.Note(
    velocity=80, pitch=drum_snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(
    velocity=80, pitch=drum_snare, start=1.125, end=1.5))

# Hihat on every 8th note (0.0, 0.375, 0.75, 1.125)
for t in [0.0, 0.375, 0.75, 1.125]:
    drums.notes.append(pretty_midi.Note(
        velocity=80, pitch=drum_hihat, start=t, end=t + 0.375))

# Bar 2-4: Full ensemble (1.5 - 6.0 seconds)

# Time variable for mid-bar placement
start_time = 1.5

# Marcus: Bass line (D2-G2, MIDI 38-43)
# Walking line with chromatic approaches
# D2 (38), F#2 (41), G2 (43), D2 (38), C#2 (40), D2 (38), F#2 (41), G2 (43)
bass_notes = [38, 41, 43, 38, 40, 38, 41, 43]
for i, pitch in enumerate(bass_notes):
    time = start_time + (i * 0.375)
    bass.notes.append(pretty_midi.Note(
        velocity=80, pitch=pitch, start=time, end=time + 0.375))

# Diane: Piano comping, open voicings, different chord each bar
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cmaj7 (C, E, G, B)
# Comp on 2 and 4 (beat 2 and 4 of each bar)

# Bar 2 (1.5 - 3.0)
# D7: D (D4=62), F# (65), A (69), C# (67)
for i in [1, 3]:
    time = start_time + (i * 0.375)
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=62, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=65, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=69, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=67, start=time, end=time + 0.375))

# Bar 3 (3.0 - 4.5)
# Gm7: G (67), Bb (62), D (69), F (58)
for i in [1, 3]:
    time = start_time + (i * 0.375) + 1.5
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=67, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=62, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=69, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=58, start=time, end=time + 0.375))

# Bar 4 (4.5 - 6.0)
# Cmaj7: C (60), E (64), G (67), B (71)
for i in [1, 3]:
    time = start_time + (i * 0.375) + 3.0
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=60, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=64, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=67, start=time, end=time + 0.375))
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=71, start=time, end=time + 0.375))

# Dante: Tenor sax, short motif, start and end with a question
# D4 (62), F#4 (65), A4 (69), C#5 (71)
# Start at 1.5, play first two notes, leave it hanging, return at 3.0

# First two notes (D4, F#4) at 1.5
sax.notes.append(pretty_midi.Note(
    velocity=100, pitch=62, start=1.5, end=1.5 + 0.375))
sax.notes.append(pretty_midi.Note(
    velocity=100, pitch=65, start=1.5, end=1.5 + 0.375))

# Return at 3.0, play A4 and C#5
sax.notes.append(pretty_midi.Note(
    velocity=100, pitch=69, start=3.0, end=3.0 + 0.375))
sax.notes.append(pretty_midi.Note(
    velocity=100, pitch=71, start=3.0, end=3.0 + 0.375))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

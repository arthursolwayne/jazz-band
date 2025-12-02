
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per bar (at 160 BPM, each beat is 0.375s, 4/4 bar = 1.5s)
BAR_LENGTH = 1.5
TIME_RESOLUTION = 1 / 24  # 24 ticks per quarter note

# Create instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS_GUITAR)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
sax = Instrument(program=Program.TENOR_SAX)

# Add instruments to the MIDI file
midi.instruments.append(drums)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# -----------------------------
# DRUMS: Little Ray – precise, energetic, full of tension (Bar 1: alone)
# -----------------------------

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = bar1_start + BAR_LENGTH

# Kick on beats 1 and 3 (0.0, 0.75)
drums.notes.append(Note(36, 100, bar1_start, bar1_start + 0.025))
drums.notes.append(Note(36, 100, bar1_start + 0.75, bar1_start + 0.775))

# Snare on beats 2 and 4 (0.375, 1.125)
drums.notes.append(Note(38, 100, bar1_start + 0.375, bar1_start + 0.385))
drums.notes.append(Note(38, 100, bar1_start + 1.125, bar1_start + 1.135))

# Hi-hats on every eighth (0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125)
for i in range(8):
    drums.notes.append(Note(42, 100, bar1_start + i * 0.1875, bar1_start + i * 0.1875 + 0.0125))

# -----------------------------
# BASS: Marcus – walking line, chromatic approaches, no repeated notes
# -----------------------------

# Bar 2-4: Bass plays a walking line
# F7 (F, A, C, E) in F minor or F Dorian
# Let's use a chromatic walking line starting at F4 (70)
# Bar 2: F4 -> F#4 -> G4 -> G#4 -> A4 -> A#4 -> Bb4 -> B4
# Bar 3: B4 -> Bb4 -> A4 -> G#4 -> G4 -> F#4 -> F4 -> E4
# Bar 4: E4 -> D4 -> C4 -> Bb4 -> A4 -> G4 -> F4 -> E4

bar2_start = bar1_end
bar2_end = bar2_start + BAR_LENGTH
bar3_start = bar2_end
bar3_end = bar3_start + BAR_LENGTH
bar4_start = bar3_end
bar4_end = bar4_start + BAR_LENGTH

# Create walking line for bass
def create_walking_line(start_time, notes):
    for i, note in enumerate(notes):
        time = start_time + i * 0.375
        bass.notes.append(Note(note, 90, time, time + 0.25))

# Bar 2
bar2_notes = [70, 71, 72, 73, 74, 75, 76, 77]
create_walking_line(bar2_start, bar2_notes)

# Bar 3
bar3_notes = [77, 76, 74, 73, 72, 71, 70, 69]
create_walking_line(bar3_start, bar3_notes)

# Bar 4
bar4_notes = [69, 67, 65, 76, 74, 72, 70, 69]
create_walking_line(bar4_start, bar4_notes)

# -----------------------------
# PIANO: Diane – 7th chords, comp on 2 and 4, moving with the rhythm
# -----------------------------

# Comp on 2 and 4 (bar 2, bar 3, bar 4)
def comp_chord(time, chord, duration=0.25):
    chord_notes = [chord[0], chord[1], chord[2], chord[3]]
    for note in chord_notes:
        piano.notes.append(Note(note, 100, time, time + duration))

# Bar 2: F7 (F, A, C, E)
comp_chord(bar2_start + 0.375, [70, 74, 77, 80])

# Bar 3: Bb7 (Bb, D, F, Ab)
comp_chord(bar3_start + 0.375, [76, 79, 70, 73])

# Bar 4: E7 (E, G#, B, D)
comp_chord(bar4_start + 0.375, [69, 72, 76, 79])

# -----------------------------
# SAX: You – concise, emotional, with a rest, and varied note durations
# -----------------------------

# Bar 2-4: Your melody
# Start at bar2_start (Bar 2)
# F4 (70) -> G4 (72) -> rest -> A4 (74) -> Bb4 (76) -> B4 (77) -> A4 (74) -> rest -> C4 (67)

# Bar 2
note1 = Note(70, 100, bar2_start + 0.1, bar2_start + 0.2)  # F4, short
note2 = Note(72, 100, bar2_start + 0.4, bar2_start + 0.6)  # G4, longer
sax.notes.append(note1)
sax.notes.append(note2)

# Bar 3
note3 = Note(74, 100, bar3_start + 0.3, bar3_start + 0.5)  # A4
note4 = Note(76, 100, bar3_start + 0.7, bar3_start + 0.9)  # Bb4
note5 = Note(77, 100, bar3_start + 1.1, bar3_start + 1.3)  # B4
sax.notes.append(note3)
sax.notes.append(note4)
sax.notes.append(note5)

# Bar 4
note6 = Note(74, 100, bar4_start + 0.2, bar4_start + 0.4)  # A4
note7 = Note(67, 100, bar4_start + 0.6, bar4_start + 0.8)  # C4
sax.notes.append(note6)
sax.notes.append(note7)

# -----------------------------
# Save the MIDI file
# -----------------------------
midi.write("dante_intro.mid")

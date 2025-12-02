
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time for each beat (in seconds)
beat = 0.375  # 160 BPM => 60 / 160 = 0.375 seconds per beat
bar = 4 * beat  # 6 seconds for 4 bars

# Define the key: F minor
Fm = [60, 62, 63, 65, 67, 68, 70]  # F, Gb, G, Ab, Bb, B, C (Fm7 = F, Ab, Bb, Db)

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS, name="Bass")
piano = Instrument(program=Program.PIANO, name="Piano")
tenor_sax = Instrument(program=Program.SAXOPHONE, name="Tenor Sax")

pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(tenor_sax)

# --- Drums: Bar 1 (0.0 to 1.5s) - Setup the tension ---
# Kick on beat 1
drums.notes.append(Note(36, 60, 0.0, 0.15))  # Kick on beat 1
# Hi-hat on every 8th note
for i in range(0, int(1.5 / 0.1875)):  # 0.1875 = 1/8th note
    drums.notes.append(Note(42, 60, i * 0.1875, i * 0.1875 + 0.05))

# --- Bar 2 (1.5s to 3.0s): Enter with melody, bass, piano ---
# Tenor Sax Melody: One short motif with space
# F (60) -> Ab (65) -> Bb (67) -> Eb (61) -> F (60) (resolve on 4th beat)
tenor_sax.notes.append(Note(60, 60, 1.5, 1.65))  # F
tenor_sax.notes.append(Note(65, 60, 1.8, 1.95))  # Ab
tenor_sax.notes.append(Note(67, 60, 2.1, 2.25))  # Bb
tenor_sax.notes.append(Note(61, 60, 2.4, 2.55))  # Eb
tenor_sax.notes.append(Note(60, 60, 2.7, 2.85))  # F

# Bass: Walking line, chromatic, with no repeated notes
# F -> Gb -> G -> Ab -> Bb -> B -> C -> Db -> Eb -> F
notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
for i in range(len(notes)):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(Note(notes[i], 60, start, end))

# Piano: 7th chords on beat 2 and 4
# Bar 2: Fm7 (F, Ab, Bb, Db)
# Bar 3: Gm7 (G, Bb, C, D)
# Bar 4: Am7 (A, C, D, E)
for i in [1, 3]:
    bar_start = 1.5 + i * 0.375
    # Fm7
    piano.notes.append(Note(60, 60, bar_start, bar_start + 0.25))
    piano.notes.append(Note(65, 60, bar_start, bar_start + 0.25))
    piano.notes.append(Note(67, 60, bar_start, bar_start + 0.25))
    piano.notes.append(Note(68, 60, bar_start, bar_start + 0.25))

# --- Drums: Bars 2-4: Full kit with kick on 1 & 3, snare on 2 & 4 ---
for bar_num in range(2, 4 + 1):
    bar_start = 1.5 * bar_num
    # Kick on 1
    drums.notes.append(Note(36, 60, bar_start, bar_start + 0.15))
    # Snare on 2
    drums.notes.append(Note(38, 60, bar_start + 0.375, bar_start + 0.525))
    # Kick on 3
    drums.notes.append(Note(36, 60, bar_start + 0.75, bar_start + 0.9))
    # Snare on 4
    drums.notes.append(Note(38, 60, bar_start + 1.125, bar_start + 1.275))
    # Hi-hat on every 8th
    for j in range(0, int(1.5 / 0.1875)):
        time = bar_start + j * 0.1875
        drums.notes.append(Note(42, 60, time, time + 0.05))

# Save the MIDI file
pm.write('cellar_door_intro.mid')
print("MIDI file saved as 'cellar_door_intro.mid'")


import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = Instrument(program=10, is_drum=True)
piano = Instrument(program=0)
bass = Instrument(program=33)
sax = Instrument(program=64)

pm.instruments = [drums, piano, bass, sax]

# Define time in seconds (160 BPM = 60/160 = 0.375 seconds per beat)
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar
time = 0

# ------------------------
# Drums: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar 1: 4 beats
for beat_num in range(4):
    time = beat_num * beat
    if beat_num == 0 or beat_num == 2:
        drums.notes.append(Note(36, 100, time, time + 0.15))
    elif beat_num == 1 or beat_num == 3:
        drums.notes.append(Note(38, 100, time, time + 0.15))
    # Hi-hat on every 8th
    for t in range(2):
        hihat_time = time + t * beat / 2
        drums.notes.append(Note(42, 90, hihat_time, hihat_time + 0.1))

# Bar 2-4: Drums same pattern
for bar_index in range(1, 4):
    for beat_num in range(4):
        time = bar_index * bar + beat_num * beat
        if beat_num == 0 or beat_num == 2:
            drums.notes.append(Note(36, 100, time, time + 0.15))
        elif beat_num == 1 or beat_num == 3:
            drums.notes.append(Note(38, 100, time, time + 0.15))
        for t in range(2):
            hihat_time = time + t * beat / 2
            drums.notes.append(Note(42, 90, hihat_time, hihat_time + 0.1))

# ------------------------
# Bass: Marcus (Walking line with chromatic tension)
# Bar 1: Dm7: D C# F A
# Chromatic line: C# -> D -> F -> E -> G -> A -> Bb -> A
bass_notes = [
    (62, 0.0),    # D
    (61, 0.375),  # C#
    (65, 0.75),   # F
    (64, 1.125),  # E
    (67, 1.5),    # G
    (69, 1.875),  # A
    (67, 2.25),   # Bb
    (69, 2.625),  # A
]

for note, t in bass_notes:
    bass.notes.append(Note(note, 80, t, t + 0.25))

# Bar 2: Dm7: D C# F A
# Chromatic line: C# -> D -> F -> E -> G -> A -> Bb -> A
bass_notes_bar2 = [
    (62, 3.0),    # D
    (61, 3.375),  # C#
    (65, 3.75),   # F
    (64, 4.125),  # E
    (67, 4.5),    # G
    (69, 4.875),  # A
    (67, 5.25),   # Bb
    (69, 5.625),  # A
]

for note, t in bass_notes_bar2:
    bass.notes.append(Note(note, 80, t, t + 0.25))

# ------------------------
# Piano: Diane (7th chords, comping on 2 and 4)
# Bar 1: Dm7 = D F Ab C
# Bar 2: Cmaj7 = C E G B
# Bar 3: Am7 = A C E G
# Bar 4: Dm7 again, resolving
def add_piano_notes(chord, time):
    # Dm7: D F Ab C
    if chord == "Dm7":
        notes = [62, 65, 68, 71]
    elif chord == "Cmaj7":
        notes = [60, 64, 67, 71]
    elif chord == "Am7":
        notes = [65, 67, 70, 73]
    else:
        return

    for n in notes:
        piano.notes.append(Note(n, 85, time, time + 0.25))

# Comp on 2 and 4 of each bar
for bar_index in range(4):
    comp_time = bar_index * bar + beat * 1  # 2nd beat
    add_piano_notes("Dm7" if bar_index == 0 else "Cmaj7" if bar_index == 1 else "Am7" if bar_index == 2 else "Dm7", comp_time)
    comp_time = bar_index * bar + beat * 3  # 4th beat
    add_piano_notes("Dm7" if bar_index == 0 else "Cmaj7" if bar_index == 1 else "Am7" if bar_index == 2 else "Dm7", comp_time)

# ------------------------
# Sax: Dante (Tenor) - Short motif in Dm7
# Bar 2: D -> Eb -> F -> G
# Play on 1 & 3
sax_notes = [
    (62, 1.5),    # D (bar 2, beat 1)
    (63, 1.5),    # Eb (on same beat, staccato)
    (65, 2.25),   # F (bar 2, beat 3)
    (67, 2.25),   # G (on same beat, staccato)
]

for note, t in sax_notes:
    sax.notes.append(Note(note, 105, t, t + 0.15))

# ------------------------
# Write MIDI file
pm.write("dante_intro.mid")

print("MIDI file written: dante_intro.mid")

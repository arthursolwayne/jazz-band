
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds for each beat
BEAT = 0.375  # 160 BPM => 60 / 160 = 0.375 seconds per beat
BAR = 4 * BEAT  # 4 beats per bar

# Create instruments
drums = Instrument(program=Program(0), is_drum=True)
bass = Instrument(program=Program(33))
piano = Instrument(program=Program(0))
sax = Instrument(program=Program(64))  # Tenor sax is program 64

pm.instruments = [drums, bass, piano, sax]

# Function to create a note
def note(note_number, start, end, velocity=100):
    return Note(note_number, start, end, velocity)

# DRUMS: Little Ray
# Bar 1: Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
drum_notes = [
    note(36, 0, 0.375),  # Kick on 1
    note(38, 0.375, 0.75),  # Snare on 2
    note(42, 0.75, 1.125),  # Hihat on 3
    note(42, 1.125, 1.5),  # Hihat on 4
    note(36, 1.5, 1.875),  # Kick on 3 (bar 1 ends at 1.5)
    note(38, 1.875, 2.25),  # Snare on 4
]

# Bar 2-4: Full rhythm with fill on bar 1
for bar in range(1, 4):
    for beat in range(4):
        time = bar * BAR + beat * BEAT
        if beat == 0 or beat == 2:
            drum_notes.append(note(36, time, time + BEAT))  # Kick
        if beat == 1 or beat == 3:
            drum_notes.append(note(38, time, time + BEAT))  # Snare
        for eighth in range(2):
            drum_notes.append(note(42, time + eighth * 0.1875, time + eighth * 0.1875 + 0.1875))  # Hihat

drums.notes.extend(drum_notes)

# BASS: Marcus - Walking line in D major, roots and fifths
# Notes in D major: D (2), E (4), F# (6), G (7), A (9), B (11), C# (13)
# Chromatic approaches: C# (13), E flat (15), A flat (10), etc.

bass_notes = [
    # Bar 1: D -> C# -> D -> E
    note(2, 0, 0.375),
    note(13, 0.375, 0.75),
    note(2, 0.75, 1.125),
    note(4, 1.125, 1.5),

    # Bar 2: E -> F# -> G -> A
    note(4, 1.5, 1.875),
    note(6, 1.875, 2.25),
    note(7, 2.25, 2.625),
    note(9, 2.625, 3.0),

    # Bar 3: A -> B -> C# -> D
    note(9, 3.0, 3.375),
    note(11, 3.375, 3.75),
    note(13, 3.75, 4.125),
    note(2, 4.125, 4.5),

    # Bar 4: D -> E -> F# -> G
    note(2, 4.5, 4.875),
    note(4, 4.875, 5.25),
    note(6, 5.25, 5.625),
    note(7, 5.625, 6.0),
]

bass.notes.extend(bass_notes)

# PIANO: Diane - Open voicings, one chord per bar, resolving on the last beat
# Dmaj7 = D G B F# -> MIDI: 2, 7, 11, 6
# Em7 = E G B D -> 4, 7, 11, 2
# F#7 = F# C# E G -> 6, 13, 4, 7
# G7 = G B D F -> 7, 11, 2, 5

def add_piano_chord(chord_notes, start_time):
    for note_number in chord_notes:
        piano.notes.append(note(note_number, start_time, start_time + BEAT))

add_piano_chord([2, 7, 11, 6], 0.0)   # Dmaj7
add_piano_chord([4, 7, 11, 2], 1.5)   # Em7
add_piano_chord([6, 13, 4, 7], 3.0)   # F#7
add_piano_chord([7, 11, 2, 5], 4.5)   # G7

# SAX: You - Tenor sax, mysterious motif: D -> F# -> D -> D
# Start bar 1, end bar 4, with a hang on bar 2 and 3

sax_notes = [
    # Bar 1: D (2)
    note(2, 0.0, 0.375),
    # Bar 2: F# (6)
    note(6, 1.5, 1.875),
    # Bar 3: D (2)
    note(2, 3.0, 3.375),
    # Bar 4: D (2) again, but longer, with slight delay
    note(2, 4.5, 5.0),
]

sax.notes.extend(sax_notes)

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file saved as 'dante_intro.mid'")

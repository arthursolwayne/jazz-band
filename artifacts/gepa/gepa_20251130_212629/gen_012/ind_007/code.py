
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time settings
BPM = 160
note_duration = 60 / BPM  # seconds per beat
bar_length = 4 * note_duration  # 4 beats per bar
total_duration = 4 * bar_length  # 4 bars

# Create instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS)
piano = Instrument(program=Program.PIANO)
sax = Instrument(program=Program.SAXOPHONE)

pm.instruments = [drums, bass, piano, sax]

# Define MIDI note numbers
# Drums
KICK = 36
SNARE = 38
HIHAT = 42

# Bass (D, E, F#, G, A, B, C#, D)
BASS_NOTES = [50, 51, 53, 55, 57, 59, 61, 62]

# Piano 7th chords in D
# D7: D (50), F# (53), A (57), C (60)
# G7: G (55), B (59), D (50), F (58)
# A7: A (57), C# (61), E (52), G (55)
# C7: C (60), E (52), G (55), B (59)
PIANO_NOTES = [
    [50, 53, 57, 60],  # D7
    [55, 59, 50, 58],  # G7
    [57, 61, 52, 55],  # A7
    [60, 52, 55, 59],  # C7
]

# Sax motif (D, A, C#, D)
SAX_NOTES = [50, 57, 61, 50]
SAX_START_TIME = 0.0
SAX_DURATION = 0.375  # 1/8 note

# Bar 1: Drums alone
for bar in range(1):
    bar_start = bar * bar_length
    for beat in range(4):
        start_time = bar_start + beat * note_duration
        if beat in [0, 2]:  # Kick on 1 and 3
            drums.notes.append(Note(note=KICK, start=start_time, end=start_time + note_duration))
        elif beat in [1, 3]:  # Snare on 2 and 4
            drums.notes.append(Note(note=SNARE, start=start_time, end=start_time + note_duration))
        # Hihat on every eighth note
        for eighth in range(2):
            hihat_start = start_time + eighth * (note_duration / 2)
            drums.notes.append(Note(note=HIHAT, start=hihat_start, end=hihat_start + (note_duration / 2)))

# Bar 2: All instruments in
for bar in range(1, 4):
    bar_start = bar * bar_length

    # Drums
    for beat in range(4):
        start_time = bar_start + beat * note_duration
        if beat in [0, 2]:  # Kick
            drums.notes.append(Note(note=KICK, start=start_time, end=start_time + note_duration))
        elif beat in [1, 3]:  # Snare
            drums.notes.append(Note(note=SNARE, start=start_time, end=start_time + note_duration))
        # Hihat on every eighth
        for eighth in range(2):
            hihat_start = start_time + eighth * (note_duration / 2)
            drums.notes.append(Note(note=HIHAT, start=hihat_start, end=hihat_start + (note_duration / 2)))

    # Bass: Walking line, chromatic twist
    for i in range(4):
        beat_start = bar_start + i * note_duration
        # Chromatic shift (start at D, go down to C#, up to D again)
        if i == 0:
            bass_notes = BASS_NOTES[0:4]
        elif i == 1:
            bass_notes = [61, 60, 59, 58]  # C#, C, B, A
        elif i == 2:
            bass_notes = BASS_NOTES[4:8]
        elif i == 3:
            bass_notes = [61, 60, 59, 58]  # C#, C, B, A

        for note in bass_notes:
            bass.notes.append(Note(note=note, start=beat_start, end=beat_start + note_duration))

    # Piano: 7th chords on 2 and 4
    for i in range(2):
        beat_start = bar_start + i * note_duration * 2
        chord = PIANO_NOTES[i]
        for note in chord:
            piano.notes.append(Note(note=note, start=beat_start, end=beat_start + note_duration))

    # Sax: Motif on beat 1
    if bar == 1:
        sax_start = bar_start
        for i, note in enumerate(SAX_NOTES):
            duration = note_duration if i == len(SAX_NOTES) - 1 else note_duration / 2
            start = sax_start + i * (note_duration / 2)
            sax.notes.append(Note(note=note, start=start, end=start + duration))

# Save the MIDI file
pm.write('jazz_intro.mid')

print("MIDI file generated: jazz_intro.mid")
print("This is your moment. Wayne's leaning forward.")

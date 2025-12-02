
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature track
time_signature = pretty_midi.TimeSignature(4, 4, 0)
pm.time_signature_changes.append(time_signature)

# Define key: F major
root = pretty_midi.note_number_to_name(65)  # F4

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Alto Sax')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Function to convert note names to MIDI numbers in F major
def note_name_to_midi(note_name):
    note_map = {
        'F': 65, 'G': 67, 'A': 69, 'Bb': 70, 'B': 71, 'C': 72, 'Db': 73,
        'D': 74, 'Eb': 76, 'E': 77, 'F': 79, 'Gb': 80, 'G': 82, 'Ab': 83,
        'A': 84, 'Bb': 86, 'B': 87, 'C': 88, 'Db': 89, 'D': 90, 'Eb': 92,
        'E': 93, 'F': 95
    }
    return note_map.get(note_name, None)

# Define the rhythm and time
tempo = 160  # BPM
beat = 60.0 / tempo  # seconds per beat
bar = 4 * beat  # seconds per bar
total_time = bar * 4  # 4 bars

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def create_drums_bar(start_time):
    kick_notes = [36]  # C2
    snare_notes = [38]  # D2
    hihat_notes = [42]  # F2
    hihat_time = 0.0

    for beat in range(4):
        time = start_time + beat * beat
        if beat % 2 == 0:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=time, end=time + 0.1)
            drums.notes.append(note)
        else:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=snare_notes[0], start=time, end=time + 0.1)
            drums.notes.append(note)

        for eighth in range(2):
            time = start_time + beat * beat + hihat_time
            note = pretty_midi.Note(velocity=60, pitch=hihat_notes[0], start=time, end=time + 0.05)
            drums.notes.append(note)
            hihat_time += beat / 2

# Bar 1
create_drums_bar(0.0)

# Bar 2 - 4: Full ensemble. Let's define the sax melody first
# Sax melody: 4 bars, one motif, with rests and space
# Melody in F major, starting on F (65)
# Motif: F - Ab - Bb - rest, then repeat with variation

# Bar 2: Start the motif
bar2_start = 1.5  # Time of bar 2

# F (65)
note = pretty_midi.Note(velocity=100, pitch=65, start=bar2_start, end=bar2_start + 0.375)
sax.notes.append(note)

# Ab (70)
note = pretty_midi.Note(velocity=100, pitch=70, start=bar2_start + 0.75, end=bar2_start + 1.125)
sax.notes.append(note)

# Bb (71)
note = pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 1.5, end=bar2_start + 1.875)
sax.notes.append(note)

# Rest
# No note here, let the space speak

# Bar 3: Continue the motif with variation
bar3_start = 3.0

# Bb (71)
note = pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 0.375)
sax.notes.append(note)

# C (72)
note = pretty_midi.Note(velocity=100, pitch=72, start=bar3_start + 0.75, end=bar3_start + 1.125)
sax.notes.append(note)

# D (74)
note = pretty_midi.Note(velocity=100, pitch=74, start=bar3_start + 1.5, end=bar3_start + 1.875)
sax.notes.append(note)

# Rest again

# Bar 4: Resolve with a return to F
bar4_start = 4.5

# F (65)
note = pretty_midi.Note(velocity=100, pitch=65, start=bar4_start, end=bar4_start + 0.375)
sax.notes.append(note)

# Ab (70)
note = pretty_midi.Note(velocity=100, pitch=70, start=bar4_start + 0.75, end=bar4_start + 1.125)
sax.notes.append(note)

# Bb (71)
note = pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 1.5, end=bar4_start + 1.875)
sax.notes.append(note)

# End the motif, leave it hanging

# Bass: Walking line, chromatic approaches, no repeated notes
# Bar 1: No bass
# Bar 2: F - Gb - G - A
# Bar 3: Bb - B - C - Db
# Bar 4: D - Eb - E - F

def walk_bass(note_sequence, start_time):
    for note in note_sequence:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + 0.25)
        bass.notes.append(note_obj)
        start_time += 0.25

bass_notes_bar2 = [65, 66, 67, 69]  # F, Gb, G, A
bass_notes_bar3 = [71, 72, 72, 73]  # Bb, B, B, C (chromatic approach)
bass_notes_bar4 = [74, 76, 77, 79]  # D, Eb, E, F

walk_bass(bass_notes_bar2, 1.5)
walk_bass(bass_notes_bar3, 3.0)
walk_bass(bass_notes_bar4, 4.5)

# Piano: 7th chords, comp on 2 and 4
def piano_comp(chord_notes, start_time):
    for beat in range(2):  # On 2 and 4
        time = start_time + beat * 2 * beat
        for note in chord_notes:
            note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
            piano.notes.append(note_obj)

# Bar 2: F7 (F, A, C, Eb)
bar2_chord = [65, 69, 72, 76]
piano_comp(bar2_chord, 1.5)

# Bar 3: Bb7 (Bb, D, F, Ab)
bar3_chord = [71, 74, 65, 70]
piano_comp(bar3_chord, 3.0)

# Bar 4: F7 again
piano_comp(bar2_chord, 4.5)

# Save the MIDI file
pm.write("waynes_moment.mid")
print("MIDI file 'waynes_moment.mid' has been created.")

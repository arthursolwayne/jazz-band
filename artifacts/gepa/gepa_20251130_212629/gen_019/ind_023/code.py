
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature (F major)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F major (C is 0, F is 5)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')

drum_inst = pretty_midi.Instrument(program=drums_program)
bass_inst = pretty_midi.Instrument(program=bass_program)
piano_inst = pretty_midi.Instrument(program=piano_program)
sax_inst = pretty_midi.Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [drum_inst, bass_inst, piano_inst, sax_inst]

# BPM = 160, 4/4 time
# Each beat = 0.375 seconds
# Bar = 1.5 seconds
# Total time = 6 seconds

# --- DRUMS ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

def add_drums():
    for bar in range(4):
        # 8 eighth notes per bar
        for i in range(8):
            time = bar * 1.5 + i * 0.375
            note_number = 36  # Kick
            if i % 2 == 0:  # 1 and 3
                drum_inst.notes.append(pretty_midi.Note(100, note_number, time, time + 0.1))
            note_number = 38  # Snare
            if i % 2 == 1:  # 2 and 4
                drum_inst.notes.append(pretty_midi.Note(100, note_number, time, time + 0.1))
            note_number = 42  # Hihat
            drum_inst.notes.append(pretty_midi.Note(100, note_number, time, time + 0.1))

# --- BASS LINE ---
# Walking line, chromatic approaches, never the same note twice

def add_bass():
    # F major scale: F, G, A, Bb, C, D, E
    # Chromatic steps between notes
    bass_notes = [71, 72, 74, 71, 72, 74, 76, 74]  # F, G, A, F, G, A, Bb, A
    for i, note in enumerate(bass_notes):
        time = i * 0.375
        bass_inst.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# --- PIANO ---
# 7th chords, comp on 2 and 4, aggressive and rhythmic

def add_piano():
    # Chords for F7: F, A, C, E♭
    # Comp on 2 and 4
    chords = [
        [71, 74, 76, 69],  # F7
        [72, 76, 77, 74],  # G7
        [74, 76, 78, 72],  # A7
        [71, 74, 76, 69],  # F7
    ]
    for bar in range(4):
        for i, chord in enumerate(chords):
            time = bar * 1.5 + 0.75 if i == 0 else bar * 1.5 + 1.25  # 2nd and 4th beats
            for note in chord:
                piano_inst.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# --- SAX LINE ---
# Haunting motif, start it, leave it hanging, come back to finish
# Motif: F (71) -> Bb (74) -> F (71) -> C (76) -> rest
# Repeat at bar 3

def add_sax():
    # Bar 1
    sax_inst.notes.append(pretty_midi.Note(110, 71, 0.0, 0.375))  # F
    sax_inst.notes.append(pretty_midi.Note(110, 74, 0.375, 0.75))  # Bb
    sax_inst.notes.append(pretty_midi.Note(110, 71, 0.75, 1.125))  # F
    sax_inst.notes.append(pretty_midi.Note(110, 76, 1.125, 1.5))  # C

    # Bar 3
    sax_inst.notes.append(pretty_midi.Note(110, 71, 3.0, 3.375))  # F
    sax_inst.notes.append(pretty_midi.Note(110, 74, 3.375, 3.75))  # Bb
    sax_inst.notes.append(pretty_midi.Note(110, 71, 3.75, 4.125))  # F
    sax_inst.notes.append(pretty_midi.Note(110, 76, 4.125, 4.5))  # C

# Add all parts
add_drums()
add_bass()
add_piano()
add_sax()

# Save the MIDI file
pm.write('dante_russo_4bar_intro.mid')

print("MIDI file 'dante_russo_4bar_intro.mid' created.")

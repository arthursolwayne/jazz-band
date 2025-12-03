
import pretty_midi
from pretty_midi import note_number_to_name, Note

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=drum_program)
bass = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Fretless Bass'))
sax = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Tenor Saxophone'))
pm.instruments = [piano, bass, sax]

# Define time in seconds per beat
bpm = 160
beats_per_bar = 4
time_per_beat = 60 / bpm  # 0.375 seconds per beat
bar_length = time_per_beat * beats_per_bar  # 1.5 seconds per bar
total_duration = bar_length * 4  # 6.0 seconds

# Define Fm chord tones (F, Ab, C, Dbb = D flat)
Fm_chords = {
    1: ['F', 'Ab', 'C', 'Db'],
    2: ['Gbm7'],  # Ab7 in Fm
    3: ['Fm9'],  # Fm7 with 9
    4: ['F7'],   # F7 with tritone
}

# Map note names to MIDI numbers
note_map = {
    'C': 60, 'Db': 61, 'D': 62, 'Eb': 63, 'E': 64, 'F': 65, 'Gb': 66, 'G': 67,
    'Ab': 68, 'A': 69, 'Bb': 70, 'B': 71
}

# Define a function to create a note
def create_note(note_name, time, duration=0.25, velocity=100):
    note_number = note_map[note_name]
    return Note(note_number, time, duration, velocity)

# -------- DRUMS --------
# Kick on 1 & 3, snare on 2 & 4, hihat on every 8th
def add_drum_stroke(instrument, time, note_name, duration=0.05, velocity=100):
    note = create_note(note_name, time, duration, velocity)
    instrument.notes.append(note)

# MIDI note numbers for percussion
Kick = 36
Snare = 38
HiHat = 42

# Time of each beat in seconds
for bar in range(4):
    for beat in range(4):
        time = bar * bar_length + beat * time_per_beat
        if beat == 0 or beat == 2:
            add_drum_stroke(piano, time, 'Kick', 0.05, 100)
        if beat == 1 or beat == 3:
            add_drum_stroke(piano, time, 'Snare', 0.05, 100)
        for eighth in [0, 1]:
            add_drum_stroke(piano, time + eighth * time_per_beat / 2, 'HiHat', 0.03, 100)

# -------- BASS LINE --------
# Walking line in Fm: F - Gb - Ab - A
# With chromatic approaches to each chord tone

bass_notes = [
    create_note('F', 0.0, 0.25, 80),
    create_note('Gb', 0.375, 0.25, 80),
    create_note('Ab', 0.75, 0.25, 80),
    create_note('A', 1.125, 0.25, 80),
    create_note('Bb', 1.5, 0.25, 80),
    create_note('B', 1.875, 0.25, 80),
    create_note('C', 2.25, 0.25, 80),
    create_note('Db', 2.625, 0.25, 80),
    create_note('D', 3.0, 0.25, 80),
    create_note('Eb', 3.375, 0.25, 80),
    create_note('E', 3.75, 0.25, 80),
    create_note('F', 4.125, 0.25, 80)
]

bass.notes.extend(bass_notes)

# -------- PIANO VOICINGS --------
# Comp on 2 and 4
# Bar 1: Fm7
# Bar 2: Ab7
# Bar 3: Fm9
# Bar 4: F7

# Bar 1: Fm7 (F, Ab, C, Eb)
bar_1_notes = [
    create_note('F', 0.0, 0.25, 100),
    create_note('Ab', 0.0, 0.25, 100),
    create_note('C', 0.0, 0.25, 100),
    create_note('Eb', 0.0, 0.25, 100),
]
# Bar 2: Ab7 (Ab, C, Eb, Gb)
bar_2_notes = [
    create_note('Ab', 1.5, 0.25, 100),
    create_note('C', 1.5, 0.25, 100),
    create_note('Eb', 1.5, 0.25, 100),
    create_note('Gb', 1.5, 0.25, 100),
]
# Bar 3: Fm9 (F, Ab, C, Eb, A)
bar_3_notes = [
    create_note('F', 3.0, 0.25, 100),
    create_note('Ab', 3.0, 0.25, 100),
    create_note('C', 3.0, 0.25, 100),
    create_note('Eb', 3.0, 0.25, 100),
    create_note('A', 3.0, 0.25, 100),
]
# Bar 4: F7 (F, Ab, C, E)
bar_4_notes = [
    create_note('F', 4.5, 0.25, 100),
    create_note('Ab', 4.5, 0.25, 100),
    create_note('C', 4.5, 0.25, 100),
    create_note('E', 4.5, 0.25, 100),
]

piano.notes.extend(bar_1_notes + bar_2_notes + bar_3_notes + bar_4_notes)

# -------- SAX MOTIF --------
# Short, emotional motif: F - Eb - D - C (with a rest on the last note)
note_1 = create_note('F', 0.0, 0.5, 110)  # F, held 0.5s
note_2 = create_note('Eb', 0.5, 0.5, 110)  # Eb, next 0.5s
note_3 = create_note('D', 1.0, 0.5, 110)   # D, next 0.5s
note_4 = create_note('C', 1.5, 0.5, 110)   # C, held but then released

sax.notes.extend([note_1, note_2, note_3, note_4])

# Write to MIDI file
pm.write('Fm_Intro.mid')

print("MIDI file 'Fm_Intro.mid' has been created.")

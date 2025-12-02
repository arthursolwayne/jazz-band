
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create instruments
instrument_drums = pretty_midi.Instrument(program=10)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_sax = pretty_midi.Instrument(program=64)

# Add instruments to the piece
pm.instruments = [instrument_drums, instrument_piano, instrument_bass, instrument_sax]

# Function to convert note names to MIDI note numbers (Fm scale: F, Gb, Ab, Bb, B, Db, Eb)
note_map = {
    'F': 65,
    'Gb': 66,
    'Ab': 67,
    'Bb': 69,
    'B': 71,
    'Db': 72,
    'Eb': 74
}

# Time per beat (seconds) = 60 / tempo
time_per_beat = 60.0 / 160.0

# Bar 1: Drums only (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for beat in range(4):
    for quarter in range(2):  # Each beat is 2 eighth notes
        time = (beat * 2 + quarter) * time_per_beat
        if beat % 2 == 0:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.05)
            instrument_drums.notes.append(note)
        if quarter == 1:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.05)
            instrument_drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
        instrument_drums.notes.append(note)

# Bar 2: Saxophone melody — start with a short motif
# Motif: F (65) -> Ab (67) -> rest -> Bb (69) -> rest -> Eb (74)
# Start at bar 2, beat 1
time_bar_2 = 1.5  # Time of bar 2
note_1 = pretty_midi.Note(velocity=110, pitch=note_map['F'], start=time_bar_2, end=time_bar_2 + 0.375)
note_2 = pretty_midi.Note(velocity=110, pitch=note_map['Ab'], start=time_bar_2 + 0.375, end=time_bar_2 + 0.75)
note_3 = pretty_midi.Note(velocity=110, pitch=note_map['Bb'], start=time_bar_2 + 1.125, end=time_bar_2 + 1.5)
note_4 = pretty_midi.Note(velocity=110, pitch=note_map['Eb'], start=time_bar_2 + 1.875, end=time_bar_2 + 2.25)
instrument_sax.notes.extend([note_1, note_2, note_3, note_4])

# Bar 2: Bass line — walking chromatically
# Notes: F (65) -> Gb (66) -> Ab (67) -> Bb (69)
# Starting at bar 2, beat 1
time = time_bar_2
notes = [
    (note_map['F'], time, time + 0.375),
    (note_map['Gb'], time + 0.375, time + 0.75),
    (note_map['Ab'], time + 0.75, time + 1.125),
    (note_map['Bb'], time + 1.125, time + 1.5)
]
for pitch, start, end in notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    instrument_bass.notes.append(note)

# Bar 2: Piano — comping on 2 and 4, 7th chords
# On beat 2: F7 (F, Ab, Bb, C)
# On beat 4: Bb7 (Bb, Db, F, Ab)
# Duration: quarter note (0.75s)
time_beat_2 = time_bar_2 + 0.75
chord_f7 = [note_map['F'], note_map['Ab'], note_map['Bb'], note_map['C']]
for pitch in chord_f7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_beat_2, end=time_beat_2 + 0.75)
    instrument_piano.notes.append(note)

time_beat_4 = time_bar_2 + 1.5
chord_bb7 = [note_map['Bb'], note_map['Db'], note_map['F'], note_map['Ab']]
for pitch in chord_bb7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_beat_4, end=time_beat_4 + 0.75)
    instrument_piano.notes.append(note)

# Bar 3: Full ensemble
# Saxophone repeats the motif with variation
time_bar_3 = time_bar_2 + 1.5
note_1 = pretty_midi.Note(velocity=110, pitch=note_map['F'], start=time_bar_3, end=time_bar_3 + 0.375)
note_2 = pretty_midi.Note(velocity=110, pitch=note_map['Ab'], start=time_bar_3 + 0.375, end=time_bar_3 + 0.75)
note_3 = pretty_midi.Note(velocity=110, pitch=note_map['Bb'], start=time_bar_3 + 1.125, end=time_bar_3 + 1.5)
note_4 = pretty_midi.Note(velocity=110, pitch=note_map['Eb'], start=time_bar_3 + 1.875, end=time_bar_3 + 2.25)
instrument_sax.notes.extend([note_1, note_2, note_3, note_4])

# Bass continues the walking line
time = time_bar_3
notes = [
    (note_map['F'], time, time + 0.375),
    (note_map['Gb'], time + 0.375, time + 0.75),
    (note_map['Ab'], time + 0.75, time + 1.125),
    (note_map['Bb'], time + 1.125, time + 1.5)
]
for pitch, start, end in notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    instrument_bass.notes.append(note)

# Piano comps again on 2 and 4
time_beat_2 = time_bar_3 + 0.75
for pitch in chord_f7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_beat_2, end=time_beat_2 + 0.75)
    instrument_piano.notes.append(note)

time_beat_4 = time_bar_3 + 1.5
for pitch in chord_bb7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_beat_4, end=time_beat_4 + 0.75)
    instrument_piano.notes.append(note)

# Bar 4: Saxophone ends with a rest and a strong closing note
time_bar_4 = time_bar_3 + 1.5
note_1 = pretty_midi.Note(velocity=110, pitch=note_map['Eb'], start=time_bar_4 + 1.125, end=time_bar_4 + 1.5)
instrument_sax.notes.append(note_1)

# Bass continues walking line
time = time_bar_4
notes = [
    (note_map['F'], time, time + 0.375),
    (note_map['Gb'], time + 0.375, time + 0.75),
    (note_map['Ab'], time + 0.75, time + 1.125),
    (note_map['Bb'], time + 1.125, time + 1.5)
]
for pitch, start, end in notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    instrument_bass.notes.append(note)

# Piano comps on 2 and 4 again
time_beat_2 = time_bar_4 + 0.75
for pitch in chord_f7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_beat_2, end=time_beat_2 + 0.75)
    instrument_piano.notes.append(note)

time_beat_4 = time_bar_4 + 1.5
for pitch in chord_bb7:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time_beat_4, end=time_beat_4 + 0.75)
    instrument_piano.notes.append(note)

# Drums continue same pattern
for beat in range(4):
    for quarter in range(2):  # Each beat is 2 eighth notes
        time = (beat * 2 + quarter) * time_per_beat + time_bar_2
        if beat % 2 == 0:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.05)
            instrument_drums.notes.append(note)
        if quarter == 1:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.05)
            instrument_drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
        instrument_drums.notes.append(note)

# Save the MIDI file
pm.write("intro_wayne.mid")

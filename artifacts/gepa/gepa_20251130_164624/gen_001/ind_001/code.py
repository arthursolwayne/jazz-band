
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
time_signature = pretty_midi.TimeSignature(4, 4, 0)
midi.time_signature_changes = [time_signature]

# Create instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Bar 1: Drums only
# Kick on 1 and 3 (0.0 and 0.75s)
kick_notes = [36, 36]
kick_times = [0.0, 0.75]
for note, time in zip(kick_notes, kick_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Snare on 2 and 4 (0.375 and 1.125s)
snare_notes = [38, 38]
snare_times = [0.375, 1.125]
for note, time in zip(snare_notes, snare_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Hi-hat on every eighth note (0.0, 0.375, 0.75, 1.125)
hihat_notes = [42] * 4
hihat_times = [0.0, 0.375, 0.75, 1.125]
for note, time in zip(hihat_notes, hihat_times):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(note_obj)

midi.instruments.append(drums)

# Bar 2-4: Full ensemble

# Bass line: Walking chromatic line in D
bass_notes = [50, 51, 53, 52, 50, 49, 51, 50]  # D chromatic walking line
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for note, time in zip(bass_notes, bass_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords on beats 2 and 4 of bars 2 and 3
# Key is D, 7th chords: D7 (D F# A C), G7 (G B D F), A7 (A C# E G)
piano_notes = [
    62, 67, 69, 60,  # D7 at 1.875
    71, 76, 79, 72,  # G7 at 3.375
    65, 70, 74, 67   # A7 at 4.875
]
piano_times = [1.875, 1.875, 1.875, 1.875,
               3.375, 3.375, 3.375, 3.375,
               4.875, 4.875, 4.875, 4.875]
for note, time in zip(piano_notes, piano_times):
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Sax: Unique, minimal motif
# D (62), F# (67), B (71), rest (0.5s), then D (62) again
sax_notes = [62, 67, 71, 62]
sax_times = [1.5, 1.75, 2.0, 2.5]
sax_durations = [0.25, 0.25, 0.5, 0.5]

for note, time, duration in zip(sax_notes, sax_times, sax_durations):
    note_obj = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + duration)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Save the MIDI file
midi.write("dante_russo_intro.mid")
print("MIDI file generated: 'dante_russo_intro.mid'")

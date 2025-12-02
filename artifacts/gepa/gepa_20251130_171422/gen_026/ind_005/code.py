
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 4/4 time and 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160, time_signature_numerator=4, time_signature_denominator=4)

# Define key: D minor (Dm)
key = 'Dm'

# Define note numbers for Dm scale (D, Eb, F, G, Ab, Bb, C) in 12-tone equal temperament
# Convert to MIDI note numbers with root at C4 = 60
note_values = {
    'C': 60,
    'C#': 61,
    'D': 62,
    'Eb': 63,
    'E': 64,
    'F': 65,
    'F#': 66,
    'G': 67,
    'Ab': 68,
    'A': 69,
    'Bb': 70,
    'B': 71,
}

# Map scale to Dm (D, Eb, F, G, Ab, Bb, C)
scale_notes = [note_values['D'], note_values['Eb'], note_values['F'], note_values['G'],
               note_values['Ab'], note_values['Bb'], note_values['C']]

# Define time in seconds per bar (160 BPM, 4/4)
beats_per_bar = 4
seconds_per_beat = 60 / 160
seconds_per_bar = beats_per_bar * seconds_per_beat

# 4 bars = 6 seconds total
duration = 4 * seconds_per_bar

# Define instruments
program = {
    'drums': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'bass': pretty_midi.instrument_name_to_program('Double Bass'),
    'piano': pretty_midi.instrument_name_to_program('Acoustic Grand Piano'),
    'sax': pretty_midi.instrument_name_to_program('Tenor Saxophone')
}

# Create instrument tracks
drum_program = pretty_midi.instrument_name_to_program('Drum Kit')
drum_inst = pretty_midi.Instrument(program=drum_program)
pm.instruments.append(drum_inst)

bass_inst = pretty_midi.Instrument(program=program['bass'])
pm.instruments.append(bass_inst)

piano_inst = pretty_midi.Instrument(program=program['piano'])
pm.instruments.append(piano_inst)

sax_inst = pretty_midi.Instrument(program=program['sax'])
pm.instruments.append(sax_inst)

# Bar 1: Drums only — build tension with dynamic variation
# Kick on 1 and 3
kick_times = [0, 1.5]
kick_volumes = [0.6, 0.5]  # soft to medium

# Snare on 2 and 4
snare_times = [0.75, 2.25]
snare_volumes = [0.7, 0.6]  # medium to soft

# Hi-hats on every eighth note
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
hihat_volumes = [0.4, 0.3, 0.35, 0.2, 0.4, 0.3, 0.35, 0.2]  # with subtle variation

# Add drum notes
for t, v in zip(kick_times, kick_volumes):
    note = pretty_midi.Note(velocity=int(v * 127), pitch=36, start=t, end=t + 0.1)
    drum_inst.notes.append(note)

for t, v in zip(snare_times, snare_volumes):
    note = pretty_midi.Note(velocity=int(v * 127), pitch=38, start=t, end=t + 0.1)
    drum_inst.notes.append(note)

for t, v in zip(hihat_times, hihat_volumes):
    note = pretty_midi.Note(velocity=int(v * 127), pitch=42, start=t, end=t + 0.05)
    drum_inst.notes.append(note)

# Bar 2: Bass enters, walking line with chromatic approaches
# Bass line: D, Eb, F#, G, Ab, Bb, C, D (chromatic approaches on F and Bb)
bass_notes = [
    note_values['D'],  # D
    note_values['Eb'], # Eb
    note_values['F#'], # chromatic up from F
    note_values['G'],  # G
    note_values['Ab'], # Ab
    note_values['Bb'], # Bb
    note_values['C'],  # C
    note_values['D'],  # D
]

# Time positions for 4 beats (0.0, 0.75, 1.5, 2.25, 2.625, 3.375, 4.0, 4.75)
# Use 4 beats per bar, so times are: 0, 0.75, 1.5, 2.25, 2.625 (end of bar), etc.
bass_times = [0.0, 0.75, 1.5, 2.25, 2.625, 3.375, 4.0, 4.75]
bass_volumes = [0.7, 0.6, 0.65, 0.7, 0.6, 0.7, 0.75, 0.7]

# Add bass notes
for t, pitch, v in zip(bass_times, bass_notes, bass_volumes):
    note = pretty_midi.Note(velocity=int(v * 127), pitch=pitch, start=t, end=t + 0.25)
    bass_inst.notes.append(note)

# Bar 2-4: Piano enters — comping with 7th chords, dynamic and emotional
# Comp on 2 and 4 (beat 2 and 4 of each bar), with some space
# Dm7 = D, F, Ab, C
# Use variations: Dm7, Gm7, Cm7, Fm7, etc.
piano_notes = []

# Bar 2: comp on beat 2 (0.75) and 4 (2.25)
bar_2_comp = [
    (note_values['D'], 0.75, 0.5),  # D
    (note_values['F'], 0.75, 0.5),  # F
    (note_values['Ab'], 0.75, 0.5), # Ab
    (note_values['C'], 0.75, 0.5),  # C
    (note_values['G'], 2.25, 0.5),  # G
    (note_values['Bb'], 2.25, 0.5), # Bb
    (note_values['D'], 2.25, 0.5),  # D
    (note_values['F'], 2.25, 0.5),  # F
]

# Bar 3: comp on beat 2 (3.375) and 4 (5.0)
bar_3_comp = [
    (note_values['C'], 3.375, 0.5),  # C
    (note_values['Eb'], 3.375, 0.5), # Eb
    (note_values['G'], 3.375, 0.5),  # G
    (note_values['Bb'], 3.375, 0.5), # Bb
    (note_values['F'], 5.0, 0.5),    # F
    (note_values['Ab'], 5.0, 0.5),   # Ab
    (note_values['C'], 5.0, 0.5),    # C
    (note_values['Eb'], 5.0, 0.5),   # Eb
]

# Bar 4: comp on beat 2 (6.125) and 4 (7.75)
bar_4_comp = [
    (note_values['G'], 6.125, 0.5),  # G
    (note_values['Bb'], 6.125, 0.5), # Bb
    (note_values['D'], 6.125, 0.5),  # D
    (note_values['F'], 6.125, 0.5),  # F
    (note_values['C'], 7.75, 0.5),   # C
    (note_values['Eb'], 7.75, 0.5),  # Eb
    (note_values['G'], 7.75, 0.5),   # G
    (note_values['Bb'], 7.75, 0.5),  # Bb
]

# Add piano notes
for pitch, t, v in bar_2_comp + bar_3_comp + bar_4_comp:
    note = pretty_midi.Note(velocity=int(v * 127), pitch=pitch, start=t, end=t + 0.25)
    piano_inst.notes.append(note)

# Bar 2: Saxophone enters with a concise, emotional motif
# D, Eb, F, D — a simple but emotionally charged motif
# D (62), Eb (63), F (65), D (62)
sax_notes = [
    (62, 0.0, 0.8),  # D
    (63, 0.25, 0.75), # Eb
    (65, 0.5, 0.7),  # F
    (62, 0.75, 0.75) # D
]

# Add saxophone notes
for pitch, t, v in sax_notes:
    note = pretty_midi.Note(velocity=int(v * 127), pitch=pitch, start=t, end=t + 0.25)
    sax_inst.notes.append(note)

# Write MIDI file to disk
pm.write('intro_wayne.mid')


import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument_list = []

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Bar duration in seconds: 160 BPM = 60 / 160 = 0.375 seconds per beat
# 4 bars = 6 seconds total

# 1. Drums (Little Ray) - Bar 1
drums_program = pretty_midi.instrument_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drums_program)

# Kick on 1 and 3 (bar 1)
# 1st beat: 0.0s
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375))
# 3rd beat: 1.5s
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875))

# Snare on 2 and 4 (bar 1)
# 2nd beat: 0.75s
drums.notes.append(pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=0.875))
# 4th beat: 2.25s
drums.notes.append(pretty_midi.Note(velocity=85, pitch=38, start=2.25, end=2.375))

# Hi-hat on every 8th note (bar 1)
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=start, end=end))

instrument_list.append(drums)

# 2. Bass (Marcus) - Bars 2-4
bass_program = pretty_midi.instrument_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

# Walking bass line in F major (F, G, A, Bb, C, D, Eb, F)
# Bar 2: F, G, A, Bb
# Bar 3: C, D, Eb, F
# Bar 4: G, A, Bb, C

bass_notes = [78, 80, 82, 79, 81, 83, 80, 78, 80, 82, 79, 81, 83, 80, 78]
bass_durations = [0.25] * len(bass_notes)

start_time = 1.5  # Bar 2 starts at 1.5s
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time + i * 0.25, end=start_time + i * 0.25 + bass_durations[i])
    bass.notes.append(note)

instrument_list.append(bass)

# 3. Piano (Diane) - Bars 2-4
piano_program = pretty_midi.instrument_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

# Comping on 2 and 4 (bars 2-4)
# Use 7th chords in F major: F7, G7, C7, D7
chords = [
    [78, 82, 84, 86],  # F7 (78=F, 82=Bb, 84=C, 86=E)
    [80, 84, 87, 89],  # G7 (80=G, 84=B, 87=D, 89=F#)
    [81, 85, 87, 89],  # C7 (81=C, 85=E, 87=G, 89=B)
    [82, 86, 88, 90],  # D7 (82=D, 86=F#, 88=A, 90=C)
]

# Comp on 2 and 4 of each bar
comp_times = [2.25, 3.75, 5.25]  # 2nd beat of bar 2, 2nd beat of bar 3, 2nd beat of bar 4
for i, chord in enumerate(chords):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=75, pitch=note, start=comp_times[i], end=comp_times[i] + 0.25))

instrument_list.append(piano)

# 4. Tenor Sax (You) - Bars 2-4
sax_program = pretty_midi.instrument_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# Your motif: F - Bb - C - E (F7 chord, but played as a melody)
# Use unique rhythms and dynamics to make it sing and end with a question
# Bar 2: F (0.25s), Bb (0.3s), C (0.25s), then rest
# Bar 3: F (0.2s), Bb (0.2s), C (0.2s), rest
# Bar 4: E (0.3s), then rest — leaving it hanging

# Bar 2: F (78), Bb (79), C (81)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=95, pitch=79, start=2.0, end=2.3))
sax.notes.append(pretty_midi.Note(velocity=98, pitch=81, start=2.3, end=2.55))

# Bar 3: F (78), Bb (79), C (81)
sax.notes.append(pretty_midi.Note(velocity=95, pitch=78, start=3.25, end=3.45))
sax.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=3.45, end=3.65))
sax.notes.append(pretty_midi.Note(velocity=92, pitch=81, start=3.65, end=3.85))

# Bar 4: E (80), then rest — a question
sax.notes.append(pretty_midi.Note(velocity=105, pitch=80, start=4.5, end=4.8))

instrument_list.append(sax)

# Add instruments to the MIDI file
for instrument in instrument_list:
    pm.instruments.append(instrument)

# Save to a file
pm.write("jazz_intro_wayne.mid")

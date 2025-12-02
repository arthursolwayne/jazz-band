
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# BPM = 160, so each beat is 0.375 seconds
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar

# Bar 1: Drums only — tension, anticipation
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0

# Kick on 1 and 3
drum_notes = {
    36: [bar1_start, bar1_start + 2 * beat],  # Kick
    38: [bar1_start + beat, bar1_start + 3 * beat],  # Snare
    42: np.arange(bar1_start, bar1_start + 4 * beat, beat / 2)  # Hihat
}

for note_number, times in drum_notes.items():
    for t in times:
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=t, end=t + 0.1)
        drums.notes.append(note)

# Bar 2: Everyone comes in — sax melody (Dm7 chord: D, F, A, C)
# Start with a short motif — D, F, Bb (Dm7 with a chromatic passing tone)

bar2_start = bar1_start + bar

# Sax melody: D, F, Bb, D (with a little mystery in the Bb)
sax_notes = [
    (62, bar2_start + 0.0),     # D4
    (65, bar2_start + 0.5),     # F4
    (60, bar2_start + 0.75),    # Bb3
    (62, bar2_start + 1.0)      # D4
]

for pitch, start_time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + 0.25)
    sax.notes.append(note)

# Bass line: Walking line with chromatic approaches
# Dm7: D, F, A, C — root, 3, 5, 7
# Walking bass line: D, F, Eb, E, A, Bb, B, C
bass_notes = [
    (62, bar2_start + 0.0),     # D4
    (65, bar2_start + 0.25),    # F4
    (63, bar2_start + 0.5),     # Eb4 (chromatic approach to E)
    (64, bar2_start + 0.75),    # E4
    (67, bar2_start + 1.0),     # A4
    (61, bar2_start + 1.25),    # Bb4 (chromatic approach to B)
    (62, bar2_start + 1.5),     # B4
    (60, bar2_start + 1.75),    # C4
]

for pitch, start_time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time, end=start_time + 0.25)
    bass.notes.append(note)

# Piano: Comp on 2 and 4 — Dm7 chords
# Dm7: D, F, A, C
# Time: bar2_start + beat (bar 2, beat 2) and bar2_start + 3*beat (bar 2, beat 4)

piano_notes = [
    (62, bar2_start + beat, bar2_start + beat + 0.5),  # D4
    (65, bar2_start + beat, bar2_start + beat + 0.5),  # F4
    (67, bar2_start + beat, bar2_start + beat + 0.5),  # A4
    (60, bar2_start + beat, bar2_start + beat + 0.5),  # C4

    (62, bar2_start + 3 * beat, bar2_start + 3 * beat + 0.5),  # D4
    (65, bar2_start + 3 * beat, bar2_start + 3 * beat + 0.5),  # F4
    (67, bar2_start + 3 * beat, bar2_start + 3 * beat + 0.5),  # A4
    (60, bar2_start + 3 * beat, bar2_start + 3 * beat + 0.5)   # C4
]

for pitch, start_time, end_time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=end_time)
    piano.notes.append(note)

# Bar 3: Sax continues the melody, with a slight variation
bar3_start = bar2_start + bar

# Sax: F, A, Bb, D — same motif, half a step higher
sax_notes = [
    (65, bar3_start + 0.0),     # F4
    (67, bar3_start + 0.5),     # A4
    (60, bar3_start + 0.75),    # Bb3
    (62, bar3_start + 1.0)      # D4
]

for pitch, start_time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + 0.25)
    sax.notes.append(note)

# Bass: Continue walking
bass_notes = [
    (62, bar3_start + 0.0),     # D4
    (65, bar3_start + 0.25),    # F4
    (63, bar3_start + 0.5),     # Eb4
    (64, bar3_start + 0.75),    # E4
    (67, bar3_start + 1.0),     # A4
    (61, bar3_start + 1.25),    # Bb4
    (62, bar3_start + 1.5),     # B4
    (60, bar3_start + 1.75)     # C4
]

for pitch, start_time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time, end=start_time + 0.25)
    bass.notes.append(note)

# Piano: Comp on 2 and 4 again
piano_notes = [
    (62, bar3_start + beat, bar3_start + beat + 0.5),  # D4
    (65, bar3_start + beat, bar3_start + beat + 0.5),  # F4
    (67, bar3_start + beat, bar3_start + beat + 0.5),  # A4
    (60, bar3_start + beat, bar3_start + beat + 0.5),  # C4

    (62, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.5),  # D4
    (65, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.5),  # F4
    (67, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.5),  # A4
    (60, bar3_start + 3 * beat, bar3_start + 3 * beat + 0.5)   # C4
]

for pitch, start_time, end_time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=end_time)
    piano.notes.append(note)

# Bar 4: Sax leaves the motif hanging, with a hint of Dm
bar4_start = bar3_start + bar

# Sax: D, F
sax_notes = [
    (62, bar4_start + 0.0),     # D4
    (65, bar4_start + 0.5),     # F4
]

for pitch, start_time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + 0.25)
    sax.notes.append(note)

# Bass: Walks into a resolution
bass_notes = [
    (62, bar4_start + 0.0),     # D4
    (65, bar4_start + 0.25),    # F4
    (67, bar4_start + 0.5),     # A4
    (60, bar4_start + 0.75),    # C4
]

for pitch, start_time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time, end=start_time + 0.25)
    bass.notes.append(note)

# Piano: Comp on 2 and 4
piano_notes = [
    (62, bar4_start + beat, bar4_start + beat + 0.5),  # D4
    (65, bar4_start + beat, bar4_start + beat + 0.5),  # F4
    (67, bar4_start + beat, bar4_start + beat + 0.5),  # A4
    (60, bar4_start + beat, bar4_start + beat + 0.5),  # C4

    (62, bar4_start + 3 * beat, bar4_start + 3 * beat + 0.5),  # D4
    (65, bar4_start + 3 * beat, bar4_start + 3 * beat + 0.5),  # F4
    (67, bar4_start + 3 * beat, bar4_start + 3 * beat + 0.5),  # A4
    (60, bar4_start + 3 * beat, bar4_start + 3 * beat + 0.5)   # C4
]

for pitch, start_time, end_time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=end_time)
    piano.notes.append(note)

# Add some subtle dynamic variation on drums
for note in drums.notes:
    note.velocity = int(np.random.uniform(80, 110))

# Write out the MIDI file
pm.write("jazz_intro.mid")

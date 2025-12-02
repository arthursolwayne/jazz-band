
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key to D minor (Dm)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0)]  # 2 = D minor

# Create instruments for each player
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI drum kit uses piano program
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [bass, piano, drums, sax]

# Constants
BPM = 160
note_duration = 60.0 / BPM  # Duration of one beat in seconds

# Time per bar (4/4 time)
time_per_bar = 4 * note_duration
time_per_beat = note_duration

# Bar 1: Drums only - build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Time of events in bar 1 (start at 0)
bar1_start = 0.0

# Kick on 1 and 3
drum_kicks = [bar1_start + 0.0, bar1_start + 2.0]
for kick_time in drum_kicks:
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

# Snare on 2 and 4
drum_snares = [bar1_start + 1.0, bar1_start + 3.0]
for snare_time in drum_snares:
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

# Hi-Hat on every 8th
hihat_times = [bar1_start + 0.0, bar1_start + 0.5, bar1_start + 1.0, bar1_start + 1.5,
               bar1_start + 2.0, bar1_start + 2.5, bar1_start + 3.0, bar1_start + 3.5]
for hihat_time in hihat_times:
    hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(hihat_note)

# Bar 2: All instruments join in
bar2_start = time_per_bar

# --- Bass: Walking line with chromatic approaches (Dm7)
# Dm7: D, F, A, C
# Walking bass line in Dm: D - Eb - F - G - A - Bb - B - C - D
# Tune it to D minor, with chromatic passing tones
bass_notes = [
    (bar2_start, 62, 100),  # D
    (bar2_start + 0.5, 63, 90),  # Eb
    (bar2_start + 1.0, 64, 95),  # F
    (bar2_start + 1.5, 67, 100),  # G
    (bar2_start + 2.0, 69, 100),  # A
    (bar2_start + 2.5, 70, 95),  # Bb
    (bar2_start + 3.0, 71, 90),  # B
    (bar2_start + 3.5, 67, 100),  # C (Dm7 root)
]

for start, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# --- Piano: 7th chords on 2 and 4, comping
# Dm7 = D, F, A, C
# Comp on 2nd and 4th beats
comp_time = bar2_start + 1.0  # 2nd beat
comp_notes = [62, 65, 69, 67]  # D, F, A, C
for note in comp_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=comp_time, end=comp_time + 0.25)
    piano.notes.append(piano_note)

comp_time = bar2_start + 3.0  # 4th beat
for note in comp_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=comp_time, end=comp_time + 0.25)
    piano.notes.append(piano_note)

# --- Drums: Same pattern but with a little more energy
bar2_drums = [bar2_start + t for t in hihat_times]
for hihat_time in bar2_drums:
    hihat_note = pretty_midi.Note(velocity=95, pitch=42, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(hihat_note)

# Kick and snare same as before, shifted to bar 2
for kick_time in [bar2_start + 0.0, bar2_start + 2.0]:
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

for snare_time in [bar2_start + 1.0, bar2_start + 3.0]:
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

# --- Sax: The motif — one short, open-ended phrase
# Motif: D - F - A - (rest) — ends on a question
# D is 62, F is 65, A is 69
sax_notes = [
    (bar2_start, 62, 110, 0.25),  # D
    (bar2_start + 0.5, 65, 110, 0.25),  # F
    (bar2_start + 1.0, 69, 110, 0.25),  # A
    (bar2_start + 1.5, 0, 0, 0.5),  # Rest
]

for start, pitch, vel, dur in sax_notes:
    if pitch != 0:
        note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + dur)
        sax.notes.append(note)

# Bar 3: Same as bar 2, but with variation in dynamics and timing
bar3_start = bar2_start + time_per_bar

# Bass: Slight variation in velocity, same line
bass_notes = [
    (bar3_start, 62, 95),  # D
    (bar3_start + 0.5, 63, 85),  # Eb
    (bar3_start + 1.0, 64, 90),  # F
    (bar3_start + 1.5, 67, 100),  # G
    (bar3_start + 2.0, 69, 100),  # A
    (bar3_start + 2.5, 70, 90),  # Bb
    (bar3_start + 3.0, 71, 85),  # B
    (bar3_start + 3.5, 67, 95),  # C
]

for start, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: Same comping, same notes, slight variation in timing
comp_time = bar3_start + 1.0
for note in comp_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=comp_time, end=comp_time + 0.25)
    piano.notes.append(piano_note)

comp_time = bar3_start + 3.0
for note in comp_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=comp_time, end=comp_time + 0.25)
    piano.notes.append(piano_note)

# Drums: Same pattern
bar3_drums = [bar3_start + t for t in hihat_times]
for hihat_time in bar3_drums:
    hihat_note = pretty_midi.Note(velocity=95, pitch=42, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(hihat_note)

# Kick and snare same as before, shifted to bar 3
for kick_time in [bar3_start + 0.0, bar3_start + 2.0]:
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

for snare_time in [bar3_start + 1.0, bar3_start + 3.0]:
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

# Bar 4: Same as bar 2 and 3, but sax ends with a question, not a statement
bar4_start = bar3_start + time_per_bar

# Bass: Same as bar 2
bass_notes = [
    (bar4_start, 62, 100),  # D
    (bar4_start + 0.5, 63, 90),  # Eb
    (bar4_start + 1.0, 64, 95),  # F
    (bar4_start + 1.5, 67, 100),  # G
    (bar4_start + 2.0, 69, 100),  # A
    (bar4_start + 2.5, 70, 95),  # Bb
    (bar4_start + 3.0, 71, 90),  # B
    (bar4_start + 3.5, 67, 100),  # C (Dm7 root)
]

for start, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: Same comping, same notes
comp_time = bar4_start + 1.0
for note in comp_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=comp_time, end=comp_time + 0.25)
    piano.notes.append(piano_note)

comp_time = bar4_start + 3.0
for note in comp_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=comp_time, end=comp_time + 0.25)
    piano.notes.append(piano_note)

# Drums: Same pattern
bar4_drums = [bar4_start + t for t in hihat_times]
for hihat_time in bar4_drums:
    hihat_note = pretty_midi.Note(velocity=95, pitch=42, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(hihat_note)

# Kick and snare same as before, shifted to bar 4
for kick_time in [bar4_start + 0.0, bar4_start + 2.0]:
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

for snare_time in [bar4_start + 1.0, bar4_start + 3.0]:
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

# Sax: Ends with a question — the rest at the end
sax_notes = [
    (bar4_start, 62, 110, 0.25),  # D
    (bar4_start + 0.5, 65, 110, 0.25),  # F
    (bar4_start + 1.0, 69, 110, 0.25),  # A
    (bar4_start + 1.5, 0, 0, 0.5),  # Rest
]

for start, pitch, vel, dur in sax_notes:
    if pitch != 0:
        note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + dur)
        sax.notes.append(note)

# Save the MIDI file
pm.write('dante_intro.mid')

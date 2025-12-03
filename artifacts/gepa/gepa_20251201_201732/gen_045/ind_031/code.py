
import pretty_midi
import numpy as np

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax (program 64)
pm.instruments.append(instrument)

# Tempo setup
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0, ticks=0)]
pm.tempos = [pretty_midi.TempoChange(tempo=160, time=0)]

# Define time per beat (in seconds)
beats_per_bar = 4
bpm = 160
seconds_per_beat = 60.0 / bpm
seconds_per_bar = seconds_per_beat * beats_per_bar
beat_ticks = pm.time_to_ticks(seconds_per_beat)
bar_ticks = beat_ticks * beats_per_bar

# Function to create a note
def note_on(note, start_time, duration, velocity=100):
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=start_time, end=start_time + duration)
    instrument.notes.append(note_obj)

# Define the motif: Tenor Sax (you)
# Motif: F - G - A - Bb (F7sus4), then rest
motif_start = 0
note_on(71, motif_start, 0.375)  # F (71)
note_on(72, motif_start + 0.375, 0.375)  # G
note_on(74, motif_start + 0.75, 0.375)  # A
note_on(73, motif_start + 1.125, 0.375)  # Bb
note_on(71, motif_start + 1.5, 0.375)  # F again, but only for 0.375s, leaving it hanging

# Bass line (Marcus) — walking line in F
# Bar 1: F (D2) -> Bb (F#2) -> B (G2) -> E (Eb2) -> F (D2)
bass_line = [38, 43, 43, 42, 38]
for i, note in enumerate(bass_line):
    start = 0 + (i * seconds_per_beat)
    note_on(note, start, 0.125)

# Piano (Diane) — open voicings
# Bar 1: Fmaj7 (F, A, C, E) — open voicing
note_on(71, 0, 0.375)  # F
note_on(74, 0, 0.375)  # A
note_on(76, 0, 0.375)  # C
note_on(79, 0, 0.375)  # E

# Bar 2: Fmaj7 -> Gm7 (G, Bb, D, F)
note_on(72, 1.5, 0.375)  # G
note_on(71, 1.5, 0.375)  # Bb
note_on(74, 1.5, 0.375)  # D
note_on(71, 1.5, 0.375)  # F (again, for a 7th)

# Bar 3: Am7 (A, C, E, G)
note_on(74, 3.0, 0.375)  # A
note_on(76, 3.0, 0.375)  # C
note_on(79, 3.0, 0.375)  # E
note_on(72, 3.0, 0.375)  # G

# Bar 4: D7 (F#, A, C#, F)
note_on(76, 4.5, 0.375)  # F# (76)
note_on(79, 4.5, 0.375)  # A
note_on(81, 4.5, 0.375)  # C#
note_on(71, 4.5, 0.375)  # F

# Drums (Little Ray)
# Kick on 1 and 3
kick_notes = [36]  # Kick drum
for i in range(0, 4):
    beat = i * seconds_per_beat
    if i % 2 == 0:
        note_on(36, beat, 0.1)

# Snare on 2 and 4
snare_notes = [38]  # Snare drum
for i in range(0, 4):
    beat = i * seconds_per_beat
    if i % 2 == 1:
        note_on(38, beat, 0.1)

# Hi-hat on every eighth note
hihat_notes = [42]  # Hi-hat
for i in range(0, 8):
    beat = i * seconds_per_beat / 2
    note_on(42, beat, 0.05)

# Save the MIDI file
pm.write('intro.mid')
print("Generated 'intro.mid' — time to make him lean forward.")


import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)
instrument_names = ["tenor_sax", "piano", "bass", "drums"]
instruments = {name: pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program(name)) for name in instrument_names}
pm.instruments.extend(instruments.values())

# Define time in seconds per bar (4/4 at 160 BPM)
beat_duration = 60.0 / 160  # 0.375 seconds per beat
bar_duration = 4 * beat_duration  # 1.5 seconds per bar
total_duration = 4 * bar_duration  # 6 seconds

# Define note durations in seconds
eighth_note = beat_duration / 2
quarter_note = beat_duration
half_note = 2 * quarter_note
whole_note = 4 * quarter_note

# Helper function to add a note to an instrument
def add_note(instrument, start, pitch, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    instrument.notes.append(note)

# GLOBAL TIME TRACKER
time = 0.0

# --- BAR 1: DRUMS ONLY (Little Ray) ---
# Kick on 1 and 3
add_note(instruments["drums"], time, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)
add_note(instruments["drums"], time + 2 * beat_duration, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)

# Snare on 2 and 4
add_note(instruments["drums"], time + beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)
add_note(instruments["drums"], time + 3 * beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)

# Hi-hats on every eighth note
for i in range(4):
    add_note(instruments["drums"], time + i * eighth_note, pretty_midi.note_number_to_name(42), eighth_note, velocity=80)

# Move to next bar
time += bar_duration

# --- BAR 2: BASS (Marcus) -- Walking line in F minor
# F minor scale: F, G#, A, Bb, C, Db, D
# Chromatic approaches, no repeated notes

# Start on F and walk up
add_note(instruments["bass"], time, 71, quarter_note, velocity=70)  # F3
add_note(instruments["bass"], time + beat_duration, 73, quarter_note, velocity=70)  # G#3
add_note(instruments["bass"], time + 2 * beat_duration, 72, quarter_note, velocity=70)  # A3
add_note(instruments["bass"], time + 3 * beat_duration, 71, quarter_note, velocity=70)  # F3

# --- BAR 2: PIANO (Diane) -- Comp on 2 and 4 with F7 chords
# F7: F, A, C, E♭
# 2nd beat: F7
for note in [71, 74, 76, 70]:  # F3, A3, C4, Eb4
    add_note(instruments["piano"], time + beat_duration, note, quarter_note, velocity=80)

# 4th beat: F7 again
for note in [71, 74, 76, 70]:  # F3, A3, C4, Eb4
    add_note(instruments["piano"], time + 3 * beat_duration, note, quarter_note, velocity=80)

# --- BAR 2: DRUMS (Little Ray) -- Same pattern as before
# Kick on 1 and 3
add_note(instruments["drums"], time, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)
add_note(instruments["drums"], time + 2 * beat_duration, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)

# Snare on 2 and 4
add_note(instruments["drums"], time + beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)
add_note(instruments["drums"], time + 3 * beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)

# Hi-hats on every eighth note
for i in range(4):
    add_note(instruments["drums"], time + i * eighth_note, pretty_midi.note_number_to_name(42), eighth_note, velocity=80)

# --- BAR 3: PIANO (Diane) -- Comp on 2 and 4 with F7 chords
# 2nd beat: F7
for note in [71, 74, 76, 70]:  # F3, A3, C4, Eb4
    add_note(instruments["piano"], time + beat_duration, note, quarter_note, velocity=80)

# 4th beat: F7 again
for note in [71, 74, 76, 70]:  # F3, A3, C4, Eb4
    add_note(instruments["piano"], time + 3 * beat_duration, note, quarter_note, velocity=80)

# --- BAR 3: BASS (Marcus) -- Walk down
# F, Eb, D, C
add_note(instruments["bass"], time, 71, quarter_note, velocity=70)  # F3
add_note(instruments["bass"], time + beat_duration, 70, quarter_note, velocity=70)  # Eb3
add_note(instruments["bass"], time + 2 * beat_duration, 69, quarter_note, velocity=70)  # D3
add_note(instruments["bass"], time + 3 * beat_duration, 67, quarter_note, velocity=70)  # C3

# --- BAR 3: DRUMS (Little Ray) -- Same pattern as before
# Kick on 1 and 3
add_note(instruments["drums"], time, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)
add_note(instruments["drums"], time + 2 * beat_duration, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)

# Snare on 2 and 4
add_note(instruments["drums"], time + beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)
add_note(instruments["drums"], time + 3 * beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)

# Hi-hats on every eighth note
for i in range(4):
    add_note(instruments["drums"], time + i * eighth_note, pretty_midi.note_number_to_name(42), eighth_note, velocity=80)

# --- BAR 4: SAX (Dante) -- Motif: A descending line with tension
# F minor scale: F, G#, A, Bb, C, Db, D
# Motif: F - Eb - D - C (descending with tension)
# Start at time (end of bar 3)
sax_notes = [71, 70, 69, 67]  # F3, Eb3, D3, C3
for i, note in enumerate(sax_notes):
    add_note(instruments["tenor_sax"], time + i * eighth_note, note, eighth_note, velocity=100)

# --- BAR 4: PIANO (Diane) -- Comp on 2 and 4 with F7 chords
# 2nd beat: F7
for note in [71, 74, 76, 70]:  # F3, A3, C4, Eb4
    add_note(instruments["piano"], time + beat_duration, note, quarter_note, velocity=80)

# 4th beat: F7 again
for note in [71, 74, 76, 70]:  # F3, A3, C4, Eb4
    add_note(instruments["piano"], time + 3 * beat_duration, note, quarter_note, velocity=80)

# --- BAR 4: BASS (Marcus) -- Walk up again
# C, Db, D, F
add_note(instruments["bass"], time, 67, quarter_note, velocity=70)  # C3
add_note(instruments["bass"], time + beat_duration, 68, quarter_note, velocity=70)  # Db3
add_note(instruments["bass"], time + 2 * beat_duration, 69, quarter_note, velocity=70)  # D3
add_note(instruments["bass"], time + 3 * beat_duration, 71, quarter_note, velocity=70)  # F3

# --- BAR 4: DRUMS (Little Ray) -- Same pattern as before
# Kick on 1 and 3
add_note(instruments["drums"], time, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)
add_note(instruments["drums"], time + 2 * beat_duration, pretty_midi.note_number_to_name(36), quarter_note, velocity=100)

# Snare on 2 and 4
add_note(instruments["drums"], time + beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)
add_note(instruments["drums"], time + 3 * beat_duration, pretty_midi.note_number_to_name(38), quarter_note, velocity=100)

# Hi-hats on every eighth note
for i in range(4):
    add_note(instruments["drums"], time + i * eighth_note, pretty_midi.note_number_to_name(42), eighth_note, velocity=80)

# Save the MIDI file
pm.write("jazz_intro_wayne.midi")
print("MIDI file saved as 'jazz_intro_wayne.midi'")

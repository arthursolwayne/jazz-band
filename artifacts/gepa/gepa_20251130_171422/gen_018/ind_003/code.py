
import pretty_midi
import numpy as np

# Initialize the Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Define time signature and key
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0, tempo=160)]
pm.key_signature_changes = [pretty_midi.KeySignature(key_number=15, time=0)]  # F minor

# Define the duration of a bar in seconds (160 BPM -> 0.375 sec per beat)
beat_duration = 0.375
bar_duration = beat_duration * 4

# --- DRUMS: Bar 1 (Intro) ---
# Kick on 1 and 3, Snare on 2 and 4
# Hihat every eighth note
for i in range(8):
    note = pretty_midi.Note(velocity=80, pitch=pretty_midi.note_number_to_name(42)[1], start=i * beat_duration / 2, end=(i + 1) * beat_duration / 2)
    drums.notes.append(note)

# Kick on 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0, end=beat_duration),
              pretty_midi.Note(velocity=100, pitch=36, start=2 * beat_duration, end=3 * beat_duration)]
for note in kick_notes:
    drums.notes.append(note)

# Snare on 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=beat_duration, end=2 * beat_duration),
               pretty_midi.Note(velocity=100, pitch=38, start=3 * beat_duration, end=4 * beat_duration)]
for note in snare_notes:
    drums.notes.append(note)

# --- PIANO: Bar 2 and 4 (Comp on 2 and 4) ---
F7 = [53, 55, 57, 50]  # F, A, C, Eb
bar_2_start = bar_duration
bar_4_start = 2 * bar_duration

for bar in [bar_2_start, bar_4_start]:
    # Comp on 2 and 4
    for idx, note_num in enumerate(F7):
        start = bar + (idx + 1) * beat_duration
        end = start + beat_duration
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_num, start=start, end=end))

# --- BASS: Bar 3 (Chromatic walking line) ---
bar_3_start = 2 * bar_duration
bass_line = [57, 58, 59, 60, 61, 62, 63, 64, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51]  # Fm chromatic walk
for i, note_num in enumerate(bass_line):
    start = bar_3_start + (i * beat_duration) / 4
    end = start + (beat_duration / 4)
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note_num, start=start, end=end))

# --- SAX: Bar 4 (Melody) ---
bar_4_start = 2 * bar_duration
motif = [55, 57, 53, 55]  # D, E, C, D (Fm melody motive)

# Spacing between notes
note_durations = [0.25, 0.5, 0.75, 1.0]  # Varying durations for tension and space

for i, note_num in enumerate(motif):
    # Start time: bar 4 + (i * beat_duration)
    start = bar_4_start + (i * beat_duration)
    end = start + note_durations[i]
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note_num, start=start, end=end))

# Save the MIDI
pm.write('dante_russo_intro.mid')
print("MIDI file written to 'dante_russo_intro.mid'")

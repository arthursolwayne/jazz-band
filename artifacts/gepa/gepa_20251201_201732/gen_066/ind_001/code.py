
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures and key
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.key_signature_changes = [pretty_midi.KeySignature(key_number=21, time=0.0)]  # F minor (key number 21)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drums_program)

tenor_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
tenor = pretty_midi.Instrument(program=tenor_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [bass, piano, drums, tenor]

# Constants
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT  # seconds per bar
NOTE_DURATION = BEAT / 2  # half note duration
EIGHTH_NOTE_DURATION = BEAT / 4  # eighth note duration

# Helper function to add a note
def add_note(instrument, pitch, start_time, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration)
    instrument.notes.append(note)

# Bar 1: Drums only — driving rhythm with kick on 1 & 3, snare on 2 & 4, hihat on every eighth
# Time: 0.0 to 1.5 seconds

# Kick on 1 and 3
add_note(drums, pretty_midi.note_number_to_name(36, octave=3)[2:], 0.0, NOTE_DURATION, velocity=100)
add_note(drums, pretty_midi.note_number_to_name(36, octave=3)[2:], 1.0, NOTE_DURATION, velocity=100)

# Snare on 2 and 4
add_note(drums, pretty_midi.note_number_to_name(38, octave=3)[2:], 0.5, NOTE_DURATION, velocity=100)
add_note(drums, pretty_midi.note_number_to_name(38, octave=3)[2:], 1.5, NOTE_DURATION, velocity=100)

# Hi-hat on every eighth note
for i in range(8):
    add_note(drums, pretty_midi.note_number_to_name(49, octave=3)[2:], i * EIGHTH_NOTE_DURATION, EIGHTH_NOTE_DURATION, velocity=80)

# Bar 2: Everyone in — Tenor sax takes a brief, singable motif
# Tenor motif: Fm (F, Ab, Bb) — a short, emotional line, like a question

# Tenor: F (65), Ab (67), Bb (62), F (65) — simple, expressive, minimal
add_note(tenor, 65, 1.5, NOTE_DURATION, velocity=100)  # F (root)
add_note(tenor, 67, 2.0, NOTE_DURATION, velocity=100)  # Ab (b9)
add_note(tenor, 62, 2.5, NOTE_DURATION, velocity=100)  # Bb (7)
add_note(tenor, 65, 3.0, NOTE_DURATION, velocity=100)  # F (restatement)

# Bass: Walking line in Fm — roots and fifths with chromatic approaches
# Fm: F, C, Ab, D, F, C, Ab, D
# Add chromatic approaches (e.g., F# before F, Db before Ab, etc.)
# Bar 2: C (60), D (62), Ab (67), Bb (62), F (65), C (60), D (62), Ab (67)

# Bass notes: [F, C, Ab, D, F, C, Ab, D]
bass_notes = [65, 60, 67, 62, 65, 60, 67, 62]
note_indices = [0, 1, 2, 3, 4, 5, 6, 7]
for i, note in enumerate(bass_notes):
    add_note(bass, note, 1.5 + (i * EIGHTH_NOTE_DURATION), EIGHTH_NOTE_DURATION, velocity=80)

# Piano: Open voicings, each bar different chord, resolve on the last
# Bar 2: Fm7 -> Ab7 -> Bbmaj7 -> Fm7

# Fm7: F, Ab, Bb, Db (65, 67, 62, 63)
add_note(piano, 65, 1.5, NOTE_DURATION, velocity=80)
add_note(piano, 67, 1.5, NOTE_DURATION, velocity=80)
add_note(piano, 62, 1.5, NOTE_DURATION, velocity=80)
add_note(piano, 63, 1.5, NOTE_DURATION, velocity=80)

# Ab7: Ab, C, Eb, Gb (67, 60, 57, 58)
add_note(piano, 67, 2.0, NOTE_DURATION, velocity=80)
add_note(piano, 60, 2.0, NOTE_DURATION, velocity=80)
add_note(piano, 57, 2.0, NOTE_DURATION, velocity=80)
add_note(piano, 58, 2.0, NOTE_DURATION, velocity=80)

# Bbmaj7: Bb, D, F, Ab (62, 65, 67, 67)
add_note(piano, 62, 2.5, NOTE_DURATION, velocity=80)
add_note(piano, 65, 2.5, NOTE_DURATION, velocity=80)
add_note(piano, 67, 2.5, NOTE_DURATION, velocity=80)
add_note(piano, 67, 2.5, NOTE_DURATION, velocity=80)

# Fm7 again (resolve)
add_note(piano, 65, 3.0, NOTE_DURATION, velocity=80)
add_note(piano, 67, 3.0, NOTE_DURATION, velocity=80)
add_note(piano, 62, 3.0, NOTE_DURATION, velocity=80)
add_note(piano, 63, 3.0, NOTE_DURATION, velocity=80)

# Bar 3: Drums continue with same rhythm
# Bar 4: Tenor completes the motif with a restrained, emotional resolution

# Bar 3: Drums
for i in range(8):
    add_note(drums, pretty_midi.note_number_to_name(49, octave=3)[2:], 3.0 + (i * EIGHTH_NOTE_DURATION), EIGHTH_NOTE_DURATION, velocity=80)

# Kick on 1 and 3
add_note(drums, pretty_midi.note_number_to_name(36, octave=3)[2:], 3.0, NOTE_DURATION, velocity=100)
add_note(drums, pretty_midi.note_number_to_name(36, octave=3)[2:], 4.0, NOTE_DURATION, velocity=100)

# Snare on 2 and 4
add_note(drums, pretty_midi.note_number_to_name(38, octave=3)[2:], 3.5, NOTE_DURATION, velocity=100)
add_note(drums, pretty_midi.note_number_to_name(38, octave=3)[2:], 4.5, NOTE_DURATION, velocity=100)

# Bar 4: Tenor completes the motif — now resolved, with a touch of yearning

# Tenor: F (65), Ab (67), Bb (62), F (65) — slightly slower, more contemplative
add_note(tenor, 65, 4.5, NOTE_DURATION, velocity=80)  # F (root)
add_note(tenor, 67, 5.0, NOTE_DURATION, velocity=80)  # Ab (b9)
add_note(tenor, 62, 5.5, NOTE_DURATION, velocity=80)  # Bb (7)
add_note(tenor, 65, 6.0, NOTE_DURATION, velocity=80)  # F (restatement, softer)

# Bass: Walking line continues
bass_notes = [60, 62, 67, 65, 60, 62, 67, 65]
note_indices = [0, 1, 2, 3, 4, 5, 6, 7]
for i, note in enumerate(bass_notes):
    add_note(bass, note, 4.5 + (i * EIGHTH_NOTE_DURATION), EIGHTH_NOTE_DURATION, velocity=80)

# Piano: Final bar — return to Fm7
add_note(piano, 65, 4.5, NOTE_DURATION, velocity=80)
add_note(piano, 67, 4.5, NOTE_DURATION, velocity=80)
add_note(piano, 62, 4.5, NOTE_DURATION, velocity=80)
add_note(piano, 63, 4.5, NOTE_DURATION, velocity=80)

# Save the MIDI file
pm.write('dante_russo_intro.mid')
print("MIDI file generated: 'dante_russo_intro.mid'")


import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # MIDI ticks per quarter note

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempos = [pretty_midi.TempoChange(160, 0)]

# Define key: Dm (D Dorian, but we'll use Dm7 as a base)
key = 'Dm'

# Define note numbers for Dm7 chord
Dm7_notes = [50, 53, 57, 60]  # D, F, A, C

# Define each instrument

# Drums (Little Ray)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

# Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# Tenor Sax (Dante)
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# Time per bar in seconds
BPM = 160
seconds_per_bar = 60 / BPM  # 0.375 seconds per beat, 1.5 seconds per bar
bar_length_ticks = int(seconds_per_bar * pm.resolution)

# Helper function to convert seconds to ticks
def seconds_to_ticks(seconds):
    return int(seconds * pm.resolution)

# Function to add a note to an instrument
def add_note(instrument, note_number, start_time, end_time, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start_time, end=end_time)
    instrument.notes.append(note)

# Bar 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
add_note(drums, 36, 0, 0.1875)  # Kick on beat 1
add_note(drums, 36, 0.75, 0.9375)  # Kick on beat 3

# Snare on 2 and 4
add_note(drums, 38, 0.375, 0.5625)  # Snare on beat 2
add_note(drums, 38, 1.125, 1.3125)  # Snare on beat 4

# Hihat on every eighth note
for i in range(8):
    add_note(drums, 42, i * 0.375, i * 0.375 + 0.0625)

# Bar 2: Everyone in. Sax starts the motif.

# Tenor sax - Dm7 - start with a motif that lingers
# D (50), F (53), A (57) - with rests and unique durations

add_note(sax, 50, 1.5, 1.75)  # D
add_note(sax, 53, 1.875, 2.0625)  # F
add_note(sax, 57, 2.25, 2.4375)  # A
add_note(sax, 50, 2.75, 2.9375)  # D again, but with rest in between for tension

# Bass - Marcus walks the Dm7 line, chromatic approach
# D (50), F (53), Bb (58), C (60) -> chromatic approach to A
add_note(bass, 50, 1.5, 1.75)
add_note(bass, 52, 1.75, 1.9375)
add_note(bass, 53, 1.9375, 2.125)
add_note(bass, 57, 2.125, 2.375)
add_note(bass, 60, 2.375, 2.625)

# Piano - Diane, 7th chords, comps on 2 and 4
# Dm7 (50, 53, 57, 60)
add_note(piano, 50, 1.5, 1.6875)
add_note(piano, 53, 1.5, 1.6875)
add_note(piano, 57, 1.5, 1.6875)
add_note(piano, 60, 1.5, 1.6875)

# Bar 3: Everyone continues

# Tenor sax - carry the motif again, but shorter
add_note(sax, 50, 3.0, 3.25)
add_note(sax, 53, 3.375, 3.5625)
add_note(sax, 57, 3.75, 3.9375)

# Bass - Marcus continues walking, chromatic
add_note(bass, 50, 3.0, 3.25)
add_note(bass, 52, 3.25, 3.4375)
add_note(bass, 53, 3.4375, 3.625)
add_note(bass, 57, 3.625, 3.875)
add_note(bass, 60, 3.875, 4.125)

# Piano - Diane comps the same Dm7 on 2 and 4
add_note(piano, 50, 3.0, 3.1875)
add_note(piano, 53, 3.0, 3.1875)
add_note(piano, 57, 3.0, 3.1875)
add_note(piano, 60, 3.0, 3.1875)

# Bar 4: Resolution, sax finishes the motif

# Tenor sax - resolve the motif
add_note(sax, 50, 4.5, 4.75)
add_note(sax, 53, 4.875, 5.0625)
add_note(sax, 57, 5.25, 5.4375)

# Bass - walk back down to D
add_note(bass, 57, 4.5, 4.75)
add_note(bass, 53, 4.75, 4.9375)
add_note(bass, 50, 4.9375, 5.125)
add_note(bass, 48, 5.125, 5.375)

# Piano - Diane plays a final Dm7 chord
add_note(piano, 50, 4.5, 4.6875)
add_note(piano, 53, 4.5, 4.6875)
add_note(piano, 57, 4.5, 4.6875)
add_note(piano, 60, 4.5, 4.6875)

# Drums - final bar - same pattern as bar 1
# Kick on 1 and 3
add_note(drums, 36, 3.0, 3.1875)
add_note(drums, 36, 3.75, 3.9375)

# Snare on 2 and 4
add_note(drums, 38, 3.375, 3.5625)
add_note(drums, 38, 4.125, 4.3125)

# Hihat on every eighth note
for i in range(8):
    add_note(drums, 42, 3.0 + i * 0.375, 3.0 + i * 0.375 + 0.0625)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file generated: 'dante_intro.mid'")

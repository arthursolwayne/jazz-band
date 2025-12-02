
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set the key to D major
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0.0)]  # D major

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define the time for each bar (6 seconds for 4 bars)
bar_length = 1.5  # seconds per bar
total_time = 6.0  # 4 bars

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
pm.instruments = [bass, piano, drums, sax]

# Define MIDI note numbers
D4 = 62
F#4 = 64
A4 = 69
C#5 = 71
E5 = 74
G5 = 76
B5 = 79
D5 = 74
F#5 = 76
A5 = 81

# Function to add a note
def add_note(instrument, note_number, start, end, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)
    instrument.notes.append(note)

# ----------------
# DRUMS (Little Ray)
# ----------------

# Kick on 1 and 3 (beat 0 and 2)
kick_beat = 0.0
kick_duration = 0.15
add_note(drums, pretty_midi.PercussionNote.kick, kick_beat, kick_beat + kick_duration)

kick_beat = 2.0
add_note(drums, pretty_midi.PercussionNote.kick, kick_beat, kick_beat + kick_duration)

# Snare on 2 and 4 (beat 1 and 3)
snare_beat = 1.0
add_note(drums, pretty_midi.PercussionNote.snare, snare_beat, snare_beat + kick_duration)

snare_beat = 3.0
add_note(drums, pretty_midi.PercussionNote.snare, snare_beat, snare_beat + kick_duration)

# Hi-hat on every eighth note (6 total per bar)
hi_hat_beat = 0.0
hi_hat_duration = 0.1
for i in range(6):
    add_note(drums, pretty_midi.PercussionNote.closed_hi_hat, hi_hat_beat, hi_hat_beat + hi_hat_duration)
    hi_hat_beat += 0.25

# ----------------
# BASS (Marcus)
# ----------------

# Walking bass line, chromatic approach, no repeated notes
# Bar 1: D4, F#4, A4, C#5
add_note(bass, D4, 0.0, 0.375)
add_note(bass, F#4, 0.375, 0.75)
add_note(bass, A4, 0.75, 1.125)
add_note(bass, C#5, 1.125, 1.5)

# Bar 2: E5 (chromatic approach from D5), G5, B5, D5
add_note(bass, E5, 1.5, 1.875)
add_note(bass, G5, 1.875, 2.25)
add_note(bass, B5, 2.25, 2.625)
add_note(bass, D5, 2.625, 3.0)

# Bar 3: F#5, A5, C#5, E5
add_note(bass, F#5, 3.0, 3.375)
add_note(bass, A5, 3.375, 3.75)
add_note(bass, C#5, 3.75, 4.125)
add_note(bass, E5, 4.125, 4.5)

# Bar 4: G5, B5, D5, F#5
add_note(bass, G5, 4.5, 4.875)
add_note(bass, B5, 4.875, 5.25)
add_note(bass, D5, 5.25, 5.625)
add_note(bass, F#5, 5.625, 6.0)

# ----------------
# PIANO (Diane)
# ----------------

# 7th chords, comp on 2 and 4 (beat 1 and 3)
# Bar 1: D7 (D, F#, A, C#)
add_note(piano, D4, 1.0, 1.375, 100)
add_note(piano, F#4, 1.0, 1.375, 100)
add_note(piano, A4, 1.0, 1.375, 100)
add_note(piano, C#5, 1.0, 1.375, 100)

# Bar 2: G7 (G, B, D, F#)
add_note(piano, G4, 3.0, 3.375, 100)
add_note(piano, B4, 3.0, 3.375, 100)
add_note(piano, D5, 3.0, 3.375, 100)
add_note(piano, F#5, 3.0, 3.375, 100)

# Bar 3: A7 (A, C#, E, G)
add_note(piano, A4, 5.0, 5.375, 100)
add_note(piano, C#5, 5.0, 5.375, 100)
add_note(piano, E5, 5.0, 5.375, 100)
add_note(piano, G5, 5.0, 5.375, 100)

# ----------------
# SAX (Dante)
# ----------------

# Motif: D4 - F#4 - A4 - D5 (suspended, lingering)
# Start it in bar 2, leave it hanging, come back in bar 3

# Bar 2 (start)
add_note(sax, D4, 1.5, 1.75, 100)
add_note(sax, F#4, 1.75, 2.0, 100)
add_note(sax, A4, 2.0, 2.25, 100)

# Bar 3 (finish)
add_note(sax, D5, 3.0, 3.25, 100)

# Bar 4 (rest, let it linger)
# No notes — let the air carry it

# Save the MIDI file
pm.write('dante_russo_intro.mid')


import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drum_inst = pretty_midi.Instrument(program=drum_program)
bass_inst = pretty_midi.Instrument(program=bass_program)
piano_inst = pretty_midi.Instrument(program=piano_program)
sax_inst = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_inst, bass_inst, piano_inst, sax_inst]

# Define time in seconds per bar (160 BPM = 60/160 = 0.375 sec per beat, 1.5 sec per bar)
bar_length = 1.5
beat_length = 0.375

# Helper function to add a note
def add_note(instrument, pitch, start, end, velocity):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    instrument.notes.append(note)

# BAR 1: Drums only — syncopated, unrelenting
# Kick on 1 and 3, snare on 2 and 4 — but with off-kilter accents and fills
# Every eighth note with hihat, but some missing for tension

bar_start = 0.0

# Kick on 1 and 3
add_note(drum_inst, 36, bar_start, bar_start + 0.1, 110)
add_note(drum_inst, 36, bar_start + 0.75, bar_start + 0.85, 110)

# Snare on 2 and 4, but with slight shifts
add_note(drum_inst, 38, bar_start + 0.375, bar_start + 0.425, 90)
add_note(drum_inst, 38, bar_start + 0.75, bar_start + 0.8, 85)

# Hi-hats on every eighth, but with some rests for tension
for t in np.arange(0, bar_length, beat_length / 2):
    if t not in [0.75, 1.125]:  # skip two places for a rest
        add_note(drum_inst, 42, t, t + 0.05, 100)

# BAR 2: Everyone in — piano, bass, sax
bar_start = 1.5

# Piano — open voicings, unresolved chords
# Bar 2: Fm7♭5 (F, Ab, C, D)
# Bar 3: B♭7 (B♭, D, F, A)
# Bar 4: E♭7 (E♭, G, B♭, D)
# Resolve on the last bar

# Bar 2: Fm7♭5 (F, Ab, C, D) — open voicing, soft
add_note(piano_inst, 65, bar_start, bar_start + 0.5, 70)  # F
add_note(piano_inst, 76, bar_start, bar_start + 0.5, 75)  # Ab
add_note(piano_inst, 72, bar_start, bar_start + 0.5, 70)  # C
add_note(piano_inst, 74, bar_start, bar_start + 0.5, 60)  # D

# Bar 3: B♭7 (B♭, D, F, A)
add_note(piano_inst, 62, bar_start + 0.75, bar_start + 1.25, 75)  # B♭
add_note(piano_inst, 72, bar_start + 0.75, bar_start + 1.25, 70)  # D
add_note(piano_inst, 65, bar_start + 0.75, bar_start + 1.25, 65)  # F
add_note(piano_inst, 76, bar_start + 0.75, bar_start + 1.25, 60)  # A

# Bar 4: E♭7 (E♭, G, B♭, D)
add_note(piano_inst, 59, bar_start + 1.5, bar_start + 2.0, 80)  # E♭
add_note(piano_inst, 67, bar_start + 1.5, bar_start + 2.0, 75)  # G
add_note(piano_inst, 62, bar_start + 1.5, bar_start + 2.0, 70)  # B♭
add_note(piano_inst, 72, bar_start + 1.5, bar_start + 2.0, 65)  # D

# Bass: Walking line in F minor
# Bar 2: F, G♭, G, A♭
# Bar 3: B♭, B, C, C♯
# Bar 4: E♭, F, F♯, G

# Bar 2
add_note(bass_inst, 65, bar_start, bar_start + 0.375, 80)  # F
add_note(bass_inst, 64, bar_start + 0.375, bar_start + 0.75, 85)  # G♭
add_note(bass_inst, 66, bar_start + 0.75, bar_start + 1.125, 80)  # G
add_note(bass_inst, 67, bar_start + 1.125, bar_start + 1.5, 75)  # A♭

# Bar 3
add_note(bass_inst, 62, bar_start + 1.5, bar_start + 1.875, 85)  # B♭
add_note(bass_inst, 63, bar_start + 1.875, bar_start + 2.25, 80)  # B
add_note(bass_inst, 65, bar_start + 2.25, bar_start + 2.625, 75)  # C
add_note(bass_inst, 66, bar_start + 2.625, bar_start + 3.0, 70)  # C♯

# Bar 4
add_note(bass_inst, 59, bar_start + 3.0, bar_start + 3.375, 80)  # E♭
add_note(bass_inst, 65, bar_start + 3.375, bar_start + 3.75, 85)  # F
add_note(bass_inst, 67, bar_start + 3.75, bar_start + 4.125, 80)  # F♯
add_note(bass_inst, 68, bar_start + 4.125, bar_start + 4.5, 75)  # G

# Saxophone: One short, haunting motif — incomplete, but full of tension
# Start on F (65), move to A♭ (76), then G (67), then rest — a question in the air

# Bar 2: F (65)
add_note(sax_inst, 65, bar_start, bar_start + 0.375, 110)

# Bar 3: A♭ (76)
add_note(sax_inst, 76, bar_start + 0.75, bar_start + 1.125, 110)

# Bar 4: G (67)
add_note(sax_inst, 67, bar_start + 1.5, bar_start + 1.875, 110)

# Drums — continue the same rhythm from bar 1 into bars 2-4, but with more energy
# Add more syncopation and fills in bar 4
for t in np.arange(1.5, 3.0, beat_length / 2):
    if t not in [1.875, 2.25]:  # skip for tension
        add_note(drum_inst, 42, t, t + 0.05, 100)

# Add a fill at the end of bar 4
add_note(drum_inst, 36, 3.0, 3.1, 110)  # kick
add_note(drum_inst, 38, 3.1, 3.15, 100)  # snare
add_note(drum_inst, 42, 3.15, 3.2, 100)  # hihat
add_note(drum_inst, 46, 3.2, 3.25, 80)  # crash

# Save the MIDI file
pm.write('intro.mid')

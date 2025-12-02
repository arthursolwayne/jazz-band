
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set the key to D minor (key number 29)
pm.key_signature_changes = [pretty_midi.KeySignature(29, 0.0)]

# -- Drums Track (Little Ray) --
drum_program = pretty_midi.instrument_program('Drums')
drum_instrument = pretty_midi.Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# Kick on 1 and 3 of each bar
for bar in range(4):
    kick_time = bar * 1.5 + 0.0  # beat 0 (1)
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drum_instrument.notes.append(kick_note)

    kick_time = bar * 1.5 + 0.75  # beat 3 (1)
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drum_instrument.notes.append(kick_note)

# Snare on 2 and 4 of each bar
for bar in range(4):
    snare_time = bar * 1.5 + 0.375  # beat 1 (2)
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drum_instrument.notes.append(snare_note)

    snare_time = bar * 1.5 + 0.75 * 2  # beat 3 (4)
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drum_instrument.notes.append(snare_note)

# Hi-hat on every eighth note
for bar in range(4):
    for i in range(8):
        hihat_time = bar * 1.5 + i * 0.125
        hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drum_instrument.notes.append(hihat_note)

# -- Bass Track (Marcus) --
bass_program = pretty_midi.instrument_program('Acoustic Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# Walking bass line in D minor
# Root: D (62), Bb (60), F (58), C (60), G (67), D (62), A (69), E (64)
# Chromatic approaches
bass_notes = [
    (62, 0.0),          # D
    (60, 0.375),        # Bb
    (58, 0.75),         # F
    (60, 1.125),        # Bb
    (67, 1.5),          # G
    (62, 1.875),        # D
    (69, 2.25),         # A
    (64, 2.625),        # E
    (62, 3.0),          # D
    (60, 3.375),        # Bb
    (58, 3.75),         # F
    (60, 4.125),        # Bb
    (67, 4.5),          # G
    (62, 4.875),        # D
    (69, 5.25),         # A
    (64, 5.625),        # E
    (62, 6.0),          # D
]

for pitch, start_time in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + 0.25)
    bass_instrument.notes.append(note)

# -- Piano Track (Diane) --
piano_program = pretty_midi.instrument_program('Acoustic Grand Piano')
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 7th chords: Dm7 (62, 64, 67, 60), G7 (67, 69, 64, 65), Cm7 (60, 62, 64, 58), F7 (58, 60, 62, 64)
# Comp on 2 and 4, letting space for the saxophone

# Bar 1: Dm7 (comp on 2 and 4)
# Bar 2: G7 (comp on 2 and 4)
# Bar 3: Cm7 (comp on 2 and 4)
# Bar 4: F7 (comp on 2 and 4)

# Bar 1: Dm7, comp on 2 and 4
for time_offset in [0.375, 0.75]:
    # Dm7: D (62), F (64), A (67), C (60)
    for pitch in [62, 64, 67, 60]:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=0.0 + time_offset, end=0.0 + time_offset + 0.25)
        piano_instrument.notes.append(note)

# Bar 2: G7, comp on 2 and 4
for time_offset in [0.375, 0.75]:
    # G7: G (67), B (69), D (62), F (64)
    for pitch in [67, 69, 62, 64]:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=1.5 + time_offset, end=1.5 + time_offset + 0.25)
        piano_instrument.notes.append(note)

# Bar 3: Cm7, comp on 2 and 4
for time_offset in [0.375, 0.75]:
    # Cm7: C (60), Eb (62), G (67), Bb (60)
    for pitch in [60, 62, 67, 60]:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=3.0 + time_offset, end=3.0 + time_offset + 0.25)
        piano_instrument.notes.append(note)

# Bar 4: F7, comp on 2 and 4
for time_offset in [0.375, 0.75]:
    # F7: F (58), A (60), C (62), E (64)
    for pitch in [58, 60, 62, 64]:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=4.5 + time_offset, end=4.5 + time_offset + 0.25)
        piano_instrument.notes.append(note)

# -- Saxophone Track (You) --
sax_program = pretty_midi.instrument_program('Soprano Sax')
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Your motif: D (62), F (64), Bb (60), D (62)
# First bar: play D, F, Bb
# Second bar: rest
# Third bar: play again, but with a chromatic approach
# Fourth bar: resolve with a D note, a little higher, with an echo

# Bar 1: D (62), F (64), Bb (60)
note = pretty_midi.Note(velocity=110, pitch=62, start=0.0, end=0.375)
sax_instrument.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=0.375, end=0.75)
sax_instrument.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=60, start=0.75, end=1.125)
sax_instrument.notes.append(note)

# Bar 2: Rest

# Bar 3: Chromatic approach to D (C#, D)
note = pretty_midi.Note(velocity=110, pitch=61, start=3.0, end=3.2)
sax_instrument.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=3.2, end=3.5)
sax_instrument.notes.append(note)

# Bar 4: Resolve with a D and a space
note = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.8)
sax_instrument.notes.append(note)

# Save the MIDI file
pm.write('dante_intro.mid')

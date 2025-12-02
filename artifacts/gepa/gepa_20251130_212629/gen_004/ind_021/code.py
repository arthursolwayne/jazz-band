
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: Dm (D Dorian or D minor)
# Scale: D, E, F, G, A, Bb, C
# We'll use D minor (Natural minor) for the tonal center

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
drum_instrument = pretty_midi.Instrument(program=drums_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drum_instrument)
pm.instruments.append(sax_instrument)

# BPM = 160 => beat duration = 0.375 sec
# 4 bars = 6 sec, so each bar is 1.5 sec

# Time variables
time = 0.0  # in seconds
note_duration = 0.375  # duration of each note (one beat)
rest = 0.0  # no rests unless specified

# Tempos are in BPM, so we set the tempo once
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=160)]

#----------------------------- DRUMS (Little Ray) -----------------------------

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375

        # Kick on beats 1 and 3
        if beat in [0, 2]:
            drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
        # Snare on beats 2 and 4
        if beat in [1, 3]:
            drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1))
        # Hi-hat on every eighth note
        for eighth in range(2):
            drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05))

#----------------------------- BASS (Marcus) -----------------------------

# Bar 1: Walking line, chromatic approaches, no repeated notes

# Define bass line: Dm7 in D minor (D, F, A, C)
# Walking line: D, C, Bb, A, G, F, E, D
# Let's transpose these to the correct MIDI pitches
bass_notes = [62, 60, 59, 61, 67, 65, 64, 62]  # D, C, Bb, A, G, F, E, D
for i, pitch in enumerate(bass_notes):
    start = time + i * note_duration
    end = start + note_duration
    bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

#----------------------------- PIANO (Diane) -----------------------------

# Bar 1: Rest
# Bars 2-4: Comp on 2 and 4, 7th chords

# Define 7th chords for Dm (Dm7: D, F, A, C)
# We'll place chords on beats 2 and 4 of bars 2-4

chord_notes = {
    2: [62, 60, 67, 64],  # Dm7: D, F, A, C
    4: [62, 60, 67, 64]   # Same chord for now
}

for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [1, 3]:
            # Play 7th chord on 2 and 4
            for pitch in chord_notes[beat + 1]:
                piano_instrument.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25))

#----------------------------- SAX (You) -----------------------------

# Your motif: four-note phrase in D minor, starts on bar 2, beats 1-2

# Motif: D, F, E, D (melodic minor) — but with a twist
# In MIDI: D (62), F (65), E (64), D (62)
# Start on bar 2, beat 1
start_time = 1.5 + 0.0  # bar 2, beat 1
note_lengths = [0.5, 0.5, 0.5, 0.5]  # quarter notes

for i, pitch in enumerate([62, 65, 64, 62]):
    start = start_time + i * note_duration
    end = start + note_duration
    sax_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

#----------------------------- Add the MIDI to a file -----------------------------
pm.write("jazz_intro_dmin_160.bpm")

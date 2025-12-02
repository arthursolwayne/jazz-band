
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature and key
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.key_signature_changes = [pretty_midi.KeySignature(key_number=21, time=0.0)]  # D minor

# Define note durations
beat = 60.0 / 160  # seconds per beat
bar = 4 * beat  # seconds per bar (4/4)
note_duration = beat  # quarter note
eighth_note = note_duration / 2

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor sax
piano_instrument = pretty_midi.Instrument(program=0)  # Acoustic piano
bass_instrument = pretty_midi.Instrument(program=33)  # Double bass
drum_instrument = pretty_midi.Instrument(program=128)  # Drum set

pm.instruments = [sax_instrument, piano_instrument, bass_instrument, drum_instrument]

# --- DRUMS ---
# Kick on 1 and 3
drum_notes = [
    (0.0, 36),  # Kick on beat 1 of bar 1
    (1.5, 36),  # Kick on beat 1 of bar 2
    (3.0, 36),  # Kick on beat 1 of bar 3
    (4.5, 36),  # Kick on beat 1 of bar 4
]

# Snare on 2 and 4
drum_notes.extend([
    (0.75, 38),  # Snare on beat 2 of bar 1
    (2.25, 38),  # Snare on beat 2 of bar 2
    (3.75, 38),  # Snare on beat 2 of bar 3
    (5.25, 38),  # Snare on beat 2 of bar 4
])

# Hi-hat on every eighth note
for t in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    drum_notes.append((t, 42))  # Hi-hat on every eighth

for time, note_number in drum_notes:
    drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.1))

# --- BASS (Walking Line) ---
# Dm7 walking line
bass_notes = [
    (0.0, 2),  # D
    (0.75, 1),  # C
    (1.5, 3),  # Eb
    (2.25, 2),  # D
    (3.0, 1),  # C
    (3.75, 3),  # Eb
    (4.5, 2),  # D
    (5.25, 1),  # C
]

for time, note_number in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=note_number + 24, start=time, end=time + 0.1))

# --- PIANO (Comping on 2 and 4) ---
# Dm7: D, F, Ab, C
# Comp on 2 and 4
piano_notes = []
for bar in [0, 1, 2, 3]:
    time = bar * bar
    piano_notes.append((time + 0.75, 62))  # F (D7)
    piano_notes.append((time + 0.75, 65))  # Ab (D7)
    piano_notes.append((time + 0.75, 67))  # C (D7)
    piano_notes.append((time + 0.75, 64))  # D (D7)
    piano_notes.append((time + 2.25, 62))  # F
    piano_notes.append((time + 2.25, 65))  # Ab
    piano_notes.append((time + 2.25, 67))  # C
    piano_notes.append((time + 2.25, 64))  # D

for time, note_number in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.1))

# --- SAXOPHONE (Motif: D Eb F G Eb) in bar 1-2, then repeat in bar 3-4 with variation ---
# Bar 1: D Eb F G Eb (each on 1, 2, 3, 4, 4.5)
sax_notes = [
    (0.0, 62),  # D
    (0.75, 64),  # Eb
    (1.5, 65),  # F
    (2.25, 67),  # G
    (2.25 + 0.375, 64),  # Eb
]

# Repeat with variation in bar 3-4
sax_notes.extend([
    (3.0, 62),  # D
    (3.75, 64),  # Eb
    (4.5, 65),  # F
    (5.25, 67),  # G
    (5.25 + 0.375, 64),  # Eb
])

for time, note_number in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.1))

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file generated: jazz_intro.mid")

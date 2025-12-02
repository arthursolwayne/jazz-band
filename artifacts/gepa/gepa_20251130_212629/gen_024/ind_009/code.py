
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: Dm (D minor)
# Dm scale: D, Eb, F, G, Ab, Bb, C
# We'll use D minor (natural) scale for this piece

# Set up instruments
# Drums
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_instrument = pretty_midi.Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# Bass
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# Piano
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# Tenor Sax
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Define the beat in seconds (160 BPM = 60 / 160 = 0.375s per beat)
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar
time = 0.0

# =============
# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# =============
# Time: 0.0 to 1.5 sec

# Kick on 1 and 3
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat*2, end=beat*2 + 0.375))

# Snare on 2 and 4
drum_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=beat, end=beat + 0.25))
drum_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=beat*3, end=beat*3 + 0.25))

# Hi-hat on every eighth note
for i in range(0, 4):
    drum_instrument.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=i*beat/2, end=i*beat/2 + 0.125))

time = bar

# =============
# Bar 2: Bass enters (Marcus)
# Walking line with chromatic approaches
# =============
# Dm7: D, F, Ab, Bb
# Start with a chromatic approach to D
bass_notes = [
    (time, 50, 0.25),    # Eb (chromatic approach to D)
    (time + 0.25, 52, 0.25),  # F
    (time + 0.5, 55, 0.25),   # Ab
    (time + 0.75, 50, 0.25),  # D
    (time + 1.0, 52, 0.25),   # F
    (time + 1.25, 55, 0.25),  # Ab
    (time + 1.5, 50, 0.25),   # D
]

for start, pitch, duration in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + duration))

time = bar * 2

# =============
# Bar 3: Diane on piano (7th chords, comp on 2 and 4)
# =============
# Dm7: D, F, Ab, Bb
# Comp on 2 and 4
piano_notes = [
    # On beat 2: Dm7
    (time + beat, 55, 0.1),   # D
    (time + beat, 52, 0.1),   # F
    (time + beat, 50, 0.1),   # Ab
    (time + beat, 48, 0.1),   # Bb

    # On beat 4: Dm7
    (time + beat*3, 55, 0.1),  # D
    (time + beat*3, 52, 0.1),  # F
    (time + beat*3, 50, 0.1),  # Ab
    (time + beat*3, 48, 0.1),  # Bb
]

for start, pitch, duration in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + duration))

time = bar * 3

# =============
# Bar 4: Dante on sax (short motif, sing, leave it hanging)
# =============
# Dm scale: D, Eb, F, G, Ab, Bb, C
# Motif: D - Eb - F - rest
# Start on beat 1, end on beat 3 with a rest

sax_notes = [
    (time, 62, 0.25),  # D
    (time + 0.25, 64, 0.25),  # Eb
    (time + 0.5, 67, 0.25),   # F
    (time + 0.75, 62, 0.0),  # Rest
    (time + 0.75, 64, 0.25),  # Eb (legato from F)
    (time + 1.0, 67, 0.25),   # F
    (time + 1.25, 69, 0.25),  # G (sings into the space)
    (time + 1.5, 62, 0.0)     # End with a rest
]

for start, pitch, duration in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file generated: 'dante_intro.mid'")

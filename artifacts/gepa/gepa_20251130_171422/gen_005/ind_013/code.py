
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to D minor (no modulation)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Drums use percussion
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# BPM = 160, 4/4 time
# Time per beat = 60 / 160 = 0.375 seconds
# 4 bars = 6 seconds
# Each bar = 1.5 seconds
# Each beat = 0.375 seconds

# Function to convert time to seconds
def time_to_sec(t):
    return t * 0.375

# -- DRUMS (Little Ray) --
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4):
    for beat in range(4):
        time = time_to_sec(bar * 4 + beat)
        if beat == 0 or beat == 2:
            # Kick
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.1))
        if beat == 1 or beat == 3:
            # Snare
            drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=time, end=time + 0.1))
        # Hi-hat on every eighth note
        for eighth in range(2):
            hihat_time = time + eighth * 0.1875
            drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=hihat_time, end=hihat_time + 0.05))

# -- BASS (Marcus) -- Walking line with chromatic approaches
# Start on D (2nd fret of E string) = MIDI 62
# Walking line: D - Eb - E - F - G - A - Bb - B - C - D - etc.
bass_notes = [62, 63, 64, 65, 67, 69, 70, 71, 72, 62]
for i, note in enumerate(bass_notes):
    time = time_to_sec(i)
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# -- PIANO (Diane) -- 7th chords on 2 and 4
# D7 (root position) = D (62), F# (67), A (69), C (60)
# D7 chord on beat 2 and 4 of each bar
for bar in range(4):
    for beat in range(4):
        time = time_to_sec(bar * 4 + beat)
        if beat == 1 or beat == 3:
            for note in [62, 67, 69, 60]:
                piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# -- SAX (Dante) -- One short motif, open-ended
# Start on D (62), then C (60), then B (59), then E (64) — a simple, haunting motif
# Play the first note, leave it hanging, then return to finish it
sax_notes = [
    (62, 0.0, 0.75),  # D, start at 0.0, end at 0.75
    (60, 0.75, 1.0),  # C, start at 0.75, end at 1.0
    (59, 1.0, 1.25),  # B, start at 1.0, end at 1.25
    (64, 1.25, 1.5)   # E, start at 1.25, end at 1.5
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")

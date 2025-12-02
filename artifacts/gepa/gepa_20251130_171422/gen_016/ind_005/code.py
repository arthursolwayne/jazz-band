
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key signature: D Major (no sharps or flats)
midi.key_signature_changes = [pretty_midi.KeySignature(2, 0)]  # D Major

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Define time per bar (160 BPM, 4/4 time)
beats_per_bar = 4
note_duration = 0.375  # 1 beat = 0.375 seconds
bar_duration = 1.5  # 4 bars = 6 seconds, so 1 bar = 1.5 seconds

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Each beat is 0.375 seconds
for beat in [0, 2]:  # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=beat * note_duration, end=(beat + 1) * note_duration)
    drums.notes.append(kick)

for beat in [1, 3]:  # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=beat * note_duration, end=(beat + 1) * note_duration)
    drums.notes.append(snare)

# Hihat on every eighth
for i in range(8):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=(i * note_duration / 2), end=(i * note_duration / 2) + 0.1)
    drums.notes.append(hihat)

# Bar 2: Everyone joins in

# Bass line: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5 + 0.375, end=1.5 + 0.75),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=1.5 + 0.75, end=1.5 + 1.125),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 1.125, end=1.5 + 1.5),  # G
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
# Bar 2: D7 on beat 2, G7 on beat 4
# D7: D, F#, A, C
# G7: G, B, D, F
# Only play on beats 2 and 4
d7_chord = [62, 64, 67, 60]  # D, F#, A, C
g7_chord = [67, 69, 72, 65]  # G, B, D, F

for pitch in d7_chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=1.5 + 0.75, end=1.5 + 0.75 + 0.15)
    piano.notes.append(note)

for pitch in g7_chord:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=1.5 + 1.5 - 0.15, end=1.5 + 1.5)
    piano.notes.append(note)

# Sax: Melody — short motif, start it, leave it hanging, come back
# D (62) -> F# (64) -> G (67) -> D (62) -> E (64) -> A (69)
# First phrase: D, F#, G
# Let it hang on G, then come back with D, E, A

# First phrase: D, F#, G
note_d = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.3)
note_fs = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.3, end=1.5 + 0.6)
note_g = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.6, end=1.5 + 0.9)

sax.notes.extend([note_d, note_fs, note_g])

# Second phrase: D, E, A — start at 1.5 + 0.9, let them resolve
note_d2 = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 0.9, end=1.5 + 1.2)
note_e = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 1.2, end=1.5 + 1.5)
note_a = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 1.5 + 0.1)

sax.notes.extend([note_d2, note_e, note_a])

# Bar 3: (Optional, but you can add more texture if needed)
# For now, we’re keeping it tight — no tension, just resolution.

# Bar 4: No new material, just resolution of the motif
# Maybe a gentle rest or a return to the motif with a soft wrap-up
# We’ll keep it simple and end on the last A (69) with a trailing note

# Add a trailing A note (extend the last note)
note_a.end = 1.5 + 1.5 + 0.2

# Save the MIDI file
midi.write("dante_intro.mid")

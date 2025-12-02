
import pretty_midi
import random

# Constants
BPM = 160
TIME_SIGNATURE = (4, 4)
NOTE_DURATION = 0.375  # 1/16 note in seconds at 160 BPM

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define instruments
drums_program = pretty_midi.instrument_program('Acoustic Drum Kit')
bass_program = pretty_midi.instrument_program('Double Bass')
piano_program = pretty_midi.instrument_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_program('Tenor Saxophone')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Helper function to convert beat to time
def beat_to_time(beat):
    return beat * (60.0 / BPM)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(0, 4):
    hihat_time = beat_to_time(i * 0.5)
    hihat = pretty_midi.Note(velocity=64, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat)

for i in [0, 2]:
    kick_time = beat_to_time(i)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

for i in [1, 3]:
    snare_time = beat_to_time(i)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

# Bar 2: Everyone in
# Fm7 chord: F, Ab, C, D
# Diane: 7th chords on 2 and 4
for i in [1, 3]:
    time = beat_to_time(i)
    # Fm7: F, Ab, C, D
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=time, end=time + 0.15))
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=time, end=time + 0.15))
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=time, end=time + 0.15))
    piano.notes.append(pretty_midi.Note(velocity=60, pitch=71, start=time, end=time + 0.15))

# Marcus: walking line in Fm
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
walking_line = [65, 64, 60, 62, 61, 62, 63, 62]  # F, Gb, Ab, A, Bb, B, C, Db
for i, pitch in enumerate(walking_line):
    time = beat_to_time(i / 2.0)
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + NOTE_DURATION)
    bass.notes.append(note)

# Your motif (Tenor Saxophone) — short, emotive, with a space
# Original motif starts at bar 2 (beat 0), with a rest and return
notes = [
    # Bar 2 (beat 0) - rest
    # Bar 2 (beat 1) - F, Ab
    pretty_midi.Note(velocity=100, pitch=65, start=beat_to_time(1), end=beat_to_time(1) + 0.2),
    pretty_midi.Note(velocity=95, pitch=60, start=beat_to_time(1) + 0.1, end=beat_to_time(1) + 0.3),
    # Bar 3 (beat 1) - Ab, Bb
    pretty_midi.Note(velocity=100, pitch=60, start=beat_to_time(3), end=beat_to_time(3) + 0.2),
    pretty_midi.Note(velocity=95, pitch=61, start=beat_to_time(3) + 0.1, end=beat_to_time(3) + 0.3),
    # Bar 4 (beat 1) - F, C
    pretty_midi.Note(velocity=100, pitch=65, start=beat_to_time(5), end=beat_to_time(5) + 0.2),
    pretty_midi.Note(velocity=95, pitch=72, start=beat_to_time(5) + 0.1, end=beat_to_time(5) + 0.3)
]

for note in notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write("fminor_intro.mid")

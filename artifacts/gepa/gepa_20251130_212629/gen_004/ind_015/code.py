
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Define the key: D major
key = 'D'

# Define the tempo and time
tempo = 160
time_per_bar = 6.0  # 4 bars = 6 seconds, so 1.5 seconds per bar
beat = time_per_bar / 4  # 0.375 seconds per beat

# Instruments
# 1. Drums (Little Ray)
# 2. Bass (Marcus)
# 3. Piano (Diane)
# 4. Tenor Sax (You)

# Create instrument tracks
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * time_per_bar + beat * beat
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1))
        # Hi-hat on every eighth
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05))

# Bar 2: All instruments in
# Time for bar 2: 1.5 seconds
time = 1.5  # start of bar 2

# Marcus (Bass): Walking line in D major
# Root, b7, 3, b7, 5, 1, 3, 7
bass_notes = [2, 11, 4, 11, 6, 0, 4, 7]
bass_notes = [n + 24 for n in bass_notes]  # in MIDI note numbers
for i, note in enumerate(bass_notes):
    start = time + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane (Piano): 7th chords, comp on 2 and 4
# D7, G7, A7, D7
chords = [
    [2, 4, 6, 11],  # D7
    [7, 9, 11, 2],  # G7
    [2, 4, 6, 11],  # A7
    [2, 4, 6, 11],  # D7
]
chords = [n + 24 for n in chords]
for i, chord in enumerate(chords):
    if i % 2 == 1:  # Comp on 2 and 4
        time_start = time + i * 0.375
        for note in chord:
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time_start, end=time_start + 0.1))

# You (Tenor Sax): Main motif, D major
# D (2) -> F# (4) -> A (6) -> C# (11) -> F# (4) -> A (6) -> D (2)
motif = [2, 4, 6, 11, 4, 6, 2]
motif = [n + 62 for n in motif]  # D4 is 62 in MIDI
for i, note in enumerate(motif):
    start = time + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Fill in the rest with space and triads
# Just a few notes to add some life and emotion
# F# (4) at 1.875s, A (6) at 2.25s, D (2) at 2.625s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=1.875 + 0.2))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.25 + 0.2))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.625 + 0.2))

# Write the MIDI file
pm.write("jazz_intro.mid")
print("MIDI file saved as jazz_intro.mid")


import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Set the key to D Major
key = 'D'

# Time setup
beat = 0.375  # 160 BPM, 4/4 time
bar = 1.5  # 4 bars = 6 seconds

# Instrument setup
# 1. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

# 2. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

# 3. Drums (Little Ray)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drums = pretty_midi.Instrument(program=drums_program)

# 4. Saxophone (Dante)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# --- Bar 1: Drums only, rhythmic tension, low volume ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Volume: low, to build anticipation

# Kick on 1 and 3 of Bar 1 (time = 0.0 and 1.125)
drums.notes.append(pretty_midi.Note(velocity=40, pitch=36, start=0.0, end=0.125))
drums.notes.append(pretty_midi.Note(velocity=40, pitch=36, start=1.125, end=1.25))

# Snare on 2 and 4 (time = 0.375 and 1.5)
drums.notes.append(pretty_midi.Note(velocity=50, pitch=38, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=38, start=1.5, end=1.625))

# Hihat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5, 1.875)
for t in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875]:
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.125))

# --- Bar 2: Saxophone enters with a motif, melodic and sparse ---
# Melody: D (D4) -> F# (F#4) -> A (A4) -> D (D4) -> Rest (space)
# Start at 1.5s (beginning of Bar 2)

# D (D4) at 1.5s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
# F# (F#4) at 1.75s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0))
# A (A4) at 2.0s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25))
# D (D4) at 2.25s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))
# Rest for the last half of Bar 2

# --- Bar 3: Full ensemble, harmonic interest, clarity ---
# Bass: walking line in D Major (D2 -> E2 -> F#2 -> G2, with chromatic approach)
# Piano: Open voicings, 4th intervals, resolve on the last chord
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Sax: rest, but prepare for resolution

# Bass line (Bar 3: 2.5s to 3.25s)
# D2 (38), E2 (39), F#2 (41), G2 (43)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=2.625, end=2.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=2.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.875, end=3.0))

# Piano: Open voicings, each bar a new chord
# Bar 3 (2.5s - 3.25s): Dmaj7 (D, F#, A, C#)

# D (62), F# (66), A (69), C# (71)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=2.5, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=3.25))

# Drums (Bar 3): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 2.5s to 3.25s
drums.notes.append(pretty_midi.Note(velocity=40, pitch=36, start=2.5, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=40, pitch=36, start=2.875, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=38, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=38, start=3.0, end=3.125))
for t in [2.5, 2.875, 3.0, 3.375]:  # hihat on 1, 3, 4, and next bar (but we only go to 3.25s)
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.125))

# --- Bar 4: Resolution, saxophone returns to complete the motif ---
# Motif: D -> F# -> A -> D -> G -> A -> B -> C# -> D
# Start at 3.25s

# D (62) at 3.25s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))
# F# (66) at 3.5s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75))
# A (69) at 3.75s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0))
# D (62) at 4.0s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25))
# G (67) at 4.25s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5))
# A (69) at 4.5s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75))
# B (71) at 4.75s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0))
# C# (72) at 5.0s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25))
# D (62) at 5.25s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))

# Bass continues walking line (Bar 4: 3.25s to 4.0s)
# D2 (38), E2 (39), F#2 (41), G2 (43)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=3.375, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=3.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=3.625, end=3.75))

# Piano: resolve on Dmaj7 again (Bar 4: 3.25s to 4.0s)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=4.0))

# Drums: kick on 1 and 3, snare on 2 and 4
# Time: 3.25s to 4.0s
drums.notes.append(pretty_midi.Note(velocity=40, pitch=36, start=3.25, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=40, pitch=36, start=3.625, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=50, pitch=38, start=3.75, end=3.875))

# Add the instruments to the MIDI file
pm.instruments = [bass, piano, drums, sax]

# Save the MIDI file
pm.write("dante_introduction.mid")

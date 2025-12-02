
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key: D Major
key_signature = pretty_midi.KeySignature(key_number=2)  # D Major (key number 2)
pm.key_signature = key_signature

# Define time signatures: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature = time_signature

# Create instruments
instrument_drums = pretty_midi.Instrument(program=10)  # Drums
instrument_bass = pretty_midi.Instrument(program=33)    # Electric Bass
instrument_piano = pretty_midi.Instrument(program=0)    # Acoustic Piano
instrument_sax = pretty_midi.Instrument(program=64)     # Tenor Sax

pm.instruments = [instrument_drums, instrument_bass, instrument_piano, instrument_sax]

# Constants
BPM = 160
BEAT = 60.0 / BPM
BAR = BEAT * 4

# Time offsets
time = 0.0

# ----------------------
# DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Only hihat and snare to build tension
# Bar 2-4: Full rhythm

# Bar 1: No kick, only snare and hihat
# Time for Bar 1:
# 0.0 to 1.5s
# Use 8th note hihat on 1, 2, 3, 4
for i in range(8):
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,  # Hihat
        start=time + i * BEAT / 2,
        end=time + i * BEAT / 2 + 0.05
    )
    instrument_drums.notes.append(note)

# Snare on 2 and 4
for i in [1, 3]:
    note = pretty_midi.Note(
        velocity=90,
        pitch=66,  # Snare
        start=time + i * BEAT / 2,
        end=time + i * BEAT / 2 + 0.1
    )
    instrument_drums.notes.append(note)

# Bar 2: Kick on 1 and 3
for i in [0, 2]:
    note = pretty_midi.Note(
        velocity=100,
        pitch=36,  # Kick
        start=time + 1.5 + i * BEAT / 2,
        end=time + 1.5 + i * BEAT / 2 + 0.15
    )
    instrument_drums.notes.append(note)

# Snare on 2 and 4
for i in [1, 3]:
    note = pretty_midi.Note(
        velocity=100,
        pitch=66,
        start=time + 1.5 + i * BEAT / 2,
        end=time + 1.5 + i * BEAT / 2 + 0.1
    )
    instrument_drums.notes.append(note)

# Hihat on every 8th
for i in range(8):
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,
        start=time + 1.5 + i * BEAT / 2,
        end=time + 1.5 + i * BEAT / 2 + 0.05
    )
    instrument_drums.notes.append(note)

# Bar 3 (same as Bar 2)
for i in [0, 2]:
    note = pretty_midi.Note(
        velocity=100,
        pitch=36,
        start=time + 3.0 + i * BEAT / 2,
        end=time + 3.0 + i * BEAT / 2 + 0.15
    )
    instrument_drums.notes.append(note)

for i in [1, 3]:
    note = pretty_midi.Note(
        velocity=100,
        pitch=66,
        start=time + 3.0 + i * BEAT / 2,
        end=time + 3.0 + i * BEAT / 2 + 0.1
    )
    instrument_drums.notes.append(note)

for i in range(8):
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,
        start=time + 3.0 + i * BEAT / 2,
        end=time + 3.0 + i * BEAT / 2 + 0.05
    )
    instrument_drums.notes.append(note)

# Bar 4 (same as Bar 2)
for i in [0, 2]:
    note = pretty_midi.Note(
        velocity=100,
        pitch=36,
        start=time + 4.5 + i * BEAT / 2,
        end=time + 4.5 + i * BEAT / 2 + 0.15
    )
    instrument_drums.notes.append(note)

for i in [1, 3]:
    note = pretty_midi.Note(
        velocity=100,
        pitch=66,
        start=time + 4.5 + i * BEAT / 2,
        end=time + 4.5 + i * BEAT / 2 + 0.1
    )
    instrument_drums.notes.append(note)

for i in range(8):
    note = pretty_midi.Note(
        velocity=80,
        pitch=42,
        start=time + 4.5 + i * BEAT / 2,
        end=time + 4.5 + i * BEAT / 2 + 0.05
    )
    instrument_drums.notes.append(note)

# ----------------------
# BASS: Marcus (chromatic walking line)
# Bar 1: Rest
# Bar 2: D -> C# -> B -> A
# Bar 3: G -> F# -> E -> D
# Bar 4: B -> A -> G -> F#

# Bar 2
# D (note 2, 0.0), C# (note 1, 0.5), B (note 0, 1.0), A (note 10, 1.5)
note = pretty_midi.Note(
    velocity=70,
    pitch=62,  # D3
    start=1.5,
    end=1.5 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=65,
    pitch=61,  # C#3
    start=1.5 + 0.5,
    end=1.5 + 0.5 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=60,
    pitch=60,  # B3
    start=1.5 + 1.0,
    end=1.5 + 1.0 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=55,
    pitch=59,  # A3
    start=1.5 + 1.5,
    end=1.5 + 1.5 + 0.1
)
instrument_bass.notes.append(note)

# Bar 3
note = pretty_midi.Note(
    velocity=70,
    pitch=67,  # G3
    start=3.0,
    end=3.0 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=65,
    pitch=66,  # F#3
    start=3.0 + 0.5,
    end=3.0 + 0.5 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=60,
    pitch=65,  # E3
    start=3.0 + 1.0,
    end=3.0 + 1.0 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=55,
    pitch=64,  # D3
    start=3.0 + 1.5,
    end=3.0 + 1.5 + 0.1
)
instrument_bass.notes.append(note)

# Bar 4
note = pretty_midi.Note(
    velocity=70,
    pitch=68,  # B3
    start=4.5,
    end=4.5 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=65,
    pitch=67,  # A3
    start=4.5 + 0.5,
    end=4.5 + 0.5 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=60,
    pitch=66,  # G3
    start=4.5 + 1.0,
    end=4.5 + 1.0 + 0.1
)
instrument_bass.notes.append(note)
note = pretty_midi.Note(
    velocity=55,
    pitch=65,  # F#3
    start=4.5 + 1.5,
    end=4.5 + 1.5 + 0.1
)
instrument_bass.notes.append(note)

# ----------------------
# PIANO: Diane (7th chords on 2 and 4, comp)
# Bar 1: Rest
# Bar 2: On 2 and 4: D7, A7
# Bar 3: On 2 and 4: G7, D7
# Bar 4: On 2 and 4: B7, F#7

# Bar 2
# D7: D, F#, A, C#
note = pretty_midi.Note(
    velocity=100,
    pitch=62,  # D3
    start=1.5 + 0.5,
    end=1.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=90,
    pitch=66,  # F#3
    start=1.5 + 0.5,
    end=1.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=95,
    pitch=67,  # A3
    start=1.5 + 0.5,
    end=1.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=85,
    pitch=69,  # C#4
    start=1.5 + 0.5,
    end=1.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)

# A7: A, C#, E, G
note = pretty_midi.Note(
    velocity=100,
    pitch=69,  # A3
    start=1.5 + 1.5,
    end=1.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=90,
    pitch=71,  # C#4
    start=1.5 + 1.5,
    end=1.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=95,
    pitch=72,  # E4
    start=1.5 + 1.5,
    end=1.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=85,
    pitch=74,  # G4
    start=1.5 + 1.5,
    end=1.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)

# Bar 3
# G7: G, B, D, F#
note = pretty_midi.Note(
    velocity=100,
    pitch=67,  # G3
    start=3.0 + 0.5,
    end=3.0 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=90,
    pitch=71,  # B3
    start=3.0 + 0.5,
    end=3.0 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=95,
    pitch=69,  # D3
    start=3.0 + 0.5,
    end=3.0 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=85,
    pitch=72,  # F#4
    start=3.0 + 0.5,
    end=3.0 + 0.5 + 0.1
)
instrument_piano.notes.append(note)

# D7: D, F#, A, C#
note = pretty_midi.Note(
    velocity=100,
    pitch=62,
    start=3.0 + 1.5,
    end=3.0 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=90,
    pitch=66,
    start=3.0 + 1.5,
    end=3.0 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=95,
    pitch=67,
    start=3.0 + 1.5,
    end=3.0 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=85,
    pitch=69,
    start=3.0 + 1.5,
    end=3.0 + 1.5 + 0.1
)
instrument_piano.notes.append(note)

# Bar 4
# B7: B, D#, F#, A
note = pretty_midi.Note(
    velocity=100,
    pitch=71,  # B3
    start=4.5 + 0.5,
    end=4.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=90,
    pitch=74,  # D#4
    start=4.5 + 0.5,
    end=4.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=95,
    pitch=74,  # F#4
    start=4.5 + 0.5,
    end=4.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=85,
    pitch=76,  # A4
    start=4.5 + 0.5,
    end=4.5 + 0.5 + 0.1
)
instrument_piano.notes.append(note)

# F#7: F#, A, C#, E
note = pretty_midi.Note(
    velocity=100,
    pitch=74,  # F#4
    start=4.5 + 1.5,
    end=4.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=90,
    pitch=76,  # A4
    start=4.5 + 1.5,
    end=4.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=95,
    pitch=77,  # C#5
    start=4.5 + 1.5,
    end=4.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)
note = pretty_midi.Note(
    velocity=85,
    pitch=79,  # E5
    start=4.5 + 1.5,
    end=4.5 + 1.5 + 0.1
)
instrument_piano.notes.append(note)

# ----------------------
# SAX: Dante (melody: question, not answer)
# Bar 1: Rest
# Bar 2: D (beat 1), E (beat 2), D (beat 3), G (beat 4)
# Bar 3: F# (beat 1), G (beat 2), A (beat 3), B (beat 4)
# Bar 4: A (beat 1), B (beat 2), C# (beat 3), rest on beat 4

# Bar 2
note = pretty_midi.Note(
    velocity=110,
    pitch=62,  # D3
    start=1.5,
    end=1.5 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=115,
    pitch=64,  # E3
    start=1.5 + 0.5,
    end=1.5 + 0.5 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=110,
    pitch=62,  # D3
    start=1.5 + 1.0,
    end=1.5 + 1.0 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=115,
    pitch=67,  # G3
    start=1.5 + 1.5,
    end=1.5 + 1.5 + 0.1
)
instrument_sax.notes.append(note)

# Bar 3
note = pretty_midi.Note(
    velocity=110,
    pitch=66,  # F#3
    start=3.0,
    end=3.0 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=115,
    pitch=67,  # G3
    start=3.0 + 0.5,
    end=3.0 + 0.5 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=110,
    pitch=69,  # A3
    start=3.0 + 1.0,
    end=3.0 + 1.0 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=115,
    pitch=71,  # B3
    start=3.0 + 1.5,
    end=3.0 + 1.5 + 0.1
)
instrument_sax.notes.append(note)

# Bar 4
note = pretty_midi.Note(
    velocity=110,
    pitch=69,  # A3
    start=4.5,
    end=4.5 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=115,
    pitch=71,  # B3
    start=4.5 + 0.5,
    end=4.5 + 0.5 + 0.1
)
instrument_sax.notes.append(note)
note = pretty_midi.Note(
    velocity=110,
    pitch=72,  # C#4
    start=4.5 + 1.0,
    end=4.5 + 1.0 + 0.1
)
instrument_sax.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")

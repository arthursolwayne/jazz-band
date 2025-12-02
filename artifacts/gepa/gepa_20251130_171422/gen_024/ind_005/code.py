
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments for each player
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# BPM = 160 => 1 beat = 0.375 seconds
# 1 bar = 4 beats = 1.5 seconds
# 4 bars = 6 seconds

# Define the key: F major
key = 'F'

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Add subtle variation to avoid predictability

# Time in seconds for each beat
beat = 0.375
bar_length = 1.5

# BAR 1: Drums only (0.0 - 1.5s)
# Kick: 0.0, 0.75
# Snare: 0.375, 1.125
# Hihat: every 8th (0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125)

# Kick
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.05))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=0.8))

# Snare
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=0.375, end=0.4))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=38, start=1.125, end=1.15))

# Hihat
for t in np.arange(0.0, 1.5, 0.1875):
    if t < 1.5:
        drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.05))

# BAR 2: Everyone comes in

# Bass line - chromatic, searching, melodic
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
# Notes in F major scale: F, G, A, Bb, C, D, Eb
# Chromatic approach, but not dissonant

# Bass notes (in F key, chromatic line)
# Time: 1.5s - 3.0s (Bar 2)
# Start at 1.5s

bass_notes = [
    (1.5, 70),  # F (70)
    (1.6875, 71),  # Gb (71)
    (1.875, 72),  # G (72)
    (2.0625, 73),  # Ab (73)
    (2.25, 74),  # A (74)
    (2.4375, 75),  # Bb (75)
    (2.625, 76),  # B (76)
    (2.8125, 77),  # C (77)
    (3.0, 78),  # D (78)
]

for t, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.15))

# Piano comp: 7th chords on 2 and 4
# F7, Bb7, F7, Bb7 (in Bar 2)
# Time: 1.5s to 3.0s

# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab

# Bar 2 - 2 and 4
# 2: 1.875s
# 4: 2.625s

# F7 on 2
piano_notes = [
    (1.875, 70, 100),  # F
    (1.875, 72, 85),  # A
    (1.875, 77, 90),  # C
    (1.875, 75, 80),  # Eb
]

# Bb7 on 4
piano_notes.extend([
    (2.625, 71, 100),  # Bb
    (2.625, 74, 85),  # D
    (2.625, 70, 90),  # F
    (2.625, 73, 80),  # Ab
])

for t, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=t, end=t + 0.2))

# Saxophone motif: Start at 1.5s
# Motif: F, Gb, G, F (a small intervallic shift that lingers)
# F (70), Gb (71), G (72), F (70)
# Timing: 1.5s to 1.875s

sax_notes = [
    (1.5, 70, 100),
    (1.6875, 71, 100),
    (1.875, 72, 100),
    (2.0, 70, 70),  # softer, lingering
]

for t, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=t, end=t + 0.1))

# Bar 3: Sax continues, bass continues, piano continues
# Sax adds a variation -- a small shift
# Gb, F, Ab, Gb (mirror the original motif but descending)

sax_notes = [
    (2.125, 71, 100),
    (2.3125, 70, 100),
    (2.5, 73, 100),
    (2.6875, 71, 90)
]

for t, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=t, end=t + 0.1))

# Bass continues with similar chromatic line
# Time: 3.0s - 4.5s (Bar 3)
# G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F -> G -> Ab

# Bass notes - continue the line
bass_notes = [
    (3.0, 78),  # D
    (3.1875, 79),  # Eb
    (3.375, 80),  # E
    (3.5625, 70),  # F
    (3.75, 71),  # Gb
    (3.9375, 72),  # G
    (4.125, 73),  # Ab
    (4.3125, 74),  # A
]

for t, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.15))

# Piano: 7th chords on 2 and 4
# Bb7 on 2, F7 on 4

# Bb7 on 2: 3.875s
piano_notes = [
    (3.875, 71, 100),  # Bb
    (3.875, 74, 85),  # D
    (3.875, 70, 90),  # F
    (3.875, 73, 80),  # Ab
]

# F7 on 4: 4.625s
piano_notes.extend([
    (4.625, 70, 100),  # F
    (4.625, 72, 85),  # A
    (4.625, 77, 90),  # C
    (4.625, 75, 80),  # Eb
])

for t, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=t, end=t + 0.2))

# Bar 4: Sax resolves with a small upward leap, bass continues, piano ends with a Bb7
# Sax: Gb -> F -> G -> A (ending on A, a half-step above the motif)
# Time: 4.5s - 6.0s

sax_notes = [
    (4.5, 71, 100),
    (4.6875, 70, 100),
    (4.875, 72, 100),
    (5.0625, 74, 90)  # A
]

for t, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=t, end=t + 0.1))

# Bass continues to B
bass_notes = [
    (4.5, 74),  # A
    (4.6875, 75),  # Bb
    (4.875, 76),  # B
    (5.0625, 77),  # C
]

for t, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.15))

# Piano: Bb7 on 4 (4.625s already done, so wrap with the final chord)

# Final chord: Bb7
final_chord = [
    (5.25, 71, 100),  # Bb
    (5.25, 74, 85),  # D
    (5.25, 70, 90),  # F
    (5.25, 73, 80),  # Ab
]

for t, pitch, vel in final_chord:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=t, end=t + 0.2))

# Add all instruments to the MIDI
midi.instruments = [drums, sax, bass, piano]

# Save the MIDI file
midi.write("dante_russo_intro.mid")

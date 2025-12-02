
import pretty_midi
import numpy as np

# Constants
BPM = 160
TEMPO = 60 / BPM  # seconds per beat
BAR_DURATION = 1.5  # seconds (4/4 time, 6 seconds for 4 bars)
NOTE_DURATION = 0.375  # 1/4 note in seconds
NOTE_RESOLUTION = 480  # MIDI resolution (used for timing)

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=BPM)

# Create instruments
tenor_sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drums')

tenor_sax = pretty_midi.Instrument(program=tenor_sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the MIDI file
midi.instruments.append(tenor_sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Key: F major
# Scale degrees: F, G, A, Bb, C, D, E
# F = 65 (MIDI note number)
# Build a simple melody for the tenor sax in F major
# Motif: F - Bb (1st bar), then G - A (2nd bar), then C - D (3rd bar), then E (4th bar)
# The motif is short, rhythmic, and ends on a strong note (E), leaving the resolution to the next phrase

# Tenor Sax: Start of the motif
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0, end=NOTE_DURATION))  # F
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=NOTE_DURATION, end=2*NOTE_DURATION))  # Bb

tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2*NOTE_DURATION, end=3*NOTE_DURATION))  # G
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3*NOTE_DURATION, end=4*NOTE_DURATION))  # A

tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4*NOTE_DURATION, end=5*NOTE_DURATION))  # C
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5*NOTE_DURATION, end=6*NOTE_DURATION))  # D

tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=6*NOTE_DURATION, end=6.375))  # E (rest of the bar)

# Bass: Chromatic walking line
# F - Gb - G - Ab - A - Bb - B - C - D - Eb - E - F - G - Ab - A - Bb
# 16 notes, each 0.375s (1/4 note)
chromatic_walk = [65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 77]
for i, pitch in enumerate(chromatic_walk):
    start = i * NOTE_DURATION
    end = start + NOTE_DURATION
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Comp on 2 and 4
# F7 on 2 and 4
# F7 chord: F, A, C, E
# Each bar = 6 seconds, 2 and 4 = 1.5s and 3s
# F7 on 1.5s and 3s, each for 0.375s
# 7th chord: F (65), A (69), C (60), E (64)
for start in [1.5, 3.0]:
    for pitch in [65, 69, 60, 64]:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + NOTE_DURATION))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar divisions:
# 0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, etc.

# Kick on 1 and 3 of each bar
for bar in range(4):
    kick_start = bar * 1.5
    kick_notes = [kick_start, kick_start + 1.5]
    for k in kick_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=k, end=k + 0.125))

# Snare on 2 and 4
for bar in range(4):
    snare_start = bar * 1.5
    snare_notes = [snare_start + 0.75, snare_start + 2.25]
    for s in snare_notes:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=s, end=s + 0.125))

# Hi-hat on every eighth note
for bar in range(4):
    start = bar * 1.5
    for i in range(8):
        hihat_start = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.125))

# Write MIDI file
midi.write("jazz_intro_f_major.mid")
print("MIDI file written: jazz_intro_f_major.mid")

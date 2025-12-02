
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create an instrument for each player
tenor_sax = pretty_midi.Instrument(program=64)  # Tenor Sax
bass = pretty_midi.Instrument(program=33)       # Double Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=10)     # Acoustic Drums

# Set up time in seconds per bar (160 BPM = 60/160 = 0.375 seconds per beat, 4 beats per bar)
bar_length = 0.375 * 4  # 1.5 seconds per bar

# Helper function to create a note
def note(note_number, start, duration, velocity):
    n = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=start + duration)
    return n

# Helper function to create a rest
def rest(start, duration):
    return pretty_midi.Note(velocity=0, pitch=0, start=start, end=start + duration)

# == Drum Pattern: Little Ray ==
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4: Same pattern but with subtle variations in timing

# Bar 1
drum_notes = [
    note(36, 0, 0.1875, 100),  # Kick on 1
    note(38, 0.375, 0.1875, 100),  # Snare on 2
    note(42, 0.75, 0.1875, 100),  # Hihat on 1/8
    note(36, 0.9375, 0.1875, 100),  # Kick on 3
    note(38, 1.125, 0.1875, 100),  # Snare on 4
    note(42, 1.5, 0.1875, 100)  # Hihat on 4/8
]

# Add to drum instrument
for n in drum_notes:
    drums.notes.append(n)

# == Bass Line: Marcus ==
# Walking line, chromatic approaches, no repeated notes
# Fm7: F, Ab, Bb, D (root, b3, 4, b7)
# Bar 1: F, Gb, G, Ab (chromatic approach to F)
# Bar 2: Bb, B, C, C#
# Bar 3: D, D#, E, F
# Bar 4: Ab, A, A#, Bb (chromatic approach to Ab)

# Note durations = 0.375 (quarter note)
# Velocities vary slightly for nuance
bass_notes = [
    note(71, 0, 0.375, 80),  # F
    note(70, 0.375, 0.375, 75),  # Gb
    note(71, 0.75, 0.375, 85),  # G
    note(70, 1.125, 0.375, 80),  # Ab

    note(76, 1.5, 0.375, 78),  # Bb
    note(77, 1.875, 0.375, 82),  # B
    note(78, 2.25, 0.375, 80),  # C
    note(79, 2.625, 0.375, 76),  # C#

    note(69, 3, 0.375, 85),  # D
    note(70, 3.375, 0.375, 83),  # D#
    note(71, 3.75, 0.375, 80),  # E
    note(71, 4.125, 0.375, 85),  # F

    note(70, 4.5, 0.375, 78),  # Ab
    note(71, 4.875, 0.375, 82),  # A
    note(72, 5.25, 0.375, 80),  # A#
    note(70, 5.625, 0.375, 76)   # Bb
]

for n in bass_notes:
    bass.notes.append(n)

# == Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4 ==
# Bar 1: Empty (rest)
# Bar 2: Fm7 (F, Ab, Bb, D)
# Bar 3: Empty (rest)
# Bar 4: Fm7 again, but with variation in velocity

# Bar 2: Fm7 on beat 2
piano_notes = [
    note(71, 1.125, 0.125, 90),  # F
    note(70, 1.125, 0.125, 95),  # Ab
    note(76, 1.125, 0.125, 85),  # Bb
    note(69, 1.125, 0.125, 90),  # D

    # Bar 4: Fm7, but with slight variation in attack
    note(71, 5.625, 0.125, 92),  # F
    note(70, 5.625, 0.125, 97),  # Ab
    note(76, 5.625, 0.125, 88),  # Bb
    note(69, 5.625, 0.125, 92)   # D
]

for n in piano_notes:
    piano.notes.append(n)

# == Tenor Sax (You): One short motif, open-ended, leaves it hanging ==
# Start with a short phrase: F, Ab, Bb, and end on a rest, leaving the resolution open
# F (71) -> Ab (70) -> Bb (76) -> Rest

# Bar 1: Rest (setup)
tenor_notes = [
    rest(0, 0.375)  # Bar 1: silence
]

# Bar 2: Start the motif
tenor_notes.append(note(71, 1.5, 0.1875, 100))  # F
tenor_notes.append(note(70, 1.6875, 0.1875, 100))  # Ab
tenor_notes.append(note(76, 1.875, 0.1875, 100))  # Bb
tenor_notes.append(rest(2.0625, 0.375))  # Rest for the last quarter to leave it hanging

# Add to sax instrument
for n in tenor_notes:
    tenor_sax.notes.append(n)

# Add instruments to the MIDI file
midi.instruments.append(tenor_sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("cellar_moment.mid")

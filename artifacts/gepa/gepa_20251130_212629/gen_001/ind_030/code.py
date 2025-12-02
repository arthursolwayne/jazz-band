
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.125, 38, 100),# Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    (1.5, 59, 100), # D
    (1.75, 57, 100), # C
    (2.0, 60, 100),  # D#
    (2.25, 62, 100), # E
    (2.5, 64, 100),  # F#
    (2.75, 62, 100), # E
    (3.0, 60, 100),  # D#
    (3.25, 59, 100), # D
    (3.5, 57, 100),  # C
    (3.75, 55, 100), # Bb
    (4.0, 57, 100),  # C
    (4.25, 59, 100), # D
    (4.5, 61, 100),  # Eb
    (4.75, 62, 100), # E
    (5.0, 64, 100),  # F#
    (5.25, 62, 100), # E
    (5.5, 60, 100),  # D#
    (5.75, 59, 100)  # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62, 100), # E7: E, G#, B, D
    (2.0, 67, 100),
    (2.0, 71, 100),
    (2.0, 64, 100),
    # Bar 3
    (3.5, 62, 100), # E7 again
    (3.5, 67, 100),
    (3.5, 71, 100),
    (3.5, 64, 100),
    # Bar 4
    (5.0, 62, 100), # E7 again
    (5.0, 67, 100),
    (5.0, 71, 100),
    (5.0, 64, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick on 1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on 3
    (2.5, 36, 100),  # Kick on 3
    (2.75, 38, 100), # Snare on 4
    (3.0, 42, 100),  # Hihat on 4
    # Bar 3
    (3.5, 36, 100),  # Kick on 1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on 3
    (4.5, 36, 100),  # Kick on 3
    (4.75, 38, 100), # Snare on 4
    (5.0, 42, 100),  # Hihat on 4
    # Bar 4
    (5.5, 36, 100),  # Kick on 1
    (6.0, 38, 100),  # Snare on 2
    (6.25, 42, 100), # Hihat on 3
    (6.5, 36, 100),  # Kick on 3
    (6.75, 38, 100), # Snare on 4
    (7.0, 42, 100)   # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Saxophone: Dante, one short motif, make it sing
sax_notes = [
    (1.5, 64, 100), # F#
    (1.625, 65, 100),# G
    (1.75, 62, 100), # E
    (1.875, 64, 100),# F#
    (2.0, 64, 100),  # F#
    (2.125, 67, 100),# A
    (2.25, 62, 100), # E
    (2.375, 64, 100),# F#
    (2.5, 69, 100),  # C
    (2.625, 67, 100),# A
    (2.75, 64, 100), # F#
    (2.875, 62, 100),# E
    (3.0, 64, 100),  # F#
    (3.125, 67, 100),# A
    (3.25, 65, 100), # G
    (3.375, 62, 100),# E
    (3.5, 64, 100),  # F#
    (3.625, 67, 100),# A
    (3.75, 69, 100), # C
    (3.875, 67, 100),# A
    (4.0, 64, 100),  # F#
    (4.125, 65, 100),# G
    (4.25, 62, 100), # E
    (4.375, 64, 100),# F#
    (4.5, 69, 100),  # C
    (4.625, 67, 100),# A
    (4.75, 64, 100), # F#
    (4.875, 62, 100),# E
    (5.0, 64, 100),  # F#
    (5.125, 67, 100),# A
    (5.25, 65, 100), # G
    (5.375, 62, 100),# E
    (5.5, 64, 100),  # F#
    (5.625, 67, 100),# A
    (5.75, 69, 100), # C
    (5.875, 67, 100),# A
    (6.0, 64, 100)   # F#
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

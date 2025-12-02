
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (1.25, 38, 100), # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    (1.5, 60, 100), # C
    (1.75, 61, 100), # C#
    (2.0, 62, 100),  # D
    (2.25, 63, 100), # D#
    (2.5, 64, 100),  # E
    (2.75, 65, 100), # F
    (3.0, 67, 100),  # G
    (3.25, 68, 100), # G#
    (3.5, 69, 100),  # A
    (3.75, 70, 100), # A#
    (4.0, 71, 100),  # B
    (4.25, 72, 100), # C
    (4.5, 73, 100),  # C#
    (4.75, 74, 100), # D
    (5.0, 75, 100),  # D#
    (5.25, 76, 100), # E
    (5.5, 77, 100),  # F
    (5.75, 79, 100), # G
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2
    (1.75, 60, 100), # C
    (1.75, 64, 100), # E
    (1.75, 67, 100), # G
    (1.75, 71, 100), # B
    # Bar 3
    (3.25, 60, 100), # C
    (3.25, 64, 100), # E
    (3.25, 67, 100), # G
    (3.25, 71, 100), # B
    # Bar 4
    (4.75, 60, 100), # C
    (4.75, 64, 100), # E
    (4.75, 67, 100), # G
    (4.75, 71, 100), # B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
drum_pattern = [
    (1.5, 36, 100),
    (1.75, 42, 100),
    (2.0, 38, 100),
    (2.25, 42, 100),
    (2.5, 36, 100),
    (2.75, 42, 100),
    (3.0, 38, 100),
    (3.25, 42, 100),
    (3.5, 36, 100),
    (3.75, 42, 100),
    (4.0, 38, 100),
    (4.25, 42, 100),
    (4.5, 36, 100),
    (4.75, 42, 100),
    (5.0, 38, 100),
    (5.25, 42, 100)
]
for time, note, velocity in drum_pattern:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62, 100), # D
    (1.75, 64, 100), # E
    (2.0, 62, 100), # D
    (2.25, 64, 100), # E
    (2.5, 62, 100), # D
    (2.75, 67, 100), # G
    (3.0, 62, 100), # D
    (3.25, 64, 100), # E
    (3.5, 62, 100), # D
    (3.75, 64, 100), # E
    (4.0, 62, 100), # D
    (4.25, 67, 100), # G
    (4.5, 62, 100), # D
    (4.75, 64, 100), # E
    (5.0, 62, 100), # D
    (5.25, 64, 100), # E
    (5.5, 62, 100), # D
    (5.75, 67, 100), # G
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

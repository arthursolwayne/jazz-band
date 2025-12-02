
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
    (1.5, 38, 100),  # Snare on 3
    (2.25, 42, 100), # Hihat on 4
    (3.0, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on 2
    (4.5, 38, 100),  # Snare on 3
    (5.25, 42, 100), # Hihat on 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    (1.5, 60, 100),  # C
    (1.875, 61, 100), # C#
    (2.25, 62, 100),  # D
    (2.625, 63, 100), # D#
    (3.0, 64, 100),   # E
    (3.375, 65, 100), # F
    (3.75, 66, 100),  # F#
    (4.125, 67, 100), # G
    (4.5, 68, 100),   # G#
    (4.875, 69, 100), # A
    (5.25, 70, 100),  # A#
    (5.625, 71, 100), # B
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    (2.25, 60, 100),  # C
    (2.25, 64, 100),  # E
    (2.25, 67, 100),  # G
    (2.25, 71, 100),  # B
    (3.75, 60, 100),  # C
    (3.75, 64, 100),  # E
    (3.75, 67, 100),  # G
    (3.75, 71, 100),  # B
    (5.25, 60, 100),  # C
    (5.25, 64, 100),  # E
    (5.25, 67, 100),  # G
    (5.25, 71, 100),  # B
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65, 100),  # E
    (1.75, 67, 100),  # G
    (2.0, 69, 100),   # A
    (2.25, 71, 100),  # B
    (3.0, 65, 100),  # E
    (3.25, 67, 100),  # G
    (3.5, 69, 100),   # A
    (3.75, 71, 100),  # B
    (4.5, 65, 100),  # E
    (4.75, 67, 100),  # G
    (5.0, 69, 100),   # A
    (5.25, 71, 100),  # B
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

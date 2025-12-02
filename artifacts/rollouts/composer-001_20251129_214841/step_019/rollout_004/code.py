
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
    # Kick on 1 and 3
    (0.0, 36, 100),
    (1.5, 36, 100),
    # Snare on 2 and 4
    (0.75, 38, 100),
    (2.25, 38, 100),
    # Hi-hat on every eighth
    (0.0, 42, 100),
    (0.375, 42, 100),
    (0.75, 42, 100),
    (1.125, 42, 100),
    (1.5, 42, 100),
    (1.875, 42, 100),
    (2.25, 42, 100),
    (2.625, 42, 100),
    (3.0, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 60, 100),  # C
    (1.875, 61, 100),  # C#
    (2.25, 62, 100),  # D
    (2.625, 63, 100),  # D#
    # Bar 3
    (3.0, 64, 100),  # E
    (3.375, 65, 100),  # F
    (3.75, 66, 100),  # F#
    (4.125, 67, 100),  # G
    # Bar 4
    (4.5, 68, 100),  # G#
    (4.875, 69, 100),  # A
    (5.25, 70, 100),  # A#
    (5.625, 71, 100)   # B
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 60, 100),  # C
    (2.25, 64, 100),  # E
    (2.25, 67, 100),  # G
    (2.25, 71, 100),  # B
    # Bar 3
    (3.75, 60, 100),  # C
    (3.75, 64, 100),  # E
    (3.75, 67, 100),  # G
    (3.75, 71, 100),  # B
    # Bar 4
    (5.25, 60, 100),  # C
    (5.25, 64, 100),  # E
    (5.25, 67, 100),  # G
    (5.25, 71, 100),  # B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Sax (Dante) - short motif, make it sing
# Motif: C, E, G, B (C7) - start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (1.5, 60, 100),  # C
    (1.75, 64, 100),  # E
    (2.0, 67, 100),  # G
    (2.25, 71, 100),  # B
    # Bar 3 (wait, don't resolve)
    (3.0, 60, 100),  # C
    (3.25, 64, 100),  # E
    (3.5, 67, 100),  # G
    # Bar 4 (resolve)
    (4.5, 71, 100),  # B
    (4.75, 67, 100),  # G
    (5.0, 64, 100),  # E
    (5.25, 60, 100)   # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick on 1
    (2.25, 38, 100),  # Snare on 2
    (2.625, 42, 100),  # Hihat on 3
    (3.0, 36, 100),  # Kick on 3
    (3.75, 38, 100),  # Snare on 4
    (4.125, 42, 100),  # Hihat on 4
    # Bar 3
    (3.0, 36, 100),  # Kick on 1
    (3.75, 38, 100),  # Snare on 2
    (4.125, 42, 100),  # Hihat on 3
    (4.5, 36, 100),  # Kick on 3
    (5.25, 38, 100),  # Snare on 4
    (5.625, 42, 100),  # Hihat on 4
    # Bar 4
    (4.5, 36, 100),  # Kick on 1
    (5.25, 38, 100),  # Snare on 2
    (5.625, 42, 100),  # Hihat on 3
    (6.0, 36, 100),  # Kick on 3
    (6.75, 38, 100),  # Snare on 4
    (7.125, 42, 100)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

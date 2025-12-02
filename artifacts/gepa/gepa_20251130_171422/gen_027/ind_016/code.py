
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 38, 100),    # snare on 2
    (0.375, 42, 60),   # hihat on 1
    (0.75, 42, 60),    # hihat on 2
    (1.125, 42, 60),   # hihat on 3
    (1.5, 42, 60),     # hihat on 4
    (1.5, 36, 110)     # kick on 4
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (Bar 2)
# Fm7 -> Bb -> Ab -> Eb -> Fm7
sax_notes = [
    (1.5, 64, 100),    # F
    (1.75, 69, 100),   # Bb
    (2.0, 67, 100),    # Ab
    (2.25, 62, 100),   # Eb
    (2.5, 64, 100),    # F
    (2.75, 69, 100),   # Bb
    (3.0, 67, 100),    # Ab
    (3.25, 62, 100),   # Eb
    (3.5, 64, 100),    # F
    (3.75, 69, 100),   # Bb
    (4.0, 67, 100),    # Ab
    (4.25, 62, 100),   # Eb
    (4.5, 64, 100),    # F
    (4.75, 69, 100),   # Bb
    (5.0, 67, 100),    # Ab
    (5.25, 62, 100)    # Eb
]
for note in sax_notes:
    sn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    sax.notes.append(sn)

# Bass line (walking, chromatic, melodic)
bass_notes = [
    (1.5, 53, 90),     # F
    (1.75, 51, 90),    # Eb
    (2.0, 49, 90),     # Db
    (2.25, 48, 90),    # C
    (2.5, 50, 90),     # D
    (2.75, 52, 90),    # E
    (3.0, 53, 90),     # F
    (3.25, 55, 90),    # G
    (3.5, 57, 90),     # A
    (3.75, 59, 90),    # Bb
    (4.0, 60, 90),     # B
    (4.25, 62, 90),    # C
    (4.5, 63, 90),     # C#
    (4.75, 64, 90),    # D
    (5.0, 65, 90),     # Eb
    (5.25, 67, 90)     # F
]
for note in bass_notes:
    bn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    bass.notes.append(bn)

# Piano comping (7th chords, on 2 and 4)
piano_notes = [
    (1.75, 64, 100),   # F7 - F
    (1.75, 67, 100),   # F7 - A
    (1.75, 69, 100),   # F7 - Bb
    (1.75, 71, 100),   # F7 - D

    (2.25, 64, 100),   # F7 - F
    (2.25, 67, 100),   # F7 - A
    (2.25, 69, 100),   # F7 - Bb
    (2.25, 71, 100),   # F7 - D

    (2.75, 64, 100),   # F7 - F
    (2.75, 67, 100),   # F7 - A
    (2.75, 69, 100),   # F7 - Bb
    (2.75, 71, 100),   # F7 - D

    (3.25, 64, 100),   # F7 - F
    (3.25, 67, 100),   # F7 - A
    (3.25, 69, 100),   # F7 - Bb
    (3.25, 71, 100),   # F7 - D

    (3.75, 64, 100),   # F7 - F
    (3.75, 67, 100),   # F7 - A
    (3.75, 69, 100),   # F7 - Bb
    (3.75, 71, 100),   # F7 - D

    (4.25, 64, 100),   # F7 - F
    (4.25, 67, 100),   # F7 - A
    (4.25, 69, 100),   # F7 - Bb
    (4.25, 71, 100),   # F7 - D

    (4.75, 64, 100),   # F7 - F
    (4.75, 67, 100),   # F7 - A
    (4.75, 69, 100),   # F7 - Bb
    (4.75, 71, 100),   # F7 - D
]
for note in piano_notes:
    pn = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25)
    piano.notes.append(pn)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 110),    # kick on 1
    (1.75, 38, 100),   # snare on 2
    (2.0, 42, 60),     # hihat on 3
    (2.25, 42, 60),    # hihat on 4
    (2.5, 36, 110),    # kick on 1
    (2.75, 38, 100),   # snare on 2
    (3.0, 42, 60),     # hihat on 3
    (3.25, 42, 60),    # hihat on 4

    # Bar 3
    (3.5, 36, 110),    # kick on 1
    (3.75, 38, 100),   # snare on 2
    (4.0, 42, 60),     # hihat on 3
    (4.25, 42, 60),    # hihat on 4
    (4.5, 36, 110),    # kick on 1
    (4.75, 38, 100),   # snare on 2
    (5.0, 42, 60),     # hihat on 3
    (5.25, 42, 60),    # hihat on 4
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_moment.mid")

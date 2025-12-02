
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 62, 100),     # C
    (1.875, 61, 100),   # Bb
    (2.25, 63, 100),    # C#
    (2.625, 64, 100),   # D
    (3.0, 62, 100),     # C
    (3.375, 61, 100),   # Bb
    (3.75, 63, 100),    # C#
    (4.125, 64, 100),   # D
    (4.5, 62, 100),     # C
    (4.875, 61, 100),   # Bb
    (5.25, 63, 100),    # C#
    (5.625, 64, 100)    # D
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60, 100),     # C7 (C, E, Bb)
    (1.5, 64, 100),
    (1.5, 67, 100),
    (1.875, 60, 100),
    (1.875, 64, 100),
    (1.875, 67, 100),
    (2.25, 60, 100),
    (2.25, 64, 100),
    (2.25, 67, 100),
    (2.625, 60, 100),
    (2.625, 64, 100),
    (2.625, 67, 100),
    (3.0, 60, 100),
    (3.0, 64, 100),
    (3.0, 67, 100),
    (3.375, 60, 100),
    (3.375, 64, 100),
    (3.375, 67, 100),
    (3.75, 60, 100),
    (3.75, 64, 100),
    (3.75, 67, 100),
    (4.125, 60, 100),
    (4.125, 64, 100),
    (4.125, 67, 100),
    (4.5, 60, 100),
    (4.5, 64, 100),
    (4.5, 67, 100),
    (4.875, 60, 100),
    (4.875, 64, 100),
    (4.875, 67, 100),
    (5.25, 60, 100),
    (5.25, 64, 100),
    (5.25, 67, 100),
    (5.625, 60, 100),
    (5.625, 64, 100),
    (5.625, 67, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C6 (C), E6 (E), G6 (G), Bb6 (Bb) as motif
sax_notes = [
    (1.5, 84, 110),     # C6
    (1.75, 87, 100),    # E6
    (2.0, 89, 100),     # G6
    (2.25, 88, 100),    # Bb6
    (3.0, 84, 110),     # C6 (return)
    (3.25, 87, 100),    # E6
    (3.5, 89, 100),     # G6
    (3.75, 88, 100)     # Bb6
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

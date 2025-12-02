
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# D minor blues: D, Eb, F, G, Ab, Bb, B
# Walking in D minor
bass_notes = [
    (1.5, 62),  # D
    (1.875, 61), # Eb
    (2.25, 63),  # F
    (2.625, 62), # D
    (2.875, 60), # C
    (3.25, 61),  # Eb
    (3.625, 63), # F
    (4.0, 62),   # D
    (4.375, 60), # C
    (4.75, 59),  # Bb
    (5.125, 60), # C
    (5.5, 62),   # D
    (5.875, 61), # Eb
    (6.25, 63)   # F
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# D7 (D F# A C), G7 (G B D F), A7 (A C# E G), B7 (B D# F# A)
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 64),  # D7
    (2.25, 71), (2.25, 76), (2.25, 74), (2.25, 72),  # G7
    (3.0, 72), (3.0, 77), (3.0, 81), (3.0, 76),  # A7
    (3.75, 76), (3.75, 81), (3.75, 84), (3.75, 78)   # B7
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), Eb (63), F (64), Eb (63), D (62)
sax_notes = [
    (1.5, 62), (1.5, 63), (1.5, 64), (1.5, 63), (1.5, 62),  # First pass
    (3.0, 62), (3.0, 63), (3.0, 64), (3.0, 63), (3.0, 62)   # Second pass
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1, 2]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")

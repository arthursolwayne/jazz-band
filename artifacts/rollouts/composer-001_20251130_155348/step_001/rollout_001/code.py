
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Marcus, walking line, chromatic approaches, no repeated notes
# F7 chord: F, A, C, E
# Chromatic approach to F: E#, F
# Chromatic approach to A: G#, A
# Chromatic approach to C: B, C
# Chromatic approach to E: D#, E

bass_notes = [
    (1.5, 75, 72),  # E#
    (1.875, 75, 76), # F
    (2.25, 75, 78),  # G#
    (2.625, 75, 80), # A
    (3.0, 75, 79),   # B
    (3.375, 75, 81), # C
    (3.75, 75, 83),  # D#
    (4.125, 75, 85), # E
]

for time, velocity, pitch in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Diane, 7th chords, comp on 2 and 4
# F7: F, A, C, E
# F7 with 7th: F, A, C, E
# Comp on 2 and 4

piano_notes = [
    (1.875, 100, 72), # F
    (1.875, 100, 76), # A
    (1.875, 100, 79), # C
    (1.875, 100, 82), # E
    (3.0, 100, 72),   # F
    (3.0, 100, 76),   # A
    (3.0, 100, 79),   # C
    (3.0, 100, 82),   # E
]

for time, velocity, pitch in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Dante, melody
# Short motif: F (72), A (76), Eb (70), F (72)
# Start it, leave it hanging, come back and finish it

sax_notes = [
    (1.5, 100, 72), # F
    (1.6875, 100, 76), # A
    (1.875, 100, 70), # Eb
    (2.0625, 100, 72), # F
    (3.0, 100, 72), # F
    (3.1875, 100, 76), # A
    (3.375, 100, 70), # Eb
    (3.5625, 100, 72), # F
]

for time, velocity, pitch in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line
bass_notes = [
    (3.0, 75, 72), # F
    (3.375, 75, 78), # G#
    (3.75, 75, 80), # A
    (4.125, 75, 79), # B
    (4.5, 75, 81),   # C
    (4.875, 75, 83), # D#
    (5.25, 75, 85),  # E
    (5.625, 75, 82), # E
]

for time, velocity, pitch in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: comp on 2 and 4
piano_notes = [
    (3.375, 100, 72), # F
    (3.375, 100, 76), # A
    (3.375, 100, 79), # C
    (3.375, 100, 82), # E
    (4.5, 100, 72),   # F
    (4.5, 100, 76),   # A
    (4.5, 100, 79),   # C
    (4.5, 100, 82),   # E
]

for time, velocity, pitch in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: repeat motif
sax_notes = [
    (3.0, 100, 72), # F
    (3.1875, 100, 76), # A
    (3.375, 100, 70), # Eb
    (3.5625, 100, 72), # F
    (4.5, 100, 72), # F
    (4.6875, 100, 76), # A
    (4.875, 100, 70), # Eb
    (5.0625, 100, 72), # F
]

for time, velocity, pitch in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: same pattern
for bar in range(2, 3):
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

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line
bass_notes = [
    (4.5, 75, 72), # F
    (4.875, 75, 78), # G#
    (5.25, 75, 80), # A
    (5.625, 75, 79), # B
    (6.0, 75, 81),   # C
    (6.375, 75, 83), # D#
    (6.75, 75, 85),  # E
    (7.125, 75, 82), # E
]

for time, velocity, pitch in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: comp on 2 and 4
piano_notes = [
    (4.875, 100, 72), # F
    (4.875, 100, 76), # A
    (4.875, 100, 79), # C
    (4.875, 100, 82), # E
    (6.0, 100, 72),   # F
    (6.0, 100, 76),   # A
    (6.0, 100, 79),   # C
    (6.0, 100, 82),   # E
]

for time, velocity, pitch in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: repeat motif
sax_notes = [
    (4.5, 100, 72), # F
    (4.6875, 100, 76), # A
    (4.875, 100, 70), # Eb
    (5.0625, 100, 72), # F
    (6.0, 100, 72), # F
    (6.1875, 100, 76), # A
    (6.375, 100, 70), # Eb
    (6.5625, 100, 72), # F
]

for time, velocity, pitch in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: same pattern
for bar in range(3, 4):
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

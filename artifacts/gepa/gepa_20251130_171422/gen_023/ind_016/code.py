
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
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (2, 1.5, 100), (3, 1.875, 100), (4, 2.25, 100), (5, 2.625, 100),
    (7, 3.0, 100), (8, 3.375, 100), (9, 3.75, 100), (10, 4.125, 100),
    (11, 4.5, 100), (12, 4.875, 100), (13, 5.25, 100), (14, 5.625, 100)
]
for pitch, start, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords comp on 2 and 4, key of D
piano_notes = [
    # Bar 2
    (7, 1.5, 100), (9, 1.5, 100), (11, 1.5, 100), (12, 1.5, 100),
    # Bar 3
    (7, 3.0, 100), (9, 3.0, 100), (11, 3.0, 100), (12, 3.0, 100),
    # Bar 4
    (7, 4.5, 100), (9, 4.5, 100), (11, 4.5, 100), (12, 4.5, 100)
]
for pitch, start, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (6, 1.5, 110), (7, 1.875, 110),
    # Bar 3
    (9, 3.0, 110), (10, 3.375, 110),
    # Bar 4
    (7, 4.5, 110), (6, 4.875, 110)
]
for pitch, start, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums: Continue pattern
for beat in [0, 2, 3, 5, 6, 8, 9, 11]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375 + 1.5, end=(beat + 1) * 0.375 + 1.5)
    drums.notes.append(note)
for beat in [1, 3, 4, 6, 7, 9, 10, 12]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375 + 1.5, end=(beat + 1) * 0.375 + 1.5)
    drums.notes.append(note)
for beat in range(12):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375 + 1.5, end=(beat + 1) * 0.375 + 1.5)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_russo_intro.mid')

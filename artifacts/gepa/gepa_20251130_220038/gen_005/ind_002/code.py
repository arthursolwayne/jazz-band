
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
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (1.5, 46),  # F
    (1.875, 47), # Gb
    (2.25, 45),  # E
    (2.625, 47), # Gb
    (2.875, 48), # G
    (3.25, 46),  # F
    (3.625, 44), # D
    (4.0, 45),   # E
    (4.375, 47), # Gb
    (4.75, 48),  # G
    (5.125, 46), # F
    (5.5, 44),   # D
    (5.875, 45)  # E
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 59), (1.5, 71), (1.5, 64), (1.5, 61),  # F7 (F, A, C, Eb)
    (2.25, 59), (2.25, 71), (2.25, 64), (2.25, 61), # F7
    (3.0, 59), (3.0, 71), (3.0, 64), (3.0, 61),    # F7
    (3.75, 59), (3.75, 71), (3.75, 64), (3.75, 61), # F7
    (4.5, 59), (4.5, 71), (4.5, 64), (4.5, 61),    # F7
    (5.25, 59), (5.25, 71), (5.25, 64), (5.25, 61)  # F7
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62),  # G
    (1.625, 60), # E
    (1.75, 62),  # G
    (1.875, 60), # E
    (2.25, 62),  # G
    (2.375, 64), # A
    (2.5, 62),   # G
    (2.625, 60), # E
    (3.0, 65),   # Bb
    (3.125, 62), # G
    (3.25, 60),  # E
    (3.375, 62), # G
    (3.5, 64),   # A
    (3.625, 62), # G
    (3.75, 60),  # E
    (3.875, 62), # G
    (4.0, 64),   # A
    (4.125, 62), # G
    (4.25, 60),  # E
    (4.375, 62), # G
    (4.5, 65),   # Bb
    (4.625, 62), # G
    (4.75, 60),  # E
    (4.875, 62), # G
    (5.0, 64),   # A
    (5.125, 62), # G
    (5.25, 60),  # E
    (5.375, 62), # G
    (5.5, 64),   # A
    (5.625, 62), # G
    (5.75, 60),  # E
    (5.875, 62)  # G
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums: Continue in bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

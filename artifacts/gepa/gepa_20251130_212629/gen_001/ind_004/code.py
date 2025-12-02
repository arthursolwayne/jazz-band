
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

# Bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 55), (1.75, 57), (2.0, 59), (2.25, 57),
    # Bar 3
    (2.5, 55), (2.75, 57), (3.0, 59), (3.25, 57),
    # Bar 4
    (3.5, 55), (3.75, 57), (4.0, 59), (4.25, 57),
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 71),
    (2.0, 62), (2.0, 65), (2.0, 69), (2.0, 72),
    # Bar 3
    (2.5, 60), (2.5, 64), (2.5, 67), (2.5, 71),
    (3.0, 62), (3.0, 65), (3.0, 69), (3.0, 72),
    # Bar 4
    (3.5, 60), (3.5, 64), (3.5, 67), (3.5, 71),
    (4.0, 62), (4.0, 65), (4.0, 69), (4.0, 72),
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.25)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=110, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.25)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + beat * 0.375, end=start + beat * 0.375 + 0.25)
        drums.notes.append(note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Motif: F - Ab - Bb - F (but spaced out)
sax_notes = [
    # Bar 2
    (1.5, 65), (1.75, 68), (2.0, 70), (2.25, 65),
    # Bar 3
    (2.5, 65), (2.75, 68), (3.0, 70), (3.25, 68),
    # Bar 4
    (3.5, 65), (3.75, 68), (4.0, 70), (4.25, 65),
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

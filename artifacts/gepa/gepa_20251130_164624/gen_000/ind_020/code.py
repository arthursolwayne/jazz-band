
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 48), (1.75, 49), (2.0, 50), (2.25, 51),  # Bar 2
    (2.5, 51), (2.75, 50), (3.0, 49), (3.25, 48),  # Bar 3
    (3.5, 48), (3.75, 49), (4.0, 50), (4.25, 51),  # Bar 4
    (4.5, 51), (4.75, 50), (5.0, 49), (5.25, 48)   # Bar 4
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 62), (1.75, 67), (1.75, 69), (1.75, 71),  # F7
    # Bar 3
    (2.75, 62), (2.75, 67), (2.75, 69), (2.75, 71),  # F7
    # Bar 4
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),  # F7
    (4.75, 62), (4.75, 67), (4.75, 69), (4.75, 71)   # F7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - Gb (66) - E (64) - D (62)
sax_notes = [
    (1.5, 65), (1.5, 66), (1.5, 64), (1.5, 62),    # Start motif
    (2.0, 62), (2.0, 64), (2.0, 66), (2.0, 65),    # Repeat motif
    (2.5, 62), (2.5, 64), (2.5, 66), (2.5, 65),    # Repeat motif
    (3.0, 62), (3.0, 64), (3.0, 66), (3.0, 65),    # Repeat motif
    (3.5, 62), (3.5, 64), (3.5, 66), (3.5, 65),    # Repeat motif
    (4.0, 62), (4.0, 64), (4.0, 66), (4.0, 65),    # Repeat motif
    (4.5, 62), (4.5, 64), (4.5, 66), (4.5, 65),    # Repeat motif
    (5.0, 62), (5.0, 64), (5.0, 66), (5.0, 65)     # Repeat motif
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('intro_wayne.mid')

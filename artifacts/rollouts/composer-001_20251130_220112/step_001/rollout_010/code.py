
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

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 53),  # F
    (1.875, 51), # Eb
    (2.25, 50),  # D
    (2.625, 53), # F
    (2.875, 55), # G
    (3.25, 53),  # F
    (3.625, 51), # Eb
    (4.0, 50),   # D
    (4.375, 53), # F
    (4.75, 55),  # G
    (5.125, 53), # F
    (5.5, 51),   # Eb
    (5.875, 50), # D
    (6.25, 53)   # F
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=75, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, Fm7, Bb7, Fm7, Bb7
piano_notes = [
    (1.875, 53), (1.875, 64), (1.875, 69), (1.875, 71),  # Fm7
    (2.625, 55), (2.625, 67), (2.625, 72), (2.625, 79),  # Bb7
    (4.375, 53), (4.375, 64), (4.375, 69), (4.375, 71),  # Fm7
    (5.5, 55), (5.5, 67), (5.5, 72), (5.5, 79)           # Bb7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif in Fm, sparse, singing
sax_notes = [
    (1.5, 62), (1.625, 64), (1.75, 62),  # F - G - F
    (2.25, 62), (2.375, 64), (2.5, 62),  # F - G - F
    (3.0, 62), (3.125, 64), (3.25, 62),  # F - G - F
    (3.75, 62), (3.875, 64), (4.0, 62),  # F - G - F
    (4.5, 62), (4.625, 64), (4.75, 62),  # F - G - F
    (5.25, 62), (5.375, 64), (5.5, 62)   # F - G - F
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

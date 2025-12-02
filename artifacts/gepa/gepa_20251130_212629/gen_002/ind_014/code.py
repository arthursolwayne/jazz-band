
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

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),   # D
    (1.875, 63), # Eb
    (2.25, 60),  # C
    (2.625, 62), # D
    (2.625, 64), # E
    (3.0, 62),   # D
    (3.375, 63), # Eb
    (3.75, 60),  # C
    (3.75, 62),  # D
    (4.125, 63), # Eb
    (4.5, 60),   # C
    (4.875, 62), # D
    (4.875, 64), # E
    (5.25, 62),  # D
    (5.625, 63), # Eb
    (6.0, 60)    # C
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 69), (1.5, 71),  # Dm7
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),  # Dm7
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 71),  # Dm7
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),  # Dm7
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 71),  # Dm7
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71)   # Dm7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Bars 2-4
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
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Eb, F, G (bar 2), then A, Bb, C (bar 3), repeat (bar 4)
sax_notes = [
    (1.5, 62), (1.5, 63), (1.5, 65), (1.5, 67),  # D, Eb, F, G
    (1.875, 62), (1.875, 63), (1.875, 65), (1.875, 67),  # D, Eb, F, G
    (2.25, 69), (2.25, 71), (2.25, 69), (2.25, 67),  # A, Bb, A, G
    (2.625, 62), (2.625, 63), (2.625, 65), (2.625, 67),  # D, Eb, F, G
    (3.0, 69), (3.0, 71), (3.0, 69), (3.0, 67),  # A, Bb, A, G
    (3.375, 62), (3.375, 63), (3.375, 65), (3.375, 67),  # D, Eb, F, G
    (3.75, 69), (3.75, 71), (3.75, 69), (3.75, 67),  # A, Bb, A, G
    (4.125, 62), (4.125, 63), (4.125, 65), (4.125, 67),  # D, Eb, F, G
    (4.5, 69), (4.5, 71), (4.5, 69), (4.5, 67),  # A, Bb, A, G
    (4.875, 62), (4.875, 63), (4.875, 65), (4.875, 67),  # D, Eb, F, G
    (5.25, 69), (5.25, 71), (5.25, 69), (5.25, 67),  # A, Bb, A, G
    (5.625, 62), (5.625, 63), (5.625, 65), (5.625, 67)   # D, Eb, F, G
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

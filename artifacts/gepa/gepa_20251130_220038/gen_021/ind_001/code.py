
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
            note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),     # D
    (1.875, 63),   # Eb
    (2.25, 60),    # C
    (2.625, 59),   # Bb
    (3.0, 62),     # D
    (3.375, 63),   # Eb
    (3.75, 60),    # C
    (4.125, 59),   # Bb
    (4.5, 62),     # D
    (4.875, 63),   # Eb
    (5.25, 60),    # C
    (5.625, 59)    # Bb
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62),     # D
    (1.5, 67),     # G
    (1.5, 69),     # Bb
    (1.5, 71),     # D
    (1.875, 62),   # D
    (1.875, 67),   # G
    (1.875, 69),   # Bb
    (1.875, 71),   # D
    (2.25, 62),    # D
    (2.25, 67),    # G
    (2.25, 69),    # Bb
    (2.25, 71),    # D
    (2.625, 62),   # D
    (2.625, 67),   # G
    (2.625, 69),   # Bb
    (2.625, 71),   # D
    (3.0, 62),     # D
    (3.0, 67),     # G
    (3.0, 69),     # Bb
    (3.0, 71),     # D
    (3.375, 62),   # D
    (3.375, 67),   # G
    (3.375, 69),   # Bb
    (3.375, 71),   # D
    (3.75, 62),    # D
    (3.75, 67),    # G
    (3.75, 69),    # Bb
    (3.75, 71),    # D
    (4.125, 62),   # D
    (4.125, 67),   # G
    (4.125, 69),   # Bb
    (4.125, 71),   # D
    (4.5, 62),     # D
    (4.5, 67),     # G
    (4.5, 69),     # Bb
    (4.5, 71),     # D
    (4.875, 62),   # D
    (4.875, 67),   # G
    (4.875, 69),   # Bb
    (4.875, 71),   # D
    (5.25, 62),    # D
    (5.25, 67),    # G
    (5.25, 69),    # Bb
    (5.25, 71),    # D
    (5.625, 62),   # D
    (5.625, 67),   # G
    (5.625, 69),   # Bb
    (5.625, 71)    # D
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65),     # E
    (1.625, 67),   # G
    (1.75, 69),    # Bb
    (1.875, 67),   # G
    (2.0, 65),     # E
    (2.25, 65),    # E
    (2.375, 67),   # G
    (2.5, 69),     # Bb
    (2.625, 67),   # G
    (2.75, 65),    # E
    (2.875, 67),   # G
    (3.0, 69),     # Bb
    (3.125, 67),   # G
    (3.25, 65)     # E
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

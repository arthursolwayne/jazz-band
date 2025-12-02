
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
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 50),   # D
    (1.875, 51), # Eb
    (2.25, 52),  # E
    (2.625, 53), # F
    (2.625, 48), # C
    (3.0, 49),   # Db
    (3.375, 50), # D
    (3.75, 51),  # Eb
    (3.75, 55),  # G
    (4.125, 56), # G#
    (4.5, 57),   # A
    (4.875, 58), # A#
    (4.875, 53), # F
    (5.25, 54),  # F#
    (5.625, 55), # G
    (6.0, 56)    # G#
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    (1.875, 50), # D7 (D, F#, A, C)
    (1.875, 62),
    (1.875, 67),
    (1.875, 60),
    (2.625, 50),
    (2.625, 62),
    (2.625, 67),
    (2.625, 60),
    (3.75, 50),
    (3.75, 62),
    (3.75, 67),
    (3.75, 60),
    (4.875, 50),
    (4.875, 62),
    (4.875, 67),
    (4.875, 60)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62),  # D
    (1.625, 64), # E
    (1.75, 62),  # D
    (1.875, 65), # F
    (2.25, 62),  # D
    (2.375, 64), # E
    (2.5, 62),   # D
    (2.625, 69), # A
    (3.0, 62),   # D
    (3.125, 64), # E
    (3.25, 62),  # D
    (3.375, 67), # G
    (3.75, 62),  # D
    (3.875, 64), # E
    (4.0, 62),   # D
    (4.125, 65), # F
    (4.5, 62),   # D
    (4.625, 64), # E
    (4.75, 62),  # D
    (4.875, 69), # A
    (5.25, 62),  # D
    (5.375, 64), # E
    (5.5, 62),   # D
    (5.625, 67), # G
    (6.0, 62)    # D
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: continue with kick, snare, hihat
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

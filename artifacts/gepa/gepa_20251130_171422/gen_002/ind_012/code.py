
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
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (1.5, 62),   # D
    (1.875, 63), # Eb
    (2.25, 64),  # E
    (2.625, 62), # D
    (2.875, 60), # C
    (3.25, 61),  # Db
    (3.625, 62), # D
    (4.0, 64),   # E
    (4.375, 65), # F
    (4.75, 64),  # E
    (5.125, 62), # D
    (5.5, 60),   # C
    (5.875, 61), # Db
    (6.25, 62)   # D
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (2.25, 62), # F
    (2.25, 67), # Bb
    (2.25, 69), # D
    (2.25, 71), # F
    (3.75, 62), # F
    (3.75, 67), # Bb
    (3.75, 69), # D
    (3.75, 71), # F
    (5.25, 62), # F
    (5.25, 67), # Bb
    (5.25, 69), # D
    (5.25, 71), # F
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax (Dante): Motif - start it, leave it hanging, come back and finish it
# Motif: Dm7 - G7 - Cm7 - F7
# Start on D, leave it hanging, return on C
sax_notes = [
    (1.5, 62), # D
    (1.6875, 65), # F
    (1.875, 67), # A
    (2.0625, 69), # C
    (2.25, 62), # D
    (2.625, 67), # Bb
    (2.8125, 69), # C
    (3.0, 64), # E
    (3.375, 62), # D
    (3.5625, 65), # F
    (3.75, 67), # A
    (3.9375, 69), # C
    (4.125, 60), # C
    (4.3125, 62), # D
    (4.5, 65), # F
    (4.6875, 67), # A
    (4.875, 69), # C
    (5.0625, 62), # D
    (5.25, 67), # Bb
    (5.4375, 69), # C
    (5.625, 64), # E
    (5.75, 62), # D
    (5.9375, 65), # F
    (6.125, 67), # A
    (6.3125, 69)  # C
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Full bar (1.5 - 6.0s)
for bar in range(3):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

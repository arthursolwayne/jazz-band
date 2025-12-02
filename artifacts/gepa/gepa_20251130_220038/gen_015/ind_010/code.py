
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (1.5, 57), # D
    (1.875, 58), # Eb
    (2.25, 59), # E
    (2.625, 60), # F
    (2.875, 58), # Eb
    (3.25, 57), # D
    (3.625, 55), # C
    (4.0, 57), # D
    (4.375, 58), # Eb
    (4.75, 59), # E
    (5.125, 60), # F
    (5.5, 58), # Eb
    (5.875, 57), # D
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

piano_notes = [
    (1.5, 62), # D
    (1.5, 65), # F
    (1.5, 67), # A
    (1.5, 69), # C
    (1.875, 69), # C
    (1.875, 71), # Eb
    (1.875, 74), # G
    (1.875, 76), # Bb
    (2.25, 62), # D
    (2.25, 65), # F
    (2.25, 67), # A
    (2.25, 69), # C
    (2.625, 67), # A
    (2.625, 71), # Eb
    (2.625, 74), # G
    (2.625, 76), # Bb
    (3.0, 62), # D
    (3.0, 65), # F
    (3.0, 67), # A
    (3.0, 69), # C
    (3.375, 69), # C
    (3.375, 71), # Eb
    (3.375, 74), # G
    (3.375, 76), # Bb
    (3.75, 62), # D
    (3.75, 65), # F
    (3.75, 67), # A
    (3.75, 69), # C
    (4.125, 67), # A
    (4.125, 71), # Eb
    (4.125, 74), # G
    (4.125, 76), # Bb
    (4.5, 62), # D
    (4.5, 65), # F
    (4.5, 67), # A
    (4.5, 69), # C
    (4.875, 69), # C
    (4.875, 71), # Eb
    (4.875, 74), # G
    (4.875, 76), # Bb
    (5.25, 62), # D
    (5.25, 65), # F
    (5.25, 67), # A
    (5.25, 69), # C
    (5.625, 67), # A
    (5.625, 71), # Eb
    (5.625, 74), # G
    (5.625, 76), # Bb
    (6.0, 62), # D
    (6.0, 65), # F
    (6.0, 67), # A
    (6.0, 69), # C
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: D - F - A - C (Dm7)
# Play on beat 2 of bar 2: 1.875
note = pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=1.875 + 0.125)
sax.notes.append(note)

note = pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=1.875 + 0.125)
sax.notes.append(note)

note = pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=1.875 + 0.125)
sax.notes.append(note)

note = pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=1.875 + 0.125)
sax.notes.append(note)

# Let it hang for a beat
note = pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.0 + 0.125)
sax.notes.append(note)

# Return to finish the motif on beat 2 of bar 4: 5.125
note = pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.125 + 0.125)
sax.notes.append(note)

note = pretty_midi.Note(velocity=110, pitch=65, start=5.125, end=5.125 + 0.125)
sax.notes.append(note)

note = pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.125 + 0.125)
sax.notes.append(note)

note = pretty_midi.Note(velocity=110, pitch=69, start=5.125, end=5.125 + 0.125)
sax.notes.append(note)

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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

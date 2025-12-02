
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
        # Hi-hats on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 46),  # F
    (1.875, 45),  # Eb
    (2.25, 47),  # Gb
    (2.625, 48),  # G
    (2.625, 49),  # Ab
    (3.0, 48),  # G
    (3.375, 47),  # Gb
    (3.75, 45),  # Eb
    (3.75, 46),  # F
    (4.125, 47),  # Gb
    (4.5, 48),  # G
    (4.875, 49),  # Ab
    (4.875, 50),  # Bb
    (5.25, 49),  # Ab
    (5.625, 50),  # Bb
    (6.0, 48)  # G
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 50), (1.5, 57), (1.5, 59), (1.5, 60),  # F7
    (1.875, 50), (1.875, 57), (1.875, 59), (1.875, 60),  # F7
    (2.25, 50), (2.25, 57), (2.25, 59), (2.25, 60),  # F7
    (2.625, 50), (2.625, 57), (2.625, 59), (2.625, 60),  # F7
    (3.0, 50), (3.0, 57), (3.0, 59), (3.0, 60),  # F7
    (3.375, 50), (3.375, 57), (3.375, 59), (3.375, 60),  # F7
    (3.75, 50), (3.75, 57), (3.75, 59), (3.75, 60),  # F7
    (4.125, 50), (4.125, 57), (4.125, 59), (4.125, 60),  # F7
    (4.5, 50), (4.5, 57), (4.5, 59), (4.5, 60),  # F7
    (4.875, 50), (4.875, 57), (4.875, 59), (4.875, 60),  # F7
    (5.25, 50), (5.25, 57), (5.25, 59), (5.25, 60),  # F7
    (5.625, 50), (5.625, 57), (5.625, 59), (5.625, 60),  # F7
    (6.0, 50), (6.0, 57), (6.0, 59), (6.0, 60)  # F7
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Melody - motif that sings, short, leaves it hanging, then returns
sax_notes = [
    (1.5, 62),  # A
    (1.875, 65),  # C
    (2.25, 69),  # E
    (2.625, 67),  # D
    (3.0, 62),  # A
    (3.375, 65),  # C
    (3.75, 69),  # E
    (4.125, 67),  # D
    (4.5, 62),  # A
    (4.875, 65),  # C
    (5.25, 69),  # E
    (5.625, 67),  # D
    (6.0, 62),  # A
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hats on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

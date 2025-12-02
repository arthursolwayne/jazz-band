
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

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 46, 100),  # F
    (1.875, 47, 100),  # Gb
    (2.25, 48, 100),  # G
    (2.625, 45, 100),  # E
    (3.0, 46, 100),  # F
    (3.375, 47, 100),  # Gb
    (3.75, 48, 100),  # G
    (4.125, 45, 100),  # E
    (4.5, 50, 100),  # A
    (4.875, 49, 100),  # Ab
    (5.25, 50, 100),  # A
    (5.625, 48, 100),  # G
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (2.25, 50, 100),  # A7
    (2.25, 43, 100),  # C
    (2.25, 47, 100),  # G
    (2.25, 46, 100),  # F
    (3.75, 50, 100),  # A7
    (3.75, 43, 100),  # C
    (3.75, 47, 100),  # G
    (3.75, 46, 100),  # F
    (5.25, 50, 100),  # A7
    (5.25, 43, 100),  # C
    (5.25, 47, 100),  # G
    (5.25, 46, 100),  # F
]
for time, pitch, vel in piano_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Sax: Short motif, melody
sax_notes = [
    (1.5, 62, 100),  # D
    (1.75, 65, 100),  # F
    (2.25, 67, 100),  # G
    (2.5, 65, 100),  # F
    (2.75, 62, 100),  # D
    (3.0, 67, 100),  # G
    (3.25, 69, 100),  # A
    (3.5, 67, 100),  # G
    (3.75, 65, 100),  # F
    (4.0, 62, 100),  # D
    (4.5, 67, 100),  # G
    (4.75, 69, 100),  # A
    (5.0, 67, 100),  # G
    (5.25, 65, 100),  # F
    (5.5, 62, 100),  # D
    (5.75, 65, 100),  # F
]
for time, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

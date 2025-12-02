
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
# Bass: walking line with chromatic approaches
bass_notes = [
    (1.5, 50, 100),    # D
    (1.875, 51, 100),  # Eb
    (2.25, 48, 100),   # C
    (2.625, 50, 100),  # D
    (2.625, 51, 100),  # Eb (chromatic)
    (3.0, 52, 100),    # E
    (3.375, 50, 100),  # D
    (3.75, 48, 100),   # C
    (4.125, 47, 100),  # Bb
    (4.5, 50, 100),    # D
    (4.875, 51, 100),  # Eb
    (5.25, 48, 100),   # C
    (5.625, 50, 100),  # D
    (6.0, 52, 100)     # E
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    (1.5, 62, 100),    # D7 (D, F#, A, C)
    (1.875, 62, 100),
    (2.25, 62, 100),
    (2.625, 62, 100),
    (3.0, 62, 100),    # D7 on beat 2
    (3.375, 62, 100),
    (3.75, 62, 100),
    (4.125, 62, 100),
    (4.5, 62, 100),    # D7 on beat 4
    (4.875, 62, 100),
    (5.25, 62, 100),
    (5.625, 62, 100),
    (6.0, 62, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif in Dm, short and singable
sax_notes = [
    (1.5, 62, 100),    # D
    (1.75, 65, 100),   # F
    (2.0, 62, 100),    # D
    (2.25, 60, 100),   # Bb
    (2.625, 62, 100),  # D (return)
    (2.875, 67, 100),  # A (extension)
    (3.125, 62, 100),  # D
    (3.375, 65, 100),  # F
    (3.625, 62, 100),  # D
    (3.875, 60, 100),  # Bb
    (4.25, 62, 100),   # D (return)
    (4.5, 67, 100),    # A (extension)
    (4.75, 62, 100),   # D
    (5.0, 65, 100),    # F
    (5.25, 62, 100),   # D
    (5.5, 60, 100)     # Bb
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

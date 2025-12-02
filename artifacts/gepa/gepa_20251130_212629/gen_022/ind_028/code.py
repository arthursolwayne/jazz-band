
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),   # D4
    (1.875, 63), # Eb4
    (2.25, 64),  # E4
    (2.625, 65), # F4
    (2.875, 65), # F4
    (3.25, 64),  # E4
    (3.625, 63), # Eb4
    (4.0, 62),   # D4
    (4.375, 60), # C4
    (4.75, 61),  # Db4
    (5.125, 62), # D4
    (5.5, 63),   # Eb4
    (5.875, 64), # E4
    (6.25, 65),  # F4
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bars 2-4, comp on beats 2 and 4
chords = [
    (1.875, [62, 67, 69, 72]),  # D7
    (2.625, [62, 67, 69, 72]),  # D7
    (3.625, [62, 67, 69, 72]),  # D7
    (4.375, [62, 67, 69, 72]),  # D7
    (5.125, [62, 67, 69, 72]),  # D7
    (5.875, [62, 67, 69, 72]),  # D7
]

for time, pitches in chords:
    for pitch in pitches:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Sax: your moment. One short motif, make it sing.
# Start it, leave it hanging, come back and finish it.

# Bar 2 (1.5s - 1.875s): motif
note = pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625)  # F4
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=1.625, end=1.75)  # A4
sax.notes.append(note)

# Bar 3 (2.25s - 2.625s): repeat
note = pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.375)  # F4
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=2.375, end=2.5)  # A4
sax.notes.append(note)

# Bar 4 (5.5s - 5.875s): finish it
note = pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.625)  # F4
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=5.75)  # A4
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=5.875)  # E4
sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')

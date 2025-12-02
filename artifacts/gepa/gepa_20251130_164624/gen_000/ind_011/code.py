
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
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),   # D
    (1.875, 63), # Eb
    (2.25, 64),  # E
    (2.625, 65), # F
    (2.875, 63), # Eb
    (3.25, 62),  # D
    (3.625, 60), # C
    (4.0, 62),   # D
    (4.375, 63), # Eb
    (4.75, 64),  # E
    (5.125, 65), # F
    (5.5, 63),   # Eb
    (5.875, 62), # D
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 67), # B
    (1.875, 64), # G
    (1.875, 62), # E
    (1.875, 59), # C
    # Bar 3
    (3.25, 67),  # B
    (3.25, 64),  # G
    (3.25, 62),  # E
    (3.25, 59),  # C
    # Bar 4
    (4.75, 71),  # F#
    (4.75, 68),  # D
    (4.75, 66),  # B
    (4.75, 63),  # G
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65), # E
    (1.6875, 67), # G
    (1.875, 62), # D
    (2.25, 65), # E
    (2.4375, 67), # G
    (2.625, 62), # D
    (3.0, 65), # E
    (3.1875, 67), # G
    (3.375, 62), # D
    (3.75, 65), # E
    (3.9375, 67), # G
    (4.125, 62), # D
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=70, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

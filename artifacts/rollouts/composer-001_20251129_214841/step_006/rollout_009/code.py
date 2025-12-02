
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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

# Bass line: walking line, chromatic approaches, never the same note twice
# C7 chord: C E G B
bass_notes = [
    (1.5, 60),     # C
    (1.875, 61),   # D
    (2.25, 62),    # D#
    (2.625, 64),   # F
    (2.875, 65),   # F#
    (3.25, 67),    # G
    (3.625, 69),   # A
    (4.0, 71),     # B
    (4.375, 72),   # C
    (4.75, 73),    # C#
    (5.125, 74),   # D
    (5.5, 76),     # E
    (5.875, 77),   # F
    (6.25, 79),    # G
    (6.625, 81),   # A
    (7.0, 83),     # B
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# C7 = C E G Bb
piano_notes = [
    # Bar 2
    (1.5, 60),     # C
    (1.5, 64),     # E
    (1.5, 67),     # G
    (1.5, 70),     # Bb
    # Bar 3
    (2.25, 60),    # C
    (2.25, 64),    # E
    (2.25, 67),    # G
    (2.25, 70),    # Bb
    # Bar 4
    (3.0, 60),     # C
    (3.0, 64),     # E
    (3.0, 67),     # G
    (3.0, 70),     # Bb
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C E Bb D
sax_notes = [
    (1.5, 60),     # C
    (1.75, 64),    # E
    (2.0, 70),     # Bb
    (2.25, 62),    # D
    (3.0, 60),     # C
    (3.25, 64),    # E
    (3.5, 70),     # Bb
    (3.75, 62),    # D
    (4.5, 60),     # C
    (4.75, 64),    # E
    (5.0, 70),     # Bb
    (5.25, 62),    # D
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

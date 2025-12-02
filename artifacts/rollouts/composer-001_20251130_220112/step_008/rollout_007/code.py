
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
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 48),  # F
    (1.875, 49), # Gb
    (2.25, 50),  # G
    (2.625, 51), # Ab
    (3.0, 52),   # A
    (3.375, 53), # Bb
    (3.75, 54),  # B
    (4.125, 55), # C
    (4.5, 56),   # C#
    (4.875, 57), # D
    (5.25, 58),  # Eb
    (5.625, 59), # E
    (6.0, 60)    # F
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    (2.25, 50),  # F7 - F, A, C, Eb
    (2.25, 60),  # F7 - F, A, C, Eb
    (2.25, 64),  # F7 - F, A, C, Eb
    (2.25, 67),  # F7 - F, A, C, Eb
    (3.75, 50),  # F7
    (3.75, 60),
    (3.75, 64),
    (3.75, 67),
    (5.25, 50),  # F7
    (5.25, 60),
    (5.25, 64),
    (5.25, 67)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (F7 arpeggio with a twist)
sax_notes = [
    (1.5, 75),  # F
    (1.875, 78), # Ab
    (2.25, 77),  # Bb
    (2.625, 75), # F
    (3.0, 75),   # F (rest)
    (3.375, 75), # F
    (3.75, 78),  # Ab
    (4.125, 77), # Bb
    (4.5, 75),   # F
    (4.875, 75), # F
    (5.25, 78),  # Ab
    (5.625, 77), # Bb
    (6.0, 75)    # F
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums continue in bars 2-4
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
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

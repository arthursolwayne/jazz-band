
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
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62),  # D
    (1.875, 63),  # Eb
    (2.25, 64),  # E
    (2.625, 62),  # D
    # Bar 3 (3.0 - 4.5s)
    (3.0, 60),  # C
    (3.375, 61),  # C#
    (3.75, 62),  # D
    (4.125, 60),  # C
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62),  # D
    (4.875, 63),  # Eb
    (5.25, 64),  # E
    (5.625, 62),  # D
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 62),  # D7 (F, A, C, D)
    (1.75, 67),  # A
    (1.75, 60),  # F
    (1.75, 64),  # C
    (2.25, 62),  # D7
    (2.25, 67),  # A
    (2.25, 60),  # F
    (2.25, 64),  # C
    # Bar 3 (3.0 - 4.5s)
    (3.25, 62),  # D7
    (3.25, 67),  # A
    (3.25, 60),  # F
    (3.25, 64),  # C
    (3.75, 62),  # D7
    (3.75, 67),  # A
    (3.75, 60),  # F
    (3.75, 64),  # C
    # Bar 4 (4.5 - 6.0s)
    (4.75, 62),  # D7
    (4.75, 67),  # A
    (4.75, 60),  # F
    (4.75, 64),  # C
    (5.25, 62),  # D7
    (5.25, 67),  # A
    (5.25, 60),  # F
    (5.25, 64),  # C
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: continue same pattern
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Sax: Motif in Dm, short, singable, leaves it hanging
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62),  # D
    (1.625, 64),  # E
    (1.75, 62),  # D
    (1.875, 60),  # C
    (2.0, 62),  # D
    (2.125, 64),  # E
    (2.25, 62),  # D
    (2.375, 60),  # C
    (2.5, 62),  # D
    (2.625, 64),  # E
    (2.75, 62),  # D
    (2.875, 60),  # C
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62),  # D
    (3.125, 64),  # E
    (3.25, 62),  # D
    (3.375, 60),  # C
    (3.5, 62),  # D
    (3.625, 64),  # E
    (3.75, 62),  # D
    (3.875, 60),  # C
    (4.0, 62),  # D
    (4.125, 64),  # E
    (4.25, 62),  # D
    (4.375, 60),  # C
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62),  # D
    (4.625, 64),  # E
    (4.75, 62),  # D
    (4.875, 60),  # C
    (5.0, 62),  # D
    (5.125, 64),  # E
    (5.25, 62),  # D
    (5.375, 60),  # C
    (5.5, 62),  # D
    (5.625, 64),  # E
    (5.75, 62),  # D
    (5.875, 60),  # C
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

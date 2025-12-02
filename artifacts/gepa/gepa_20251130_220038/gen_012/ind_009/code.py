
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
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 62), (1.875, 60), (2.25, 61), (2.625, 64),
    # Bar 3
    (3.0, 62), (3.375, 60), (3.75, 61), (4.125, 64),
    # Bar 4
    (4.5, 62), (4.875, 60), (5.25, 61), (5.625, 64)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64), (1.875, 67), (1.875, 71), (1.875, 72),
    (2.625, 64), (2.625, 67), (2.625, 71), (2.625, 72),
    # Bar 3
    (3.375, 64), (3.375, 67), (3.375, 71), (3.375, 72),
    (4.125, 64), (4.125, 67), (4.125, 71), (4.125, 72),
    # Bar 4
    (4.875, 64), (4.875, 67), (4.875, 71), (4.875, 72),
    (5.625, 64), (5.625, 67), (5.625, 71), (5.625, 72)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax (Dante): Motif in Dm
# Dm7: D, F, A, C
# Motif: D -> F -> A -> C, then rest and resolve on the next bar
sax_notes = [
    (1.5, 62), (1.5 + 0.375, 65), (1.5 + 0.75, 67), (1.5 + 1.125, 60),
    (2.625, 62), (2.625 + 0.375, 65), (2.625 + 0.75, 67), (2.625 + 1.125, 60)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

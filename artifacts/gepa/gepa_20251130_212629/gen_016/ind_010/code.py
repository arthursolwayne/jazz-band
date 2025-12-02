
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 50, 100), (1.875, 49, 100), (2.25, 51, 100), (2.625, 52, 100),
    # Bar 3
    (3.0, 53, 100), (3.375, 51, 100), (3.75, 49, 100), (4.125, 50, 100),
    # Bar 4
    (4.5, 51, 100), (4.875, 53, 100), (5.25, 54, 100), (5.625, 52, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on 2, F7 on 4
    (2.25, 72, 100), (2.25, 74, 100), (2.25, 76, 100), (2.25, 79, 100),
    (3.0, 72, 100), (3.0, 74, 100), (3.0, 77, 100), (3.0, 79, 100),
    # Bar 3: C7 on 2, F7 on 4
    (3.75, 72, 100), (3.75, 74, 100), (3.75, 76, 100), (3.75, 79, 100),
    (4.5, 72, 100), (4.5, 74, 100), (4.5, 77, 100), (4.5, 79, 100),
    # Bar 4: C7 on 2, F7 on 4
    (5.25, 72, 100), (5.25, 74, 100), (5.25, 76, 100), (5.25, 79, 100),
    (6.0, 72, 100), (6.0, 74, 100), (6.0, 77, 100), (6.0, 79, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: continue pattern, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65, 110, 0.5),  # F
    (1.75, 67, 110, 0.25), # A
    (2.0, 65, 110, 0.25),  # F
    (2.25, 60, 110, 0.25), # D
    (2.5, 62, 110, 0.25),  # E
    (2.75, 65, 110, 0.25), # F
    (3.0, 67, 110, 0.5),   # A
    (3.5, 65, 110, 0.25),  # F
    (3.75, 67, 110, 0.25), # A
    (4.0, 65, 110, 0.25),  # F
    (4.25, 60, 110, 0.25), # D
    (4.5, 62, 110, 0.25),  # E
    (4.75, 65, 110, 0.25), # F
    (5.0, 67, 110, 0.5)    # A
]
for time, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

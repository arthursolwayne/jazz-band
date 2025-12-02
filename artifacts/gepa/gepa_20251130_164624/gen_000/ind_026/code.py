
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
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 47), (1.875, 48), (2.25, 49), (2.625, 50),
    # Bar 3
    (3.0, 50), (3.375, 49), (3.75, 48), (4.125, 47),
    # Bar 4
    (4.5, 47), (4.875, 48), (5.25, 49), (5.625, 50)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62), (1.875, 67), (2.25, 67), (2.625, 62), (2.625, 67),
    # Bar 3
    (3.375, 62), (3.375, 67), (3.75, 67), (4.125, 62), (4.125, 67),
    # Bar 4
    (4.875, 62), (4.875, 67), (5.25, 67), (5.625, 62), (5.625, 67)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing
# Start with a simple melody that leaves a question
sax_notes = [
    # Bar 2
    (1.5, 65), (1.875, 67), (2.25, 64), (2.625, 62),
    # Bar 3
    (3.0, 62), (3.375, 64), (3.75, 67), (4.125, 65),
    # Bar 4
    (4.5, 65), (4.875, 67), (5.25, 64), (5.625, 62)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 4):
    start_time = bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

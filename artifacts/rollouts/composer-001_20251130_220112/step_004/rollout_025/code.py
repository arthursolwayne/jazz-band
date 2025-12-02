
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
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 48), (1.875, 49), (2.25, 50), (2.625, 51),
    # Bar 3
    (3.0, 51), (3.375, 50), (3.75, 49), (4.125, 48),
    # Bar 4
    (4.5, 48), (4.875, 49), (5.25, 50), (5.625, 51)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62), (1.875, 67), (1.875, 71), (1.875, 72),  # F7 on 2
    # Bar 3
    (3.375, 62), (3.375, 67), (3.375, 71), (3.375, 72),  # F7 on 2
    # Bar 4
    (4.875, 62), (4.875, 67), (4.875, 71), (4.875, 72)   # F7 on 2
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 62), (1.5, 64), (1.625, 65), (1.75, 62),
    (2.25, 62), (2.375, 64), (2.5, 65), (2.625, 62),
    (3.0, 62), (3.125, 64), (3.25, 65), (3.375, 62),
    (3.75, 62), (3.875, 64), (4.0, 65), (4.125, 62),
    (4.5, 62), (4.625, 64), (4.75, 65), (4.875, 62),
    (5.25, 62), (5.375, 64), (5.5, 65), (5.625, 62)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: continue for bars 2-4
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

midi.write("fm_intro.mid")

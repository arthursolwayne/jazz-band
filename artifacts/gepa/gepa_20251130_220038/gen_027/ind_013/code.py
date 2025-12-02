
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
    for i in range(4):
        time = bar * 1.5 + i * 0.375
        if i == 0 or i == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if i == 1 or i == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 44), (1.75, 45), (2.0, 46), (2.25, 47),
    (2.5, 47), (2.75, 46), (3.0, 45), (3.25, 44),
    (3.5, 42), (3.75, 43), (4.0, 44), (4.25, 45),
    (4.5, 45), (4.75, 44), (5.0, 43), (5.25, 42)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 60), (2.0, 64), (2.0, 67), (2.0, 70),
    (3.0, 60), (3.0, 64), (3.0, 67), (3.0, 70),
    (4.0, 60), (4.0, 64), (4.0, 67), (4.0, 70)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 62), (1.625, 64), (1.75, 62), (2.0, 60),
    (2.5, 62), (2.625, 64), (2.75, 62), (3.0, 60),
    (3.5, 62), (3.625, 64), (3.75, 62), (4.0, 60)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Little Ray on drums (bar 2-4)
for bar in range(2, 4):
    for i in range(4):
        time = bar * 1.5 + i * 0.375
        if i == 0 or i == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if i == 1 or i == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

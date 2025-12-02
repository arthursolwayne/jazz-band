
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
for i in range(0, 160):
    time = i / 160
    if time < 1.5:
        if time % 1.0 < 0.1:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if time % 1.0 < 0.3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        if time % 0.5 < 0.1:
            note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 42), (1.75, 43), (2.0, 41), (2.25, 40),
    (2.5, 42), (2.75, 43), (3.0, 41), (3.25, 40),
    (3.5, 42), (3.75, 43), (4.0, 41), (4.25, 40),
    (4.5, 42), (4.75, 43), (5.0, 41), (5.25, 40)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 71),
    (2.0, 60), (2.0, 64), (2.0, 67), (2.0, 71),
    (3.0, 60), (3.0, 64), (3.0, 67), (3.0, 71),
    (4.0, 60), (4.0, 64), (4.0, 67), (4.0, 71)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 60), (1.55, 62), (1.6, 64), (1.65, 62), (1.7, 60),  # first phrase
    (2.0, 64), (2.05, 66), (2.1, 68), (2.15, 66), (2.2, 64),  # second phrase
    (2.5, 60), (2.55, 62), (2.6, 64), (2.65, 62), (2.7, 60)   # resolution
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.05)
    sax.notes.append(note)

# Drums continue in bars 2-4
for i in range(0, 160):
    time = (i / 160) + 1.5
    if time < 6.0:
        if time % 1.0 < 0.1:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if time % 1.0 < 0.3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        if time % 0.5 < 0.1:
            note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

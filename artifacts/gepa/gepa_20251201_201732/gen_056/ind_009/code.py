
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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, Fm7 -> Bbm7 -> Ebm7 -> Abm7
bass_notes = [
    (1.5, 43), (1.75, 42), (2.0, 43), (2.25, 41),
    (2.5, 43), (2.75, 42), (3.0, 43), (3.25, 41)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Open voicings, Fm7 -> Bbm7 -> Ebm7 -> Abm7
piano_notes = [
    # Bar 2
    (1.5, 45), (1.5, 41), (1.5, 38), (1.5, 35),  # Fm7
    # Bar 3
    (2.5, 48), (2.5, 44), (2.5, 41), (2.5, 38),  # Bbm7
    # Bar 4
    (3.5, 50), (3.5, 46), (3.5, 43), (3.5, 40),  # Ebm7
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note_obj)

# Sax: Melody starts on beat 1, plays a short motif, leaves it hanging
sax_notes = [
    (1.5, 50), (1.75, 48), (2.0, 50), (2.25, 48),
    (2.5, 50), (2.75, 48), (3.0, 50), (3.25, 48)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, Abm7 -> Dbm7 -> Gbm7 -> Bbm7
bass_notes = [
    (3.0, 41), (3.25, 40), (3.5, 41), (3.75, 39),
    (4.0, 41), (4.25, 40), (4.5, 41), (4.75, 39)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Open voicings, Abm7 -> Dbm7 -> Gbm7 -> Bbm7
piano_notes = [
    # Bar 3
    (3.5, 50), (3.5, 46), (3.5, 43), (3.5, 40),  # Abm7
    # Bar 4
    (4.5, 53), (4.5, 49), (4.5, 46), (4.5, 43),  # Dbm7
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note_obj)

# Sax: Continuation of the motif, resolves on beat 4
sax_notes = [
    (3.0, 50), (3.25, 48), (3.5, 50), (3.75, 48),
    (4.0, 50), (4.25, 48), (4.5, 50), (4.75, 48)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, Bbm7 -> Ebm7 -> Abm7 -> Dm7
bass_notes = [
    (4.5, 38), (4.75, 37), (5.0, 38), (5.25, 36),
    (5.5, 38), (5.75, 37), (6.0, 38), (6.25, 36)
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: Open voicings, Bbm7 -> Ebm7 -> Abm7 -> Dm7
piano_notes = [
    # Bar 4
    (4.5, 48), (4.5, 44), (4.5, 41), (4.5, 38),  # Bbm7
    (5.5, 50), (5.5, 46), (5.5, 43), (5.5, 40),  # Ebm7
    (6.5, 52), (6.5, 48), (6.5, 45), (6.5, 42),  # Abm7
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(note_obj)

# Sax: Resolves motif and ends on a strong note
sax_notes = [
    (4.5, 50), (4.75, 48), (5.0, 50), (5.25, 48),
    (5.5, 50), (5.75, 48), (6.0, 50), (6.25, 48)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 36), (7.125, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

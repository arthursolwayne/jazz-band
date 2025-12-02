
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42),
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# BAR 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    (1.5, 62), (1.875, 59), (2.25, 60), (2.625, 58),  # Fm7 -> Bb -> C -> Ab
    (3.0, 62), (3.375, 59), (3.75, 60), (4.125, 58),  # Fm7 -> Bb -> C -> Ab
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 (1.875)
    (1.875, 64), (1.875, 67), (1.875, 71), (1.875, 76),
    # Bb7 (3.375)
    (3.375, 67), (3.375, 71), (3.375, 76), (3.375, 81),
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Motif (1.5s)
sax_notes = [
    # Start of motif: F (64), Ab (68), C (72), Bb (71)
    (1.5, 64), (1.5, 68), (1.5, 72), (1.5, 71),
    # End of motif: F (64) again but delayed
    (3.0, 64),
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# BAR 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    (3.0, 62), (3.375, 59), (3.75, 60), (4.125, 58),  # Fm7 -> Bb -> C -> Ab
    (4.5, 62), (4.875, 59), (5.25, 60), (5.625, 58),  # Fm7 -> Bb -> C -> Ab
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 (3.375)
    (3.375, 64), (3.375, 67), (3.375, 71), (3.375, 76),
    # Bb7 (4.875)
    (4.875, 67), (4.875, 71), (4.875, 76), (4.875, 81),
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Continue motif (3.0s)
sax_notes = [
    # Continue motif: Ab (68), C (72), Bb (71)
    (3.0, 68), (3.0, 72), (3.0, 71),
    # End of motif: F (64)
    (4.5, 64),
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# BAR 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    (4.5, 62), (4.875, 59), (5.25, 60), (5.625, 58),  # Fm7 -> Bb -> C -> Ab
    (6.0, 62), (6.375, 59), (6.75, 60), (7.125, 58),  # Fm7 -> Bb -> C -> Ab
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 (4.875)
    (4.875, 64), (4.875, 67), (4.875, 71), (4.875, 76),
    # Bb7 (6.375)
    (6.375, 67), (6.375, 71), (6.375, 76), (6.375, 81),
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Sax: Finish motif (4.5s)
sax_notes = [
    # Continue motif: Ab (68), C (72), Bb (71)
    (4.5, 68), (4.5, 72), (4.5, 71),
    # End of motif: F (64)
    (6.0, 64),
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42), (3.0, 38),
    (1.5, 42), (1.875, 42), (2.25, 42), (2.625, 42), (3.0, 42),
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38),
    (3.0, 42), (3.375, 42), (3.75, 42), (4.125, 42), (4.5, 42),
    # Bar 4
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42), (6.0, 38),
    (4.5, 42), (4.875, 42), (5.25, 42), (5.625, 42), (6.0, 42),
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

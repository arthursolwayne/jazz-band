
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38), (1.875, 42),
    (2.25, 36), (2.625, 42), (3.0, 38), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)

# Bass - walking line in Fm (F, Gb, Ab, Bb, Bb, Ab, Gb, F)
bass_notes = [
    (1.5, 45), (1.875, 44), (2.25, 42), (2.625, 41),
    (2.625, 41), (3.0, 42), (3.375, 44), (3.75, 45)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
# Fm7 (F, Ab, Bb, Db) on 2nd beat (2.25s)
# Ab7 (Ab, Bb, Db, Eb) on 4th beat (3.75s)
piano_notes = [
    # Fm7 (2.25s)
    (2.25, 45), (2.25, 43), (2.25, 41), (2.25, 40),
    # Ab7 (3.75s)
    (3.75, 43), (3.75, 41), (3.75, 40), (3.75, 42)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Saxophone - simple melody (F, Gb, Ab, Bb) starting at 1.5s
# Play F (1.5s), Gb (1.875s), Ab (2.25s), Bb (2.625s)
sax_notes = [
    (1.5, 45), (1.875, 44), (2.25, 42), (2.625, 41)
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)

# Bass - continue walking line
bass_notes = [
    (3.0, 45), (3.375, 44), (3.75, 42), (4.125, 41),
    (4.125, 41), (4.5, 42), (4.875, 44), (5.25, 45)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
# Fm7 (F, Ab, Bb, Db) on 2nd beat (3.375s)
# Ab7 (Ab, Bb, Db, Eb) on 4th beat (4.875s)
piano_notes = [
    # Fm7 (3.375s)
    (3.375, 45), (3.375, 43), (3.375, 41), (3.375, 40),
    # Ab7 (4.875s)
    (4.875, 43), (4.875, 41), (4.875, 40), (4.875, 42)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Saxophone - repeat the motif at a higher register
# F (3.0s), Gb (3.375s), Ab (3.75s), Bb (4.125s)
sax_notes = [
    (3.0, 55), (3.375, 54), (3.75, 52), (4.125, 51)
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bar 4: Full ensemble (4.5 - 6.0s)

# Bass - continue walking line
bass_notes = [
    (4.5, 45), (4.875, 44), (5.25, 42), (5.625, 41),
    (5.625, 41), (6.0, 42), (6.375, 44), (6.75, 45)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
# Fm7 (F, Ab, Bb, Db) on 2nd beat (4.875s)
# Ab7 (Ab, Bb, Db, Eb) on 4th beat (6.375s)
piano_notes = [
    # Fm7 (4.875s)
    (4.875, 45), (4.875, 43), (4.875, 41), (4.875, 40),
    # Ab7 (6.375s)
    (6.375, 43), (6.375, 41), (6.375, 40), (6.375, 42)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Saxophone - finish the motif
# F (4.5s), Gb (4.875s), Ab (5.25s), Bb (5.625s)
sax_notes = [
    (4.5, 55), (4.875, 54), (5.25, 52), (5.625, 51)
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Drums - continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42), (4.5, 38), (4.875, 42),
    (5.25, 36), (5.625, 42), (6.0, 38), (6.375, 42), (6.75, 36), (7.125, 42)
]
for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

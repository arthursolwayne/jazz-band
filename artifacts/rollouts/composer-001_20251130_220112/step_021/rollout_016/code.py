
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875)
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm motif - F, Ab, Bb, D, Eb, F (motif starts here)
sax_notes = [
    (84, 1.5, 0.375), (81, 1.875, 0.375), (82, 2.25, 0.375),
    (80, 2.625, 0.375), (79, 3.0, 0.375), (84, 3.375, 0.375)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (53, 1.5, 0.375), (52, 1.875, 0.375), (51, 2.25, 0.375),
    (52, 2.625, 0.375), (50, 3.0, 0.375), (51, 3.375, 0.375),
    (52, 3.75, 0.375), (50, 4.125, 0.375)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, F7, Bb7
piano_notes = [
    # F7: F, A, C, Eb
    (53, 1.875, 0.375), (58, 1.875, 0.375), (55, 1.875, 0.375), (52, 1.875, 0.375),
    # Bb7: Bb, D, F, Ab
    (50, 3.0, 0.375), (55, 3.0, 0.375), (53, 3.0, 0.375), (51, 3.0, 0.375)
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repetition of the motif, starting at 3.0s
sax_notes = [
    (84, 3.0, 0.375), (81, 3.375, 0.375), (82, 3.75, 0.375),
    (80, 4.125, 0.375), (79, 4.5, 0.375), (84, 4.875, 0.375)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (53, 3.0, 0.375), (52, 3.375, 0.375), (51, 3.75, 0.375),
    (52, 4.125, 0.375), (50, 4.5, 0.375), (51, 4.875, 0.375),
    (52, 5.25, 0.375), (50, 5.625, 0.375)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, F7, Bb7
piano_notes = [
    # F7: F, A, C, Eb
    (53, 3.375, 0.375), (58, 3.375, 0.375), (55, 3.375, 0.375), (52, 3.375, 0.375),
    # Bb7: Bb, D, F, Ab
    (50, 4.5, 0.375), (55, 4.5, 0.375), (53, 4.5, 0.375), (51, 4.5, 0.375)
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif and resolve on Eb
sax_notes = [
    (84, 4.5, 0.375), (81, 4.875, 0.375), (82, 5.25, 0.375),
    (80, 5.625, 0.375), (79, 6.0, 0.375)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    (53, 4.5, 0.375), (52, 4.875, 0.375), (51, 5.25, 0.375),
    (52, 5.625, 0.375), (50, 6.0, 0.375)
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, F7, Bb7
piano_notes = [
    # F7: F, A, C, Eb
    (53, 4.875, 0.375), (58, 4.875, 0.375), (55, 4.875, 0.375), (52, 4.875, 0.375),
    # Bb7: Bb, D, F, Ab
    (50, 6.0, 0.375), (55, 6.0, 0.375), (53, 6.0, 0.375), (51, 6.0, 0.375)
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('jazz_intro.mid')

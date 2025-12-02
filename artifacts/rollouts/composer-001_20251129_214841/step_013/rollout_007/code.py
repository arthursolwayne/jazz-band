
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), (61, 1.875, 0.375), (59, 2.25, 0.375), (60, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2 (1.875) and 4 (2.625)
    (60, 1.875, 0.375), (64, 1.875, 0.375), (67, 1.875, 0.375), (71, 1.875, 0.375),
    (60, 2.625, 0.375), (64, 2.625, 0.375), (67, 2.625, 0.375), (71, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Melody - one short motif, start it, leave it hanging
# C (60), E (64), G (67), B (71) - skip the last note, leave it hanging
sax_notes = [
    (60, 1.5, 0.375), (64, 1.875, 0.375), (67, 2.25, 0.375)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    (60, 3.0, 0.375), (61, 3.375, 0.375), (59, 3.75, 0.375), (60, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 3: C7 on beat 2 (3.375) and 4 (4.125)
    (60, 3.375, 0.375), (64, 3.375, 0.375), (67, 3.375, 0.375), (71, 3.375, 0.375),
    (60, 4.125, 0.375), (64, 4.125, 0.375), (67, 4.125, 0.375), (71, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Melody - return to finish the motif
sax_notes = [
    (71, 3.0, 0.375), (60, 3.375, 0.375), (64, 3.75, 0.375), (67, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in C, chromatic approaches
bass_notes = [
    (60, 4.5, 0.375), (61, 4.875, 0.375), (59, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 4: C7 on beat 2 (4.875) and 4 (5.625)
    (60, 4.875, 0.375), (64, 4.875, 0.375), (67, 4.875, 0.375), (71, 4.875, 0.375),
    (60, 5.625, 0.375), (64, 5.625, 0.375), (67, 5.625, 0.375), (71, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax: Melody - leave it open, no resolution
sax_notes = [
    (71, 4.5, 0.375), (60, 4.875, 0.375), (64, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

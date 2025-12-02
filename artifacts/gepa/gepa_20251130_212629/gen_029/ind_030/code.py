
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F minor with chromatic approaches
bass_notes = [
    (53, 1.5, 0.375), (51, 1.875, 0.375),
    (52, 2.25, 0.375), (55, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comping in F minor
piano_notes = [
    (59, 1.5, 0.25), (60, 1.5, 0.25), (62, 1.5, 0.25), (64, 1.5, 0.25),  # F7
    (56, 2.25, 0.25), (57, 2.25, 0.25), (59, 2.25, 0.25), (61, 2.25, 0.25)  # D7
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax: Motif starting on F, short and leaving it hanging
sax_notes = [
    (58, 1.5, 0.25), (60, 1.75, 0.25), (57, 2.0, 0.25)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F minor with chromatic approaches
bass_notes = [
    (55, 3.0, 0.375), (53, 3.375, 0.375),
    (54, 3.75, 0.375), (57, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comping in F minor
piano_notes = [
    (59, 3.0, 0.25), (60, 3.0, 0.25), (62, 3.0, 0.25), (64, 3.0, 0.25),  # F7
    (56, 3.75, 0.25), (57, 3.75, 0.25), (59, 3.75, 0.25), (61, 3.75, 0.25)  # D7
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (42, 3.0, 0.125),
    (38, 3.375, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (42, 3.75, 0.125),
    (38, 4.125, 0.375), (42, 4.125, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: Continue motif but leave it hanging
sax_notes = [
    (61, 3.0, 0.25), (63, 3.25, 0.25), (60, 3.5, 0.25)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F minor with chromatic approaches
bass_notes = [
    (57, 4.5, 0.375), (55, 4.875, 0.375),
    (56, 5.25, 0.375), (59, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comping in F minor
piano_notes = [
    (59, 4.5, 0.25), (60, 4.5, 0.25), (62, 4.5, 0.25), (64, 4.5, 0.25),  # F7
    (56, 5.25, 0.25), (57, 5.25, 0.25), (59, 5.25, 0.25), (61, 5.25, 0.25)  # D7
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (42, 4.5, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125),
    (36, 5.25, 0.375), (42, 5.25, 0.125),
    (38, 5.625, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax: Complete the motif with a question at the end
sax_notes = [
    (63, 4.5, 0.25), (65, 4.75, 0.25), (62, 5.0, 0.25)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")

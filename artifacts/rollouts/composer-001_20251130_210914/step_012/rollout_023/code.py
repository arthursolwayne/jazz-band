
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
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (61, 2.25, 0.375), (60, 2.625, 0.375),
    (62, 3.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, measure 2
    (72, 1.875, 0.375), (76, 1.875, 0.375), (74, 1.875, 0.375), (70, 1.875, 0.375),
    # Bar 2, measure 4
    (72, 2.625, 0.375), (76, 2.625, 0.375), (74, 2.625, 0.375), (70, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - D, F#, B, G (D7 chord arpeggio with syncopation)
sax_notes = [
    (62, 1.5, 0.1875), (66, 1.6875, 0.1875), (67, 1.875, 0.1875), (69, 2.0625, 0.1875)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (60, 3.0, 0.375), (61, 3.375, 0.375), (62, 3.75, 0.375), (63, 4.125, 0.375),
    (60, 4.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, measure 2
    (72, 3.375, 0.375), (76, 3.375, 0.375), (74, 3.375, 0.375), (70, 3.375, 0.375),
    # Bar 3, measure 4
    (72, 4.125, 0.375), (76, 4.125, 0.375), (74, 4.125, 0.375), (70, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue motif
sax_notes = [
    (62, 3.0, 0.1875), (66, 3.1875, 0.1875), (67, 3.375, 0.1875), (69, 3.5625, 0.1875),
    (62, 3.75, 0.1875), (66, 3.9375, 0.1875), (67, 4.125, 0.1875), (69, 4.3125, 0.1875)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (63, 4.5, 0.375), (62, 4.875, 0.375), (61, 5.25, 0.375), (60, 5.625, 0.375),
    (63, 6.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, measure 2
    (72, 4.875, 0.375), (76, 4.875, 0.375), (74, 4.875, 0.375), (70, 4.875, 0.375),
    # Bar 4, measure 4
    (72, 5.625, 0.375), (76, 5.625, 0.375), (74, 5.625, 0.375), (70, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish motif
sax_notes = [
    (62, 4.5, 0.1875), (66, 4.6875, 0.1875), (67, 4.875, 0.1875), (69, 5.0625, 0.1875),
    (62, 5.25, 0.1875), (66, 5.4375, 0.1875), (67, 5.625, 0.1875), (69, 5.8125, 0.1875)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_moment.mid')


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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F (G#) - A - Bb - F (G#)
sax_notes = [
    (66, 1.5, 0.375), (69, 1.875, 0.375), (67, 2.25, 0.375), (66, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: F - G - A - F (walking line)
bass_notes = [
    (53, 1.5, 0.375), (55, 1.875, 0.375), (57, 2.25, 0.375), (53, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# F7 on 2 (1.875), Bb7 on 4 (2.625)
piano_notes_f7 = [(53, 1.875, 0.375), (57, 1.875, 0.375), (60, 1.875, 0.375), (62, 1.875, 0.375)]
piano_notes_bb7 = [(58, 2.625, 0.375), (62, 2.625, 0.375), (65, 2.625, 0.375), (67, 2.625, 0.375)]
for note, start, duration in piano_notes_f7 + piano_notes_bb7:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: F (G#) - Bb - C - F (G#)
sax_notes = [
    (66, 3.0, 0.375), (67, 3.375, 0.375), (69, 3.75, 0.375), (66, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: F - G - A - F (walking line)
bass_notes = [
    (53, 3.0, 0.375), (55, 3.375, 0.375), (57, 3.75, 0.375), (53, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bb7 on 2 (3.375), F7 on 4 (4.125)
piano_notes_bb7 = [(58, 3.375, 0.375), (62, 3.375, 0.375), (65, 3.375, 0.375), (67, 3.375, 0.375)]
piano_notes_f7 = [(53, 4.125, 0.375), (57, 4.125, 0.375), (60, 4.125, 0.375), (62, 4.125, 0.375)]
for note, start, duration in piano_notes_bb7 + piano_notes_f7:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F (G#) - A - Bb - F (G#)
sax_notes = [
    (66, 4.5, 0.375), (69, 4.875, 0.375), (67, 5.25, 0.375), (66, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: F - G - A - F (walking line)
bass_notes = [
    (53, 4.5, 0.375), (55, 4.875, 0.375), (57, 5.25, 0.375), (53, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# F7 on 2 (4.875), Bb7 on 4 (5.625)
piano_notes_f7 = [(53, 4.875, 0.375), (57, 4.875, 0.375), (60, 4.875, 0.375), (62, 4.875, 0.375)]
piano_notes_bb7 = [(58, 5.625, 0.375), (62, 5.625, 0.375), (65, 5.625, 0.375), (67, 5.625, 0.375)]
for note, start, duration in piano_notes_f7 + piano_notes_bb7:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

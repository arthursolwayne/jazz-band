
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
]

for note, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif - Fm7 (F, Ab, Bb, D)
# F, Ab, Bb, D, F, Ab
sax_notes = [
    (65, 1.5, 0.375), (69, 1.875, 0.375), (62, 2.25, 0.375), (67, 2.625, 0.375),
    (65, 2.625, 0.375), (69, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: Walking line in Fm
# F, Gb, Ab, Bb, Bb, C, Db, D
bass_notes = [
    (65, 1.5, 0.375), (66, 1.875, 0.375), (69, 2.25, 0.375), (62, 2.625, 0.375),
    (62, 2.625, 0.375), (67, 3.0, 0.375), (64, 3.375, 0.375), (67, 3.75, 0.375)
]
for note, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2: 2nd beat - Fm7 (F, Ab, Bb, D)
# Bar 2: 4th beat - Bb7 (Bb, D, F, Ab)
piano_notes = [
    (65, 1.875, 0.375), (69, 1.875, 0.375), (62, 1.875, 0.375), (67, 1.875, 0.375),
    (62, 2.625, 0.375), (67, 2.625, 0.375), (65, 2.625, 0.375), (69, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat and resolve - F, Ab, Bb, D (ending on D)
sax_notes = [
    (65, 3.0, 0.375), (69, 3.375, 0.375), (62, 3.75, 0.375), (67, 4.125, 0.375),
]
for note, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: Walking line in Fm - F, Gb, Ab, Bb, Bb, C, Db, D
bass_notes = [
    (65, 3.0, 0.375), (66, 3.375, 0.375), (69, 3.75, 0.375), (62, 4.125, 0.375),
    (62, 4.125, 0.375), (67, 4.5, 0.375), (64, 4.875, 0.375), (67, 5.25, 0.375)
]
for note, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 3: 2nd beat - Fm7 (F, Ab, Bb, D)
# Bar 3: 4th beat - Bb7 (Bb, D, F, Ab)
piano_notes = [
    (65, 3.375, 0.375), (69, 3.375, 0.375), (62, 3.375, 0.375), (67, 3.375, 0.375),
    (62, 4.125, 0.375), (67, 4.125, 0.375), (65, 4.125, 0.375), (69, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
]

for note, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Echo the motif but resolve - D, Bb, Ab, F
sax_notes = [
    (67, 4.5, 0.375), (62, 4.875, 0.375), (69, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: Walking line in Fm
# F, Gb, Ab, Bb, Bb, C, Db, D
bass_notes = [
    (65, 4.5, 0.375), (66, 4.875, 0.375), (69, 5.25, 0.375), (62, 5.625, 0.375),
    (62, 5.625, 0.375), (67, 6.0, 0.375), (64, 6.375, 0.375), (67, 6.75, 0.375)
]
for note, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 4: 2nd beat - Fm7 (F, Ab, Bb, D)
# Bar 4: 4th beat - Bb7 (Bb, D, F, Ab)
piano_notes = [
    (65, 4.875, 0.375), (69, 4.875, 0.375), (62, 4.875, 0.375), (67, 4.875, 0.375),
    (62, 5.625, 0.375), (67, 5.625, 0.375), (65, 5.625, 0.375), (69, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875),
    (42, 6.1875, 0.1875), (42, 6.375, 0.1875), (42, 6.5625, 0.1875),
    (42, 6.75, 0.1875), (42, 6.9375, 0.1875), (42, 7.125, 0.1875),
    (42, 7.3125, 0.1875),
]

for note, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")

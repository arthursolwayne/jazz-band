
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (42, 0.9375, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),   # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),   # E
    (62, 2.625, 0.375),  # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    (67, 1.875, 0.1875),  # B7 on 2
    (64, 1.875, 0.1875),
    (69, 1.875, 0.1875),
    (71, 1.875, 0.1875),
    (67, 2.625, 0.1875),  # B7 on 4
    (64, 2.625, 0.1875),
    (69, 2.625, 0.1875),
    (71, 2.625, 0.1875),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif (start at 1.5s)
sax_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375),  # E
    (62, 2.25, 0.375),   # D
    (65, 2.625, 0.375),  # F
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (62, 3.0, 0.375),   # D
    (63, 3.375, 0.375),  # Eb
    (64, 3.75, 0.375),   # E
    (62, 4.125, 0.375),  # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    (67, 3.375, 0.1875),  # B7 on 2
    (64, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    (71, 3.375, 0.1875),
    (67, 4.125, 0.1875),  # B7 on 4
    (64, 4.125, 0.1875),
    (69, 4.125, 0.1875),
    (71, 4.125, 0.1875),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1 & 2
    (42, 3.1875, 0.1875),
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 3.75, 0.1875),  # Hihat on 3 & 4
    (42, 3.9375, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (62, 4.5, 0.375),   # D
    (63, 4.875, 0.375),  # Eb
    (64, 5.25, 0.375),   # E
    (62, 5.625, 0.375),  # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    (67, 4.875, 0.1875),  # B7 on 2
    (64, 4.875, 0.1875),
    (69, 4.875, 0.1875),
    (71, 4.875, 0.1875),
    (67, 5.625, 0.1875),  # B7 on 4
    (64, 5.625, 0.1875),
    (69, 5.625, 0.1875),
    (71, 5.625, 0.1875),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1 & 2
    (42, 4.6875, 0.1875),
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.25, 0.1875),  # Hihat on 3 & 4
    (42, 5.4375, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif variation (end on a question)
sax_notes = [
    (62, 4.5, 0.25),   # D
    (64, 4.75, 0.25),  # E
    (62, 5.0, 0.25),   # D
    (65, 5.25, 0.25),  # F
    (62, 5.5, 0.25),   # D
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BAR 2: Full quartet (1.5 - 3.0s)
# 1st bar of the melody - sax motif
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (65, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: walking line in F minor (F, Gb, G, A)
bass_notes = [
    (71, 1.5, 0.375), (70, 1.875, 0.375), (72, 2.25, 0.375), (74, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    (71, 1.875, 0.375), (74, 1.875, 0.375), (69, 1.875, 0.375), (72, 1.875, 0.375),
    (71, 2.625, 0.375), (74, 2.625, 0.375), (69, 2.625, 0.375), (72, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BAR 3: (3.0 - 4.5s)
# 2nd bar of the melody - repeat motif an octave higher
sax_notes = [
    (72, 3.0, 0.375), (74, 3.375, 0.375), (75, 3.75, 0.375), (72, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: walking line in F minor (Bb, B, C, D)
bass_notes = [
    (67, 3.0, 0.375), (68, 3.375, 0.375), (69, 3.75, 0.375), (71, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    (67, 3.375, 0.375), (70, 3.375, 0.375), (65, 3.375, 0.375), (68, 3.375, 0.375),
    (67, 4.125, 0.375), (70, 4.125, 0.375), (65, 4.125, 0.375), (68, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BAR 4: (4.5 - 6.0s)
# 3rd bar of the melody - return to original motif
sax_notes = [
    (62, 4.5, 0.375), (64, 4.875, 0.375), (65, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: walking line in F minor (F, Gb, G, A)
bass_notes = [
    (71, 4.5, 0.375), (70, 4.875, 0.375), (72, 5.25, 0.375), (74, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    (71, 4.875, 0.375), (74, 4.875, 0.375), (69, 4.875, 0.375), (72, 4.875, 0.375),
    (71, 5.625, 0.375), (74, 5.625, 0.375), (69, 5.625, 0.375), (72, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

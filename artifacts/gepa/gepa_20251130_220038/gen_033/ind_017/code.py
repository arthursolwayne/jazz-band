
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
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (62, 2.25, 0.375), (60, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass walking line in Dm
bass_notes = [
    (50, 1.5, 0.375), (51, 1.875, 0.375), (48, 2.25, 0.375), (50, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    (64, 1.875, 0.1875), (67, 1.875, 0.1875), (62, 1.875, 0.1875), (60, 1.875, 0.1875),
    (64, 2.625, 0.1875), (67, 2.625, 0.1875), (62, 2.625, 0.1875), (60, 2.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody continuation
sax_notes = [
    (62, 3.0, 0.375), (64, 3.375, 0.375), (62, 3.75, 0.375), (60, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass walking line in Dm
bass_notes = [
    (51, 3.0, 0.375), (53, 3.375, 0.375), (50, 3.75, 0.375), (52, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    (64, 3.375, 0.1875), (67, 3.375, 0.1875), (62, 3.375, 0.1875), (60, 3.375, 0.1875),
    (64, 4.125, 0.1875), (67, 4.125, 0.1875), (62, 4.125, 0.1875), (60, 4.125, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody resolution
sax_notes = [
    (62, 4.5, 0.375), (65, 4.875, 0.375), (62, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass walking line in Dm
bass_notes = [
    (52, 4.5, 0.375), (53, 4.875, 0.375), (50, 5.25, 0.375), (52, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comping on 2 and 4 with 7th chords
piano_notes = [
    (64, 4.875, 0.1875), (67, 4.875, 0.1875), (62, 4.875, 0.1875), (60, 4.875, 0.1875),
    (64, 5.625, 0.1875), (67, 5.625, 0.1875), (62, 5.625, 0.1875), (60, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875), 
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

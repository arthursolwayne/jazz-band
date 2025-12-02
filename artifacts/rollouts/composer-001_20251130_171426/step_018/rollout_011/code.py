
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    (37, 1.5, 0.375), (38, 1.875, 0.375), (36, 2.25, 0.375), (39, 2.625, 0.375),
    (37, 3.0, 0.375), (38, 3.375, 0.375), (36, 3.75, 0.375), (39, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    (62, 1.875, 0.1875), (69, 1.875, 0.1875),
    (62, 2.625, 0.1875), (69, 2.625, 0.1875),
    (62, 3.375, 0.1875), (69, 3.375, 0.1875),
    (62, 4.125, 0.1875), (69, 4.125, 0.1875)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax melody (start it, leave it hanging)
sax_notes = [
    (65, 1.5, 0.375), (67, 1.875, 0.375), (65, 2.25, 0.375),
    (62, 2.625, 0.375), (65, 3.0, 0.375), (67, 3.375, 0.375),
    (65, 3.75, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    (39, 3.0, 0.375), (40, 3.375, 0.375), (38, 3.75, 0.375), (41, 4.125, 0.375),
    (39, 4.5, 0.375), (40, 4.875, 0.375), (38, 5.25, 0.375), (41, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    (64, 3.375, 0.1875), (71, 3.375, 0.1875),
    (64, 4.125, 0.1875), (71, 4.125, 0.1875),
    (64, 4.875, 0.1875), (71, 4.875, 0.1875),
    (64, 5.625, 0.1875), (71, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax melody (finish it)
sax_notes = [
    (65, 3.0, 0.375), (67, 3.375, 0.375), (65, 3.75, 0.375),
    (62, 4.125, 0.375), (65, 4.5, 0.375), (67, 4.875, 0.375),
    (65, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (36, 5.875, 0.375), (38, 6.25, 0.375), (42, 5.875, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    (41, 4.5, 0.375), (42, 4.875, 0.375), (40, 5.25, 0.375), (43, 5.625, 0.375),
    (41, 6.0, 0.375), (42, 6.375, 0.375), (40, 6.75, 0.375), (43, 7.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    (64, 4.875, 0.1875), (71, 4.875, 0.1875),
    (64, 5.625, 0.1875), (71, 5.625, 0.1875),
    (64, 6.375, 0.1875), (71, 6.375, 0.1875),
    (64, 7.125, 0.1875), (71, 7.125, 0.1875)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax melody (finish it)
sax_notes = [
    (65, 4.5, 0.375), (67, 4.875, 0.375), (65, 5.25, 0.375),
    (62, 5.625, 0.375), (65, 6.0, 0.375), (67, 6.375, 0.375),
    (65, 6.75, 0.375), (62, 7.125, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")

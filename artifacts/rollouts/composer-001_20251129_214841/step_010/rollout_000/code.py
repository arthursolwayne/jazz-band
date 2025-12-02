
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
    (42, 1.0, 0.1875), (42, 1.1875, 0.1875), (42, 1.375, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif in C minor, start on C4, then Eb4, G4, Bb4
sax_notes = [
    (60, 1.5, 0.375), (63, 1.875, 0.375), (67, 2.25, 0.375), (69, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line in C minor, chromatic approach to 3rd
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on Bb7 and F7
piano_notes = [
    (71, 1.875, 0.1875), (74, 1.875, 0.1875), (76, 1.875, 0.1875), (79, 1.875, 0.1875),
    (65, 2.625, 0.1875), (68, 2.625, 0.1875), (70, 2.625, 0.1875), (72, 2.625, 0.1875)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but end on Bb4
sax_notes = [
    (60, 3.0, 0.375), (63, 3.375, 0.375), (67, 3.75, 0.375), (69, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line in C minor, chromatic approach to 3rd
bass_notes = [
    (52, 3.0, 0.375), (53, 3.375, 0.375), (54, 3.75, 0.375), (55, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on Bb7 and F7
piano_notes = [
    (71, 3.375, 0.1875), (74, 3.375, 0.1875), (76, 3.375, 0.1875), (79, 3.375, 0.1875),
    (65, 4.125, 0.1875), (68, 4.125, 0.1875), (70, 4.125, 0.1875), (72, 4.125, 0.1875)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolve motif, end on C5
sax_notes = [
    (60, 4.5, 0.375), (63, 4.875, 0.375), (67, 5.25, 0.375), (72, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line in C minor, chromatic approach to 3rd
bass_notes = [
    (56, 4.5, 0.375), (57, 4.875, 0.375), (58, 5.25, 0.375), (59, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, comp on Bb7 and F7
piano_notes = [
    (71, 4.875, 0.1875), (74, 4.875, 0.1875), (76, 4.875, 0.1875), (79, 4.875, 0.1875),
    (65, 5.625, 0.1875), (68, 5.625, 0.1875), (70, 5.625, 0.1875), (72, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

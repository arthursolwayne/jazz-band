
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
    (36, 0.0, 0.375), (42, 0.0, 0.375),
    (38, 0.375, 0.375), (42, 0.375, 0.375),
    (36, 0.75, 0.375), (42, 0.75, 0.375),
    (38, 1.125, 0.375), (42, 1.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif - F, Bb, Ab, G
sax_notes = [
    (84, 1.5, 0.375), (78, 1.875, 0.375), (76, 2.25, 0.375), (75, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in F
bass_notes = [
    (45, 1.5, 0.375), (46, 1.875, 0.375), (47, 2.25, 0.375), (48, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    (64, 1.875, 0.375), (69, 1.875, 0.375), (67, 1.875, 0.375),  # F7
    (64, 2.625, 0.375), (69, 2.625, 0.375), (67, 2.625, 0.375)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif with slight variation (F, Bb, Ab, G)
sax_notes = [
    (84, 3.0, 0.375), (78, 3.375, 0.375), (76, 3.75, 0.375), (75, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in F
bass_notes = [
    (48, 3.0, 0.375), (49, 3.375, 0.375), (50, 3.75, 0.375), (51, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    (64, 3.375, 0.375), (69, 3.375, 0.375), (67, 3.375, 0.375),  # F7
    (64, 4.125, 0.375), (69, 4.125, 0.375), (67, 4.125, 0.375)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif with resolution (F, Bb, Ab, F)
sax_notes = [
    (84, 4.5, 0.375), (78, 4.875, 0.375), (76, 5.25, 0.375), (84, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in F
bass_notes = [
    (51, 4.5, 0.375), (52, 4.875, 0.375), (53, 5.25, 0.375), (54, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    (64, 4.875, 0.375), (69, 4.875, 0.375), (67, 4.875, 0.375),  # F7
    (64, 5.625, 0.375), (69, 5.625, 0.375), (67, 5.625, 0.375)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: same pattern for bar 2-4
for i in range(3):
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5 + i * 1.5, end=start + 1.5 + i * 1.5 + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

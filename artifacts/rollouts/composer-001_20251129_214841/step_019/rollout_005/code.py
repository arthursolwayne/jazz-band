
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts here
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (65, 1.875, 0.375), # F#4
    (67, 2.25, 0.375),  # A4
    (62, 2.625, 0.375)  # D4
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line
bass_notes = [
    (49, 1.5, 0.375),  # C3
    (50, 1.875, 0.375), # Db3
    (51, 2.25, 0.375),  # D3
    (49, 2.625, 0.375)  # C3
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (71, 1.875, 0.375),  # G4 (C7)
    (74, 1.875, 0.375),  # Bb4 (C7)
    (76, 1.875, 0.375),  # C5 (C7)
    (79, 1.875, 0.375),  # E5 (C7)
    (71, 2.625, 0.375),  # G4 (C7)
    (74, 2.625, 0.375),  # Bb4 (C7)
    (76, 2.625, 0.375),  # C5 (C7)
    (79, 2.625, 0.375)   # E5 (C7)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif
sax_notes = [
    (62, 3.0, 0.375),  # D4
    (65, 3.375, 0.375), # F#4
    (67, 3.75, 0.375),  # A4
    (62, 4.125, 0.375)  # D4
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line
bass_notes = [
    (52, 3.0, 0.375),  # Eb3
    (53, 3.375, 0.375), # E3
    (55, 3.75, 0.375),  # G3
    (52, 4.125, 0.375)  # Eb3
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (71, 3.375, 0.375),  # G4 (C7)
    (74, 3.375, 0.375),  # Bb4 (C7)
    (76, 3.375, 0.375),  # C5 (C7)
    (79, 3.375, 0.375),  # E5 (C7)
    (71, 4.125, 0.375),  # G4 (C7)
    (74, 4.125, 0.375),  # Bb4 (C7)
    (76, 4.125, 0.375),  # C5 (C7)
    (79, 4.125, 0.375)   # E5 (C7)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolve the motif
sax_notes = [
    (62, 4.5, 0.375),  # D4
    (65, 4.875, 0.375), # F#4
    (67, 5.25, 0.375),  # A4
    (69, 5.625, 0.375)  # B4
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: walking line
bass_notes = [
    (56, 4.5, 0.375),  # Ab3
    (57, 4.875, 0.375), # A3
    (59, 5.25, 0.375),  # C4
    (56, 5.625, 0.375)  # Ab3
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (71, 4.875, 0.375),  # G4 (C7)
    (74, 4.875, 0.375),  # Bb4 (C7)
    (76, 4.875, 0.375),  # C5 (C7)
    (79, 4.875, 0.375),  # E5 (C7)
    (71, 5.625, 0.375),  # G4 (C7)
    (74, 5.625, 0.375),  # Bb4 (C7)
    (76, 5.625, 0.375),  # C5 (C7)
    (79, 5.625, 0.375)   # E5 (C7)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1 & 2
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2 & 3
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3 & 4
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

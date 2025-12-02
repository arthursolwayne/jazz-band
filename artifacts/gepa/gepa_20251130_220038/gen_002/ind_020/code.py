
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

# Bass (Marcus) - walking line in Fm
bass_notes = [
    (39, 1.5, 0.375),  # Fm root (F) on 1
    (40, 1.875, 0.375),  # Gb on 2
    (41, 2.25, 0.375),  # Ab on 3
    (42, 2.625, 0.375)   # Bb on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2
    (44, 1.875, 0.375),  # F
    (47, 1.875, 0.375),  # A
    (49, 1.875, 0.375),  # C
    (50, 1.875, 0.375),  # Db
    # Bar 3: Fm7 on 4
    (44, 2.625, 0.375),  # F
    (47, 2.625, 0.375),  # A
    (49, 2.625, 0.375),  # C
    (50, 2.625, 0.375)   # Db
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax (Dante) - motif in Fm, short and singing
sax_notes = [
    (44, 1.5, 0.25),  # F
    (47, 1.75, 0.25),  # A
    (49, 2.0, 0.25),  # C
    (44, 2.25, 0.25)   # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 3.0, end=start + 3.0 + duration))

# Bass (Marcus) - walking line in Fm
bass_notes = [
    (42, 3.0, 0.375),  # Bb on 1
    (44, 3.375, 0.375),  # F on 2
    (47, 3.75, 0.375),  # A on 3
    (49, 4.125, 0.375)   # C on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on 2
    (44, 3.375, 0.375),  # F
    (47, 3.375, 0.375),  # A
    (49, 3.375, 0.375),  # C
    (50, 3.375, 0.375),  # Db
    # Bar 4: Fm7 on 4
    (44, 4.125, 0.375),  # F
    (47, 4.125, 0.375),  # A
    (49, 4.125, 0.375),  # C
    (50, 4.125, 0.375)   # Db
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax (Dante) - continuation of the motif
sax_notes = [
    (49, 3.0, 0.25),  # C
    (44, 3.25, 0.25),  # F
    (47, 3.5, 0.25),  # A
    (49, 3.75, 0.25),  # C
    (44, 4.0, 0.25),  # F
    (47, 4.25, 0.25),  # A
    (49, 4.5, 0.25)   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 4.5, end=start + 4.5 + duration))

# Bass (Marcus) - walking line in Fm
bass_notes = [
    (49, 4.5, 0.375),  # C on 1
    (50, 4.875, 0.375),  # Db on 2
    (52, 5.25, 0.375),  # Eb on 3
    (53, 5.625, 0.375)   # F on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on 2
    (44, 4.875, 0.375),  # F
    (47, 4.875, 0.375),  # A
    (49, 4.875, 0.375),  # C
    (50, 4.875, 0.375),  # Db
    # Bar 4: Fm7 on 4
    (44, 5.625, 0.375),  # F
    (47, 5.625, 0.375),  # A
    (49, 5.625, 0.375),  # C
    (50, 5.625, 0.375)   # Db
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax (Dante) - resolve the motif
sax_notes = [
    (49, 4.5, 0.25),  # C
    (47, 4.75, 0.25),  # A
    (44, 5.0, 0.25),  # F
    (47, 5.25, 0.25),  # A
    (44, 5.5, 0.25),  # F
    (47, 5.75, 0.25),  # A
    (49, 6.0, 0.25)   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

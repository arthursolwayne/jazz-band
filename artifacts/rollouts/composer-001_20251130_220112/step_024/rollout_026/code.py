
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start a motif on Fm7 (F, Ab, Bb, D)
sax_notes = [
    (64, 1.5, 0.375),  # F
    (69, 1.875, 0.375), # Ab
    (62, 2.25, 0.375),  # Bb
    (67, 2.625, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375), # Gb
    (69, 2.25, 0.375),  # Ab
    (71, 2.625, 0.375)  # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Ab7 and Bb7)
piano_notes = [
    (69, 1.875, 0.375), # Ab
    (71, 1.875, 0.375), # Bb
    (76, 1.875, 0.375), # Db
    (74, 1.875, 0.375), # F
    (71, 2.625, 0.375), # Bb
    (74, 2.625, 0.375), # F
    (77, 2.625, 0.375), # G
    (79, 2.625, 0.375)  # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif, wrap it up
sax_notes = [
    (64, 3.0, 0.375),  # F
    (69, 3.375, 0.375), # Ab
    (62, 3.75, 0.375),  # Bb
    (67, 4.125, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm (Bb, B, C, Db)
bass_notes = [
    (62, 3.0, 0.375),  # Bb
    (63, 3.375, 0.375), # B
    (64, 3.75, 0.375),  # C
    (66, 4.125, 0.375)  # Db
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Bb7 and C7)
piano_notes = [
    (71, 3.375, 0.375), # Bb
    (74, 3.375, 0.375), # F
    (76, 3.375, 0.375), # Db
    (77, 3.375, 0.375), # G
    (72, 4.125, 0.375), # C
    (74, 4.125, 0.375), # F
    (77, 4.125, 0.375), # G
    (79, 4.125, 0.375)  # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif
sax_notes = [
    (64, 4.5, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm (Db, D, Eb, E)
bass_notes = [
    (66, 4.5, 0.375),  # Db
    (67, 4.875, 0.375), # D
    (69, 5.25, 0.375),  # Eb
    (71, 5.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Db7 and Eb7)
piano_notes = [
    (66, 4.875, 0.375), # Db
    (69, 4.875, 0.375), # Eb
    (71, 4.875, 0.375), # F
    (74, 4.875, 0.375), # Ab
    (69, 5.625, 0.375), # Eb
    (71, 5.625, 0.375), # F
    (74, 5.625, 0.375), # Ab
    (76, 5.625, 0.375)  # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

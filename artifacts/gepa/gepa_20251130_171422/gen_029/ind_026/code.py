
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.375, 0.125),   # Hihat on 1& 
    (38, 0.75, 0.375),    # Snare on 2
    (42, 0.75, 0.125),    # Hihat on 2& 
    (36, 1.125, 0.375),   # Kick on 3
    (42, 1.125, 0.125),   # Hihat on 3& 
    (38, 1.5, 0.375),     # Snare on 4
    (42, 1.5, 0.125)      # Hihat on 4& 
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody (starts on D, chromatic approach to E)
sax_notes = [
    (62, 1.5, 0.375),     # D
    (63, 1.875, 0.375),   # E
    (61, 2.25, 0.375),    # C
    (60, 2.625, 0.375)    # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass line - walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),     # D
    (63, 1.875, 0.375),   # Eb
    (60, 2.25, 0.375),    # B
    (59, 2.625, 0.375)    # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords - 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.875, 0.375),   # G7 (Bb)
    (62, 1.875, 0.375),   # G7 (D)
    (60, 1.875, 0.375),   # G7 (F)
    (58, 1.875, 0.375),   # G7 (G)
    (64, 2.625, 0.375),   # G7 (Bb)
    (62, 2.625, 0.375),   # G7 (D)
    (60, 2.625, 0.375),   # G7 (F)
    (58, 2.625, 0.375)    # G7 (G)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue with same pattern
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues the motif, but with space
sax_notes = [
    (62, 3.0, 0.375),     # D
    (64, 3.375, 0.375),   # E
    (61, 3.75, 0.375),    # C
    (60, 4.125, 0.375)    # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass line continues with walking line
bass_notes = [
    (65, 3.0, 0.375),     # E
    (64, 3.375, 0.375),   # D
    (62, 3.75, 0.375),    # B
    (60, 4.125, 0.375)    # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords
piano_notes = [
    (64, 3.375, 0.375),   # G7 (Bb)
    (62, 3.375, 0.375),   # G7 (D)
    (60, 3.375, 0.375),   # G7 (F)
    (58, 3.375, 0.375),   # G7 (G)
    (64, 4.125, 0.375),   # G7 (Bb)
    (62, 4.125, 0.375),   # G7 (D)
    (60, 4.125, 0.375),   # G7 (F)
    (58, 4.125, 0.375)    # G7 (G)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 3.0, end=start + 3.0 + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax resolves the motif
sax_notes = [
    (62, 4.5, 0.375),     # D
    (64, 4.875, 0.375),   # E
    (61, 5.25, 0.375),    # C
    (60, 5.625, 0.375)    # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=120, pitch=note, start=start, end=start + duration))

# Bass line ends with a resolution
bass_notes = [
    (65, 4.5, 0.375),     # E
    (64, 4.875, 0.375),   # D
    (62, 5.25, 0.375),    # B
    (60, 5.625, 0.375)    # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords resolve
piano_notes = [
    (64, 4.875, 0.375),   # G7 (Bb)
    (62, 4.875, 0.375),   # G7 (D)
    (60, 4.875, 0.375),   # G7 (F)
    (58, 4.875, 0.375),   # G7 (G)
    (64, 5.625, 0.375),   # G7 (Bb)
    (62, 5.625, 0.375),   # G7 (D)
    (60, 5.625, 0.375),   # G7 (F)
    (58, 5.625, 0.375)    # G7 (G)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 4.5, end=start + 4.5 + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

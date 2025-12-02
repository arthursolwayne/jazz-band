
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),  # Kick on beat 1
    (42, 0.0, 0.1875), # Hihat on 1 &
    (38, 0.375, 0.375),# Snare on beat 2
    (42, 0.375, 0.1875),# Hihat on 2 &
    (36, 0.75, 0.375),  # Kick on beat 3
    (42, 0.75, 0.1875), # Hihat on 3 &
    (38, 1.125, 0.375),# Snare on beat 4
    (42, 1.125, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Fm7 -> Bb -> Eb -> Ab
sax_notes = [
    (87, 1.5, 0.25),   # Fm7 (F, Ab, Bb, Db) => F (87)
    (80, 1.75, 0.25),  # Bb (80)
    (76, 2.0, 0.25),   # Eb (76)
    (71, 2.25, 0.25)   # Ab (71)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (64, 1.5, 0.25),   # F (64)
    (62, 1.75, 0.25),  # Eb (62)
    (59, 2.0, 0.25),   # Db (59)
    (57, 2.25, 0.25)   # C (57)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 & 4
piano_notes = [
    (87, 1.75, 0.25),  # Fm7 (F, Ab, Bb, Db)
    (80, 1.75, 0.25),
    (76, 1.75, 0.25),
    (64, 1.75, 0.25),
    (87, 2.25, 0.25),  # Fm7 (F, Ab, Bb, Db)
    (80, 2.25, 0.25),
    (76, 2.25, 0.25),
    (64, 2.25, 0.25)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on beat 1
    (42, 1.5, 0.1875), # Hihat on 1 &
    (38, 1.875, 0.375),# Snare on beat 2
    (42, 1.875, 0.1875),# Hihat on 2 &
    (36, 2.25, 0.375),  # Kick on beat 3
    (42, 2.25, 0.1875), # Hihat on 3 &
    (38, 2.625, 0.375),# Snare on beat 4
    (42, 2.625, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: Repeat with variation
sax_notes = [
    (87, 3.0, 0.25),   # Fm7 (F, Ab, Bb, Db) => F (87)
    (80, 3.25, 0.25),  # Bb (80)
    (76, 3.5, 0.25),   # Eb (76)
    (71, 3.75, 0.25)   # Ab (71)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (64, 3.0, 0.25),   # F (64)
    (62, 3.25, 0.25),  # Eb (62)
    (59, 3.5, 0.25),   # Db (59)
    (57, 3.75, 0.25)   # C (57)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 & 4
piano_notes = [
    (87, 3.25, 0.25),  # Fm7 (F, Ab, Bb, Db)
    (80, 3.25, 0.25),
    (76, 3.25, 0.25),
    (64, 3.25, 0.25),
    (87, 3.75, 0.25),  # Fm7 (F, Ab, Bb, Db)
    (80, 3.75, 0.25),
    (76, 3.75, 0.25),
    (64, 3.75, 0.25)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on beat 1
    (42, 3.0, 0.1875), # Hihat on 1 &
    (38, 3.375, 0.375),# Snare on beat 2
    (42, 3.375, 0.1875),# Hihat on 2 &
    (36, 3.75, 0.375),  # Kick on beat 3
    (42, 3.75, 0.1875), # Hihat on 3 &
    (38, 4.125, 0.375),# Snare on beat 4
    (42, 4.125, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: Finish the phrase
sax_notes = [
    (87, 4.5, 0.25),   # Fm7 (F, Ab, Bb, Db) => F (87)
    (80, 4.75, 0.25),  # Bb (80)
    (76, 5.0, 0.25),   # Eb (76)
    (71, 5.25, 0.25)   # Ab (71)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (64, 4.5, 0.25),   # F (64)
    (62, 4.75, 0.25),  # Eb (62)
    (59, 5.0, 0.25),   # Db (59)
    (57, 5.25, 0.25)   # C (57)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 & 4
piano_notes = [
    (87, 4.75, 0.25),  # Fm7 (F, Ab, Bb, Db)
    (80, 4.75, 0.25),
    (76, 4.75, 0.25),
    (64, 4.75, 0.25),
    (87, 5.25, 0.25),  # Fm7 (F, Ab, Bb, Db)
    (80, 5.25, 0.25),
    (76, 5.25, 0.25),
    (64, 5.25, 0.25)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on beat 1
    (42, 4.5, 0.1875), # Hihat on 1 &
    (38, 4.875, 0.375),# Snare on beat 2
    (42, 4.875, 0.1875),# Hihat on 2 &
    (36, 5.25, 0.375),  # Kick on beat 3
    (42, 5.25, 0.1875), # Hihat on 3 &
    (38, 5.625, 0.375),# Snare on beat 4
    (42, 5.625, 0.1875) # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

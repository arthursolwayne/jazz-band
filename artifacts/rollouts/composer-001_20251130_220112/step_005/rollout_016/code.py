
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
    (42, 0.0, 0.375),  # Hihat on beat 1
    (38, 0.375, 0.375),  # Snare on beat 2
    (42, 0.375, 0.375),  # Hihat on beat 2
    (36, 0.75, 0.375),  # Kick on beat 3
    (42, 0.75, 0.375),  # Hihat on beat 3
    (38, 1.125, 0.375),  # Snare on beat 4
    (42, 1.125, 0.375),  # Hihat on beat 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif - Fm7 -> Ab -> Bb -> Db
sax_notes = [
    (90, 1.5, 0.375),  # F (Fm7)
    (88, 1.875, 0.375),  # Ab
    (87, 2.25, 0.375),  # Bb
    (84, 2.625, 0.375),  # Db
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (64, 1.5, 0.375),  # F
    (62, 1.875, 0.375),  # Eb
    (60, 2.25, 0.375),  # D
    (61, 2.625, 0.375),  # Eb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (87, 1.875, 0.375),  # Bb7 (Bb, D, F, Ab)
    (84, 1.875, 0.375),  # Ab
    (82, 1.875, 0.375),  # G
    (80, 1.875, 0.375),  # F

    (87, 2.625, 0.375),  # Bb7
    (84, 2.625, 0.375),  # Ab
    (82, 2.625, 0.375),  # G
    (80, 2.625, 0.375),  # F
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif - F -> Ab -> Bb -> Db
sax_notes = [
    (90, 3.0, 0.375),  # F
    (88, 3.375, 0.375),  # Ab
    (87, 3.75, 0.375),  # Bb
    (84, 4.125, 0.375),  # Db
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line
bass_notes = [
    (64, 3.0, 0.375),  # F
    (62, 3.375, 0.375),  # Eb
    (60, 3.75, 0.375),  # D
    (61, 4.125, 0.375),  # Eb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords
piano_notes = [
    (87, 3.375, 0.375),  # Bb7
    (84, 3.375, 0.375),  # Ab
    (82, 3.375, 0.375),  # G
    (80, 3.375, 0.375),  # F

    (87, 4.125, 0.375),  # Bb7
    (84, 4.125, 0.375),  # Ab
    (82, 4.125, 0.375),  # G
    (80, 4.125, 0.375),  # F
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Complete motif - F -> Ab -> Bb -> Db
sax_notes = [
    (90, 4.5, 0.375),  # F
    (88, 4.875, 0.375),  # Ab
    (87, 5.25, 0.375),  # Bb
    (84, 5.625, 0.375),  # Db
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line
bass_notes = [
    (64, 4.5, 0.375),  # F
    (62, 4.875, 0.375),  # Eb
    (60, 5.25, 0.375),  # D
    (61, 5.625, 0.375),  # Eb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords
piano_notes = [
    (87, 4.875, 0.375),  # Bb7
    (84, 4.875, 0.375),  # Ab
    (82, 4.875, 0.375),  # G
    (80, 4.875, 0.375),  # F

    (87, 5.625, 0.375),  # Bb7
    (84, 5.625, 0.375),  # Ab
    (82, 5.625, 0.375),  # G
    (80, 5.625, 0.375),  # F
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on beat 1
    (42, 4.5, 0.375),  # Hihat on beat 1
    (38, 4.875, 0.375),  # Snare on beat 2
    (42, 4.875, 0.375),  # Hihat on beat 2
    (36, 5.25, 0.375),  # Kick on beat 3
    (42, 5.25, 0.375),  # Hihat on beat 3
    (38, 5.625, 0.375),  # Snare on beat 4
    (42, 5.625, 0.375),  # Hihat on beat 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

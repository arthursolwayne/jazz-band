
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums, with a subtle groove that hums with energy but doesn't resolve

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36, 100), (0.375, 42, 80),
    (0.75, 36, 100), (1.125, 42, 80),
    (1.5, 38, 100), (1.875, 42, 80),
    (2.25, 38, 100), (2.625, 42, 80),
    (3.0, 36, 100), (3.375, 42, 80),
    (3.75, 36, 100), (4.125, 42, 80),
    (4.5, 38, 100), (4.875, 42, 80),
    (5.25, 38, 100), (5.625, 42, 80)
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, Dm7 -> Gm7 -> Cm7 -> F7
# D-F-G-A-Bb-D (Dm7) -> G-Bb-C-D-F-G (Gm7) -> C-Eb-F-G-A-C (Cm7) -> F-A-Bb-C-E-F (F7)
bass_notes = [
    (1.5, 50, 80), (1.75, 52, 80), (2.0, 53, 80), (2.25, 55, 80), (2.5, 50, 80), (2.75, 52, 80)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Dm7 on beat 2, Gm7 on beat 4
piano_notes = [
    # Dm7 on beat 2 (2.0 - 2.5s)
    (2.0, 62, 100), (2.0, 67, 100), (2.0, 69, 100), (2.0, 71, 100),
    # Gm7 on beat 4 (2.5 - 3.0s)
    (2.5, 67, 100), (2.5, 72, 100), (2.5, 74, 100), (2.5, 76, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.5))

# Sax: Motif, starts on beat 1, ends on beat 4 with a rest
# D (62), Bb (67), F (65), rest (no note on beat 4)
sax_notes = [
    (1.5, 62, 100), (1.5, 67, 100), (1.5, 65, 100)
]
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5)
])

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, Dm7 -> Gm7 -> Cm7 -> F7
# D-F-G-A-Bb-D (Dm7) -> G-Bb-C-D-F-G (Gm7) -> C-Eb-F-G-A-C (Cm7) -> F-A-Bb-C-E-F (F7)
bass_notes = [
    (3.0, 50, 80), (3.25, 52, 80), (3.5, 53, 80), (3.75, 55, 80), (4.0, 50, 80), (4.25, 52, 80)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Dm7 on beat 2 (3.5 - 4.0s)
# Gm7 on beat 4 (4.0 - 4.5s)
piano_notes = [
    # Dm7 on beat 2 (3.5 - 4.0s)
    (3.5, 62, 100), (3.5, 67, 100), (3.5, 69, 100), (3.5, 71, 100),
    # Gm7 on beat 4 (4.0 - 4.5s)
    (4.0, 67, 100), (4.0, 72, 100), (4.0, 74, 100), (4.0, 76, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.5))

# Sax: Motif again, with a slight variation
# D (62), Bb (67), F (65), rest (no note on beat 4)
sax_notes = [
    (3.0, 62, 100), (3.0, 67, 100), (3.0, 65, 100)
]
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0)
])

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line, Dm7 -> Gm7 -> Cm7 -> F7
# D-F-G-A-Bb-D (Dm7) -> G-Bb-C-D-F-G (Gm7) -> C-Eb-F-G-A-C (Cm7) -> F-A-Bb-C-E-F (F7)
bass_notes = [
    (4.5, 50, 80), (4.75, 52, 80), (5.0, 53, 80), (5.25, 55, 80), (5.5, 50, 80), (5.75, 52, 80)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Dm7 on beat 2 (5.0 - 5.5s)
# Gm7 on beat 4 (5.5 - 6.0s)
piano_notes = [
    # Dm7 on beat 2 (5.0 - 5.5s)
    (5.0, 62, 100), (5.0, 67, 100), (5.0, 69, 100), (5.0, 71, 100),
    # Gm7 on beat 4 (5.5 - 6.0s)
    (5.5, 67, 100), (5.5, 72, 100), (5.5, 74, 100), (5.5, 76, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.5))

# Sax: Motif again, but ending with a suspension on the last note
# D (62), Bb (67), F (65), D (62)
sax_notes = [
    (4.5, 62, 100), (4.5, 67, 100), (4.5, 65, 100), (4.5, 62, 100)
]
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0)
])

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (3.0, 36, 100), (3.375, 42, 80),
    (3.75, 36, 100), (4.125, 42, 80),
    (4.5, 38, 100), (4.875, 42, 80),
    (5.25, 38, 100), (5.625, 42, 80),
    (6.0, 36, 100), (6.375, 42, 80),
    (6.75, 36, 100), (7.125, 42, 80),
    (7.5, 38, 100), (7.875, 42, 80),
    (8.25, 38, 100), (8.625, 42, 80)
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")

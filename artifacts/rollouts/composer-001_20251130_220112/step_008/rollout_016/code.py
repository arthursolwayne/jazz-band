
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
    # Bar 1
    (36, 0.0, 1.0), (38, 0.5, 1.0), (42, 0.0, 1.0),
    (36, 1.0, 1.0), (38, 1.5, 1.0), (42, 1.0, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    (60, 1.5, 0.5), (61, 2.0, 0.5), (59, 2.5, 0.5), (58, 3.0, 0.5)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# F7 on 2, Bbm7 on 4
piano_notes = [
    # F7 on beat 2 (2.0s)
    (65, 2.0, 0.5), (68, 2.0, 0.5), (72, 2.0, 0.5), (76, 2.0, 0.5),
    # Bbm7 on beat 4 (3.0s)
    (67, 3.0, 0.5), (70, 3.0, 0.5), (74, 3.0, 0.5), (77, 3.0, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif - F, Ab, Bb, F (start at 1.5s)
sax_notes = [
    (65, 1.5, 0.5), (67, 2.0, 0.5), (69, 2.5, 0.5), (65, 3.0, 0.5)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    (58, 3.0, 0.5), (59, 3.5, 0.5), (60, 4.0, 0.5), (61, 4.5, 0.5)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# F7 on 2 (4.0s), Bbm7 on 4 (4.5s)
piano_notes = [
    # F7 on beat 2 (4.0s)
    (65, 4.0, 0.5), (68, 4.0, 0.5), (72, 4.0, 0.5), (76, 4.0, 0.5),
    # Bbm7 on beat 4 (4.5s)
    (67, 4.5, 0.5), (70, 4.5, 0.5), (74, 4.5, 0.5), (77, 4.5, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif - repeat and resolve
sax_notes = [
    (65, 3.0, 0.5), (67, 3.5, 0.5), (69, 4.0, 0.5), (65, 4.5, 0.5)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 3
    (36, 3.0, 1.0), (38, 3.5, 1.0), (42, 3.0, 1.0),
    (36, 4.0, 1.0), (38, 4.5, 1.0), (42, 4.0, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    (61, 4.5, 0.5), (60, 5.0, 0.5), (59, 5.5, 0.5), (58, 6.0, 0.5)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# F7 on 2 (5.0s), Bbm7 on 4 (6.0s)
piano_notes = [
    # F7 on beat 2 (5.0s)
    (65, 5.0, 0.5), (68, 5.0, 0.5), (72, 5.0, 0.5), (76, 5.0, 0.5),
    # Bbm7 on beat 4 (6.0s)
    (67, 6.0, 0.5), (70, 6.0, 0.5), (74, 6.0, 0.5), (77, 6.0, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif - repeat and resolve
sax_notes = [
    (65, 4.5, 0.5), (67, 5.0, 0.5), (69, 5.5, 0.5), (65, 6.0, 0.5)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4
    (36, 4.5, 1.0), (38, 5.0, 1.0), (42, 4.5, 1.0),
    (36, 5.5, 1.0), (38, 6.0, 1.0), (42, 5.5, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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
    (36, 1.0, 0.375),  # Kick on 1
    (42, 1.0, 0.375),  # Hihat on 1
    (36, 2.0, 0.375),  # Kick on 3
    (42, 2.0, 0.375),  # Hihat on 3
    (38, 3.0, 0.375),  # Snare on 4
    (42, 3.0, 0.375),  # Hihat on 4
    (42, 4.0, 0.375),  # Hihat on 1 (next bar)
]
for note, velocity, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: First motif (Fm7 chord, sparse, expressive)
sax_notes = [
    (77, 100, 1.5),  # F
    (72, 100, 1.75), # Ab
    (74, 100, 2.0),  # Bb
    (77, 100, 2.25), # F
]
for note, velocity, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line with chromatic approaches (Fm7 -> Bb7)
bass_notes = [
    (64, 80, 1.5),   # F
    (63, 80, 1.75),  # E
    (62, 80, 2.0),   # Eb
    (60, 80, 2.25),  # D
]
for note, velocity, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (comping)
piano_notes = [
    (64, 90, 1.75),  # F7 (F, A, C, Eb)
    (60, 90, 1.75),  # C
    (65, 90, 1.75),  # G
    (62, 90, 1.75),  # Eb

    (65, 90, 2.25),  # Bb7 (Bb, D, F, Ab)
    (62, 90, 2.25),  # F
    (67, 90, 2.25),  # G
    (64, 90, 2.25),  # Eb
]
for note, velocity, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 100, 1.5),  # Kick on 1
    (42, 100, 1.5),  # Hihat on 1
    (38, 100, 1.75), # Snare on 2
    (42, 100, 1.75), # Hihat on 2
    (36, 100, 2.0),  # Kick on 3
    (42, 100, 2.0),  # Hihat on 3
    (38, 100, 2.25), # Snare on 4
    (42, 100, 2.25), # Hihat on 4
]
for note, velocity, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Answer to the motif (Fm7 chord, sparse, expressive)
sax_notes = [
    (72, 100, 3.0),  # Ab
    (74, 100, 3.25), # Bb
    (77, 100, 3.5),  # F
    (72, 100, 3.75), # Ab
]
for note, velocity, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line with chromatic approaches (Bb7 -> Eb7)
bass_notes = [
    (62, 80, 3.0),   # Eb
    (61, 80, 3.25),  # D
    (60, 80, 3.5),   # C
    (59, 80, 3.75),  # B
]
for note, velocity, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (comping)
piano_notes = [
    (62, 90, 3.25),  # Eb7 (Eb, G, Bb, Db)
    (60, 90, 3.25),  # Bb
    (65, 90, 3.25),  # F
    (62, 90, 3.25),  # Db

    (59, 90, 3.75),  # B7 (B, D#, F#, A)
    (57, 90, 3.75),  # G
    (62, 90, 3.75),  # C
    (59, 90, 3.75),  # A
]
for note, velocity, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 100, 3.0),  # Kick on 1
    (42, 100, 3.0),  # Hihat on 1
    (38, 100, 3.25), # Snare on 2
    (42, 100, 3.25), # Hihat on 2
    (36, 100, 3.5),  # Kick on 3
    (42, 100, 3.5),  # Hihat on 3
    (38, 100, 3.75), # Snare on 4
    (42, 100, 3.75), # Hihat on 4
]
for note, velocity, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolution to the motif (Fm7 chord, sparse, expressive)
sax_notes = [
    (77, 100, 4.5),  # F
    (72, 100, 4.75), # Ab
    (74, 100, 5.0),  # Bb
    (77, 100, 5.25), # F
]
for note, velocity, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line with chromatic approaches (Eb7 -> Fm7)
bass_notes = [
    (59, 80, 4.5),   # B
    (58, 80, 4.75),  # Bb
    (60, 80, 5.0),   # B
    (64, 80, 5.25),  # F
]
for note, velocity, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (comping)
piano_notes = [
    (59, 90, 4.75),  # B7 (B, D#, F#, A)
    (62, 90, 4.75),  # F
    (64, 90, 4.75),  # G
    (60, 90, 4.75),  # Eb

    (64, 90, 5.25),  # F7 (F, A, C, Eb)
    (67, 90, 5.25),  # G
    (72, 90, 5.25),  # Bb
    (64, 90, 5.25),  # C
]
for note, velocity, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 100, 4.5),  # Kick on 1
    (42, 100, 4.5),  # Hihat on 1
    (38, 100, 4.75), # Snare on 2
    (42, 100, 4.75), # Hihat on 2
    (36, 100, 5.0),  # Kick on 3
    (42, 100, 5.0),  # Hihat on 3
    (38, 100, 5.25), # Snare on 4
    (42, 100, 5.25), # Hihat on 4
]
for note, velocity, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_russo_intro.mid')

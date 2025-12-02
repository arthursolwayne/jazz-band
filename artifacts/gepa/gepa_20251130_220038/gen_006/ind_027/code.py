
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif starting on D (D, E, F#, D)
sax_notes = [
    (1.5, 62), (1.75, 64), (2.0, 66), (2.25, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line in D minor (D, Eb, F, G, A, Bb, C, D)
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 65), (2.25, 67),
    (2.5, 69), (2.75, 70), (3.0, 71), (3.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (D7 on 2, Bm7 on 4)
piano_notes = [
    # D7 (D, F#, A, C) on beat 2
    (2.0, 62), (2.0, 66), (2.0, 69), (2.0, 67),
    # Bm7 (B, D, F#, A) on beat 4
    (3.0, 71), (3.0, 62), (3.0, 66), (3.0, 69)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42)
]
for time, note in drum_notes_bar2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continue motif (D, F#, G, A)
sax_notes = [
    (3.0, 62), (3.25, 66), (3.5, 67), (3.75, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line in D minor (D, Eb, F, G, A, Bb, C, D)
bass_notes = [
    (3.0, 62), (3.25, 63), (3.5, 65), (3.75, 67),
    (4.0, 69), (4.25, 70), (4.5, 71), (4.75, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (D7 on 2, Bm7 on 4)
piano_notes = [
    # D7 (D, F#, A, C) on beat 2
    (3.5, 62), (3.5, 66), (3.5, 69), (3.5, 67),
    # Bm7 (B, D, F#, A) on beat 4
    (4.5, 71), (4.5, 62), (4.5, 66), (4.5, 69)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes_bar3:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: complete motif and resolve (D, F#, G, D)
sax_notes = [
    (4.5, 62), (4.75, 66), (5.0, 67), (5.25, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line in D minor (D, Eb, F, G, A, Bb, C, D)
bass_notes = [
    (4.5, 62), (4.75, 63), (5.0, 65), (5.25, 67),
    (5.5, 69), (5.75, 70), (6.0, 71), (6.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (D7 on 2, Bm7 on 4)
piano_notes = [
    # D7 (D, F#, A, C) on beat 2
    (5.0, 62), (5.0, 66), (5.0, 69), (5.0, 67),
    # Bm7 (B, D, F#, A) on beat 4
    (6.0, 71), (6.0, 62), (6.0, 66), (6.0, 69)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar4 = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes_bar4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

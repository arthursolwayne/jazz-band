
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

# Bar 1 - Drums
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - walking in F, chromatic approach to Bb
bass_notes = [
    (1.5, 65), (1.875, 66), (2.25, 67), (2.625, 69),
    (3.0, 71), (3.375, 72), (3.75, 71), (4.125, 69)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2 (1.875)
    (1.875, 59), (1.875, 60), (1.875, 62), (1.875, 64),
    # Bar 2, beat 4 (2.625)
    (2.625, 57), (2.625, 59), (2.625, 60), (2.625, 62),
    # Bar 3, beat 2 (3.375)
    (3.375, 64), (3.375, 65), (3.375, 67), (3.375, 69),
    # Bar 3, beat 4 (4.125)
    (4.125, 67), (4.125, 69), (4.125, 71), (4.125, 72)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax - motif starts now
sax_notes = [
    (1.5, 62), (1.6875, 64), (1.875, 65), (2.0625, 62),
    (2.25, 65), (2.4375, 67), (2.625, 64), (2.8125, 62),
    (3.0, 64), (3.1875, 67), (3.375, 69), (3.5625, 67),
    (3.75, 69), (3.9375, 71), (4.125, 67), (4.3125, 64)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

# Bar 3: Drums
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 36), (7.125, 42),
    (7.5, 38), (7.875, 42), (8.25, 38), (8.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4: Full quartet (3.0 - 6.0s)

# Bass line - walking in F, chromatic approach to Bb
bass_notes = [
    (3.0, 71), (3.375, 72), (3.75, 71), (4.125, 69),
    (4.5, 67), (4.875, 66), (5.25, 65), (5.625, 64),
    (6.0, 65), (6.375, 66), (6.75, 67), (7.125, 69)
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(n)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4, beat 2 (3.375)
    (3.375, 64), (3.375, 65), (3.375, 67), (3.375, 69),
    # Bar 4, beat 4 (4.125)
    (4.125, 64), (4.125, 65), (4.125, 67), (4.125, 69),
    # Bar 5, beat 2 (4.875)
    (4.875, 64), (4.875, 65), (4.875, 67), (4.875, 69),
    # Bar 5, beat 4 (5.625)
    (5.625, 64), (5.625, 65), (5.625, 67), (5.625, 69)
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(n)

# Sax - motif resolves now
sax_notes = [
    (3.0, 62), (3.1875, 64), (3.375, 65), (3.5625, 62),
    (3.75, 64), (3.9375, 67), (4.125, 64), (4.3125, 62),
    (4.5, 64), (4.6875, 67), (4.875, 69), (5.0625, 67),
    (5.25, 69), (5.4375, 71), (5.625, 67), (5.8125, 64),
    (6.0, 64), (6.1875, 67), (6.375, 69), (6.5625, 67),
    (6.75, 69), (6.9375, 71), (7.125, 67), (7.3125, 64)
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

# Bar 4: Drums
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 36), (7.125, 42),
    (7.5, 38), (7.875, 42), (8.25, 38), (8.625, 42)
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

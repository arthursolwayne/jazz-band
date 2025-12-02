
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
    (0.0, 36),  # Kick on 1
    (0.75, 42), # Hihat on 2
    (1.125, 42), # Hihat on 3
    (1.5, 38)   # Snare on 4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: F, G, Ab, Bb
sax_notes = [
    (1.5, 84),  # F
    (1.75, 87), # G
    (2.0, 86),  # Ab
    (2.25, 83)  # Bb
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: F, G, Ab, Bb
bass_notes = [
    (1.5, 65),  # F
    (1.75, 67), # G
    (2.0, 66),  # Ab
    (2.25, 64)  # Bb
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: Bb7 on 2 and 4
piano_notes = [
    (1.75, 73),  # Bb
    (1.75, 77),  # D
    (1.75, 78),  # Eb
    (1.75, 81),  # G
    (2.25, 73),  # Bb
    (2.25, 77),  # D
    (2.25, 78),  # Eb
    (2.25, 81)   # G
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36),  # Kick on 1
    (1.75, 38), # Snare on 2
    (2.0, 36),  # Kick on 3
    (2.25, 38), # Snare on 4
    (1.5, 42),  # Hihat on 1
    (1.625, 42), # Hihat on 2
    (1.75, 42), # Hihat on 3
    (1.875, 42), # Hihat on 4
    (2.0, 42),  # Hihat on 1
    (2.125, 42), # Hihat on 2
    (2.25, 42), # Hihat on 3
    (2.375, 42)  # Hihat on 4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: D, Eb, F, G
sax_notes = [
    (3.0, 80),  # D
    (3.25, 81), # Eb
    (3.5, 84),  # F
    (3.75, 87)  # G
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: D, Eb, F, G
bass_notes = [
    (3.0, 62),  # D
    (3.25, 63), # Eb
    (3.5, 65),  # F
    (3.75, 67)  # G
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: G7 on 2 and 4
piano_notes = [
    (3.25, 78),  # G
    (3.25, 81),  # Bb
    (3.25, 82),  # B
    (3.25, 84),  # D
    (3.75, 78),  # G
    (3.75, 81),  # Bb
    (3.75, 82),  # B
    (3.75, 84)   # D
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36),  # Kick on 1
    (3.25, 38), # Snare on 2
    (3.5, 36),  # Kick on 3
    (3.75, 38), # Snare on 4
    (3.0, 42),  # Hihat on 1
    (3.125, 42), # Hihat on 2
    (3.25, 42), # Hihat on 3
    (3.375, 42), # Hihat on 4
    (3.5, 42),  # Hihat on 1
    (3.625, 42), # Hihat on 2
    (3.75, 42), # Hihat on 3
    (3.875, 42)  # Hihat on 4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: Ab, Bb, C, D
sax_notes = [
    (4.5, 86),  # Ab
    (4.75, 83), # Bb
    (5.0, 85),  # C
    (5.25, 80)  # D
]
for time, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line: Ab, Bb, C, D
bass_notes = [
    (4.5, 66),  # Ab
    (4.75, 64), # Bb
    (5.0, 67),  # C
    (5.25, 62)  # D
]
for time, note in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: C7 on 2 and 4
piano_notes = [
    (4.75, 72),  # C
    (4.75, 76),  # E
    (4.75, 77),  # F
    (4.75, 79),  # G
    (5.25, 72),  # C
    (5.25, 76),  # E
    (5.25, 77),  # F
    (5.25, 79)   # G
]
for time, note in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36),  # Kick on 1
    (4.75, 38), # Snare on 2
    (5.0, 36),  # Kick on 3
    (5.25, 38), # Snare on 4
    (4.5, 42),  # Hihat on 1
    (4.625, 42), # Hihat on 2
    (4.75, 42), # Hihat on 3
    (4.875, 42), # Hihat on 4
    (5.0, 42),  # Hihat on 1
    (5.125, 42), # Hihat on 2
    (5.25, 42), # Hihat on 3
    (5.375, 42)  # Hihat on 4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")

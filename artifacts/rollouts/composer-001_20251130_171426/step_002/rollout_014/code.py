
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody in Fm
sax_notes = [
    (64, 1.5, 0.375),  # F (root)
    (66, 1.875, 0.375),  # Gb
    (69, 2.25, 0.375),  # A
    (67, 2.625, 0.375)  # Bb
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line in Fm
bass_notes = [
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375),  # Gb
    (48, 2.25, 0.375),  # A
    (47, 2.625, 0.375)  # Bb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (64, 1.875, 0.375),  # F7 - F, Ab, Bb, C
    (69, 1.875, 0.375),
    (67, 1.875, 0.375),
    (72, 1.875, 0.375),
    (64, 2.625, 0.375),  # F7 again
    (69, 2.625, 0.375),
    (67, 2.625, 0.375),
    (72, 2.625, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1] + 1.5, end=note[2] + 1.5))

# Bass: Walking line
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1] + 1.5, end=note[2] + 1.5))

# Piano: 7th chords on 2 and 4
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1] + 1.5, end=note[2] + 1.5))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1] + 3.0, end=note[2] + 3.0))

# Bass: Walking line
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1] + 3.0, end=note[2] + 3.0))

# Piano: 7th chords on 2 and 4
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1] + 3.0, end=note[2] + 3.0))

# Drums: Bar 4
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1] + 3.0, end=note[2] + 3.0))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")

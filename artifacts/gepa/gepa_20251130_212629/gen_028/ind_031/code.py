
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.625))

# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7: D, F, A, C
# Walking line: D, Eb, F, G, A, Bb, B, C, D...

bass_notes = [
    (1.5, 50, 1),  # D
    (1.875, 48, 1),  # Eb
    (2.25, 53, 1),  # F
    (2.625, 55, 1),  # G
    (3.0, 57, 1),  # A
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
piano_notes = [
    (1.875, 50, 100),  # D
    (1.875, 53, 100),  # F
    (1.875, 57, 100),  # A
    (1.875, 60, 100),  # C
    (3.0, 50, 100),  # D
    (3.0, 53, 100),  # F
    (3.0, 57, 100),  # A
    (3.0, 60, 100),  # C
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm: D, Eb, F, G, A, Bb, B, C
# Motif: D (1.5), Eb (1.75), F (2.0), rest (2.375), then D (3.0), Eb (3.25), F (3.5)

sax_notes = [
    (1.5, 50, 100),
    (1.75, 48, 100),
    (2.0, 53, 100),
    (3.0, 50, 100),
    (3.25, 48, 100),
    (3.5, 53, 100)
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Continue the walking line
bass_notes = [
    (3.375, 62, 1),  # Bb
    (3.75, 64, 1),  # B
    (4.125, 67, 1),  # C
    (4.5, 50, 1),  # D
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano: comp on 2 and 4
piano_notes = [
    (3.75, 50, 100),  # D
    (3.75, 53, 100),  # F
    (3.75, 57, 100),  # A
    (3.75, 60, 100),  # C
    (4.5, 50, 100),  # D
    (4.5, 53, 100),  # F
    (4.5, 57, 100),  # A
    (4.5, 60, 100),  # C
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax: continue motif
sax_notes = [
    (3.5, 55, 100),  # G
    (3.75, 50, 100),  # D
    (4.0, 48, 100),  # Eb
    (4.25, 53, 100),  # F
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Continue the walking line
bass_notes = [
    (4.875, 53, 1),  # F
    (5.25, 55, 1),  # G
    (5.625, 57, 1),  # A
    (6.0, 50, 1),  # D
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano: comp on 2 and 4
piano_notes = [
    (5.25, 50, 100),  # D
    (5.25, 53, 100),  # F
    (5.25, 57, 100),  # A
    (5.25, 60, 100),  # C
    (6.0, 50, 100),  # D
    (6.0, 53, 100),  # F
    (6.0, 57, 100),  # A
    (6.0, 60, 100),  # C
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Sax: finish the motif
sax_notes = [
    (4.75, 55, 100),  # G
    (5.0, 57, 100),  # A
    (5.25, 50, 100),  # D
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

# Drums: fill the bar
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125))

# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

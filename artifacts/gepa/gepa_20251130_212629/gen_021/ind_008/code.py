
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), # Kick on 1
    (0.375, 42), # Hihat on 2
    (0.75, 38), # Snare on 2
    (1.125, 42), # Hihat on 3
    (1.5, 36), # Kick on 3
    (1.875, 42), # Hihat on 4
    (2.25, 38), # Snare on 4
    (2.625, 42) # Hihat on 4
]

for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - walking line with chromatic approaches
bass_notes = [
    (1.5, 65), # D (root)
    (1.75, 66), # Eb (chromatic)
    (2.0, 67), # E (3rd)
    (2.25, 69), # F# (5th)
    (2.5, 67), # E (3rd)
    (2.75, 66), # Eb (chromatic)
    (3.0, 65), # D (root)
    (3.25, 64)  # C (chromatic)
]

for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Diane - 7th chords on 2 and 4
piano_notes = [
    (1.5, 67), # D7: D (root)
    (1.75, 71), # F# (3rd)
    (2.0, 74), # A (5th)
    (2.25, 76), # C (7th)
    (2.5, 67), # D7 again
    (2.75, 71),
    (3.0, 74),
    (3.25, 76)
]

for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), # Kick on 1
    (1.875, 42), # Hihat on 2
    (2.25, 38), # Snare on 2
    (2.625, 42), # Hihat on 3
    (3.0, 36), # Kick on 3
    (3.375, 42), # Hihat on 4
    (3.75, 38), # Snare on 4
    (4.125, 42) # Hihat on 4
]

for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(drum_note)

# Dante - sax, one short motif
# Start with a short phrase (D, G, Bb), leave it hanging
sax_notes = [
    (1.5, 62), # D
    (1.75, 67), # G
    (2.0, 60), # Bb
    (2.25, 60), # Bb (rest here, let it hang)
    (2.5, 62), # D (come back)
    (2.75, 67), # G
    (3.0, 60), # Bb
    (3.25, 60)  # Bb (end on a question)
]

for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - walking line with chromatic approaches
bass_notes = [
    (3.0, 65), # D (root)
    (3.25, 66), # Eb (chromatic)
    (3.5, 67), # E (3rd)
    (3.75, 69), # F# (5th)
    (4.0, 67), # E (3rd)
    (4.25, 66), # Eb (chromatic)
    (4.5, 65), # D (root)
    (4.75, 64)  # C (chromatic)
]

for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Diane - 7th chords on 2 and 4
piano_notes = [
    (3.0, 67), # D7: D (root)
    (3.25, 71), # F# (3rd)
    (3.5, 74), # A (5th)
    (3.75, 76), # C (7th)
    (4.0, 67), # D7 again
    (4.25, 71),
    (4.5, 74),
    (4.75, 76)
]

for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), # Kick on 1
    (3.375, 42), # Hihat on 2
    (3.75, 38), # Snare on 2
    (4.125, 42), # Hihat on 3
    (4.5, 36), # Kick on 3
    (4.875, 42), # Hihat on 4
    (5.25, 38), # Snare on 4
    (5.625, 42) # Hihat on 4
]

for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(drum_note)

# Dante - sax, continuation of the motif, subtle variation
sax_notes = [
    (3.0, 62), # D
    (3.25, 67), # G
    (3.5, 60), # Bb
    (3.75, 60), # Bb (rest)
    (4.0, 62), # D
    (4.25, 67), # G
    (4.5, 60), # Bb
    (4.75, 60)  # Bb (end on a question)
]

for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - walking line with chromatic approaches
bass_notes = [
    (4.5, 65), # D (root)
    (4.75, 66), # Eb (chromatic)
    (5.0, 67), # E (3rd)
    (5.25, 69), # F# (5th)
    (5.5, 67), # E (3rd)
    (5.75, 66), # Eb (chromatic)
    (6.0, 65), # D (root)
    (6.25, 64)  # C (chromatic)
]

for start, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(bass_note)

# Diane - 7th chords on 2 and 4
piano_notes = [
    (4.5, 67), # D7: D (root)
    (4.75, 71), # F# (3rd)
    (5.0, 74), # A (5th)
    (5.25, 76), # C (7th)
    (5.5, 67), # D7 again
    (5.75, 71),
    (6.0, 74),
    (6.25, 76)
]

for start, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(piano_note)

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), # Kick on 1
    (4.875, 42), # Hihat on 2
    (5.25, 38), # Snare on 2
    (5.625, 42), # Hihat on 3
    (6.0, 36), # Kick on 3
    (6.375, 42), # Hihat on 4
    (6.75, 38), # Snare on 4
    (7.125, 42) # Hihat on 4
]

for start, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(drum_note)

# Dante - sax, end on a question
sax_notes = [
    (4.5, 62), # D
    (4.75, 67), # G
    (5.0, 60), # Bb
    (5.25, 60), # Bb (rest)
    (5.5, 62), # D
    (5.75, 67), # G
    (6.0, 60), # Bb
    (6.25, 60)  # Bb (end on a question)
]

for start, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

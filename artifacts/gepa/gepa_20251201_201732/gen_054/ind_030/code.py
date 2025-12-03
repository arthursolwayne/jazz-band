
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 to F2, walking line with chromatic approaches
bass_notes = [
    (1.5, 38), (1.75, 40), (2.0, 38), (2.25, 41),
    (2.5, 43), (2.75, 41), (3.0, 40), (3.25, 38)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, resolving on bar 2
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 77),
    (2.0, 60), (2.0, 65), (2.0, 70), (2.0, 76),
    (2.5, 60), (2.5, 64), (2.5, 69), (2.5, 74),
    (3.0, 62), (3.0, 67), (3.0, 72), (3.0, 77)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif starting on D3 (62), with a syncopated rhythm
sax_notes = [
    (1.5, 62), (1.75, 67), (2.0, 64), (2.25, 62),
    (2.5, 67), (2.75, 72), (3.0, 69), (3.25, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 to Bb2, walking line with chromatic approaches
bass_notes = [
    (3.0, 43), (3.25, 45), (3.5, 43), (3.75, 44),
    (4.0, 46), (4.25, 44), (4.5, 43), (4.75, 45)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, resolving on bar 3
piano_notes = [
    (3.0, 62), (3.0, 67), (3.0, 72), (3.0, 77),
    (3.5, 62), (3.5, 67), (3.5, 72), (3.5, 77),
    (4.0, 64), (4.0, 69), (4.0, 74), (4.0, 79),
    (4.5, 62), (4.5, 67), (4.5, 72), (4.5, 77)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif variation, using the same phrase, but with dynamic contrast
sax_notes = [
    (3.0, 62), (3.25, 67), (3.5, 64), (3.75, 67),
    (4.0, 62), (4.25, 67), (4.5, 64), (4.75, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C2 to D2, walking line with chromatic approaches
bass_notes = [
    (4.5, 44), (4.75, 46), (5.0, 44), (5.25, 45),
    (5.5, 43), (5.75, 45), (6.0, 44), (6.25, 46)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, resolving on bar 4
piano_notes = [
    (4.5, 62), (4.5, 67), (4.5, 72), (4.5, 77),
    (5.0, 64), (5.0, 69), (5.0, 74), (5.0, 79),
    (5.5, 62), (5.5, 67), (5.5, 72), (5.5, 77),
    (6.0, 62), (6.0, 67), (6.0, 72), (6.0, 77)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif resolution, full phrase with dynamic build
sax_notes = [
    (4.5, 62), (4.75, 67), (5.0, 64), (5.25, 62),
    (5.5, 67), (5.75, 72), (6.0, 69), (6.25, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

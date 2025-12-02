
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar at 120 BPM

# Bar 1: Drums only
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100),  # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 100),  # Hihat on 4
    (1.5, 36, 100),  # Kick on 1 (next bar)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: C Eb G Bb (C7, Bb7, G7, Eb7)
sax_notes = [
    (1.5, 60, 100),  # C
    (1.75, 62, 100),  # Eb
    (2.0, 67, 100),  # G
    (2.25, 62, 100),  # Bb
    (2.5, 60, 100),  # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass line: Walking chromatic line starting at C
bass_notes = [
    (1.5, 60, 100),  # C
    (1.75, 61, 100),  # C#
    (2.0, 62, 100),  # D
    (2.25, 63, 100),  # D#
    (2.5, 64, 100),  # E
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 60, 100),  # C
    (1.75, 64, 100),  # E
    (1.75, 67, 100),  # G
    (1.75, 71, 100),  # Bb
    (2.25, 60, 100),  # C
    (2.25, 64, 100),  # E
    (2.25, 67, 100),  # G
    (2.25, 71, 100),  # Bb
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums for Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.875, 42, 100),  # Hihat on 2
    (2.25, 38, 100),  # Snare on 3
    (2.625, 42, 100),  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: Bb G Eb C (Bb7, G7, Eb7, C7)
sax_notes = [
    (3.0, 62, 100),  # Bb
    (3.25, 67, 100),  # G
    (3.5, 62, 100),  # Eb
    (3.75, 60, 100),  # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass line: Walking chromatic line starting at Bb
bass_notes = [
    (3.0, 62, 100),  # Bb
    (3.25, 63, 100),  # B
    (3.5, 64, 100),  # C
    (3.75, 65, 100),  # C#
    (4.0, 66, 100),  # D
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 62, 100),  # Bb
    (3.25, 65, 100),  # D
    (3.25, 67, 100),  # G
    (3.25, 71, 100),  # Bb
    (3.75, 62, 100),  # Bb
    (3.75, 65, 100),  # D
    (3.75, 67, 100),  # G
    (3.75, 71, 100),  # Bb
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums for Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.375, 42, 100),  # Hihat on 2
    (3.75, 38, 100),  # Snare on 3
    (4.125, 42, 100),  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: C Eb G Bb (C7, Bb7, G7, Eb7)
sax_notes = [
    (4.5, 60, 100),  # C
    (4.75, 62, 100),  # Eb
    (5.0, 67, 100),  # G
    (5.25, 62, 100),  # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass line: Walking chromatic line starting at C
bass_notes = [
    (4.5, 60, 100),  # C
    (4.75, 61, 100),  # C#
    (5.0, 62, 100),  # D
    (5.25, 63, 100),  # D#
    (5.5, 64, 100),  # E
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 60, 100),  # C
    (4.75, 64, 100),  # E
    (4.75, 67, 100),  # G
    (4.75, 71, 100),  # Bb
    (5.25, 60, 100),  # C
    (5.25, 64, 100),  # E
    (5.25, 67, 100),  # G
    (5.25, 71, 100),  # Bb
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums for Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 100),  # Hihat on 2
    (5.25, 38, 100),  # Snare on 3
    (5.625, 42, 100),  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")

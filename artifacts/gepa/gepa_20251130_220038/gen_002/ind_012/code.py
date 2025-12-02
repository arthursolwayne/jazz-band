
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
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100),  # Hihat on 2
    (0.75, 38, 100),  # Snare on 3
    (1.125, 42, 100),  # Hihat on 4
    (1.5, 36, 100),  # Kick on 1 (end of bar)
]

# Add drums
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 62, 100),  # D (root)
    (1.875, 63, 100),  # Eb (chromatic approach)
    (2.25, 65, 100),  # F (3rd)
    (2.625, 67, 100),  # G (5th)
    (3.0, 69, 100),  # A (7th)
    (3.375, 71, 100),  # Bb (chromatic approach)
    (3.75, 72, 100),  # B (leading tone)
    (4.125, 71, 100),  # Bb (chromatic approach)
    (4.5, 69, 100),  # A (7th)
    (4.875, 67, 100),  # G (5th)
    (5.25, 65, 100),  # F (3rd)
    (5.625, 63, 100),  # Eb (chromatic approach)
    (6.0, 62, 100)  # D (root)
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62, 100),  # D7: D
    (1.875, 67, 100),  # D7: G
    (1.875, 71, 100),  # D7: Bb
    (2.25, 64, 100),  # D7: F
    # Bar 3
    (3.375, 62, 100),  # D7: D
    (3.375, 67, 100),  # D7: G
    (3.375, 71, 100),  # D7: Bb
    (3.75, 64, 100),  # D7: F
    # Bar 4
    (4.875, 62, 100),  # D7: D
    (4.875, 67, 100),  # D7: G
    (4.875, 71, 100),  # D7: Bb
    (5.25, 64, 100),  # D7: F
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

# Sax: Motif in D, playing the melody
sax_notes = [
    (1.5, 62, 100),  # D
    (1.875, 67, 100),  # G
    (2.25, 71, 100),  # Bb
    (2.625, 69, 100),  # A
    (3.0, 62, 100),  # D
    (3.375, 67, 100),  # G
    (3.75, 71, 100),  # Bb
    (4.125, 69, 100),  # A
    (4.5, 62, 100),  # D
    (4.875, 67, 100),  # G
    (5.25, 71, 100),  # Bb
    (5.625, 69, 100)  # A
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")

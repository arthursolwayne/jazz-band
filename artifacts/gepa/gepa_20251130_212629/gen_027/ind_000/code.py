
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
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 80), # Hihat on 2
    (0.75, 38, 100), # Snare on 2
    (1.125, 42, 80), # Hihat on 3
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 80), # Hihat on 4
    (2.25, 38, 100), # Snare on 4
    (2.625, 42, 80)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 64, 100), # F (root)
    (1.75, 65, 100), # Gb (chromatic)
    (2.0, 62, 100), # Eb (3rd)
    (2.25, 63, 100), # E (chromatic)
    (2.5, 60, 100), # C (5th)
    (2.75, 61, 100), # C# (chromatic)
    (3.0, 59, 100)  # Bb (7th)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.5, 64, 90), # F7 (F, A, C, Eb)
    (1.75, 69, 90),
    (2.0, 60, 90),
    (2.25, 62, 90),
    (2.5, 72, 90), # F7 on 2
    (2.75, 77, 90),
    (3.0, 69, 90),
    (3.25, 72, 90)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Melody - short motif, make it sing
sax_notes = [
    (1.5, 66, 100), # G (Fm scale)
    (1.75, 64, 100), # F
    (2.0, 67, 100), # G#
    (2.25, 64, 100), # F
    (2.5, 66, 100), # G
    (2.75, 69, 100), # Bb
    (3.0, 64, 100), # F (end on root, with a question)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (3.0, 64, 100), # F (root)
    (3.25, 65, 100), # Gb (chromatic)
    (3.5, 62, 100), # Eb (3rd)
    (3.75, 63, 100), # E (chromatic)
    (4.0, 60, 100), # C (5th)
    (4.25, 61, 100), # C# (chromatic)
    (4.5, 59, 100)  # Bb (7th)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.0, 64, 90), # F7 (F, A, C, Eb)
    (3.25, 69, 90),
    (3.5, 60, 90),
    (3.75, 62, 90),
    (4.0, 72, 90), # F7 on 2
    (4.25, 77, 90),
    (4.5, 69, 90),
    (4.75, 72, 90)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.375, 42, 80), # Hihat on 2
    (3.75, 38, 100), # Snare on 2
    (4.125, 42, 80), # Hihat on 3
    (4.5, 36, 100),  # Kick on 3
    (4.875, 42, 80), # Hihat on 4
    (5.25, 38, 100), # Snare on 4
    (5.625, 42, 80)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (4.5, 64, 100), # F (root)
    (4.75, 65, 100), # Gb (chromatic)
    (5.0, 62, 100), # Eb (3rd)
    (5.25, 63, 100), # E (chromatic)
    (5.5, 60, 100), # C (5th)
    (5.75, 61, 100), # C# (chromatic)
    (6.0, 59, 100)  # Bb (7th)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.5, 64, 90), # F7 (F, A, C, Eb)
    (4.75, 69, 90),
    (5.0, 60, 90),
    (5.25, 62, 90),
    (5.5, 72, 90), # F7 on 2
    (5.75, 77, 90),
    (6.0, 69, 90),
    (6.25, 72, 90)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 80), # Hihat on 2
    (5.25, 38, 100), # Snare on 2
    (5.625, 42, 80), # Hihat on 3
    (6.0, 36, 100),  # Kick on 3
    (6.375, 42, 80), # Hihat on 4
    (6.75, 38, 100), # Snare on 4
    (7.125, 42, 80)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Sax: Melody variation
sax_notes = [
    (4.5, 67, 100), # G# (departure)
    (4.75, 71, 100), # B (chromatic)
    (5.0, 69, 100), # Bb (touch back)
    (5.25, 67, 100), # G#
    (5.5, 69, 100), # Bb
    (5.75, 64, 100), # F (return to root)
    (6.0, 62, 100), # Eb (question)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")

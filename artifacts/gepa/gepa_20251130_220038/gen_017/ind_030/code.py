
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
    # Kick on 1 and 3
    (0.0, 36, 100),
    (0.75, 36, 100),
    # Snare on 2 and 4
    (0.375, 38, 100),
    (1.125, 38, 100),
    # Hi-hat on every eighth
    (0.0, 42, 100),
    (0.375, 42, 100),
    (0.75, 42, 100),
    (1.125, 42, 100),
    (1.5, 42, 100)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts
sax_notes = [
    (1.5, 64, 100),  # Fm7: F, Ab, Bb, D
    (1.75, 67, 100),  # Bb
    (2.0, 64, 100),  # F
    (2.25, 69, 100)   # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bass: Walking line in Fm
bass_notes = [
    (1.5, 43, 100),  # F
    (1.75, 42, 100),  # Eb
    (2.0, 41, 100),  # D
    (2.25, 43, 100),  # F
    (2.5, 46, 100),  # Ab
    (2.75, 48, 100),  # Bb
    (3.0, 46, 100),  # Ab
    (3.25, 43, 100)   # F
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (1.75, 53, 100),  # F
    (1.75, 60, 100),  # Ab
    (1.75, 62, 100),  # Bb
    (1.75, 67, 100),  # D
    # Bar 3: Bb7 on beat 2
    (2.75, 57, 100),  # Bb
    (2.75, 64, 100),  # D
    (2.75, 66, 100),  # F
    (2.75, 71, 100),  # Ab
    # Bar 4: Fm7 on beat 2
    (3.75, 53, 100),  # F
    (3.75, 60, 100),  # Ab
    (3.75, 62, 100),  # Bb
    (3.75, 67, 100)   # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: Bar 2
drum_notes = [
    (1.5, 36, 100),
    (1.875, 38, 100),
    (2.25, 36, 100),
    (2.625, 38, 100),
    (3.0, 36, 100),
    (3.375, 38, 100),
    (3.75, 36, 100),
    (4.125, 38, 100),
    (1.5, 42, 100),
    (1.875, 42, 100),
    (2.25, 42, 100),
    (2.625, 42, 100),
    (3.0, 42, 100),
    (3.375, 42, 100),
    (3.75, 42, 100),
    (4.125, 42, 100)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    (3.0, 69, 100),  # D
    (3.25, 64, 100),  # F
    (3.5, 67, 100),  # Bb
    (3.75, 69, 100)   # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bass: Walking line in Fm
bass_notes = [
    (3.0, 43, 100),  # F
    (3.25, 42, 100),  # Eb
    (3.5, 41, 100),  # D
    (3.75, 43, 100),  # F
    (4.0, 46, 100),  # Ab
    (4.25, 48, 100),  # Bb
    (4.5, 46, 100),  # Ab
    (4.75, 43, 100)   # F
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    (3.75, 57, 100),  # Bb
    (3.75, 64, 100),  # D
    (3.75, 66, 100),  # F
    (3.75, 71, 100),  # Ab
    # Bar 4: Fm7 on beat 2
    (4.75, 53, 100),  # F
    (4.75, 60, 100),  # Ab
    (4.75, 62, 100),  # Bb
    (4.75, 67, 100)   # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: Bar 3
drum_notes = [
    (3.0, 36, 100),
    (3.375, 38, 100),
    (3.75, 36, 100),
    (4.125, 38, 100),
    (4.5, 36, 100),
    (4.875, 38, 100),
    (5.25, 36, 100),
    (5.625, 38, 100),
    (3.0, 42, 100),
    (3.375, 42, 100),
    (3.75, 42, 100),
    (4.125, 42, 100),
    (4.5, 42, 100),
    (4.875, 42, 100),
    (5.25, 42, 100),
    (5.625, 42, 100)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolve motif
sax_notes = [
    (4.5, 64, 100),  # F
    (4.75, 67, 100),  # Bb
    (5.0, 64, 100),  # F
    (5.25, 62, 100),  # Bb
    (5.5, 64, 100),  # F
    (5.75, 69, 100)   # D
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bass: Walking line in Fm
bass_notes = [
    (4.5, 43, 100),  # F
    (4.75, 42, 100),  # Eb
    (5.0, 41, 100),  # D
    (5.25, 43, 100),  # F
    (5.5, 46, 100),  # Ab
    (5.75, 48, 100),  # Bb
    (6.0, 46, 100),  # Ab
    (6.25, 43, 100)   # F
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    (4.75, 53, 100),  # F
    (4.75, 60, 100),  # Ab
    (4.75, 62, 100),  # Bb
    (4.75, 67, 100),  # D
    # Bar 4: Fm7 on beat 4
    (5.75, 53, 100),  # F
    (5.75, 60, 100),  # Ab
    (5.75, 62, 100),  # Bb
    (5.75, 67, 100)   # D
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: Bar 4
drum_notes = [
    (4.5, 36, 100),
    (4.875, 38, 100),
    (5.25, 36, 100),
    (5.625, 38, 100),
    (6.0, 36, 100),
    (6.375, 38, 100),
    (6.75, 36, 100),
    (7.125, 38, 100),
    (4.5, 42, 100),
    (4.875, 42, 100),
    (5.25, 42, 100),
    (5.625, 42, 100),
    (6.0, 42, 100),
    (6.375, 42, 100),
    (6.75, 42, 100),
    (7.125, 42, 100)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")

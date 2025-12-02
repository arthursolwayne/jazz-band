
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
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 60), # Hihat
    (0.75, 38, 90),  # Snare on 2
    (1.125, 42, 60), # Hihat
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 60), # Hihat
    (2.25, 38, 90),  # Snare on 4
    (2.625, 42, 60)  # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Marcus - Walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62, 80), # D
    (1.75, 60, 80), # Bb (chromatic)
    (2.0, 62, 80), # D
    (2.25, 64, 80), # F (chromatic)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane - 7th chords on 2 and 4, Dm7
piano_notes = [
    (1.75, 62, 90), # D
    (1.75, 67, 70), # G
    (1.75, 67, 70), # G
    (1.75, 71, 60), # C
    (2.25, 62, 90), # D
    (2.25, 67, 70), # G
    (2.25, 67, 70), # G
    (2.25, 71, 60), # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Dante - Sax melody (sparse, expressive, starts on beat 2)
sax_notes = [
    (1.75, 65, 100), # E
    (2.0, 67, 100),  # G
    (2.25, 62, 90),  # D
    (2.5, 65, 100),  # E
    (2.75, 67, 100), # G
    (3.0, 62, 90),   # D
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bar 3: (3.0 - 4.5s)
# Marcus - Walking line with chromatic passing
bass_notes = [
    (3.0, 64, 80), # F
    (3.25, 62, 80), # D
    (3.5, 64, 80), # F
    (3.75, 66, 80), # A (chromatic)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane - 7th chords with space
piano_notes = [
    (3.25, 62, 90), # D
    (3.25, 67, 70), # G
    (3.25, 67, 70), # G
    (3.25, 71, 60), # C
    (3.75, 62, 90), # D
    (3.75, 67, 70), # G
    (3.75, 67, 70), # G
    (3.75, 71, 60), # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Dante - Sax continues, with a pause for space
sax_notes = [
    (3.25, 62, 90), # D
    (3.5, 67, 100), # G
    (3.75, 65, 100), # E
    (4.0, 62, 90),   # D
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bar 4: (4.5 - 6.0s)
# Marcus - Walking line
bass_notes = [
    (4.5, 62, 80), # D
    (4.75, 64, 80), # F
    (5.0, 62, 80), # D
    (5.25, 67, 80), # G
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane - 7th chords with space, ends on Dm7
piano_notes = [
    (4.75, 62, 90), # D
    (4.75, 67, 70), # G
    (4.75, 67, 70), # G
    (4.75, 71, 60), # C
    (5.25, 62, 90), # D
    (5.25, 67, 70), # G
    (5.25, 67, 70), # G
    (5.25, 71, 60), # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Little Ray - Drums continue
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 60), # Hihat
    (5.25, 38, 90),  # Snare on 2
    (5.625, 42, 60), # Hihat
    (6.0, 36, 100),  # Kick on 3
    (6.375, 42, 60), # Hihat
    (6.75, 38, 90),  # Snare on 4
    (7.125, 42, 60)  # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Dante - Sax ends with a lingering note
sax_notes = [
    (5.25, 67, 100), # G
    (5.5, 65, 100),  # E
    (5.75, 62, 90),  # D
    (6.0, 62, 80),   # D (sustained)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

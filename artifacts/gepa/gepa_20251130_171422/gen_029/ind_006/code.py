
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Mysterious, sparse, with space and tension
drum_notes = [
    (0.0, 36, 80),  # Kick on 1
    (0.75, 42, 60), # Hihat on & of 1
    (1.0, 38, 90),  # Snare on 2
    (1.5, 42, 60)   # Hihat on 3
]
for start, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Tension builds, sax starts the melody, bass walks, piano comps
# Sax motif: F (1st beat), G# (2nd), A (3rd), Bb (4th)
sax_notes = [
    (1.5, 84, 100),  # F4
    (1.75, 86, 110), # G#4
    (2.0, 87, 105),  # A4
    (2.25, 85, 90)   # Bb4
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Marcus's bass line (chromatic walk)
bass_notes = [
    (1.5, 46, 60),  # F3
    (1.75, 47, 65), # F#3
    (2.0, 48, 60),  # G3
    (2.25, 49, 65)  # G#3
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Diane's piano comp: 7th chords on 2 and 4
piano_notes = [
    (1.75, 71, 80),  # F7 (F, A, C, E)
    (2.25, 71, 80),
    (2.25, 74, 75),  # A
    (2.25, 76, 75),  # C
    (2.25, 79, 75)   # E
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Bar 3: (3.0 - 4.5s)
# Glimmer of resolution, sax repeats motif with slight variation
sax_notes = [
    (3.0, 84, 100),  # F4
    (3.25, 86, 100), # G#4
    (3.5, 87, 100),  # A4
    (3.75, 85, 90)   # Bb4
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Marcus's bass line
bass_notes = [
    (3.0, 49, 60),  # G#3
    (3.25, 50, 65), # A3
    (3.5, 51, 60),  # Bb3
    (3.75, 52, 65)  # B3
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Diane's piano comp
piano_notes = [
    (3.25, 71, 80),  # F7
    (3.75, 71, 80),
    (3.75, 74, 75),
    (3.75, 76, 75),
    (3.75, 79, 75)
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Drums
drum_notes = [
    (3.0, 36, 80),  # Kick on 1
    (3.25, 42, 65), # Hihat on & of 1
    (3.5, 38, 90),  # Snare on 2
    (3.75, 42, 65), # Hihat on & of 2
    (4.0, 36, 90),  # Kick on 3
    (4.25, 42, 65), # Hihat on & of 3
    (4.5, 38, 90)   # Snare on 4
]
for start, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bar 4: (4.5 - 6.0s)
# Lingering question, sax ends with a rest on the last beat
sax_notes = [
    (4.5, 87, 100),  # A4 on beat 1
    (4.75, 87, 100), # A4 on & of 1
    (5.0, 87, 100),  # A4 on beat 2
    (5.25, 87, 100), # A4 on & of 2
    (5.5, 87, 100),  # A4 on beat 3
    (5.75, 87, 100), # A4 on & of 3
    (6.0, 87, 100)   # A4 on beat 4
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Marcus's bass line
bass_notes = [
    (4.5, 52, 60),  # B3
    (4.75, 53, 65), # C4
    (5.0, 54, 60),  # C#4
    (5.25, 55, 65), # D4
    (5.5, 56, 60),  # D#4
    (5.75, 57, 65), # E4
    (6.0, 58, 60)   # F4
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Diane's piano comp
piano_notes = [
    (4.5, 71, 80),  # F7
    (4.75, 71, 80),
    (5.0, 71, 80),
    (5.25, 71, 80),
    (5.5, 71, 80),
    (5.75, 71, 80),
    (6.0, 71, 80)
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Drums
drum_notes = [
    (4.5, 36, 90),  # Kick on 1
    (4.75, 42, 65), # Hihat on & of 1
    (5.0, 38, 90),  # Snare on 2
    (5.25, 42, 65), # Hihat on & of 2
    (5.5, 36, 90),  # Kick on 3
    (5.75, 42, 65), # Hihat on & of 3
    (6.0, 38, 90)   # Snare on 4
]
for start, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

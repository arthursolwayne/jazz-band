
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on & of 2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (1.5, 62, 100),  # C5
    (1.75, 65, 100), # E5
    (2.0, 64, 100),  # D5
    (2.25, 62, 100), # C5
    (2.5, 67, 100),  # G5
    (2.75, 69, 100), # A5
    (3.0, 67, 100),  # G5
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line (walking, chromatic approaches)
bass_notes = [
    (1.5, 48, 100),  # C3
    (1.75, 49, 100), # C#3
    (2.0, 50, 100),  # D3
    (2.25, 51, 100), # D#3
    (2.5, 52, 100),  # E3
    (2.75, 53, 100), # F3
    (3.0, 55, 100),  # G3
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano comping on 2 and 4 (7th chords)
piano_notes = [
    (1.75, 64, 100),  # C7 (C E G B)
    (1.75, 69, 100),  # E7
    (1.75, 71, 100),  # G7
    (1.75, 74, 100),  # B7
    (2.75, 64, 100),  # C7
    (2.75, 69, 100),  # E7
    (2.75, 71, 100),  # G7
    (2.75, 74, 100),  # B7
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (repeat of the first 3 notes with variation)
sax_notes = [
    (3.0, 62, 100),  # C5
    (3.25, 65, 100), # E5
    (3.5, 64, 100),  # D5
    (3.75, 62, 100), # C5
    (4.0, 69, 100),  # A5
    (4.25, 67, 100), # G5
    (4.5, 62, 100),  # C5
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line (walking, chromatic approaches)
bass_notes = [
    (3.0, 55, 100),  # G3
    (3.25, 56, 100), # G#3
    (3.5, 57, 100),  # A3
    (3.75, 58, 100), # A#3
    (4.0, 59, 100),  # B3
    (4.25, 60, 100), # C4
    (4.5, 62, 100),  # D4
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano comping on 2 and 4 (7th chords)
piano_notes = [
    (3.25, 64, 100),  # C7
    (3.25, 69, 100),  # E7
    (3.25, 71, 100),  # G7
    (3.25, 74, 100),  # B7
    (4.25, 64, 100),  # C7
    (4.25, 69, 100),  # E7
    (4.25, 71, 100),  # G7
    (4.25, 74, 100),  # B7
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums for Bar 3
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on & of 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.75, 42, 100), # Hihat on & of 2
    (5.0, 36, 100),  # Kick on beat 3
    (5.75, 42, 100), # Hihat on & of 3
    (6.0, 38, 100),  # Snare on beat 4
    (6.75, 42, 100)  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (finish the motif)
sax_notes = [
    (4.5, 64, 100),  # D5
    (4.75, 62, 100), # C5
    (5.0, 67, 100),  # G5
    (5.25, 69, 100), # A5
    (5.5, 67, 100),  # G5
    (5.75, 64, 100), # D5
    (6.0, 62, 100),  # C5
]
for time, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass line (walking, chromatic approaches)
bass_notes = [
    (4.5, 62, 100),  # D4
    (4.75, 63, 100), # D#4
    (5.0, 64, 100),  # E4
    (5.25, 65, 100), # F4
    (5.5, 67, 100),  # G4
    (5.75, 69, 100), # A4
    (6.0, 71, 100),  # B4
]
for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano comping on 2 and 4 (7th chords)
piano_notes = [
    (4.75, 64, 100),  # C7
    (4.75, 69, 100),  # E7
    (4.75, 71, 100),  # G7
    (4.75, 74, 100),  # B7
    (5.75, 64, 100),  # C7
    (5.75, 69, 100),  # E7
    (5.75, 71, 100),  # G7
    (5.75, 74, 100),  # B7
]
for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums for Bar 4
drum_notes = [
    (4.5, 36, 100),  # Kick on beat 1
    (5.25, 42, 100), # Hihat on & of 1
    (5.5, 38, 100),  # Snare on beat 2
    (6.25, 42, 100), # Hihat on & of 2
    (6.5, 36, 100),  # Kick on beat 3
    (7.25, 42, 100), # Hihat on & of 3
    (7.5, 38, 100),  # Snare on beat 4
    (8.25, 42, 100)  # Hihat on & of 4
]
for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")

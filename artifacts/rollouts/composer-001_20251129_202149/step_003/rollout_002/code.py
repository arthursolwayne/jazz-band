
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
    (0.75, 42, 100), # Hihat on beat 2
    (1.5, 38, 100),  # Snare on beat 3
    (2.25, 42, 100), # Hihat on beat 4
    (3.0, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on beat 2
    (4.5, 38, 100),  # Snare on beat 3
    (5.25, 42, 100), # Hihat on beat 4
]
for start, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approach to C
bass_notes = [
    (1.5, 60, 100), # C
    (1.75, 61, 100), # C#
    (2.0, 62, 100), # D
    (2.25, 63, 100), # D#
    (2.5, 64, 100), # E
    (2.75, 65, 100), # F
    (3.0, 64, 100), # E (resolve up)
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 60, 100), # C
    (1.75, 64, 100), # E
    (1.75, 67, 100), # G
    (1.75, 71, 100), # B
    (2.25, 60, 100), # C
    (2.25, 64, 100), # E
    (2.25, 67, 100), # G
    (2.25, 71, 100), # B
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Melody starts here. Short motif, leave it hanging
sax_notes = [
    (1.5, 62, 100), # D
    (1.75, 64, 100), # E
    (2.0, 62, 100), # D
    (2.25, 64, 100), # E
    (2.5, 62, 100), # D
    (2.75, 64, 100), # E
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approach to C
bass_notes = [
    (3.0, 64, 100), # E
    (3.25, 65, 100), # F
    (3.5, 66, 100), # F#
    (3.75, 67, 100), # G
    (4.0, 68, 100), # G#
    (4.25, 69, 100), # A
    (4.5, 67, 100), # G
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 60, 100), # C
    (3.25, 64, 100), # E
    (3.25, 67, 100), # G
    (3.25, 71, 100), # B
    (3.75, 60, 100), # C
    (3.75, 64, 100), # E
    (3.75, 67, 100), # G
    (3.75, 71, 100), # B
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Continue the melody, finish the motif
sax_notes = [
    (3.0, 65, 100), # F
    (3.25, 64, 100), # E
    (3.5, 62, 100), # D
    (3.75, 64, 100), # E
    (4.0, 62, 100), # D
    (4.25, 64, 100), # E
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approach to C
bass_notes = [
    (4.5, 67, 100), # G
    (4.75, 68, 100), # G#
    (5.0, 69, 100), # A
    (5.25, 71, 100), # B
    (5.5, 72, 100), # C
    (5.75, 71, 100), # B
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 60, 100), # C
    (4.75, 64, 100), # E
    (4.75, 67, 100), # G
    (4.75, 71, 100), # B
    (5.25, 60, 100), # C
    (5.25, 64, 100), # E
    (5.25, 67, 100), # G
    (5.25, 71, 100), # B
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Finish the motif, resolution
sax_notes = [
    (4.5, 65, 100), # F
    (4.75, 64, 100), # E
    (5.0, 62, 100), # D
    (5.25, 64, 100), # E
    (5.5, 62, 100), # D
    (5.75, 60, 100), # C
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums: Bar 3-4
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on beat 2
    (4.5, 38, 100),  # Snare on beat 3
    (5.25, 42, 100), # Hihat on beat 4
    (6.0, 36, 100),  # Kick on beat 1
    (6.75, 42, 100), # Hihat on beat 2
    (7.5, 38, 100),  # Snare on beat 3
    (8.25, 42, 100), # Hihat on beat 4
]
for start, pitch, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

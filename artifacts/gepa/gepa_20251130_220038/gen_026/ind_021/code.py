
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
    (0.0, 36), # Kick on 1
    (0.375, 42), # Hihat on 2
    (0.75, 38), # Snare on 2
    (1.125, 42), # Hihat on 3
    (1.5, 36), # Kick on 3
    (1.875, 42), # Hihat on 4
    (2.25, 38), # Snare on 4
    (2.625, 42) # Hihat on 4
]
for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    (1.5, 62), # D (root)
    (1.875, 60), # Bb (chromatic approach)
    (2.25, 64), # F (third)
    (2.625, 66), # G (fifth)
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: Comping with 7th chords (Dm7)
# Comp on 2 and 4
piano_notes = [
    # Dm7: D, F, A, C
    (1.875, 62), (1.875, 64), (1.875, 67), (1.875, 69),
    (2.625, 62), (2.625, 64), (2.625, 67), (2.625, 69)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Start of melody (Dm scale with a twist)
# Whisper at first, then a cry
sax_notes = [
    (1.5, 62), # D
    (1.625, 64), # E
    (1.75, 62), # D
    (2.0, 65), # F#
    (2.25, 67), # G
    (2.5, 65), # F#
    (2.75, 64), # E
    (3.0, 62) # D
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm
bass_notes = [
    (3.0, 62), # D
    (3.375, 60), # Bb
    (3.75, 64), # F
    (4.125, 66), # G
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: Comping with 7th chords (Dm7)
# Comp on 2 and 4
piano_notes = [
    # Dm7: D, F, A, C
    (3.375, 62), (3.375, 64), (3.375, 67), (3.375, 69),
    (4.125, 62), (4.125, 64), (4.125, 67), (4.125, 69)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Continue melody with a slightly altered motif
# Let it breathe, build naturally
sax_notes = [
    (3.0, 62), # D
    (3.125, 64), # E
    (3.25, 61), # C
    (3.5, 62), # D
    (3.75, 65), # F#
    (4.0, 67), # G
    (4.25, 65), # F#
    (4.5, 64) # E
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    (4.5, 62), # D
    (4.875, 60), # Bb
    (5.25, 64), # F
    (5.625, 66) # G
]
for time, note_number in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: Comping with 7th chords (Dm7)
# Comp on 2 and 4
piano_notes = [
    # Dm7: D, F, A, C
    (4.875, 62), (4.875, 64), (4.875, 67), (4.875, 69),
    (5.625, 62), (5.625, 64), (5.625, 67), (5.625, 69)
]
for time, note_number in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: End of melody
# Build naturally, leave it hanging
sax_notes = [
    (4.5, 62), # D
    (4.625, 64), # E
    (4.75, 62), # D
    (5.0, 65), # F#
    (5.25, 67), # G
    (5.5, 65), # F#
    (5.75, 64), # E
    (6.0, 62) # D
]
for time, note_number in sax_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: continue (4.5 - 6.0s)
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
for time, note_number in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

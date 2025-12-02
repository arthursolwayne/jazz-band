
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 36, 100),    # Kick on 1
    (0.75, 42, 100),   # Hihat on &1
    (1.0, 38, 100),    # Snare on 2
    (1.25, 42, 100),   # Hihat on &2
    (1.5, 36, 100),    # Kick on 3
    (1.75, 42, 100),   # Hihat on &3
    (2.0, 38, 100),    # Snare on 4
    (2.25, 42, 100),   # Hihat on &4
]
for time, note_number, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line - walking in Fm
bass_notes = [
    (1.5, 44, 100),    # Fm root (F)
    (1.75, 46, 100),   # b7 (E)
    (2.0, 45, 100),    # 3 (G)
    (2.25, 43, 100),   # b9 (D)
    (2.5, 44, 100),    # F
    (2.75, 47, 100),   # 11 (Ab)
    (3.0, 45, 100),    # G
    (3.25, 43, 100),   # D
]
for time, note_number, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    (1.75, 59, 100),   # C7 (Fm)
    (1.75, 60, 100),   # C7
    (1.75, 64, 100),   # C7
    (1.75, 67, 100),   # C7
    (2.25, 59, 100),   # C7
    (2.25, 60, 100),   # C7
    (2.25, 64, 100),   # C7
    (2.25, 67, 100),   # C7
    (3.0, 59, 100),    # C7
    (3.0, 60, 100),    # C7
    (3.0, 64, 100),    # C7
    (3.0, 67, 100),    # C7
]
for time, note_number, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax - motif: F - G - Ab - Bb (melodic whisper)
sax_notes = [
    (1.5, 71, 100),    # F
    (1.75, 72, 100),   # G
    (2.0, 74, 100),    # Ab
    (2.25, 75, 100),   # Bb
    (2.5, 74, 100),    # Ab (repeat)
    (2.75, 71, 100),   # F (back to start)
    (3.0, 72, 100),    # G
    (3.25, 75, 100),   # Bb (end on a question)
]
for time, note_number, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line - walking in Fm
bass_notes = [
    (3.5, 44, 100),    # F
    (3.75, 46, 100),   # E
    (4.0, 45, 100),    # G
    (4.25, 43, 100),   # D
    (4.5, 44, 100),    # F
    (4.75, 47, 100),   # Ab
    (5.0, 45, 100),    # G
    (5.25, 43, 100),   # D
]
for time, note_number, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    (3.75, 59, 100),   # C7
    (3.75, 60, 100),   # C7
    (3.75, 64, 100),   # C7
    (3.75, 67, 100),   # C7
    (4.25, 59, 100),   # C7
    (4.25, 60, 100),   # C7
    (4.25, 64, 100),   # C7
    (4.25, 67, 100),   # C7
    (5.0, 59, 100),    # C7
    (5.0, 60, 100),    # C7
    (5.0, 64, 100),    # C7
    (5.0, 67, 100),    # C7
]
for time, note_number, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax - motif variation: F - Ab - G - Bb (builds tension)
sax_notes = [
    (3.5, 71, 100),    # F
    (3.75, 74, 100),   # Ab
    (4.0, 72, 100),    # G
    (4.25, 75, 100),   # Bb
    (4.5, 74, 100),    # Ab
    (4.75, 71, 100),   # F
    (5.0, 72, 100),    # G
    (5.25, 75, 100),   # Bb (builds tension)
]
for time, note_number, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: same pattern as before
drum_notes = [
    (3.0, 36, 100),    # Kick on 1
    (3.75, 42, 100),   # Hihat on &1
    (4.0, 38, 100),    # Snare on 2
    (4.25, 42, 100),   # Hihat on &2
    (4.5, 36, 100),    # Kick on 3
    (4.75, 42, 100),   # Hihat on &3
    (5.0, 38, 100),    # Snare on 4
    (5.25, 42, 100),   # Hihat on &4
]
for time, note_number, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line - walking in Fm
bass_notes = [
    (5.5, 44, 100),    # F
    (5.75, 46, 100),   # E
    (6.0, 45, 100),    # G
    (6.25, 43, 100),   # D
]
for time, note_number, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    (5.75, 59, 100),   # C7
    (5.75, 60, 100),   # C7
    (5.75, 64, 100),   # C7
    (5.75, 67, 100),   # C7
]
for time, note_number, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax - motif resolution: F - G - Ab - Bb (back to the start, but with more force)
sax_notes = [
    (5.5, 71, 100),    # F
    (5.75, 72, 100),   # G
    (6.0, 74, 100),    # Ab
    (6.25, 75, 100),   # Bb
]
for time, note_number, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: same pattern as before
drum_notes = [
    (4.5, 36, 100),    # Kick on 1
    (5.25, 42, 100),   # Hihat on &1
    (5.5, 38, 100),    # Snare on 2
    (5.75, 42, 100),   # Hihat on &2
    (6.0, 36, 100),    # Kick on 3
    (6.25, 42, 100),   # Hihat on &3
    (6.5, 38, 100),    # Snare on 4
    (6.75, 42, 100),   # Hihat on &4
]
for time, note_number, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time, end=time + 0.25)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

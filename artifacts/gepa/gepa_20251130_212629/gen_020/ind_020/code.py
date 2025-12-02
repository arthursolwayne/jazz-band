
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
    (0.0, 36),  # Kick on 1
    (0.375, 42), # Hihat on &1
    (0.75, 38),  # Snare on 2
    (1.125, 42), # Hihat on &2
    (1.5, 36),   # Kick on 3
    (1.875, 42), # Hihat on &3
    (2.25, 38),  # Snare on 4
    (2.625, 42)  # Hihat on &4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full band enters
# Marcus: Walking bass line in D, chromatic approaches
bass_notes = [
    (1.5, 65),  # D3
    (1.75, 64), # C#3
    (2.0, 66),  # D#3
    (2.25, 67), # E3
    (2.5, 69),  # F#3
    (2.75, 67), # E3
    (3.0, 65),  # D3
    (3.25, 64), # C#3
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4
piano_notes = [
    (1.75, 67), # E3
    (1.75, 76), # B3 (E7)
    (2.25, 65), # D3
    (2.25, 74), # A3 (D7)
    (3.25, 67), # E3
    (3.25, 76), # B3 (E7)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Dante: Tenor sax. Motif starts on &1 of bar 2
sax_notes = [
    (1.875, 69), # F#4 (1/2 note)
    (2.375, 67), # E4 (1/2 note)
    (2.875, 65), # D4 (1/2 note)
    (3.375, 62), # B3 (1/2 note)
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.5)
    sax.notes.append(note_obj)

# Bar 3: Marcus continues walking line
bass_notes = [
    (3.5, 69),  # F#3
    (3.75, 67), # E3
    (4.0, 65),  # D3
    (4.25, 64), # C#3
    (4.5, 66),  # D#3
    (4.75, 67), # E3
    (5.0, 69),  # F#3
    (5.25, 67), # E3
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4
piano_notes = [
    (3.75, 67), # E3
    (3.75, 76), # B3 (E7)
    (4.25, 65), # D3
    (4.25, 74), # A3 (D7)
    (5.25, 67), # E3
    (5.25, 76), # B3 (E7)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36),  # Kick on 1
    (3.375, 42), # Hihat on &1
    (3.75, 38),  # Snare on 2
    (4.125, 42), # Hihat on &2
    (4.5, 36),   # Kick on 3
    (4.875, 42), # Hihat on &3
    (5.25, 38),  # Snare on 4
    (5.625, 42)  # Hihat on &4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 4: Full band
# Marcus: Walking line
bass_notes = [
    (5.5, 67),  # E3
    (5.75, 69), # F#3
    (6.0, 67),  # E3
    (6.25, 65), # D3
]
for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chord on 2
piano_notes = [
    (5.75, 67), # E3
    (5.75, 76), # B3 (E7)
]
for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Dante: Motif returns, rests on the last note
sax_notes = [
    (5.875, 69), # F#4 (1/2 note)
    (6.375, 67), # E4 (1/2 note)
    (6.875, 65), # D4 (1/2 note)
    (7.375, 62), # B3
]
for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.5)
    sax.notes.append(note_obj)

# Drums: Kick on 1, snare on 2, hihat on every eighth
drum_notes = [
    (6.0, 36),  # Kick on 1
    (6.375, 42), # Hihat on &1
    (6.75, 38),  # Snare on 2
    (7.125, 42), # Hihat on &2
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

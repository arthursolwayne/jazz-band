
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 80), # Hihat on &1
    (0.75, 42, 80),  # Hihat on &2
    (1.125, 38, 100),# Snare on 2
    (1.5, 42, 80),   # Hihat on &3
    (1.875, 42, 80), # Hihat on &4
    (2.25, 36, 100), # Kick on 3
    (2.625, 42, 80), # Hihat on &3
    (3.0, 42, 80),   # Hihat on &4
    (3.375, 38, 100),# Snare on 4
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line, chromatic approaches, no repeating notes
# D minor key, root = D (62)
bass_notes = [
    (1.5, 62, 70),   # D
    (1.75, 61, 70),  # C
    (2.0, 64, 70),   # E
    (2.25, 63, 70),  # D#
    (2.5, 66, 70),   # G
    (2.75, 65, 70),  # F#
    (3.0, 62, 70),   # D
]

for time, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# D7: D (62), F# (67), A (69), C (60)
# Comp on 2 and 4
piano_notes = [
    (1.75, 62, 90),  # D
    (1.75, 67, 90),  # F#
    (1.75, 69, 90),  # A
    (1.75, 60, 90),  # C
    (2.0, 62, 90),   # D
    (2.0, 67, 90),   # F#
    (2.0, 69, 90),   # A
    (2.0, 60, 90),   # C
    (3.0, 62, 90),   # D
    (3.0, 67, 90),   # F#
    (3.0, 69, 90),   # A
    (3.0, 60, 90),   # C
]

for time, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Dante: Sax melody, one short motif, start it, leave it hanging
# Motif: D (62), F# (67), A (69), C (60) in 16th notes
# D -> F# -> A -> C, but start with D and leave the rest hanging
sax_notes = [
    (1.5, 62, 100),  # D
    (1.625, 67, 100), # F#
    (1.75, 69, 100),  # A
    (1.875, 60, 100), # C
]

for time, note, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    (3.0, 62, 70),   # D
    (3.25, 61, 70),  # C
    (3.5, 64, 70),   # E
    (3.75, 63, 70),  # D#
    (4.0, 66, 70),   # G
    (4.25, 65, 70),  # F#
    (4.5, 62, 70),   # D
]

for time, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (3.25, 62, 90),  # D
    (3.25, 67, 90),  # F#
    (3.25, 69, 90),  # A
    (3.25, 60, 90),  # C
    (3.5, 62, 90),   # D
    (3.5, 67, 90),   # F#
    (3.5, 69, 90),   # A
    (3.5, 60, 90),   # C
    (4.5, 62, 90),   # D
    (4.5, 67, 90),   # F#
    (4.5, 69, 90),   # A
    (4.5, 60, 90),   # C
]

for time, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on 1
    (3.375, 42, 80), # Hihat on &1
    (3.75, 42, 80),  # Hihat on &2
    (4.125, 38, 100),# Snare on 2
    (4.5, 42, 80),   # Hihat on &3
    (4.875, 42, 80), # Hihat on &4
    (5.25, 36, 100), # Kick on 3
    (5.625, 42, 80), # Hihat on &3
    (6.0, 42, 80),   # Hihat on &4
    (6.375, 38, 100),# Snare on 4
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    (4.5, 62, 70),   # D
    (4.75, 61, 70),  # C
    (5.0, 64, 70),   # E
    (5.25, 63, 70),  # D#
    (5.5, 66, 70),   # G
    (5.75, 65, 70),  # F#
    (6.0, 62, 70),   # D
]

for time, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (4.75, 62, 90),  # D
    (4.75, 67, 90),  # F#
    (4.75, 69, 90),  # A
    (4.75, 60, 90),  # C
    (5.0, 62, 90),   # D
    (5.0, 67, 90),   # F#
    (5.0, 69, 90),   # A
    (5.0, 60, 90),   # C
    (6.0, 62, 90),   # D
    (6.0, 67, 90),   # F#
    (6.0, 69, 90),   # A
    (6.0, 60, 90),   # C
]

for time, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Dante: Continue the motif, finish it
# D -> F# -> A -> C, all in 16th notes
sax_notes = [
    (4.5, 62, 100),  # D
    (4.625, 67, 100), # F#
    (4.75, 69, 100),  # A
    (4.875, 60, 100), # C
]

for time, note, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

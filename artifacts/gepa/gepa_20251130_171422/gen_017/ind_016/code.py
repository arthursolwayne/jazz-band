
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
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 80),  # Hihat on &1
    (1.0, 38, 100),  # Snare on beat 2
    (1.25, 42, 80),  # Hihat on &2
    (1.5, 36, 100),  # Kick on beat 3
    (1.75, 42, 80),  # Hihat on &3
    (2.0, 38, 100),  # Snare on beat 4
    (2.25, 42, 80)   # Hihat on &4
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here, lingering, unresolved
sax_notes = [
    (1.5, 62, 100),  # Dm7 - D
    (1.75, 65, 100), # F
    (2.0, 64, 100),  # Eb
    (2.25, 62, 100), # D
]
for start, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(n)

# Bass: Walking line, chromatic approach
bass_notes = [
    (1.5, 50, 80),   # D
    (1.75, 49, 80),  # C
    (2.0, 51, 80),   # Eb
    (2.25, 50, 80),  # D
    (2.5, 52, 80),   # F
    (2.75, 51, 80),  # Eb
    (3.0, 50, 80),   # D
    (3.25, 49, 80)   # C
]
for start, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4, sparse comp
piano_notes = [
    (1.75, 62, 80),  # D7: D
    (1.75, 67, 80),  # A
    (1.75, 64, 80),  # F
    (1.75, 69, 80),  # C
    (2.25, 62, 80),  # D
    (2.25, 67, 80),  # A
    (2.25, 64, 80),  # F
    (2.25, 69, 80),  # C
]
for start, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(n)

# Drums: Bar 2
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 80),  # Hihat on &1
    (2.0, 38, 100),  # Snare on beat 2
    (2.25, 42, 80),  # Hihat on &2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 80),  # Hihat on &3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 80)   # Hihat on &4
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 3: Sax continues motif, expands slightly, tension builds
sax_notes = [
    (3.0, 64, 100),  # Eb
    (3.25, 67, 100), # G
    (3.5, 64, 100),  # Eb
    (3.75, 62, 100), # D
]
for start, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(n)

# Bass: Chromatic walk
bass_notes = [
    (3.0, 50, 80),   # D
    (3.25, 51, 80),  # Eb
    (3.5, 52, 80),   # F
    (3.75, 53, 80),  # F#
    (4.0, 52, 80),   # F
    (4.25, 51, 80),  # Eb
    (4.5, 50, 80),   # D
    (4.75, 49, 80)   # C
]
for start, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(n)

# Piano: Comp on 2 and 4
piano_notes = [
    (3.25, 62, 80),  # D
    (3.25, 67, 80),  # A
    (3.25, 64, 80),  # F
    (3.25, 69, 80),  # C
    (3.75, 62, 80),  # D
    (3.75, 67, 80),  # A
    (3.75, 64, 80),  # F
    (3.75, 69, 80),  # C
]
for start, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(n)

# Drums: Bar 3
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.25, 42, 80),  # Hihat on &1
    (3.5, 38, 100),  # Snare on beat 2
    (3.75, 42, 80),  # Hihat on &2
    (4.0, 36, 100),  # Kick on beat 3
    (4.25, 42, 80),  # Hihat on &3
    (4.5, 38, 100),  # Snare on beat 4
    (4.75, 42, 80)   # Hihat on &4
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 4: Sax resolves motif, ends on a question
sax_notes = [
    (4.5, 62, 100),  # D
    (4.75, 65, 100), # F
    (5.0, 64, 100),  # Eb
    (5.25, 62, 100), # D
]
for start, note, velocity in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(n)

# Bass: Walking line, chromatic approach
bass_notes = [
    (4.5, 50, 80),   # D
    (4.75, 49, 80),  # C
    (5.0, 51, 80),   # Eb
    (5.25, 50, 80),  # D
    (5.5, 52, 80),   # F
    (5.75, 51, 80),  # Eb
    (6.0, 50, 80),   # D
    (6.25, 49, 80)   # C
]
for start, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(n)

# Piano: Comp on 2 and 4
piano_notes = [
    (4.75, 62, 80),  # D
    (4.75, 67, 80),  # A
    (4.75, 64, 80),  # F
    (4.75, 69, 80),  # C
    (5.25, 62, 80),  # D
    (5.25, 67, 80),  # A
    (5.25, 64, 80),  # F
    (5.25, 69, 80),  # C
]
for start, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    piano.notes.append(n)

# Drums: Bar 4
drum_notes = [
    (4.5, 36, 100),  # Kick on beat 1
    (4.75, 42, 80),  # Hihat on &1
    (5.0, 38, 100),  # Snare on beat 2
    (5.25, 42, 80),  # Hihat on &2
    (5.5, 36, 100),  # Kick on beat 3
    (5.75, 42, 80),  # Hihat on &3
    (6.0, 38, 100),  # Snare on beat 4
    (6.25, 42, 80)   # Hihat on &4
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

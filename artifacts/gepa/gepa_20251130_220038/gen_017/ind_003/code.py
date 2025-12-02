
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

# Drums in Bar 1
drum_notes = [
    (0.0, 36),  # Kick on 1
    (0.75, 42), # Hihat on 2
    (1.125, 38), # Snare on 3
    (1.5, 42)   # Hihat on 4
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line in Dm
bass_notes = [
    (1.5, 62),  # D (root)
    (1.75, 60), # C (chromatic approach)
    (2.0, 64),  # F (3rd)
    (2.25, 62), # D (root)
    (2.5, 60),  # C (chromatic approach)
    (2.75, 64), # F (3rd)
    (3.0, 62)   # D (root)
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    (2.0, 62),  # D
    (2.0, 67),  # G
    (2.0, 70),  # C
    (2.0, 74),  # F
    (2.75, 62), # D
    (2.75, 67), # G
    (2.75, 70), # C
    (2.75, 74)  # F
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Saxophone motif: Start it, leave it hanging, finish it
sax_notes = [
    (1.5, 65),  # E (start of motif)
    (1.75, 67), # G
    (2.0, 65),  # E (return)
    (2.25, 62), # D (resolution)
    (2.75, 67), # G (extension)
    (3.0, 65)   # E (end)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums in Bar 2
drum_notes = [
    (1.5, 36),  # Kick on 1
    (2.0, 38),  # Snare on 2
    (2.25, 42), # Hihat on 3
    (2.5, 36),  # Kick on 3
    (2.75, 38), # Snare on 4
    (3.0, 42)   # Hihat on 4
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Walking line in Dm
bass_notes = [
    (3.0, 62),  # D
    (3.25, 60), # C
    (3.5, 64),  # F
    (3.75, 62), # D
    (4.0, 60),  # C
    (4.25, 64), # F
    (4.5, 62)   # D
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    (3.5, 62),  # D
    (3.5, 67),  # G
    (3.5, 70),  # C
    (3.5, 74),  # F
    (4.25, 62), # D
    (4.25, 67), # G
    (4.25, 70), # C
    (4.25, 74)  # F
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Saxophone motif: Continue the story
sax_notes = [
    (3.0, 62),  # D
    (3.25, 64), # F
    (3.5, 62),  # D
    (3.75, 67), # G
    (4.0, 65),  # E
    (4.25, 62), # D
    (4.5, 64)   # F
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums in Bar 3
drum_notes = [
    (3.0, 36),  # Kick on 1
    (3.5, 38),  # Snare on 2
    (3.75, 42), # Hihat on 3
    (4.0, 36),  # Kick on 3
    (4.25, 38), # Snare on 4
    (4.5, 42)   # Hihat on 4
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: Walking line in Dm
bass_notes = [
    (4.5, 62),  # D
    (4.75, 60), # C
    (5.0, 64),  # F
    (5.25, 62), # D
    (5.5, 60),  # C
    (5.75, 64), # F
    (6.0, 62)   # D
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano chords: 7th chords, comp on 2 and 4
piano_notes = [
    (5.0, 62),  # D
    (5.0, 67),  # G
    (5.0, 70),  # C
    (5.0, 74),  # F
    (5.75, 62), # D
    (5.75, 67), # G
    (5.75, 70), # C
    (5.75, 74)  # F
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Saxophone motif: Finish it with a question
sax_notes = [
    (4.5, 62),  # D
    (4.75, 64), # F
    (5.0, 67),  # G
    (5.25, 62), # D
    (5.5, 64),  # F
    (5.75, 67), # G
    (6.0, 65)   # E
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Drums in Bar 4
drum_notes = [
    (4.5, 36),  # Kick on 1
    (5.0, 38),  # Snare on 2
    (5.25, 42), # Hihat on 3
    (5.5, 36),  # Kick on 3
    (5.75, 38), # Snare on 4
    (6.0, 42)   # Hihat on 4
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.dump()


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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2: Start of the quartet (1.5 - 3.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 61), (2.0, 60), (2.25, 59),
    (2.5, 60), (2.75, 61), (3.0, 62), (3.25, 63)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 71), (1.5, 72),  # D7
    (2.0, 64), (2.0, 67), (2.0, 71), (2.0, 72),  # D7
    (2.5, 64), (2.5, 67), (2.5, 71), (2.5, 72),  # D7
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 72)   # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Melody - One short motif, make it sing
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 62), (2.25, 67),  # Motif
    (2.5, 62), (2.75, 65), (3.0, 62), (3.25, 67),  # Repeat motif
    (3.5, 62), (3.75, 65), (4.0, 62), (4.25, 67),  # Repeat again
    (4.5, 62), (4.75, 65), (5.0, 62), (5.25, 67)   # Repeat again
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3: Continue the quartet (3.0 - 4.5s)
# Marcus: Keep walking
bass_notes = [
    (3.25, 63), (3.5, 62), (3.75, 61), (4.0, 60),
    (4.25, 60), (4.5, 61), (4.75, 62), (5.0, 63)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords again
piano_notes = [
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 72),  # D7
    (3.5, 64), (3.5, 67), (3.5, 71), (3.5, 72),  # D7
    (4.0, 64), (4.0, 67), (4.0, 71), (4.0, 72),  # D7
    (4.5, 64), (4.5, 67), (4.5, 71), (4.5, 72)   # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Continue motif
sax_notes = [
    (3.5, 62), (3.75, 65), (4.0, 62), (4.25, 67),
    (4.5, 62), (4.75, 65), (5.0, 62), (5.25, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 4: Final bar (4.5 - 6.0s)
# Marcus: Walking again
bass_notes = [
    (5.0, 63), (5.25, 62), (5.5, 61), (5.75, 60)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords again
piano_notes = [
    (4.5, 64), (4.5, 67), (4.5, 71), (4.5, 72),  # D7
    (5.0, 64), (5.0, 67), (5.0, 71), (5.0, 72),  # D7
    (5.5, 64), (5.5, 67), (5.5, 71), (5.5, 72),  # D7
    (6.0, 64), (6.0, 67), (6.0, 71), (6.0, 72)   # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: End with resolution
sax_notes = [
    (5.0, 62), (5.25, 65), (5.5, 62), (5.75, 67),
    (6.0, 62)  # End on D, strong and clear
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums: Continue rhythm
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 36), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('waynes_introduction.mid')

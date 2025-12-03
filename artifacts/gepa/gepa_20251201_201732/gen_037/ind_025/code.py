
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (F2 - C3)
bass_notes = [
    (1.5, 77), (1.875, 82), (2.25, 79), (2.625, 80),
    (3.0, 77), (3.375, 82), (3.75, 79), (4.125, 80)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (Fmaj7)
    (1.5, 65), (1.5, 72), (1.5, 76), (1.5, 77),
    # Bar 3 (Bbmaj7)
    (2.25, 62), (2.25, 69), (2.25, 73), (2.25, 74),
    # Bar 4 (Em7)
    (3.0, 60), (3.0, 67), (3.0, 71), (3.0, 72)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Sax: Motif - F, G, Ab, Bb, then leave it hanging
sax_notes = [
    (1.5, 87), (1.875, 89), (2.25, 88), (2.625, 86),
    (3.0, 87), (3.375, 89), (3.75, 88), (4.125, 86)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line (F2 - C3)
bass_notes = [
    (3.0, 77), (3.375, 82), (3.75, 79), (4.125, 80),
    (4.5, 77), (4.875, 82), (5.25, 79), (5.625, 80)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3 (Bbmaj7)
    (3.0, 62), (3.0, 69), (3.0, 73), (3.0, 74),
    # Bar 4 (Em7)
    (3.75, 60), (3.75, 67), (3.75, 71), (3.75, 72)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Sax: Motif (continue from bar 2)
sax_notes = [
    (3.0, 87), (3.375, 89), (3.75, 88), (4.125, 86),
    (4.5, 87), (4.875, 89), (5.25, 88), (5.625, 86)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line (F2 - C3)
bass_notes = [
    (4.5, 77), (4.875, 82), (5.25, 79), (5.625, 80)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4 (Em7)
    (4.5, 60), (4.5, 67), (4.5, 71), (4.5, 72)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Sax: Motif
sax_notes = [
    (4.5, 87), (4.875, 89), (5.25, 88), (5.625, 86)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')

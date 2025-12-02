
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42), (1.5, 38),
    (0.0, 42), (0.375, 42), (0.75, 42), (1.125, 42), (1.5, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 59), (1.875, 57), (2.25, 58), (2.625, 60),
    # Bar 3
    (3.0, 60), (3.375, 58), (3.75, 57), (4.125, 59),
    # Bar 4
    (4.5, 59), (4.875, 57), (5.25, 58), (5.625, 60)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 64), (2.0, 67), (2.0, 69), (2.0, 71),
    # Bar 3
    (3.5, 64), (3.5, 67), (3.5, 69), (3.5, 71),
    # Bar 4
    (5.0, 64), (5.0, 67), (5.0, 69), (5.0, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (1.5, 62), (1.75, 64), (2.0, 62),
    # Bar 3
    (3.0, 62), (3.25, 64), (3.5, 62),
    # Bar 4
    (4.5, 62), (4.75, 64), (5.0, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.875))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.499))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.25))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dantes_shot.mid")

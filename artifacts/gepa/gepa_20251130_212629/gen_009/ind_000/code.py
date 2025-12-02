
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (35, 1.5, 0.375),  # Gb
    (32, 1.875, 0.375),  # Eb
    (34, 2.25, 0.375),  # F
    (33, 2.625, 0.375),  # E
    (35, 2.625, 0.375),  # Gb
    (32, 2.625, 0.375),  # Eb
    (34, 3.0, 0.375),  # F
    (33, 3.375, 0.375),  # E
    (35, 3.375, 0.375),  # Gb
    (32, 3.375, 0.375),  # Eb
    (34, 3.75, 0.375),  # F
    (33, 4.125, 0.375),  # E
    (35, 4.125, 0.375),  # Gb
    (32, 4.125, 0.375),  # Eb
    (34, 4.5, 0.375),  # F
    (33, 4.875, 0.375),  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (Diane)
piano_notes = [
    (62, 1.5, 0.375),  # Bb7
    (60, 1.5, 0.375),  # F7
    (59, 1.5, 0.375),
    (57, 1.5, 0.375),
    (62, 1.875, 0.375),
    (60, 1.875, 0.375),
    (59, 1.875, 0.375),
    (57, 1.875, 0.375),
    (62, 2.25, 0.375),
    (60, 2.25, 0.375),
    (59, 2.25, 0.375),
    (57, 2.25, 0.375),
    (62, 2.625, 0.375),
    (60, 2.625, 0.375),
    (59, 2.625, 0.375),
    (57, 2.625, 0.375),
    (62, 3.0, 0.375),
    (60, 3.0, 0.375),
    (59, 3.0, 0.375),
    (57, 3.0, 0.375),
    (62, 3.375, 0.375),
    (60, 3.375, 0.375),
    (59, 3.375, 0.375),
    (57, 3.375, 0.375),
    (62, 3.75, 0.375),
    (60, 3.75, 0.375),
    (59, 3.75, 0.375),
    (57, 3.75, 0.375),
    (62, 4.125, 0.375),
    (60, 4.125, 0.375),
    (59, 4.125, 0.375),
    (57, 4.125, 0.375),
    (62, 4.5, 0.375),
    (60, 4.5, 0.375),
    (59, 4.5, 0.375),
    (57, 4.5, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    for i in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + i * 0.75, end=start + i * 0.75 + 0.375))
    # Snare on 2 and 4
    for i in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + i * 0.75, end=start + i * 0.75 + 0.375))
    # Hi-hat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Saxophone (Dante)
sax_notes = [
    (62, 1.5, 0.375),  # Bb
    (64, 1.875, 0.375),  # Db
    (62, 2.25, 0.375),  # Bb
    (60, 2.625, 0.375),  # F
    (62, 2.625, 0.375),  # Bb
    (64, 3.0, 0.375),  # Db
    (62, 3.375, 0.375),  # Bb
    (60, 3.75, 0.375),  # F
    (62, 4.125, 0.375),  # Bb
    (64, 4.5, 0.375),  # Db
    (62, 4.875, 0.375),  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

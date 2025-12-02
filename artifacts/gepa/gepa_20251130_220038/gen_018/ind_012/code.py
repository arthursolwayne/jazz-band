
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.1875, 0.1875), # Hihat on 1 &
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.5625, 0.1875), # Hihat on 2 &
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.9375, 0.1875), # Hihat on 3 &
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.3125, 0.1875)  # Hihat on 4 &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),    # D (1)
    (60, 1.875, 0.375),   # Bb (2)
    (61, 2.25, 0.375),    # B (3)
    (62, 2.625, 0.375),   # D (4)
    (64, 3.0, 0.375),     # F (1)
    (62, 3.375, 0.375),   # D (2)
    (63, 3.75, 0.375),    # Eb (3)
    (64, 4.125, 0.375),   # F (4)
    (65, 4.5, 0.375),     # F# (1)
    (64, 4.875, 0.375),   # F (2)
    (63, 5.25, 0.375),    # Eb (3)
    (62, 5.625, 0.375)    # D (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (62, 1.5, 0.375),    # D
    (67, 1.5, 0.375),    # G
    (69, 1.5, 0.375),    # Bb
    (72, 1.5, 0.375),    # F
    # Bar 3: Dm7
    (62, 3.0, 0.375),
    (67, 3.0, 0.375),
    (69, 3.0, 0.375),
    (72, 3.0, 0.375),
    # Bar 4: Dm7
    (62, 4.5, 0.375),
    (67, 4.5, 0.375),
    (69, 4.5, 0.375),
    (72, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5, 0.375),    # D (1)
    (65, 2.25, 0.375),   # F# (3)
    (62, 3.0, 0.375),    # D (1)
    (67, 3.75, 0.375),   # G (3)
    (65, 4.5, 0.375),    # F# (1)
    (62, 5.25, 0.375)    # D (3)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.1875, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375))
    # Hihat on 2 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.5625, end=start + 0.1875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.375))
    # Hihat on 3 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.9375, end=start + 0.1875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 0.375))
    # Hihat on 4 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

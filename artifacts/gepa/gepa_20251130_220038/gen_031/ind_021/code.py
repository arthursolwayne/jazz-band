
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
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Fm, chromatic approaches
bass_notes = [
    (37, 1.5, 0.375),    # Fm root (F) chromatic up
    (38, 1.875, 0.375),  # Gb (chromatic)
    (39, 2.25, 0.375),   # G
    (40, 2.625, 0.375),  # Ab
    (39, 2.625, 0.375),  # G (repeating)
    (38, 3.0, 0.375),    # Gb
    (37, 3.375, 0.375),  # F
    (36, 3.75, 0.375),   # Eb (chromatic down)
    (35, 4.125, 0.375),  # D
    (34, 4.5, 0.375),    # Db
    (33, 4.875, 0.375),  # C
    (32, 5.25, 0.375),   # Bb
    (33, 5.625, 0.375),  # C
    (34, 6.0, 0.375)     # Db
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (45, 1.5, 0.1875),   # F7 (F, A, C, Eb) on 1
    (48, 1.5, 0.1875),
    (50, 1.5, 0.1875),
    (53, 1.5, 0.1875),
    (48, 1.875, 0.1875),  # comp on 2
    (50, 1.875, 0.1875),
    (53, 1.875, 0.1875),
    (45, 2.25, 0.1875),   # F7 on 3
    (48, 2.25, 0.1875),
    (50, 2.25, 0.1875),
    (53, 2.25, 0.1875),
    (48, 2.625, 0.1875),  # comp on 4
    (50, 2.625, 0.1875),
    (53, 2.625, 0.1875),
    (45, 3.0, 0.1875),    # F7 on 5
    (48, 3.0, 0.1875),
    (50, 3.0, 0.1875),
    (53, 3.0, 0.1875),
    (48, 3.375, 0.1875),  # comp on 6
    (50, 3.375, 0.1875),
    (53, 3.375, 0.1875),
    (45, 3.75, 0.1875),   # F7 on 7
    (48, 3.75, 0.1875),
    (50, 3.75, 0.1875),
    (53, 3.75, 0.1875),
    (48, 4.125, 0.1875),  # comp on 8
    (50, 4.125, 0.1875),
    (53, 4.125, 0.1875),
    (45, 4.5, 0.1875),    # F7 on 9
    (48, 4.5, 0.1875),
    (50, 4.5, 0.1875),
    (53, 4.5, 0.1875),
    (48, 4.875, 0.1875),  # comp on 10
    (50, 4.875, 0.1875),
    (53, 4.875, 0.1875),
    (45, 5.25, 0.1875),   # F7 on 11
    (48, 5.25, 0.1875),
    (50, 5.25, 0.1875),
    (53, 5.25, 0.1875),
    (48, 5.625, 0.1875),  # comp on 12
    (50, 5.625, 0.1875),
    (53, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick 1
    (42, 1.5, 0.375),    # Hihat 1
    (38, 1.875, 0.375),  # Snare 2
    (42, 1.875, 0.375),  # Hihat 2
    (36, 2.25, 0.375),   # Kick 3
    (42, 2.25, 0.375),   # Hihat 3
    (38, 2.625, 0.375),  # Snare 4
    (42, 2.625, 0.375),  # Hihat 4
    (36, 3.0, 0.375),    # Kick 5
    (42, 3.0, 0.375),    # Hihat 5
    (38, 3.375, 0.375),  # Snare 6
    (42, 3.375, 0.375),  # Hihat 6
    (36, 3.75, 0.375),   # Kick 7
    (42, 3.75, 0.375),   # Hihat 7
    (38, 4.125, 0.375),  # Snare 8
    (42, 4.125, 0.375),  # Hihat 8
    (36, 4.5, 0.375),    # Kick 9
    (42, 4.5, 0.375),    # Hihat 9
    (38, 4.875, 0.375),  # Snare 10
    (42, 4.875, 0.375),  # Hihat 10
    (36, 5.25, 0.375),   # Kick 11
    (42, 5.25, 0.375),   # Hihat 11
    (38, 5.625, 0.375),  # Snare 12
    (42, 5.625, 0.375)   # Hihat 12
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): Motif in Fm
# First bar setup: Start the motif, leave it hanging
sax_notes = [
    (50, 1.5, 0.375),    # G (Fm)
    (48, 1.875, 0.375),  # E
    (50, 2.25, 0.375),   # G
    (53, 2.625, 0.375),  # Bb
    (55, 3.0, 0.375),    # D
    (53, 3.375, 0.375),  # Bb
    (50, 3.75, 0.375),   # G
    (48, 4.125, 0.375),  # E
    (50, 4.5, 0.375),    # G
    (53, 4.875, 0.375),  # Bb
    (55, 5.25, 0.375),   # D
    (53, 5.625, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

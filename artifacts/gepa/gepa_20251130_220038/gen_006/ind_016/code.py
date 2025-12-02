
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.375),     # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.375),   # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.375),    # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.375),   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums for bar 2 (1.5 - 3.0s)
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 1.5, end=start + 1.5 + duration))

# Drums for bar 3 (3.0 - 4.5s)
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 3.0, end=start + 3.0 + duration))

# Drums for bar 4 (4.5 - 6.0s)
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + 4.5, end=start + 4.5 + duration))

# Bass line (Marcus): walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375),     # Fm root (F) on 1
    (40, 1.875, 0.375),   # Gb (chromatic approach) on 2
    (41, 2.25, 0.375),    # Ab (chromatic approach) on 3
    (43, 2.625, 0.375),   # Bb on 4
    (43, 3.0, 0.375),     # Bb on 1
    (44, 3.375, 0.375),   # C (chromatic approach) on 2
    (45, 3.75, 0.375),    # Db (chromatic approach) on 3
    (47, 4.125, 0.375),   # Eb on 4
    (47, 4.5, 0.375),     # Eb on 1
    (48, 4.875, 0.375),   # F (chromatic approach) on 2
    (49, 5.25, 0.375),    # Gb (chromatic approach) on 3
    (50, 5.625, 0.375),   # Ab on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.875, 0.375),   # Ab7 on 2
    (48, 1.875, 0.375),
    (47, 1.875, 0.375),
    (45, 1.875, 0.375),
    # Bar 3
    (50, 3.375, 0.375),   # Ab7 on 2
    (48, 3.375, 0.375),
    (47, 3.375, 0.375),
    (45, 3.375, 0.375),
    # Bar 4
    (50, 4.875, 0.375),   # Ab7 on 2
    (48, 4.875, 0.375),
    (47, 4.875, 0.375),
    (45, 4.875, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Saxophone (Dante): Motif in Fm, one idea, sing it, leave it hanging
sax_notes = [
    # Bar 2
    (45, 1.5, 0.375),     # Eb
    (47, 1.875, 0.375),   # F
    (43, 2.25, 0.375),    # Bb
    (41, 2.625, 0.375),   # Ab
    # Bar 3
    (43, 3.0, 0.375),     # Bb
    (45, 3.375, 0.375),   # Eb
    (47, 3.75, 0.375),    # F
    (49, 4.125, 0.375),   # G
    # Bar 4
    (43, 4.5, 0.375),     # Bb
    (45, 4.875, 0.375),   # Eb
    (47, 5.25, 0.375),    # F
    (50, 5.625, 0.375),   # Ab
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

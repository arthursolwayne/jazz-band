
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

# Marcus: Walking bass line in Fm
bass_notes = [
    (37, 1.5, 0.375),  # F (root)
    (35, 1.875, 0.375),  # Eb (chromatic)
    (37, 2.25, 0.375),  # F
    (39, 2.625, 0.375),  # G (chromatic)
    (37, 3.0, 0.375),  # F
    (35, 3.375, 0.375),  # Eb
    (37, 3.75, 0.375),  # F
    (39, 4.125, 0.375),  # G
    (37, 4.5, 0.375),  # F
    (35, 4.875, 0.375),  # Eb
    (37, 5.25, 0.375),  # F
    (39, 5.625, 0.375),  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Piano comping with 7th chords (on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (44, 1.5, 0.375),  # Bb7 (Fm7 chord tone)
    (46, 1.5, 0.375),  # D7
    (45, 1.5, 0.375),  # C7
    (42, 1.5, 0.375),  # F7
    (44, 2.25, 0.375),  # Bb7
    (46, 2.25, 0.375),  # D7
    (45, 2.25, 0.375),  # C7
    (42, 2.25, 0.375),  # F7
    
    # Bar 3 (3.0 - 4.5s)
    (44, 3.0, 0.375),
    (46, 3.0, 0.375),
    (45, 3.0, 0.375),
    (42, 3.0, 0.375),
    (44, 3.75, 0.375),
    (46, 3.75, 0.375),
    (45, 3.75, 0.375),
    (42, 3.75, 0.375),
    
    # Bar 4 (4.5 - 6.0s)
    (44, 4.5, 0.375),
    (46, 4.5, 0.375),
    (45, 4.5, 0.375),
    (42, 4.5, 0.375),
    (44, 5.25, 0.375),
    (46, 5.25, 0.375),
    (45, 5.25, 0.375),
    (42, 5.25, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))

# Dante: Tenor sax, one short motif
# Bar 2: Start motif (F - Ab - Bb - F)
sax_notes = [
    (59, 1.5, 0.375),  # F
    (57, 1.875, 0.375),  # Ab
    (58, 2.25, 0.375),  # Bb
    (59, 2.625, 0.375),  # F
    # Bar 3: Leave it hanging
    (59, 3.0, 0.1875),  # F
    (61, 3.1875, 0.1875),  # D
    (59, 3.375, 0.1875),  # F
    (61, 3.5625, 0.1875),  # D
    # Bar 4: Finish it
    (59, 4.5, 0.375),  # F
    (57, 4.875, 0.375),  # Ab
    (58, 5.25, 0.375),  # Bb
    (59, 5.625, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

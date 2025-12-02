
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

# Marcus: Walking bass line in Fm (F, Eb, D, C)
# Fm scale: F, Ab, Bb, C, Db, Eb, D
bass_notes = [
    (64, 1.5, 0.375),     # F
    (60, 1.875, 0.375),   # Eb
    (59, 2.25, 0.375),    # D
    (60, 2.625, 0.375),   # C
    (57, 2.625, 0.375),   # Db
    (60, 2.625, 0.375),   # C
    (64, 3.0, 0.375),     # F
    (60, 3.375, 0.375),   # Eb
    (59, 3.75, 0.375),    # D
    (60, 4.125, 0.375),   # C
    (57, 4.125, 0.375),   # Db
    (60, 4.125, 0.375),   # C
    (64, 4.5, 0.375),     # F
    (60, 4.875, 0.375),   # Eb
    (59, 5.25, 0.375),    # D
    (60, 5.625, 0.375),   # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
piano_notes = [
    # Bar 2
    (64, 1.5, 0.1875),    # F
    (76, 1.5, 0.1875),    # Ab
    (72, 1.5, 0.1875),    # C
    (69, 1.5, 0.1875),    # Eb
    (76, 1.875, 0.1875),  # Ab
    (72, 1.875, 0.1875),  # C
    (69, 1.875, 0.1875),  # Eb
    # Bar 3
    (64, 2.25, 0.1875),   # F
    (76, 2.25, 0.1875),   # Ab
    (72, 2.25, 0.1875),   # C
    (69, 2.25, 0.1875),   # Eb
    (76, 2.625, 0.1875),  # Ab
    (72, 2.625, 0.1875),  # C
    (69, 2.625, 0.1875),  # Eb
    # Bar 4
    (64, 3.0, 0.1875),    # F
    (76, 3.0, 0.1875),    # Ab
    (72, 3.0, 0.1875),    # C
    (69, 3.0, 0.1875),    # Eb
    (76, 3.375, 0.1875),  # Ab
    (72, 3.375, 0.1875),  # C
    (69, 3.375, 0.1875),  # Eb
    (64, 3.75, 0.1875),   # F
    (76, 3.75, 0.1875),   # Ab
    (72, 3.75, 0.1875),   # C
    (69, 3.75, 0.1875),   # Eb
    (76, 4.125, 0.1875),  # Ab
    (72, 4.125, 0.1875),  # C
    (69, 4.125, 0.1875),  # Eb
    (64, 4.5, 0.1875),    # F
    (76, 4.5, 0.1875),    # Ab
    (72, 4.5, 0.1875),    # C
    (69, 4.5, 0.1875),    # Eb
    (76, 4.875, 0.1875),  # Ab
    (72, 4.875, 0.1875),  # C
    (69, 4.875, 0.1875),  # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.375),     # Hihat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.375),   # Hihat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.375),    # Hihat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.375),   # Hihat on 4
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.375),     # Hihat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.375),   # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.375),    # Hihat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.375),   # Hihat on 4
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.375),     # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.375),   # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.375),    # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.375),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, C, Ab, D
sax_notes = [
    (64, 1.5, 0.375),     # F
    (76, 1.875, 0.375),   # Ab
    (71, 2.25, 0.375),    # Bb
    (72, 2.625, 0.375),   # C
    (76, 3.0, 0.375),     # Ab
    (62, 3.375, 0.375),   # D
    (64, 3.75, 0.375),    # F
    (76, 4.125, 0.375),   # Ab
    (71, 4.5, 0.375),     # Bb
    (72, 4.875, 0.375),   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

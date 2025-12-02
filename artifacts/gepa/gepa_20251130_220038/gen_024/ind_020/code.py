
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
bass_notes = [
    (36, 1.5, 0.375),     # F
    (34, 1.875, 0.375),   # Eb
    (33, 2.25, 0.375),    # D
    (31, 2.625, 0.375),   # C
    (36, 3.0, 0.375),     # F
    (34, 3.375, 0.375),   # Eb
    (33, 3.75, 0.375),    # D
    (31, 4.125, 0.375),   # C
    (36, 4.5, 0.375),     # F
    (34, 4.875, 0.375),   # Eb
    (33, 5.25, 0.375),    # D
    (31, 5.625, 0.375)    # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (53, 1.875, 0.375),   # Bb7 on 2 (Fm7)
    (50, 1.875, 0.375),
    (48, 1.875, 0.375),
    (45, 1.875, 0.375),
    (53, 3.375, 0.375),   # Bb7 on 2 (Fm7)
    (50, 3.375, 0.375),
    (48, 3.375, 0.375),
    (45, 3.375, 0.375),
    (53, 4.875, 0.375),   # Bb7 on 2 (Fm7)
    (50, 4.875, 0.375),
    (48, 4.875, 0.375),
    (45, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

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
    (42, 5.625, 0.375)    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Sax — short motif on Fm7 (F, Ab, Bb, D)
sax_notes = [
    (53, 1.5, 0.375),     # F
    (51, 1.875, 0.375),   # Ab
    (50, 2.25, 0.375),    # Bb
    (48, 2.625, 0.375),   # D
    (53, 3.0, 0.375),     # F
    (51, 3.375, 0.375),   # Ab
    (50, 3.75, 0.375),    # Bb
    (48, 4.125, 0.375),   # D
    (53, 4.5, 0.375),     # F
    (51, 4.875, 0.375),   # Ab
    (50, 5.25, 0.375),    # Bb
    (48, 5.625, 0.375)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on 2
    (38, 0.375, 0.375),  # Snare on 3
    (42, 0.375, 0.1875), # Hihat on 3
    (42, 0.5625, 0.1875), # Hihat on 4
    (36, 0.75, 0.375),  # Kick on 4
    (38, 1.125, 0.375),  # Snare on 4 (fill)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet starts
# Marcus: Walking bass line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    (53, 1.5, 0.375),  # F2
    (51, 1.875, 0.375), # Ab2
    (50, 2.25, 0.375),  # D2
    (55, 2.625, 0.375), # G2
    (53, 3.0, 0.375),   # F2
    (51, 3.375, 0.375), # Ab2
    (50, 3.75, 0.375),  # D2
    (55, 4.125, 0.375), # G2
    (53, 4.5, 0.375),   # F2
    (51, 4.875, 0.375), # Ab2
    (50, 5.25, 0.375),  # D2
    (55, 5.625, 0.375), # G2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Open voicings on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (64, 1.5, 0.125),  # Fm7 (F, Ab, C, D)
    (69, 1.5, 0.125),
    (72, 1.5, 0.125),
    (71, 1.5, 0.125),
    # Bar 3 (2.5 - 3.0s)
    (64, 2.5, 0.125),  # Fm7
    (69, 2.5, 0.125),
    (72, 2.5, 0.125),
    (71, 2.5, 0.125),
    # Bar 4 (4.0 - 4.5s)
    (64, 4.0, 0.125),  # Fm7
    (69, 4.0, 0.125),
    (72, 4.0, 0.125),
    (71, 4.0, 0.125),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Motif in Fm (F, Ab, Bb, D)
sax_notes = [
    (64, 1.5, 0.1875),  # F
    (69, 1.6875, 0.1875),  # Ab
    (62, 1.875, 0.1875),  # Bb
    (67, 2.0625, 0.1875),  # D
    (64, 2.25, 0.1875),  # F (repeat)
    (69, 2.4375, 0.1875),  # Ab
    (62, 2.625, 0.1875),  # Bb
    (67, 2.8125, 0.1875),  # D
    (64, 3.0, 0.1875),  # F
    (69, 3.1875, 0.1875),  # Ab
    (62, 3.375, 0.1875),  # Bb
    (67, 3.5625, 0.1875),  # D
    (64, 3.75, 0.1875),  # F (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on 2
    (38, 1.875, 0.375),  # Snare on 3
    (42, 1.875, 0.1875), # Hihat on 3
    (42, 2.0625, 0.1875), # Hihat on 4
    (36, 2.25, 0.375),  # Kick on 4
    # Bar 3
    (36, 2.625, 0.375),  # Kick on 1
    (42, 2.625, 0.1875), # Hihat on 1
    (42, 2.8125, 0.1875), # Hihat on 2
    (38, 3.0, 0.375),  # Snare on 3
    (42, 3.0, 0.1875), # Hihat on 3
    (42, 3.1875, 0.1875), # Hihat on 4
    (36, 3.375, 0.375),  # Kick on 4
    # Bar 4
    (36, 3.75, 0.375),  # Kick on 1
    (42, 3.75, 0.1875), # Hihat on 1
    (42, 3.9375, 0.1875), # Hihat on 2
    (38, 4.125, 0.375),  # Snare on 3
    (42, 4.125, 0.1875), # Hihat on 3
    (42, 4.3125, 0.1875), # Hihat on 4
    (36, 4.5, 0.375),  # Kick on 4
    (38, 4.875, 0.375),  # Snare on 4 (fill)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_quartet.mid")

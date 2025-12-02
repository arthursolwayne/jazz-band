
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

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375),  # Kick on 3
    (38, 1.875, 0.375), # Snare on 4
    (42, 1.5, 0.1875), # Hihat on 3 & 4
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (61, 2.625, 0.375), # C
    # Bar 3
    (60, 2.999, 0.375),  # B
    (62, 3.375, 0.375),  # D
    (63, 3.75, 0.375),   # Eb
    (65, 4.125, 0.375),  # F
    # Bar 4
    (64, 4.5, 0.375),    # E
    (63, 4.875, 0.375),  # Eb
    (62, 5.25, 0.375),   # D
    (60, 5.625, 0.375)   # B
]

for note, start, duration in bass_notes:
    nb = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(nb)

# Piano: 7th chords on 2 and 4, 4th on 1 and 3
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D
    (66, 1.5, 0.375),  # G
    (67, 1.5, 0.375),  # Ab
    (69, 1.5, 0.375),  # B
    # Bar 3
    (62, 2.999, 0.375),  # D
    (66, 2.999, 0.375),  # G
    (67, 2.999, 0.375),  # Ab
    (69, 2.999, 0.375),  # B
    # Bar 4
    (62, 4.5, 0.375),   # D
    (66, 4.5, 0.375),   # G
    (67, 4.5, 0.375),   # Ab
    (69, 4.5, 0.375)    # B
]

for note, start, duration in piano_notes:
    np = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(np)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> Eb (63) -> D (62) -> C (60)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 4.5, 0.375),   # D
    (63, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # C
]

for note, start, duration in sax_notes:
    ns = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(ns)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

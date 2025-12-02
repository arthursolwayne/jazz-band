
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375),
    (50, 2.625, 0.375), (49, 3.0, 0.375), (48, 3.375, 0.375), (47, 3.75, 0.375),
    (47, 3.75, 0.375), (48, 4.125, 0.375), (49, 4.5, 0.375), (50, 4.875, 0.375),
    (51, 5.25, 0.375), (50, 5.625, 0.375), (49, 6.0, 0.375)
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (53, 1.5, 0.375), (55, 1.5, 0.375), (57, 1.5, 0.375), (58, 1.5, 0.375),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (50, 2.625, 0.375), (52, 2.625, 0.375), (53, 2.625, 0.375), (55, 2.625, 0.375),
    # Bar 4: Fm7 (F, Ab, C, Eb)
    (53, 3.75, 0.375), (55, 3.75, 0.375), (57, 3.75, 0.375), (58, 3.75, 0.375)
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.625, 0.375), (38, 3.0, 0.375), (42, 2.625, 0.1875),
    # Bar 3
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.875, 0.375), (38, 5.25, 0.375), (42, 4.875, 0.1875),
    # Bar 4
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875)
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53) - Gb (54) - Eb (58) - F (53)
sax_notes = [
    (53, 1.5, 0.375), (54, 1.875, 0.375), (58, 2.25, 0.375), (53, 2.625, 0.375),
    (53, 3.0, 0.375), (54, 3.375, 0.375), (58, 3.75, 0.375), (53, 4.125, 0.375)
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

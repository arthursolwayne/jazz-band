
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
    (42, 0.375, 0.75), # Hihat on & 2
    (38, 0.75, 1.125), # Snare on 3
    (42, 1.125, 1.5)   # Hihat on & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F2, G2, D2, C2, Eb2, D2, C2, Bb2)
# Roots and fifths with chromatic approaches
bass_notes = [
    (53, 1.5, 0.375),  # F2
    (55, 1.875, 0.375), # G2
    (50, 2.25, 0.375),  # D2
    (51, 2.625, 0.375), # C2
    (52, 2.999, 0.375), # Eb2
    (50, 3.375, 0.375), # D2
    (51, 3.75, 0.375),  # C2
    (50, 4.125, 0.375), # Bb2
    (53, 4.5, 0.375),   # F2
    (55, 4.875, 0.375), # G2
    (50, 5.25, 0.375),  # D2
    (51, 5.625, 0.375)  # C2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    (53, 1.5, 0.375),  # F
    (60, 1.5, 0.375),  # Ab
    (60, 1.5, 0.375),  # C
    (62, 1.5, 0.375),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 2.25, 0.375), # Bb
    (62, 2.25, 0.375), # D
    (53, 2.25, 0.375), # F
    (60, 2.25, 0.375), # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (55, 3.0, 0.375),  # Eb
    (67, 3.0, 0.375),  # G
    (58, 3.0, 0.375),  # Bb
    (62, 3.0, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 2.25s
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.875, 0.75), # Hihat on 2 and &
    (38, 2.25, 0.375), # Snare on 3
    (42, 2.625, 0.75), # Hihat on 4 and &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: 2.25 - 3.0s
drum_notes = [
    (36, 2.25, 0.375),  # Kick on 1
    (42, 2.625, 0.75), # Hihat on 2 and &
    (38, 3.0, 0.375),  # Snare on 3
    (42, 3.375, 0.75)  # Hihat on 4 and &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: 3.0 - 3.75s
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.375, 0.75), # Hihat on 2 and &
    (38, 3.75, 0.375), # Snare on 3
    (42, 4.125, 0.75)  # Hihat on 4 and &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, Bb — then repeat on the and of 4
sax_notes = [
    (53, 1.5, 0.375),  # F
    (60, 1.875, 0.375), # Ab
    (60, 2.25, 0.375),  # C
    (58, 2.625, 0.375), # Bb
    (53, 3.0, 0.375),   # F
    (60, 3.375, 0.375), # Ab
    (60, 3.75, 0.375),  # C
    (58, 4.125, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

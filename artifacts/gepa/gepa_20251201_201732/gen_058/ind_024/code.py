
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (48, 1.5, 1.5),     # F2 (root)
    (50, 1.875, 1.875), # G2 (fifth)
    (47, 2.25, 2.25),   # E2 (chromatic approach)
    (52, 2.625, 2.625), # A2 (extension)
    (53, 3.0, 3.0),     # Bb2 (root)
    (55, 3.375, 3.375), # C2 (fifth)
    (54, 3.75, 3.75),   # B2 (chromatic approach)
    (57, 4.125, 4.125), # D2 (extension)
    (59, 4.5, 4.5),     # E2 (root)
    (61, 4.875, 4.875), # F2 (fifth)
    (60, 5.25, 5.25),   # Eb2 (chromatic approach)
    (64, 5.625, 5.625)  # G2 (extension)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (53, 1.5, 1.5), (55, 1.5, 1.5), (57, 1.5, 1.5), (59, 1.5, 1.5),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 2.25, 2.25), (60, 2.25, 2.25), (53, 2.25, 2.25), (55, 2.25, 2.25),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (57, 3.0, 3.0), (59, 3.0, 3.0), (61, 3.0, 3.0), (58, 3.0, 3.0),
    # Resolutions on the last beat of each bar
    (59, 1.875, 1.875), (55, 2.625, 2.625), (57, 3.375, 3.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Full kit for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.5), (38, 1.875, 1.875), (42, 1.5, 1.5), (42, 1.875, 1.875), (42, 2.25, 2.25), (42, 2.625, 2.625),
    # Bar 3
    (36, 2.25, 2.25), (38, 2.625, 2.625), (42, 2.25, 2.25), (42, 2.625, 2.625), (42, 3.0, 3.0), (42, 3.375, 3.375),
    # Bar 4
    (36, 3.0, 3.0), (38, 3.375, 3.375), (42, 3.0, 3.0), (42, 3.375, 3.375), (42, 3.75, 3.75), (42, 4.125, 4.125)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 1.875),  # G3 on 1
    (64, 1.875, 2.25), # A3 on 2
    (67, 2.25, 2.625), # B3 on 3
    (62, 3.0, 3.375),  # G3 on 1
    (64, 3.375, 3.75), # A3 on 2
    (67, 3.75, 4.125), # B3 on 3
    (62, 4.5, 5.0)     # G3 on 1 (finish)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

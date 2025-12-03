
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1& 
    (42, 0.1875, 0.1875),# Hihat on 2
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2&
    (42, 0.5625, 0.1875),# Hihat on 3
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3&
    (42, 0.9375, 0.1875),# Hihat on 4
    (38, 1.125, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm (F2, Ab2, D2, G2, etc.), roots and fifths with chromatic approaches
bass_notes = [
    (43, 1.5, 0.375),   # F2 on 1
    (41, 1.875, 0.375),  # Ab2 on 2
    (47, 2.25, 0.375),   # D2 on 3
    (49, 2.625, 0.375),  # G2 on 4
    (48, 3.0, 0.375),    # F2 on 1
    (47, 3.375, 0.375),  # D2 on 2
    (44, 3.75, 0.375),   # Eb2 on 3 (chromatic approach)
    (43, 4.125, 0.375),  # F2 on 4
    (41, 4.5, 0.375),    # Ab2 on 1
    (47, 4.875, 0.375),  # D2 on 2
    (49, 5.25, 0.375),   # G2 on 3
    (45, 5.625, 0.375),  # Bb2 on 4 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 0.375),  # F
    (60, 1.5, 0.375),  # Ab
    (65, 1.5, 0.375),  # C
    (67, 1.5, 0.375),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    (58, 2.25, 0.375),  # Bb
    (62, 2.25, 0.375),  # D
    (53, 2.25, 0.375),  # F
    (60, 2.25, 0.375),  # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    (55, 3.0, 0.375),   # Eb
    (59, 3.0, 0.375),   # G
    (58, 3.0, 0.375),   # Bb
    (67, 3.0, 0.375),   # D
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, G, F (4 notes across 2 bars)
sax_notes = [
    (53, 1.5, 0.375),  # F on 1
    (60, 1.875, 0.375), # Ab on 2
    (67, 2.25, 0.375),  # G on 3
    (53, 2.625, 0.375), # F on 4
    (58, 3.0, 0.375),   # Bb on 1
    (62, 3.375, 0.375), # D on 2
    (67, 3.75, 0.375),  # G on 3
    (53, 4.125, 0.375)  # F on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1&
    (42, 1.6875, 0.1875),# Hihat on 2
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2&
    (42, 2.0625, 0.1875),# Hihat on 3
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3&
    (42, 2.4375, 0.1875),# Hihat on 4
    (38, 2.625, 0.375),  # Snare on 4
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1&
    (42, 3.1875, 0.1875),# Hihat on 2
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2&
    (42, 3.5625, 0.1875),# Hihat on 3
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3&
    (42, 3.9375, 0.1875),# Hihat on 4
    (38, 4.125, 0.375),  # Snare on 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1&
    (42, 4.6875, 0.1875),# Hihat on 2
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2&
    (42, 5.0625, 0.1875),# Hihat on 3
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3&
    (42, 5.4375, 0.1875),# Hihat on 4
    (38, 5.625, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled


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
    (42, 1.125, 0.375)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Fm (F, Ab, D, Eb)
# Bar 2: F, Ab, D, Eb
# Bar 3: Bb, C, G, Ab
# Bar 4: D, Eb, Bb, C
bass_notes = [
    (65, 1.5, 0.375), # F2
    (61, 1.875, 0.375), # Ab2
    (62, 2.25, 0.375), # D2
    (64, 2.625, 0.375), # Eb2
    (59, 3.0, 0.375), # Bb2
    (60, 3.375, 0.375), # C2
    (67, 3.75, 0.375), # G2
    (61, 4.125, 0.375), # Ab2
    (62, 4.5, 0.375), # D2
    (64, 4.875, 0.375), # Eb2
    (59, 5.25, 0.375), # Bb2
    (60, 5.625, 0.375) # C2
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2: Fm7
    (65, 1.5, 0.5),   # F
    (61, 1.5, 0.5),   # Ab
    (60, 1.5, 0.5),   # C
    (64, 1.5, 0.5),   # Eb

    # Bar 3: Bb7
    (59, 2.25, 0.5),  # Bb
    (62, 2.25, 0.5),  # D
    (65, 2.25, 0.5),  # F
    (61, 2.25, 0.5),  # Ab

    # Bar 4: Eb7
    (64, 3.0, 0.5),   # Eb
    (67, 3.0, 0.5),   # G
    (59, 3.0, 0.5),   # Bb
    (62, 3.0, 0.5)    # D
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing.
# Motif: F - Ab - Eb - F (two octaves up)
sax_notes = [
    (65, 1.5, 0.5),   # F3
    (61, 1.875, 0.5), # Ab3
    (64, 2.25, 0.5),  # Eb3
    (84, 2.625, 0.5), # F5 (hanging note)
    (65, 3.0, 0.5),   # F3 (return)
    (61, 3.375, 0.5), # Ab3
    (64, 3.75, 0.5),  # Eb3
    (84, 4.125, 0.5)  # F5 (hanging again)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled


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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.125),  # Hi-hat on 1&
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.75, 0.125),  # Hi-hat on 2&
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.125),  # Hi-hat on 3&
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.5, 0.125)   # Hi-hat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2 (F - C - B - D)
    (48, 1.5, 0.375),  # F
    (53, 1.875, 0.375),  # C
    (52, 2.25, 0.375),  # B
    (50, 2.625, 0.375),  # D
    # Bar 3 (G - D - C - E)
    (51, 3.0, 0.375),  # G
    (50, 3.375, 0.375),  # D
    (48, 3.75, 0.375),  # C
    (52, 4.125, 0.375),  # E
    # Bar 4 (A - E - D - F)
    (52, 4.5, 0.375),  # A
    (50, 4.875, 0.375),  # E
    (48, 5.25, 0.375),  # D
    (48, 5.625, 0.375),  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    (64, 1.5, 0.5),  # F
    (69, 1.5, 0.5),  # A
    (72, 1.5, 0.5),  # C
    (76, 1.5, 0.5),  # E
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    (67, 3.0, 0.5),  # G
    (71, 3.0, 0.5),  # Bb
    (69, 3.0, 0.5),  # D
    (72, 3.0, 0.5),  # F
])
# Bar 4: Am7 (A C E G)
piano_notes.extend([
    (69, 4.5, 0.5),  # A
    (72, 4.5, 0.5),  # C
    (76, 4.5, 0.5),  # E
    (71, 4.5, 0.5),  # G
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# You: One short motif (F - Bb - C - F), start it, leave it hanging
# Bar 2: F (64), Bb (67), C (69), F (64)
sax_notes = [
    (64, 1.5, 0.375),  # F
    (67, 1.875, 0.375),  # Bb
    (69, 2.25, 0.375),  # C
    (64, 2.625, 0.375),  # F
]
# Bar 3: Let it breathe, no notes
# Bar 4: Repeat the motif with a slight variation
sax_notes.extend([
    (64, 4.5, 0.375),  # F
    (67, 4.875, 0.375),  # Bb
    (69, 5.25, 0.375),  # C
    (64, 5.625, 0.375)  # F
])
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
# Bar 2: Kick on 1, snare on 2, kick on 3, snare on 4
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.125),  # Hi-hat on 1&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.125),  # Hi-hat on 2&
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.125),  # Hi-hat on 3&
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.125)   # Hi-hat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Kick on 1, snare on 2, kick on 3, snare on 4
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.125),  # Hi-hat on 1&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.125),  # Hi-hat on 2&
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.125),  # Hi-hat on 3&
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.125)   # Hi-hat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Kick on 1, snare on 2, kick on 3, snare on 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hi-hat on 1&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hi-hat on 2&
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.125),  # Hi-hat on 3&
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.125)   # Hi-hat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")

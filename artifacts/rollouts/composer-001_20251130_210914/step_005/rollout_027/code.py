
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
    (36, 0.0, 0.375),  # kick on 1
    (42, 0.0, 0.375),  # hihat on 1
    (38, 0.375, 0.375),  # snare on 2
    (42, 0.375, 0.375),  # hihat on 2
    (36, 0.75, 0.375),  # kick on 3
    (42, 0.75, 0.375),  # hihat on 3
    (38, 1.125, 0.375),  # snare on 4
    (42, 1.125, 0.375)   # hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (59, 1.5, 0.375),  # D
    (60, 1.875, 0.375),  # Eb
    (61, 2.25, 0.375),  # E
    (62, 2.625, 0.375),  # F
    (63, 3.0, 0.375),  # F#
    (64, 3.375, 0.375),  # G
    (62, 3.75, 0.375),  # F
    (60, 4.125, 0.375),  # Eb
    (62, 4.5, 0.375),  # F
    (64, 4.875, 0.375),  # G
    (65, 5.25, 0.375),  # G#
    (67, 5.625, 0.375)  # A
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - comp on 2 and 4
piano_notes = [
    # Bar 1: comp on 2 and 4
    (64, 1.875, 0.375),  # C
    (67, 1.875, 0.375),  # E
    (69, 1.875, 0.375),  # G
    (71, 1.875, 0.375),  # Bb
    (64, 4.125, 0.375),  # C
    (67, 4.125, 0.375),  # E
    (69, 4.125, 0.375),  # G
    (71, 4.125, 0.375),  # Bb
    # Bar 2: comp on 2 and 4
    (64, 3.375, 0.375),  # C
    (67, 3.375, 0.375),  # E
    (69, 3.375, 0.375),  # G
    (71, 3.375, 0.375),  # Bb
    (64, 5.625, 0.375),  # C
    (67, 5.625, 0.375),  # E
    (69, 5.625, 0.375),  # G
    (71, 5.625, 0.375)   # Bb
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = (36, bar_start, 0.375)
    kick3 = (36, bar_start + 0.75, 0.375)
    # Snare on 2 and 4
    snare2 = (38, bar_start + 0.375, 0.375)
    snare4 = (38, bar_start + 1.125, 0.375)
    # Hi-hat on every eighth
    hihat1 = (42, bar_start, 0.375)
    hihat2 = (42, bar_start + 0.375, 0.375)
    hihat3 = (42, bar_start + 0.75, 0.375)
    hihat4 = (42, bar_start + 1.125, 0.375)

    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick1[0], start=kick1[1], end=kick1[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick3[0], start=kick3[1], end=kick3[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare2[0], start=snare2[1], end=snare2[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare4[0], start=snare4[1], end=snare4[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat1[0], start=hihat1[1], end=hihat1[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat2[0], start=hihat2[1], end=hihat2[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat3[0], start=hihat3[1], end=hihat3[2]))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat4[0], start=hihat4[1], end=hihat4[2]))

# Saxophone (Dante)
sax_notes = [
    (62, 1.5, 0.375),   # E
    (64, 1.875, 0.375),  # F
    (62, 2.25, 0.375),   # E
    (59, 2.625, 0.375),  # D
    (62, 3.0, 0.375),    # E
    (64, 3.375, 0.375),  # F
    (62, 3.75, 0.375),   # E
    (59, 4.125, 0.375),  # D
    (62, 4.5, 0.375),    # E
    (64, 4.875, 0.375),  # F
    (62, 5.25, 0.375),   # E
    (59, 5.625, 0.375)   # D
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

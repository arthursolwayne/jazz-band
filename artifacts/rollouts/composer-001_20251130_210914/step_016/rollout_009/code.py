
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1&
    (42, 0.1875, 0.1875),# Hihat on 2&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2&
    (42, 0.5625, 0.1875),# Hihat on 3&
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3&
    (42, 0.9375, 0.1875),# Hihat on 4&
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4&
    (42, 1.3125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),    # D
    (63, 1.875, 0.375),  # Eb
    (60, 2.25, 0.375),   # C
    (62, 2.625, 0.375),  # D
    (64, 2.625, 0.375),  # E
    (62, 3.0, 0.375),    # D
    (60, 3.375, 0.375),  # C
    (62, 3.75, 0.375),   # D
    (65, 4.125, 0.375),  # F
    (62, 4.5, 0.375),    # D
    (60, 4.875, 0.375),  # C
    (62, 5.25, 0.375),   # D
    (64, 5.625, 0.375),  # E
    (62, 6.0, 0.375)     # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.5, 0.375),    # D7 - D
    (67, 1.5, 0.375),    # D7 - F#
    (69, 1.5, 0.375),    # D7 - A
    (71, 1.5, 0.375),    # D7 - C
    (67, 1.875, 0.375),  # Rest on 2
    (69, 1.875, 0.375),  # Rest on 2
    (71, 1.875, 0.375),  # Rest on 2
    (64, 1.875, 0.375),  # Rest on 2
    (64, 2.25, 0.375),   # D7 - D
    (67, 2.25, 0.375),   # D7 - F#
    (69, 2.25, 0.375),   # D7 - A
    (71, 2.25, 0.375),   # D7 - C
    (67, 2.625, 0.375),  # Rest on 3
    (69, 2.625, 0.375),  # Rest on 3
    (71, 2.625, 0.375),  # Rest on 3
    (64, 2.625, 0.375),  # Rest on 3
    (64, 3.0, 0.375),    # D7 - D
    (67, 3.0, 0.375),    # D7 - F#
    (69, 3.0, 0.375),    # D7 - A
    (71, 3.0, 0.375),    # D7 - C
    (67, 3.375, 0.375),  # Rest on 4
    (69, 3.375, 0.375),  # Rest on 4
    (71, 3.375, 0.375),  # Rest on 4
    (64, 3.375, 0.375),  # Rest on 4
    (64, 3.75, 0.375),   # D7 - D
    (67, 3.75, 0.375),   # D7 - F#
    (69, 3.75, 0.375),   # D7 - A
    (71, 3.75, 0.375),   # D7 - C
    (67, 4.125, 0.375),  # Rest on 5
    (69, 4.125, 0.375),  # Rest on 5
    (71, 4.125, 0.375),  # Rest on 5
    (64, 4.125, 0.375),  # Rest on 5
    (64, 4.5, 0.375),    # D7 - D
    (67, 4.5, 0.375),    # D7 - F#
    (69, 4.5, 0.375),    # D7 - A
    (71, 4.5, 0.375),    # D7 - C
    (67, 4.875, 0.375),  # Rest on 6
    (69, 4.875, 0.375),  # Rest on 6
    (71, 4.875, 0.375),  # Rest on 6
    (64, 4.875, 0.375),  # Rest on 6
    (64, 5.25, 0.375),   # D7 - D
    (67, 5.25, 0.375),   # D7 - F#
    (69, 5.25, 0.375),   # D7 - A
    (71, 5.25, 0.375),   # D7 - C
    (67, 5.625, 0.375),  # Rest on 7
    (69, 5.625, 0.375),  # Rest on 7
    (71, 5.625, 0.375),  # Rest on 7
    (64, 5.625, 0.375),  # Rest on 7
    (64, 6.0, 0.375)     # D7 - D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Dante: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),    # D
    (65, 1.875, 0.375),  # F
    (67, 2.25, 0.375),   # G
    (69, 2.625, 0.375),  # A (leave it hanging)
    (67, 3.0, 0.375),    # G
    (65, 3.375, 0.375),  # F
    (62, 3.75, 0.375),   # D
    (64, 4.125, 0.375),  # E
    (67, 4.5, 0.375),    # G
    (69, 4.875, 0.375),  # A
    (67, 5.25, 0.375),   # G
    (65, 5.625, 0.375),  # F
    (62, 6.0, 0.375)     # D (finish it)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums continue in bars 2-4
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1&
    (42, 1.6875, 0.1875),# Hihat on 2&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2&
    (42, 2.0625, 0.1875),# Hihat on 3&
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3&
    (42, 2.4375, 0.1875),# Hihat on 4&
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4&
    (42, 2.8125, 0.1875),# Hihat on 4&
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1&
    (42, 3.1875, 0.1875),# Hihat on 2&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2&
    (42, 3.5625, 0.1875),# Hihat on 3&
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3&
    (42, 3.9375, 0.1875),# Hihat on 4&
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4&
    (42, 4.3125, 0.1875),# Hihat on 4&
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1&
    (42, 4.6875, 0.1875),# Hihat on 2&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2&
    (42, 5.0625, 0.1875),# Hihat on 3&
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3&
    (42, 5.4375, 0.1875),# Hihat on 4&
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4&
    (42, 5.8125, 0.1875),# Hihat on 4&
    (36, 6.0, 0.375)     # Kick on 1
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

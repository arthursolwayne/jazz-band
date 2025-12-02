
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
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.875, 0.125),  # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.5, 0.125)     # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),    # D
    (63, 1.875, 0.375),  # Eb
    (60, 2.25, 0.375),   # C
    (62, 2.625, 0.375),  # D
    (64, 2.875, 0.375),  # E
    (62, 3.25, 0.375),   # D
    (60, 3.625, 0.375),  # C
    (59, 4.0, 0.375),    # Bb
    (62, 4.375, 0.375),  # D
    (64, 4.75, 0.375),   # E
    (62, 5.125, 0.375),  # D
    (60, 5.5, 0.375)     # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (62, 2.25, 0.375),  # D7 - D
    (67, 2.25, 0.375),  # D7 - G
    (64, 2.25, 0.375),  # D7 - Bb
    (69, 2.25, 0.375),  # D7 - D
    (62, 3.75, 0.375),  # D7 - D
    (67, 3.75, 0.375),  # D7 - G
    (64, 3.75, 0.375),  # D7 - Bb
    (69, 3.75, 0.375),  # D7 - D
    (62, 5.25, 0.375),  # D7 - D
    (67, 5.25, 0.375),  # D7 - G
    (64, 5.25, 0.375),  # D7 - Bb
    (69, 5.25, 0.375)   # D7 - D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.125),    # Hihat on 1
    (42, 1.625, 0.125),  # Hihat on &1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.125),  # Hihat on 2
    (42, 1.875, 0.125),  # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.125),   # Hihat on 3
    (42, 2.375, 0.125),  # Hihat on &3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.125),  # Hihat on 4
    (42, 2.625, 0.125),  # Hihat on 4
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.125),    # Hihat on 1
    (42, 3.125, 0.125),  # Hihat on &1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.125),  # Hihat on 2
    (42, 3.375, 0.125),  # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.125),   # Hihat on 3
    (42, 3.875, 0.125),  # Hihat on &3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.125),  # Hihat on 4
    (42, 4.125, 0.125),  # Hihat on 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.125),    # Hihat on 1
    (42, 4.625, 0.125),  # Hihat on &1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on 2
    (42, 4.875, 0.125),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.125),   # Hihat on 3
    (42, 5.375, 0.125),  # Hihat on &3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.125),  # Hihat on 4
    (42, 5.625, 0.125)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante) - mysterious, whispering motif with a cry at the end
sax_notes = [
    (62, 2.0, 0.25),     # D
    (64, 2.25, 0.25),    # E
    (62, 2.5, 0.25),     # D
    (60, 2.75, 0.25),    # C
    (62, 3.25, 0.25),    # D
    (64, 3.5, 0.25),     # E
    (67, 3.75, 0.5),     # G (hold longer, cry)
    (65, 4.25, 0.25),    # F
    (67, 4.5, 0.25),     # G
    (65, 4.75, 0.25),    # F
    (64, 5.0, 0.25),     # E
    (62, 5.25, 0.25),    # D
    (60, 5.5, 0.25)      # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.75),     # Kick on 1
    (38, 0.75, 0.75),    # Snare on 2
    (42, 0.0, 0.5),      # Hihat on 1 & 2
    (42, 0.5, 0.5),      # Hihat on 3 & 4
    (36, 1.25, 0.75),    # Kick on 3
    (38, 1.5, 0.75)      # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (60, 1.5, 0.375),    # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),   # D
    (63, 2.625, 0.375),  # D#
    (64, 3.0, 0.375),    # E
    (65, 3.375, 0.375),  # F
    (66, 3.75, 0.375),   # F#
    (67, 4.125, 0.375),  # G
    (68, 4.5, 0.375),    # G#
    (69, 4.875, 0.375),  # A
    (70, 5.25, 0.375),   # A#
    (71, 5.625, 0.375)   # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords, comp on 2 and 4
# Bar 2: C7 on beat 2
piano_notes = [
    (60, 2.25, 0.375),   # C
    (64, 2.25, 0.375),   # E
    (67, 2.25, 0.375),   # G
    (71, 2.25, 0.375),   # B
    # Bar 3: F7 on beat 2
    (65, 3.75, 0.375),   # F
    (69, 3.75, 0.375),   # A
    (71, 3.75, 0.375),   # B
    (76, 3.75, 0.375),   # D
    # Bar 4: G7 on beat 2
    (67, 5.25, 0.375),   # G
    (71, 5.25, 0.375),   # B
    (74, 5.25, 0.375),   # D
    (78, 5.25, 0.375)    # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums - Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.75),     # Kick on 1 (bar 2)
    (38, 1.875, 0.75),   # Snare on 2
    (42, 1.5, 0.5),      # Hihat on 1 and 2
    (42, 2.0, 0.5),      # Hihat on 3 and 4
    (36, 2.25, 0.75),    # Kick on 1 (bar 3)
    (38, 2.625, 0.75),   # Snare on 2
    (42, 2.25, 0.5),     # Hihat on 1 and 2
    (42, 2.75, 0.5),     # Hihat on 3 and 4
    (36, 3.0, 0.75),     # Kick on 1 (bar 4)
    (38, 3.375, 0.75),   # Snare on 2
    (42, 3.0, 0.5),      # Hihat on 1 and 2
    (42, 3.5, 0.5),      # Hihat on 3 and 4
    (36, 4.5, 0.75),     # Kick on 1 (bar 4)
    (38, 4.875, 0.75),   # Snare on 2
    (42, 4.5, 0.5),      # Hihat on 1 and 2
    (42, 5.0, 0.5)       # Hihat on 3 and 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - E - G - B (C7), then leave it hanging on B
sax_notes = [
    (60, 1.5, 0.375),    # C
    (64, 1.875, 0.375),  # E
    (67, 2.25, 0.375),   # G
    (71, 2.625, 0.375),  # B
    (71, 3.0, 0.375),    # B (hold)
    (71, 3.375, 0.375),  # B
    (71, 3.75, 0.375),   # B
    (71, 4.125, 0.375),  # B
    (71, 4.5, 0.375),    # B
    (71, 4.875, 0.375),  # B
    (71, 5.25, 0.375),   # B
    (71, 5.625, 0.375)   # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

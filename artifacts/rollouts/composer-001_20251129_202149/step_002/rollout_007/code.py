
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
    (42, 0.0, 0.375),    # Hihat on 1 & 2
    (38, 0.75, 0.75),    # Snare on 2
    (42, 0.75, 0.375),   # Hihat on 2 & 3
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.375),  # Hihat on 3 & 4
    (38, 1.5, 0.75),     # Snare on 4
    (42, 1.5, 0.375)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    (60, 1.5, 0.375),    # G
    (61, 1.875, 0.375),  # G#
    (62, 2.25, 0.375),   # A
    (63, 2.625, 0.375),  # A#
    (64, 3.0, 0.375),    # B
    (65, 3.375, 0.375),  # C#
    (66, 3.75, 0.375),   # D
    (67, 4.125, 0.375),  # D#
    (68, 4.5, 0.375),    # E
    (69, 4.875, 0.375),  # F#
    (70, 5.25, 0.375),   # G
    (71, 5.625, 0.375)   # G#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4.
piano_notes = [
    (60, 1.5, 0.375),    # C7 (C, E, B)
    (64, 1.5, 0.375),
    (67, 1.5, 0.375),
    (62, 1.875, 0.375),  # D7 (D, F#, C)
    (65, 1.875, 0.375),
    (69, 1.875, 0.375),
    (60, 2.25, 0.375),   # C7
    (64, 2.25, 0.375),
    (67, 2.25, 0.375),
    (62, 2.625, 0.375),  # D7
    (65, 2.625, 0.375),
    (69, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# You: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.5),      # A (start)
    (64, 2.0, 0.5),      # B (second note)
    (62, 2.5, 0.5),      # A (third note)
    (60, 3.0, 0.5),      # G (fourth note)
    (62, 3.5, 0.5),      # A (fifth note)
    (64, 4.0, 0.5),      # B (sixth note)
    (62, 4.5, 0.5),      # A (seventh note)
    (60, 5.0, 0.5)       # G (end)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")


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
    (36, 0.0, 0.375),      # Kick on 1
    (42, 0.0, 0.1875),     # Hihat on 1 & 2
    (38, 0.375, 0.375),    # Snare on 2
    (42, 0.375, 0.1875),   # Hihat on 2 & 3
    (36, 0.75, 0.375),     # Kick on 3
    (42, 0.75, 0.1875),    # Hihat on 3 & 4
    (38, 1.125, 0.375),    # Snare on 4
    (42, 1.125, 0.1875),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),      # D
    (63, 1.875, 0.375),    # Eb
    (64, 2.25, 0.375),     # E
    (65, 2.625, 0.375),    # F
    (67, 3.0, 0.375),      # G
    (68, 3.375, 0.375),    # G#
    (69, 3.75, 0.375),     # A
    (70, 4.125, 0.375),    # A#
    (72, 4.5, 0.375),      # B
    (73, 4.875, 0.375),    # C
    (74, 5.25, 0.375),     # C#
    (75, 5.625, 0.375),    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.5, 0.375),      # G7 (G, B, D, F)
    (69, 1.5, 0.375),
    (71, 1.5, 0.375),
    (69, 1.5, 0.375),
    (67, 1.875, 0.375),    # B7 (B, D#, F#, A)
    (71, 1.875, 0.375),
    (74, 1.875, 0.375),
    (76, 1.875, 0.375),
    (67, 2.625, 0.375),    # G7 (again)
    (69, 2.625, 0.375),
    (71, 2.625, 0.375),
    (69, 2.625, 0.375),
    (67, 3.375, 0.375),    # B7 (again)
    (71, 3.375, 0.375),
    (74, 3.375, 0.375),
    (76, 3.375, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.4995)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5])

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - G - B (D7 arpeggio, slow and deliberate)
sax_notes = [
    (62, 1.5, 0.375),      # D
    (66, 1.875, 0.375),    # F#
    (67, 2.25, 0.375),     # G
    (69, 2.625, 0.375),    # B
    (62, 3.0, 0.375),      # D again
    (66, 3.375, 0.375),    # F#
    (67, 3.75, 0.375),     # G
    (69, 4.125, 0.375),    # B
    (62, 4.5, 0.375),      # D
    (66, 4.875, 0.375),    # F#
    (67, 5.25, 0.375),     # G
    (69, 5.625, 0.375),    # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

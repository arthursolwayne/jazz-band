
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.375, 0.125),   # Hihat on &1
    (38, 0.75, 0.375),    # Snare on 2
    (42, 0.875, 0.125),   # Hihat on &2
    (36, 1.125, 0.375),   # Kick on 3
    (42, 1.5, 0.125),     # Hihat on &3
    (38, 1.875, 0.375),   # Snare on 4
    (42, 2.0, 0.125),     # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (Bass): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (45, 1.5, 0.375),    # A (F7)
    (46, 1.875, 0.375),  # Bb (F7)
    (47, 2.25, 0.375),   # B (F7)
    (48, 2.625, 0.375),  # C (F7)
    (50, 2.625, 0.375),  # D (F7)
    (49, 3.0, 0.375),    # C (F7)
    (48, 3.375, 0.375),  # B (F7)
    (47, 3.75, 0.375),   # A (F7)
    (46, 4.125, 0.375),  # G (F7)
    (45, 4.5, 0.375),    # F (F7)
    (46, 4.875, 0.375),  # G (F7)
    (47, 5.25, 0.375),   # A (F7)
    (48, 5.625, 0.375),  # Bb (F7)
    (49, 6.0, 0.375)     # B (F7)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane (Piano): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (53, 2.25, 0.125),   # F
    (57, 2.25, 0.125),   # A
    (60, 2.25, 0.125),   # C
    (62, 2.25, 0.125),   # D
    (53, 2.75, 0.125),   # F
    (57, 2.75, 0.125),   # A
    (60, 2.75, 0.125),   # C
    (62, 2.75, 0.125),   # D

    # Bar 3: F7 on 2 and 4
    (53, 3.25, 0.125),
    (57, 3.25, 0.125),
    (60, 3.25, 0.125),
    (62, 3.25, 0.125),
    (53, 3.75, 0.125),
    (57, 3.75, 0.125),
    (60, 3.75, 0.125),
    (62, 3.75, 0.125),

    # Bar 4: F7 on 2 and 4
    (53, 4.25, 0.125),
    (57, 4.25, 0.125),
    (60, 4.25, 0.125),
    (62, 4.25, 0.125),
    (53, 4.75, 0.125),
    (57, 4.75, 0.125),
    (60, 4.75, 0.125),
    (62, 4.75, 0.125),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray (Drums): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.125)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.875)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.25)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.625)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.875, end=bar_start + 2.0)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.25, end=bar_start + 2.375)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.625, end=bar_start + 2.75)

    drums.notes.extend([kick1, kick3, snare2, snare4,
                        hihat1, hihat2, hihat3, hihat4,
                        hihat5, hihat6, hihat7, hihat8])

# Dante (Sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (62), G (63), A (64), Bb (65) -> F7
sax_notes = [
    (62, 1.5, 0.125),  # F
    (63, 1.625, 0.125), # G
    (64, 1.75, 0.125),  # A
    (65, 1.875, 0.125), # Bb
    (62, 2.25, 0.125),  # F
    (63, 2.375, 0.125), # G
    (64, 2.5, 0.125),   # A
    (65, 2.625, 0.125), # Bb
    (62, 3.0, 0.125),   # F
    (63, 3.125, 0.125), # G
    (64, 3.25, 0.125),  # A
    (65, 3.375, 0.125), # Bb
    (62, 3.75, 0.125),  # F
    (63, 3.875, 0.125), # G
    (64, 4.0, 0.125),   # A
    (65, 4.125, 0.125), # Bb
    (62, 4.5, 0.125),   # F
    (63, 4.625, 0.125), # G
    (64, 4.75, 0.125),  # A
    (65, 4.875, 0.125), # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")

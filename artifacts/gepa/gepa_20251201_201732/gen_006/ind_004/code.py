
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # D (38) -> F (41) -> G (43) -> Bb (46) -> C (48) -> D (38) -> F (41) -> G (43)
    # Chromatic approach on G -> A -> G
    if bar == 2:
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start, end=start + 0.375))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=start + 0.375, end=start + 0.75))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start + 0.75, end=start + 1.125))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=start + 1.125, end=start + 1.5))
    elif bar == 3:
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=46, start=start, end=start + 0.375))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=start + 0.375, end=start + 0.75))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=start + 0.75, end=start + 1.125))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=start + 1.125, end=start + 1.5))
    elif bar == 4:
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start, end=start + 0.375))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=start + 0.375, end=start + 0.75))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=start + 0.75, end=start + 1.125))
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=start + 1.125, end=start + 1.5))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.375))  # D (62)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.5 + 0.375))  # F (65)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.375))  # A (69)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.5 + 0.375))  # C (72)

# Bar 3: G7 (G-B-D-F)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.0 + 0.375))  # G (67)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.0 + 0.375))  # B (71)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.0 + 0.375))  # D (69)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.0 + 0.375))  # F (65)

# Bar 4: Cm7 (C-Eb-G-Bb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.5 + 0.375))  # C (60)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.5 + 0.375))  # Eb (63)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.5 + 0.375))  # G (67)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.5 + 0.375))  # Bb (65)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Sax: D - Eb - F - D (MIDI 62 - 63 - 64 - 62), over 3 bars, with a rest on the 4th bar
# Bar 2: Play D - Eb - F - D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.5 + 0.375, end=1.5 + 0.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.125, end=1.5 + 1.5))

# Bar 3: Rest
# Bar 4: Repeat motif, but end with a note that lingers
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.5 + 0.375, end=4.5 + 0.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5 + 0.75, end=4.5 + 1.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5 + 1.125, end=4.5 + 1.5))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

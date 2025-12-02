
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Roots and fifths, chromatic approaches
# F - C - G - D
# Root movements: F -> C -> G -> D
# Times: 1.5s, 2.25s, 3.0s, 3.75s
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),   # F (root)
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625),  # C (fifth)
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),   # G (root)
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # D (fifth)
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.875),   # C# chromatic approach
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # D (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Am7 (A, C, E, G)
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),   # E

    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=3.0),   # F

    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),   # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),   # G
]
piano.notes.extend(piano_notes)

# Sax: Motif - one idea, start it, leave it hanging, return and finish
# F - G - A - F (start), then Bb - A - G - F (resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),   # F (on 2)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # G (on 3)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # A (on 3)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # F (on 4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # Bb (on 4)
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # A (on 2)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),   # G (on 3)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # F (on 4)
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick on 1 (bar_start)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Hihat on 1
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375))
    # Snare on 2 (bar_start + 0.75)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Hihat on 2
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3 (bar_start + 1.125)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on 3
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4 (bar_start + 1.5)
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875))
    # Hihat on 4
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")


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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Drum pattern continues
for i in range(3):
    start = 1.5 + i * 1.5
    # Kick
    midi.note_add(drums, pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    midi.note_add(drums, pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare
    midi.note_add(drums, pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875))
    midi.note_add(drums, pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0))
    # Hi-hat
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375))
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75))
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125))
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5))
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875))
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25))
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625))
    midi.note_add(drums, pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0))

# Bass line: Walking line (roots and fifths with chromatic approaches)
# F7 (F, C, Bb, E) -> Gm7 (G, D, F, Bb) -> Am7 (A, E, G, C) -> D7 (D, A, C, F)
bass_notes = [
    # Bar 2: F7 -> Gm7
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # E
    # Bar 3: Gm7 -> Am7
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),  # Bb
    # Bar 4: Am7 -> D7
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # E
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=66, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # F
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # G
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Introduce motif (F, G, A, Bb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.5),  # Bb
    # Bar 3: Leave it hanging (rest, then repeat motif at higher register)
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=83, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=82, start=3.75, end=4.0),  # Bb
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=87, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=89, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=88, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=86, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=70, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=70, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (root), D# (chromatic), F (fifth), F# (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=45, start=2.625, end=3.0),
    # Bar 3: G (root), G#, B (fifth), B#
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=48, start=4.125, end=4.5),
    # Bar 4: D (root), D#, F (fifth), F# (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=40, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=45, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=69, start=1.5, end=1.875),
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.375),
    # Bar 4: Dmin7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0
for bar_start in [1.5, 3.0]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hats on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=70, pitch=42, start=bar_start + i * 0.1875, end=bar_start + (i + 1) * 0.1875)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif (D, F#, A)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=4.875)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

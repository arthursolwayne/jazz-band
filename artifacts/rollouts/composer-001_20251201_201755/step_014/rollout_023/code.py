
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm7 -> Bbm7 -> Eb7 -> Am7
# Roots: F, Bb, Eb, A
# Walking line with chromatic approaches
bass_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # G
    # Bar 3: Bbm7
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # B
    # Bar 4: Eb7
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=46, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # F
    # Bar 4: Am7
    pretty_midi.Note(velocity=80, pitch=45, start=6.0, end=6.375),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=6.375, end=6.75),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=6.75, end=7.125),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=7.125, end=7.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=54, start=1.5, end=2.0),
    # Bar 3: Bbm7 (Bb, D, F, G)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.0),
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=45, start=6.0, end=6.5),
    pretty_midi.Note(velocity=100, pitch=52, start=6.0, end=6.5),
    pretty_midi.Note(velocity=100, pitch=57, start=6.0, end=6.5),
    pretty_midi.Note(velocity=100, pitch=55, start=6.0, end=6.5),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (43) -> Ab (41) -> Bb (42) -> F (43)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=43, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=41, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=42, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=43, start=2.25, end=2.5),
    pretty_midi.Note(velocity=110, pitch=42, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=41, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=43, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=44, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=42, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=41, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=43, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=44, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=42, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=41, start=5.75, end=6.0),
    pretty_midi.Note(velocity=110, pitch=43, start=6.0, end=6.25),
    pretty_midi.Note(velocity=110, pitch=44, start=6.25, end=6.5)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

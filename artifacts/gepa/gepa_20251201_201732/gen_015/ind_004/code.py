
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) -> G (40) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=39, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.0),
    # Bar 3: Bb (42) -> C (44) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=44, start=2.375, end=2.5),
    # Bar 4: D (38) -> E (41) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=41, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=41, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.75),  # E
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # Ab
    # Bar 4: D7sus (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # C
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
]
for start in [1.5, 2.0, 2.25, 2.5, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Bb (62), D (62), F (65)
# Bar 2: play F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),
    # Bar 3: play Bb (62)
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),
    # Bar 4: play D (62) then F (65)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

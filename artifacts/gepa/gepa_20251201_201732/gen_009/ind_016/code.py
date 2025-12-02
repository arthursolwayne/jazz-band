
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (chromatic approach), G2 (fifth), D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
    # Bar 3: G2 (root), A2 (chromatic approach), C3 (fifth), G2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
    # Bar 4: C3 (root), D3 (chromatic approach), F3 (fifth), C3 (root)
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=48, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),  # E
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.375),  # C
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=59, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - A - Bb (F, G, A, Bb), then repeat an octave higher (F, G, A, Bb)
# Play first motif from 1.5s to 2.5s, then repeat from 3.5s to 4.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=58, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # F (octave higher)
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=73, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=110, pitch=74, start=4.25, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")


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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root of F7)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.0),
    # Bar 3: G2 (fifth of Cmaj7)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to A2
    pretty_midi.Note(velocity=80, pitch=44, start=2.375, end=2.625),
    # Bar 4: A2 (root of Dm7)
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=2.875),
    # Chromatic approach to Bb2
    pretty_midi.Note(velocity=80, pitch=45, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=75, pitch=69, start=1.5, end=1.875),  # Eb

    # Bar 3: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.375),  # C
    pretty_midi.Note(velocity=85, pitch=76, start=2.0, end=2.375),  # E
    pretty_midi.Note(velocity=80, pitch=79, start=2.0, end=2.375),  # G
    pretty_midi.Note(velocity=75, pitch=82, start=2.0, end=2.375),  # B

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.875),  # A
    pretty_midi.Note(velocity=75, pitch=76, start=2.625, end=2.875),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (72) - G# (74) - F (72) - A (76) -> rest until bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.0),   # A
    # Rest until bar 4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=2.875),  # G#
    pretty_midi.Note(velocity=110, pitch=72, start=2.875, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Continue in bars 2-4
# Add more variety in the fill
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

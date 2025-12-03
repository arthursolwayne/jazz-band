
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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
    # Bar 2: F (38), C (43), chromatic approach to Bb (41)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 3: Bb (41), F (38), chromatic approach to Eb (40)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.5),
    # Bar 4: Eb (40), Bb (41), chromatic approach to Ab (40)
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.25),  # E
]
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # Ab
])
# Bar 4: Ebmaj7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # D
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) -> Bb (62) -> F (65) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

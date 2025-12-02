
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

# Bass line (walking line, Fm)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # C3
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Ab2
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # C3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Eb4
    # Bar 3: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # A5
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E6
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G5
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A6
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Motif: F, Ab, C, Bb (Fm triad with Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Ab5
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # C6
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # Bb6
    # Repeat motif resolved on F5
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # Ab5
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),  # C6
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # Bb6
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # F5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

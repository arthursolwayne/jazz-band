
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus) - walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F2

    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Eb2

    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D5
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875),  # G4
]
# Bar 3: Gm7 (Bb, D, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb4
])
# Bar 4: Cm7 (Eb, G, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # Eb5
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # C6
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # Eb5
])
piano.notes.extend(piano_notes)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]
# Bar 3 (3.0 - 4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
])
# Bar 4 (4.5 - 6.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])
drums.notes.extend(drum_notes)

# Sax (Dante) - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 - D (E5), Bb (D4), F (F4), D (E5)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # Bb5
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # A5
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),  # Bb5

    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # Bb5
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # F5
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # A5
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),  # Bb5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled


import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Fm, walking line with chromatic approaches)
bass_notes = [
    # Bar 2: F (D2), Ab (E2), G (F2), E (Eb2)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=39, start=2.625, end=3.0),
    # Bar 3: D (C2), F (D2), Eb (C#2), Ab (E2)
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),
    # Bar 4: G (F2), Bb (G2), A (Ab2), F (D2)
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano chords (Fm, Bb7, Eb7, Abmaj7)
piano_notes = [
    # Bar 2: Fm (F, Ab, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=2.25),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=5.25),
    # Bar 4: Abmaj7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax melody (Dante's motif)
sax_notes = [
    # Bar 2: Start the motif (F, Ab, G, Eb)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=50, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=52, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=51, start=2.25, end=2.5),
    # Bar 3: Leave it hanging (F, Ab, G)
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=50, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=52, start=3.5, end=3.75),
    # Bar 4: Return and finish it (Eb, F, Ab)
    pretty_midi.Note(velocity=110, pitch=51, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=53, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=50, start=5.0, end=5.25),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

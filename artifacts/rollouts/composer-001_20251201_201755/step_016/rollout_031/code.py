
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, Fm root and fifth with chromatic approaches
bass_notes = [
    # Bar 2: F (D2), chromatic approach on D#2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.875),
    # Bar 2: C (G2), chromatic approach on G#2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),
    # Bar 2: Ab (A2), chromatic approach on A#2
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),
    # Bar 2: D (B2), chromatic approach on C3
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),
    # Bar 4: Fm7 again for resolution
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm, short and singable
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 3: Continue
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    # Bar 4: Continue
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),
    # Bar 4: End the motif
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

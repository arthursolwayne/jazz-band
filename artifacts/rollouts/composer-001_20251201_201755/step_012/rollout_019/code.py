
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

# Bar 2: Everyone comes in
# Bass: F2 (D2) -> Ab2 (Eb2) -> Bb2 (F2) -> D2 (Ab2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875),  # Ab
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=56, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # D
]

piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Ab, Bb, F (hanging on Ab)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.625, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=2.75),  # Ab (return)
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=3.0),  # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')

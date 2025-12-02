
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
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2: Fm (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (Bass)
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3: Fm (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    # Bar 4: Fm (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),  # Eb
    # Bar 3: F7 (F, A, C, Eb) - comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F - Gb - Ab - (rest) - F - Gb - Ab - (rest)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=87, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=84, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=82, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=87, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=84, start=2.125, end=2.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=82, start=2.25, end=2.375),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")


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

# Bass line (Marcus): walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),  # F

    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # G

    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=37, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # C

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Ab

    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # Db
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),

    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax (Dante): one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

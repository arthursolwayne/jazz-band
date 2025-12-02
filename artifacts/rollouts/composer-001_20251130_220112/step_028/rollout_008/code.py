
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

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=36, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=35, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=34, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=33, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=32, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=31, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=30, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=31, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=32, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=33, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm (F, Ab, G, Eb), start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=110, pitch=61, start=2.0625, end=2.25), # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.4375, end=2.625), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.8125), # G
    pretty_midi.Note(velocity=110, pitch=61, start=2.8125, end=3.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1875),   # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=110, pitch=61, start=3.5625, end=3.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.9375, end=4.125), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=110, pitch=61, start=4.3125, end=4.5),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 1: Drums only
# Bar 2-4: Full quartet

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

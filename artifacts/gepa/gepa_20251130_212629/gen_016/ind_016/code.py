
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # A
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # A
]
piano.notes.extend(piano_notes)

# Sax: Dante - short motif, one phrase, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.1875, end=2.375), # E
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.5625, end=2.75), # E
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=2.9375), # D
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625), # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.5625, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.3125), # E
    pretty_midi.Note(velocity=110, pitch=60, start=4.3125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625), # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.0625, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.8125), # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.8125, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")

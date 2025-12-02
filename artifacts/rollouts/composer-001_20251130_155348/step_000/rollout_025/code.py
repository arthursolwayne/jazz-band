
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
]

bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (bars 2 and 4), comp in F
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    # Bar 3: Syncopated comp
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.8125), # D
    # Bar 4: F7 on 4
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # D
]

piano.notes.extend(piano_notes)

# Dante: Motif in F, short, singable, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # G
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')


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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),   # E
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),   # F#
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # C#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # C7
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax - melody (your moment)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    # Hi-hats
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    # Hi-hats
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=6.125, end=6.25),  # Snare
    # Hi-hats
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

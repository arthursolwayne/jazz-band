
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # Bb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping with Dm7, F7, Bb7, etc.
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.625),  # F
    # Bar 3
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.125),  # F
    # Bar 4
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=85, pitch=76, start=5.25, end=5.625),  # F
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Motif starts
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # G
    # Bar 3 - leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # G
    # Bar 4 - finish the motif
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

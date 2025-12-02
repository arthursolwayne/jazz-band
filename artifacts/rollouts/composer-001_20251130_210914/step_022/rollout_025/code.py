
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice. He's the anchor.
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=2.375, end=2.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.625),  # Db
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=90, pitch=43, start=2.875, end=3.0),  # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.625),  # F7
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.625),
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.375),  # F7
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.375),
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=59, start=2.75, end=2.875),  # F7
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=66, start=2.75, end=2.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
]
drums.notes.extend(drum_notes)

# Sax: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs — that's student shit.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.375),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")

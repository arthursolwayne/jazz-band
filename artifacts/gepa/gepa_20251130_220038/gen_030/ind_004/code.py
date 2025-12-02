
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=2.375, end=2.5),  # Bb
    # Bar 3 (2.5 - 4.0s)
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.5),  # Bb
    # Bar 4 (3.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=4.25, end=4.375),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.375, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=5.125, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=5.25, end=5.375),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=54, start=5.75, end=5.875),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=5.875, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    # Bar 3 (2.5 - 4.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),
    # Bar 4 (3.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=4.25, end=4.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=5.0, end=5.125),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=5.125, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=5.75, end=5.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums in Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=3.125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375),
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

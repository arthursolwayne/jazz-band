
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Gb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

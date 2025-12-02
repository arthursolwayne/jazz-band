
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # C
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),     # Hihat 1-2
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.5),     # Hihat 2-3
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=3.0),     # Hihat 3-4
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Hihat 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),     # Hihat 1-2
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=4.0),     # Hihat 2-3
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.5),     # Hihat 3-4
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),     # Hihat 1-2
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.5),     # Hihat 2-3
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=6.0),     # Hihat 3-4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat 4
]
drums.notes.extend(drum_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),    # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.1875, end=2.375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),    # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),    # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),    # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.1875, end=5.375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5),    # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.6875, end=5.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0),    # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

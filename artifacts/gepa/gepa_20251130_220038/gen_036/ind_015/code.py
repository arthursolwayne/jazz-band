
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=54, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Notes in Dm: D, Eb, F, G, A, Bb, C
# Motif: D - Eb - F - G (ascending)
# Then a rest, then repeat but end on Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),   # G
    # Rest
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.375, end=2.5),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")

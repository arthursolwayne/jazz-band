
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.6, end=1.7),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.7, end=1.8),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.8, end=1.9),  # E
    # Bar 3: Rest
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.1, end=3.2),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.2, end=3.3),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.3, end=3.4),  # E
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.6),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.6, end=4.7),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.7, end=4.8),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.8, end=4.9),  # E
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=4.9, end=5.0),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

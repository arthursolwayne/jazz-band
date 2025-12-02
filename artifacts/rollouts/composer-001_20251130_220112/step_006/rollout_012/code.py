
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
    pretty_midi.Note(start=0.0, end=0.375, pitch=36, velocity=100),
    pretty_midi.Note(start=1.125, end=1.5, pitch=36, velocity=100),
    # Snare on 2 and 4
    pretty_midi.Note(start=0.75, end=1.125, pitch=38, velocity=110),
    pretty_midi.Note(start=1.875, end=2.25, pitch=38, velocity=110),
    # Hi-hat on every eighth
    pretty_midi.Note(start=0.0, end=0.375, pitch=42, velocity=80),
    pretty_midi.Note(start=0.375, end=0.75, pitch=42, velocity=80),
    pretty_midi.Note(start=0.75, end=1.125, pitch=42, velocity=80),
    pretty_midi.Note(start=1.125, end=1.5, pitch=42, velocity=80),
    pretty_midi.Note(start=1.5, end=1.875, pitch=42, velocity=80),
    pretty_midi.Note(start=1.875, end=2.25, pitch=42, velocity=80),
    pretty_midi.Note(start=2.25, end=2.625, pitch=42, velocity=80),
    pretty_midi.Note(start=2.625, end=3.0, pitch=42, velocity=80)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(start=1.5, end=1.875, pitch=62, velocity=90),  # D
    pretty_midi.Note(start=1.875, end=2.25, pitch=61, velocity=90),  # C
    pretty_midi.Note(start=2.25, end=2.625, pitch=63, velocity=90),  # Eb
    pretty_midi.Note(start=2.625, end=3.0, pitch=64, velocity=90),   # E
    # Bar 3
    pretty_midi.Note(start=3.0, end=3.375, pitch=65, velocity=90),   # F
    pretty_midi.Note(start=3.375, end=3.75, pitch=64, velocity=90),   # E
    pretty_midi.Note(start=3.75, end=4.125, pitch=62, velocity=90),   # D
    pretty_midi.Note(start=4.125, end=4.5, pitch=61, velocity=90),    # C
    # Bar 4
    pretty_midi.Note(start=4.5, end=4.875, pitch=63, velocity=90),    # Eb
    pretty_midi.Note(start=4.875, end=5.25, pitch=64, velocity=90),    # E
    pretty_midi.Note(start=5.25, end=5.625, pitch=65, velocity=90),    # F
    pretty_midi.Note(start=5.625, end=6.0, pitch=67, velocity=90)     # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(start=1.5, end=1.875, pitch=62, velocity=90),  # D
    pretty_midi.Note(start=1.875, end=2.25, pitch=67, velocity=90),  # F#
    pretty_midi.Note(start=1.875, end=2.25, pitch=71, velocity=90),  # A
    pretty_midi.Note(start=1.875, end=2.25, pitch=64, velocity=90),  # C
    # Bar 3: D7 (same)
    pretty_midi.Note(start=3.0, end=3.375, pitch=62, velocity=90),
    pretty_midi.Note(start=3.375, end=3.75, pitch=67, velocity=90),
    pretty_midi.Note(start=3.375, end=3.75, pitch=71, velocity=90),
    pretty_midi.Note(start=3.375, end=3.75, pitch=64, velocity=90),
    # Bar 4: D7 (same)
    pretty_midi.Note(start=4.5, end=4.875, pitch=62, velocity=90),
    pretty_midi.Note(start=4.875, end=5.25, pitch=67, velocity=90),
    pretty_midi.Note(start=4.875, end=5.25, pitch=71, velocity=90),
    pretty_midi.Note(start=4.875, end=5.25, pitch=64, velocity=90)
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(start=1.5, end=1.875, pitch=69, velocity=110),  # Bb
    pretty_midi.Note(start=1.875, end=2.25, pitch=71, velocity=110),  # D
    pretty_midi.Note(start=2.25, end=2.625, pitch=69, velocity=110),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(start=3.0, end=3.375, pitch=67, velocity=110),  # F#
    pretty_midi.Note(start=3.375, end=3.75, pitch=69, velocity=110),  # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(start=4.5, end=4.875, pitch=71, velocity=110),  # D
    pretty_midi.Note(start=4.875, end=5.25, pitch=69, velocity=110),  # Bb
    pretty_midi.Note(start=5.25, end=5.625, pitch=71, velocity=110),  # D
    pretty_midi.Note(start=5.625, end=6.0, pitch=69, velocity=110)   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

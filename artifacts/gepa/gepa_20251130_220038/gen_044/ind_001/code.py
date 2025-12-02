
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    # Bar 3 - Dm7 (same chord, comp on 2 and 4 only)
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),
    # Bar 4 - Dm7 (same chord, comp on 2 and 4 only)
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax - the melody
sax_notes = [
    # Bar 2 - Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # C
    # Bar 3 - Continue the motif, make it sing
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # Eb
    # Bar 4 - Finish the motif, return to D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # G#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # D
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # D
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Eb - D - F
# Start on beat 2 of bar 2, leave it hanging on beat 3, return on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_piece.mid")

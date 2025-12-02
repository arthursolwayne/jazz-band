
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

# Bass line (Marcus): Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # Ab
]
piano.notes.extend(piano_notes)

# Sax (Dante): The melody — one short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # Eb
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

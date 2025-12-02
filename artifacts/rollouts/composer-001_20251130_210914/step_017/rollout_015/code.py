
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.125, end=2.25),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.375, end=2.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=2.75),  # A#
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=80, pitch=54, start=2.875, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 7th chord on 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),  # E
    # Bar 3 - 7th chord on 2
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),  # E
    # Bar 4 - 7th chord on 4
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.625),  # F# (start motif)
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # A (leave it hanging)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.125),  # F# (come back)
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625),  # A (resolve with a grace)
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # Bb (resolve)
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

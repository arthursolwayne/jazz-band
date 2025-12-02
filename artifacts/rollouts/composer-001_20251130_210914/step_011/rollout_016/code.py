
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.6875, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.0),    # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.1875),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=48, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=90, pitch=49, start=2.375, end=2.5625), # A#
    pretty_midi.Note(velocity=90, pitch=50, start=2.5625, end=2.75), # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=2.9375), # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=52, start=2.9375, end=3.125), # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.125, end=3.3125), # B
    pretty_midi.Note(velocity=90, pitch=50, start=3.3125, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=49, start=3.5, end=3.6875),   # A#
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=59, start=1.75, end=1.875),  # F7
    pretty_midi.Note(velocity=95, pitch=61, start=1.75, end=1.875),
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=1.875),
    pretty_midi.Note(velocity=95, pitch=65, start=1.75, end=1.875),
    pretty_midi.Note(velocity=95, pitch=59, start=2.25, end=2.375),
    pretty_midi.Note(velocity=95, pitch=61, start=2.25, end=2.375),
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.375),
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.375),
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=59, start=2.75, end=2.875),
    pretty_midi.Note(velocity=95, pitch=61, start=2.75, end=2.875),
    pretty_midi.Note(velocity=95, pitch=64, start=2.75, end=2.875),
    pretty_midi.Note(velocity=95, pitch=65, start=2.75, end=2.875),
    pretty_midi.Note(velocity=95, pitch=59, start=3.25, end=3.375),
    pretty_midi.Note(velocity=95, pitch=61, start=3.25, end=3.375),
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.375),
    pretty_midi.Note(velocity=95, pitch=65, start=3.25, end=3.375),
]
piano.notes.extend(piano_notes)

# Dante on sax: motif
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.0),   # A#
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875), # A
    # Bar 3 (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=60, start=2.1875, end=2.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5625), # A
    # Bar 4 (come back and finish it)
    pretty_midi.Note(velocity=100, pitch=63, start=2.9375, end=3.125), # A#
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.3125), # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.3125, end=3.5),   # G
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.6875),  # E
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),   # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.3125, end=3.5),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.1875, end=2.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.625),     # Snare
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=2.9375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),     # Snare
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

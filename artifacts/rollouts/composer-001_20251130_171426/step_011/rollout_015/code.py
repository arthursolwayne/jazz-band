
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
    # Hi-hat on every eighth
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

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=85, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=85, pitch=65, start=2.625, end=3.0),   # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),    # G
    pretty_midi.Note(velocity=85, pitch=68, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=85, pitch=70, start=4.125, end=4.5),   # A#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=4.875),    # B
    pretty_midi.Note(velocity=85, pitch=73, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=85, pitch=76, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),    # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),    # B
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),    # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),    # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),    # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),    # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),    # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),    # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),    # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125), # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
# Bar 3 (3.0 - 4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625), # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
])
# Bar 4 (4.5 - 6.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125), # Snare on 4
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

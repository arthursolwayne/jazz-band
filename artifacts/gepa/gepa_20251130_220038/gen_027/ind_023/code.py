
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

# Bass line: Marcus. Walking line, chromatic approaches, no repeating notes.
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.1875),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=2.1875, end=2.375), # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.375, end=2.5625), # A#
    pretty_midi.Note(velocity=90, pitch=54, start=2.5625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=2.9375),  # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=2.9375, end=3.125), # B
    pretty_midi.Note(velocity=90, pitch=55, start=3.125, end=3.3125), # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.3125, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.6875),   # A#
    pretty_midi.Note(velocity=90, pitch=52, start=3.6875, end=3.875), # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.875, end=4.0),    # G#
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.1875),   # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.1875, end=4.375), # F#
    pretty_midi.Note(velocity=90, pitch=48, start=4.375, end=4.5625), # F
]
bass.notes.extend(bass_notes)

# Piano: Diane. 7th chords, comp on 2 and 4. Stay out of the way.
# Bar 2
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=57, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.6875),  # D
    # Bar 3 (no piano on 1 and 3)
    pretty_midi.Note(velocity=95, pitch=57, start=2.375, end=2.5625),  # F7
    pretty_midi.Note(velocity=95, pitch=60, start=2.375, end=2.5625),  # A
    pretty_midi.Note(velocity=95, pitch=62, start=2.375, end=2.5625),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=2.375, end=2.5625),  # D
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=57, start=3.875, end=4.0),    # F7
    pretty_midi.Note(velocity=95, pitch=60, start=3.875, end=4.0),    # A
    pretty_midi.Note(velocity=95, pitch=62, start=3.875, end=4.0),    # C
    pretty_midi.Note(velocity=95, pitch=64, start=3.875, end=4.0),    # D
]
piano.notes.extend(piano_notes)

# Sax: Dante. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),   # A
    # Bar 3: Space
    # Bar 4: Continue motif
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),   # D
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
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
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

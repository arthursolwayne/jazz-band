
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

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # G#
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A#
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # B#
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=95, pitch=79, start=1.5, end=1.875),  # B
    # Bar 3: D7
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.375),  # B
    # Bar 4: D7
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=4.875),  # B
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.8125, end=5.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.9375, end=6.0),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=105, pitch=67, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=105, pitch=69, start=1.75, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=105, pitch=67, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=105, pitch=71, start=3.25, end=3.5),  # F#
    # Bar 4
    pretty_midi.Note(velocity=105, pitch=67, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=105, pitch=69, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=105, pitch=71, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=105, pitch=72, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=105, pitch=74, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=105, pitch=76, start=5.75, end=6.0),  # B
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

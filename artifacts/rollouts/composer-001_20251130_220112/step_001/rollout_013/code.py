
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
    # Hihat on every eighth
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

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.0625, end=2.25), # G#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.4375), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.4375, end=2.625), # A#
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.8125, end=3.0), # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.1875), # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.1875, end=3.375), # B
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=3.5625, end=3.75), # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping, angry energy
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.6875),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.4375),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.1875),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.1875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.0),
]
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (64) -> B (71) -> A (69) -> G (67) -> F (64)
# Start on bar 2, end on bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=71, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

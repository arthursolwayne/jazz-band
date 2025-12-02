
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in D (D F# A C)
# Start at 1.5s
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.0625, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.4375, end=2.625), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.8125, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.5625, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.9375, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.3125), # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.3125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),   # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.0625, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.4375, end=5.625), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.8125), # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.8125, end=6.0)    # C
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
# D7: D F# A C
# G7: G B D F
# C7: C E G B
piano_notes = [
    # Bar 2: D7 on 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.8125),
    # Bar 4: C7 on 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5625),
    # Bar 4: D7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625)
]
piano.notes.extend(piano_notes)

# Saxophone - one short motif, make it sing
# Start at 1.5s: D (62) - B (66) - D (62) - C (60), leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=60, start=2.0625, end=2.25)
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D (D F# A B)
# Start at 1.5s
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
# D7 (D F# A C) on 2nd and 4th beats
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # F#
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),   # C
]
piano.notes.extend(piano_notes)

# Dante: Saxophone - short motif starting at 1.5s
# D (62) -> F# (64) -> A (67) -> B (69) -> D (62) - then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_shorter_intro.mid")

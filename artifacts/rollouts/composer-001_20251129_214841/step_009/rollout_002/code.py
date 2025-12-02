
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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

# Marcus on bass - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),    # D
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.1875),  # D#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=2.1875, end=2.375), # E
    pretty_midi.Note(velocity=90, pitch=53, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=90, pitch=54, start=2.5625, end=2.75),  # F#
    pretty_midi.Note(velocity=90, pitch=55, start=2.75, end=2.9375),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=2.9375, end=3.125), # G#
    pretty_midi.Note(velocity=90, pitch=57, start=3.125, end=3.3125), # A
    pretty_midi.Note(velocity=90, pitch=58, start=3.3125, end=3.5),   # A#
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=3.6875),   # B
    # Wrap up
    pretty_midi.Note(velocity=90, pitch=60, start=3.6875, end=3.875), # C
    pretty_midi.Note(velocity=90, pitch=61, start=3.875, end=4.0),    # C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.1875),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.1875, end=4.375), # D#
    pretty_midi.Note(velocity=90, pitch=64, start=4.375, end=4.5625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=4.5625, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=4.9375),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.9375, end=5.125), # G
    pretty_midi.Note(velocity=90, pitch=68, start=5.125, end=5.3125), # G#
    pretty_midi.Note(velocity=90, pitch=69, start=5.3125, end=5.5),   # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.5, end=5.6875),   # A#
    pretty_midi.Note(velocity=90, pitch=71, start=5.6875, end=5.875), # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.875, end=6.0),    # C
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.1875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.1875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.1875),  # B
    # Bar 3 - F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.1875),  # D
    # Bar 4 - G7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.1875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.1875),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.1875),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.0, end=4.1875),  # F
]
piano.notes.extend(piano_notes)

# Dante on sax - motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 - start the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),   # A
    # Bar 3 - leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.1875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.1875, end=2.375), # A
    # Bar 4 - come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75), # C
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.9375, end=4.125), # C
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.3125), # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.3125, end=4.5),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),   # B
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.1875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.1875, end=5.375), # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.375, end=5.5625), # E
    pretty_midi.Note(velocity=110, pitch=64, start=5.5625, end=5.75), # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=5.9375), # C
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

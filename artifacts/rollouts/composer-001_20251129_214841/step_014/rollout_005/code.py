
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.5),  # D#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),  # A#
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # B
    # Wrap up with a chromatic approach to C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25),  # A#
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=5.5, end=5.75),  # G#
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # B
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # B
]
piano.notes.extend(piano_notes)

# Saxophone - short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # B
    # Repeat the first part of the motif
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # B
    # Final resolution
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.125, end=start + i * 0.125 + 0.125)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

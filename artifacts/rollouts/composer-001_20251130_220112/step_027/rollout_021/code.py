
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.125, end=2.25),  # G#
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=2.375, end=2.5),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.0),  # D
    # Bar 3 - Comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.75),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=2.75),  # D
    # Bar 4 - Comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax - One short motif, make it sing
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0),  # G
    # Bar 3: Leave it hanging, come back and finish it
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),  # G#
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75),  # G#
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=3.875),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=3.125, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.625),  # B
    pretty_midi.Note(velocity=80, pitch=70, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=3.875, end=4.0),  # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 - Comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5),  # D
    # Bar 4 - Comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.25),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=80, pitch=70, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.125),  # C#
    pretty_midi.Note(velocity=80, pitch=72, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.375),  # C#
    pretty_midi.Note(velocity=80, pitch=69, start=5.375, end=5.5),  # B
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4 - Comp on 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),  # F7 - F
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")

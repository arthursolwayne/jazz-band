
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.0),  # G#
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=80, pitch=54, start=2.125, end=2.25),  # A#
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=2.5, end=2.625),  # C#
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.875),  # D#
    pretty_midi.Note(velocity=80, pitch=62, start=2.875, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # E
]
# Bar 3: C7 on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # C
])
# Bar 4: G7 on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.0),  # G
])
piano.notes.extend(piano_notes)

# Sax: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (53) - A (55) - D (62) - F (53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=2.0),  # F
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Bass
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=3.125, end=3.25),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.5),  # D#
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.625, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.875, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.0, end=4.125),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=4.25, end=4.375),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=4.375, end=4.5),  # C#
]
bass.notes.extend(bass_notes)

# Bar 4: Bass
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.625),  # C#
    pretty_midi.Note(velocity=80, pitch=75, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=4.875),  # D#
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=80, pitch=79, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=80, pitch=80, start=5.125, end=5.25),  # G#
    pretty_midi.Note(velocity=80, pitch=81, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=80, pitch=83, start=5.375, end=5.5),  # B
    pretty_midi.Note(velocity=80, pitch=84, start=5.5, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=85, start=5.625, end=5.75),  # C#
    pretty_midi.Note(velocity=80, pitch=86, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=80, pitch=88, start=5.875, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Bar 3: Piano
# F7 on beat 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.25),  # E
]
piano.notes.extend(piano_notes)

# Bar 4: Piano
# C7 on beat 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.75),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=5.75, end=5.875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.875, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.0),  # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.375),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.5, end=2.625),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=2.75, end=2.875),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=2.875, end=3.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (C7)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),
    # Bar 2, beat 4 (C7)
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75),
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.5),
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.25),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2, beat 1 (E)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),
    # Bar 2, beat 2 (G)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    # Bar 3, beat 1 (G)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),
    # Bar 3, beat 2 (E)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),
    # Bar 3, beat 3 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),
    # Bar 3, beat 4 (G)
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.25),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=4.75, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=5.0, end=5.125),  # D#
    pretty_midi.Note(velocity=80, pitch=77, start=5.125, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=78, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=80, pitch=79, start=5.375, end=5.5),  # F#
    pretty_midi.Note(velocity=80, pitch=80, start=5.5, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=5.75),  # G#
    pretty_midi.Note(velocity=80, pitch=82, start=5.75, end=5.875),  # A
    pretty_midi.Note(velocity=80, pitch=83, start=5.875, end=6.0),  # A#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (B7)
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=75, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.375),
    # Bar 4, beat 4 (B7)
    pretty_midi.Note(velocity=90, pitch=71, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=75, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=78, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=82, start=5.875, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Bar 4, beat 1 (B)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),
    # Bar 4, beat 2 (D)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.375),
    # Bar 4, beat 3 (E)
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),
    # Bar 4, beat 4 (F)
    pretty_midi.Note(velocity=100, pitch=65, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

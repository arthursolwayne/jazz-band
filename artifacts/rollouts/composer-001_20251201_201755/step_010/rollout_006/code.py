
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Bar 2: C#2 (37) chromatic approach
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.0),
    # Bar 3: G2 (43)
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    # Bar 3: F#2 (42)
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.5),
    # Bar 4: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),
    # Bar 4: C#2 (37)
    pretty_midi.Note(velocity=100, pitch=37, start=2.875, end=3.0),
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # Bar 2: C#2 (37)
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.5),
    # Bar 3: G2 (43)
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.875),
    # Bar 3: F#2 (42)
    pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=4.0),
    # Bar 4: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),
    # Bar 4: C#2 (37)
    pretty_midi.Note(velocity=100, pitch=37, start=4.375, end=4.5),
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Bar 2: C#2 (37)
    pretty_midi.Note(velocity=100, pitch=37, start=4.875, end=5.0),
    # Bar 3: G2 (43)
    pretty_midi.Note(velocity=100, pitch=43, start=5.0, end=5.375),
    # Bar 3: F#2 (42)
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.5),
    # Bar 4: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=3.0),
])
# Bar 2: Dm7 again (echo)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),
])
# Bar 3: G7 again
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),
])
# Bar 4: Cm7 again
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.5),
])
# Add back the final Dm7 on the last bar
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),
])
# Repeat one more time for resolution
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.5),
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm (D F A C), but played as a question: D -> F -> A -> C -> D
sax_notes = [
    # Bar 2: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    # Bar 2: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),
    # Bar 2: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    # Bar 2: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    # Bar 3: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),
    # Bar 3: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),
    # Bar 3: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),
    # Bar 3: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5),
    # Bar 4: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),
    # Bar 4: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),
    # Bar 4: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),
    # Bar 4: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),
    # Bar 2: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    # Bar 2: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),
    # Bar 2: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),
    # Bar 2: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),
    # Bar 3: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),
    # Bar 3: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.75),
    # Bar 3: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),
    # Bar 3: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),
    # Bar 4: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),
    # Bar 4: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.25),
    # Bar 4: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.375),
    # Bar 4: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=4.375, end=4.5),
    # Bar 2: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),
    # Bar 2: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),
    # Bar 2: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    # Bar 2: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    # Bar 3: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),
    # Bar 3: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25),
    # Bar 3: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),
    # Bar 3: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5),
    # Bar 4: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625),
    # Bar 4: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),
    # Bar 4: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=5.875),
    # Bar 4: C (69)
    pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    # Hi-hat on every eighth
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

# Bass line (Marcus) - walking line in Dm
# Dm7: D F A C
bass_notes = [
    # Bar 2: D (root) -> F (b3) -> A (5) -> C (7)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    # Bar 3: Ab (chromatic approach) -> D (root) -> F (b3) -> Bb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.5),
    # Bar 4: C (7) -> D (root) -> F (b3) -> A (5)
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: Dm7 (D F A C) on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    # Bar 3: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    # Bar 4: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif (D F A), leave it hanging
sax_notes = [
    # Bar 2: D (62)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 2: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    # Bar 2: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    # Bar 3: D (62) - return to motif
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Bar 3: F (64)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    # Bar 3: A (67)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    # Bar 4: C (69) - finish the motif, leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),
]
sax.notes.extend(sax_notes)

# Add drum notes for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
]
# Bar 3: Kick on 1 and 3, snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
])
# Bar 4: Kick on 1 and 3, snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
])
# Hi-hat on every eighth for bars 2-4
for t in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.375))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

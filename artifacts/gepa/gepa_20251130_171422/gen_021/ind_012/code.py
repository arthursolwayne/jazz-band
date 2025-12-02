
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
# Bass: Walking line in F minor
bass_notes = [
    # F (1.5s) to Bb (1.75s)
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),
    # Ab (1.75s) to D (2.0s)
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),
    # C (2.0s) to E (2.25s)
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),
    # G (2.25s) to Bb (2.5s)
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.25),
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=76, start=2.5, end=2.75),
]
piano.notes.extend(piano_notes)

# Sax: Motif
sax_notes = [
    # First note: F (1.5s) to G# (1.75s)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),
    # Rest on 1.75s to 2.0s
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    # Next note: A (2.0s) to B (2.25s)
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),
    # Rest on 2.25s to 2.5s
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),
    # Next note: C (2.5s) to D (2.75s)
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),
    # Rest on 2.75s to 3.0s
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F minor
bass_notes = [
    # Bb (3.0s) to D (3.25s)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    # F (3.25s) to Ab (3.5s)
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),
    # C (3.5s) to E (3.75s)
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),
    # G (3.75s) to Bb (4.0s)
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=76, start=3.5, end=3.75),
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=72, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=76, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    # First note: F (3.0s) to G# (3.25s)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),
    # Rest on 3.25s to 3.5s
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),
    # Next note: A (3.5s) to B (3.75s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),
    # Rest on 3.75s to 4.0s
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),
    # Next note: C (4.0s) to D (4.25s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),
    # Rest on 4.25s to 4.5s
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F minor
bass_notes = [
    # Bb (4.5s) to D (4.75s)
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    # F (4.75s) to Ab (5.0s)
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),
    # C (5.0s) to E (5.25s)
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),
    # G (5.25s) to Bb (5.5s)
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=76, start=5.0, end=5.25),
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=72, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=76, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    # First note: F (4.5s) to G# (4.75s)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),
    # Rest on 4.75s to 5.0s
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),
    # Next note: A (5.0s) to B (5.25s)
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),
    # Rest on 5.25s to 5.5s
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),
    # Next note: C (5.5s) to D (5.75s)
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),
    # Rest on 5.75s to 6.0s
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

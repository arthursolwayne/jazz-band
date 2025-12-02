
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
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),
    # G7 on beat 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),
    # G7 on beat 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Complete motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=43, start=5.5, end=5.75),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),
    # G7 on beat 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Drums for bar 3 and 4
for bar in [3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar + 1.875, end=bar + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar, end=bar + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.1875, end=bar + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.375, end=bar + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.5625, end=bar + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.75, end=bar + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.9375, end=bar + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.125, end=bar + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.3125, end=bar + 1.5),
    # Add to drums
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5),
        pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=bar + 1.875, end=bar + 2.0),
        pretty_midi.Note(velocity=80, pitch=42, start=bar, end=bar + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.1875, end=bar + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.375, end=bar + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.5625, end=bar + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.75, end=bar + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 0.9375, end=bar + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.125, end=bar + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar + 1.3125, end=bar + 1.5),
    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

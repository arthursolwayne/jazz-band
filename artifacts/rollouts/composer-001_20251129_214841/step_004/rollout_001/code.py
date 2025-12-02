
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # C (1.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    # D# (1.875s)
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),
    # E (2.25s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    # F (2.625s)
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # C7 on beat 2 (1.875s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    # F7 on beat 4 (2.625s)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: motif in C, start it, leave it hanging
sax_notes = [
    # C (1.5s)
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.6875),
    # E (1.6875s)
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),
    # G (1.875s)
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625),
    # Bb (2.0625s)
    pretty_midi.Note(velocity=110, pitch=69, start=2.0625, end=2.25)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # C (3.0s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    # D# (3.375s)
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),
    # E (3.75s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    # F (4.125s)
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # C7 on beat 2 (3.375s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    # F7 on beat 4 (4.125s)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5)
]
piano.notes.extend(piano_notes)

# Sax: motif continuation and finish
sax_notes = [
    # C (3.0s)
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.1875),
    # E (3.1875s)
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375),
    # G (3.375s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625),
    # Bb (3.5625s)
    pretty_midi.Note(velocity=110, pitch=69, start=3.5625, end=3.75),
    # C (3.75s)
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=3.9375),
    # E (3.9375s)
    pretty_midi.Note(velocity=110, pitch=64, start=3.9375, end=4.125),
    # G (4.125s)
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.3125),
    # Bb (4.3125s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.3125, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    # C (4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    # D# (4.875s)
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),
    # E (5.25s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),
    # F (5.625s)
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # C7 on beat 2 (4.875s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    # F7 on beat 4 (5.625s)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Sax: motif continuation and finish
sax_notes = [
    # C (4.5s)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.6875),
    # E (4.6875s)
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875),
    # G (4.875s)
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625),
    # Bb (5.0625s)
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.25),
    # C (5.25s)
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.4375),
    # E (5.4375s)
    pretty_midi.Note(velocity=110, pitch=64, start=5.4375, end=5.625),
    # G (5.625s)
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.8125),
    # Bb (5.8125s)
    pretty_midi.Note(velocity=110, pitch=69, start=5.8125, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

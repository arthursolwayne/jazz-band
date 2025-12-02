
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
    # 0.0s: Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    # 0.375s: Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    # 0.75s: Snare on 3
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    # 1.125s: Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    # F (1.5s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    # Bb (1.875s)
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),
    # Eb (2.25s)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),
    # Ab (2.625s)
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),
    # 4th beat: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm
sax_notes = [
    # F (1.5s)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),
    # Ab (1.6875s)
    pretty_midi.Note(velocity=110, pitch=61, start=1.6875, end=1.875),
    # E (1.875s)
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0625),
    # Bb (2.0625s)
    pretty_midi.Note(velocity=110, pitch=61, start=2.0625, end=2.25),
    # D (2.25s)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),
    # F (2.4375s)
    pretty_midi.Note(velocity=110, pitch=65, start=2.4375, end=2.625),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    # Bb (3.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),
    # Eb (3.375s)
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75),
    # Ab (3.75s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),
    # F (4.125s)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75),
    # 4th beat: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm (variation)
sax_notes = [
    # F (3.0s)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1875),
    # Ab (3.1875s)
    pretty_midi.Note(velocity=110, pitch=61, start=3.1875, end=3.375),
    # E (3.375s)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625),
    # Bb (3.5625s)
    pretty_midi.Note(velocity=110, pitch=61, start=3.5625, end=3.75),
    # D (3.75s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375),
    # F (3.9375s)
    pretty_midi.Note(velocity=110, pitch=65, start=3.9375, end=4.125),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1, snare on 3, hihat on every eighth
drum_notes = [
    # 3.0s: Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    # 3.375s: Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    # 3.75s: Snare on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    # 4.125s: Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    # Eb (4.5s)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),
    # Ab (4.875s)
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),
    # F (5.25s)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),
    # Bb (5.625s)
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),
    # 4th beat: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm (finale)
sax_notes = [
    # F (4.5s)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6875),
    # Ab (4.6875s)
    pretty_midi.Note(velocity=110, pitch=61, start=4.6875, end=4.875),
    # E (4.875s)
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625),
    # Bb (5.0625s)
    pretty_midi.Note(velocity=110, pitch=61, start=5.0625, end=5.25),
    # D (5.25s)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),
    # F (5.4375s)
    pretty_midi.Note(velocity=110, pitch=65, start=5.4375, end=5.625),
    # Eb (5.625s)
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=5.8125),
    # F (5.8125s)
    pretty_midi.Note(velocity=110, pitch=65, start=5.8125, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1, snare on 3, hihat on every eighth
drum_notes = [
    # 4.5s: Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # 4.875s: Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    # 5.25s: Snare on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    # 5.625s: Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

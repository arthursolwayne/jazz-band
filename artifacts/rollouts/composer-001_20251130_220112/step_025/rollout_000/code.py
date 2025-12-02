
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
# Bass: Walking line, chromatic approaches
bass_notes = [
    # F - Gb - G - Ab (chromatic walk)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 1
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.625),  # Ab
    # Rest on beat 2
    # F7 on beat 3
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=2.25, end=2.375),  # Ab
    # Rest on beat 4
]
piano.notes.extend(piano_notes)

# Sax: Motif - F (71) Ab (74) G (72) F (71) - then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # Ab - A - Bb - B (chromatic walk)
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 1
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=3.0, end=3.125),  # Ab
    # Rest on beat 2
    # F7 on beat 3
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=3.875),  # Ab
    # Rest on beat 4
]
piano.notes.extend(piano_notes)

# Sax: Motif - F (71) Ab (74) G (72) F (71) - then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.125, end=3.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # B - C - Db - D (chromatic walk)
    pretty_midi.Note(velocity=80, pitch=73, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=4.875),  # Db
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # F7 on beat 1
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.625),  # Ab
    # Rest on beat 2
    # F7 on beat 3
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=5.25, end=5.375),  # Ab
    # Rest on beat 4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif - F (71) Ab (74) G (72) F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

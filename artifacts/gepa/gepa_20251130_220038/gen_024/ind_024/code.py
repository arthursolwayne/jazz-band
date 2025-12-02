
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
# Bass: Walking line in Fm, chromatic approach to Eb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0625),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=2.0625, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=2.4375, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=2.8125),  # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=2.8125, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 1 & 3
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # D
    # Bar 2: Fm7 on 3 & 4 (same chord)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif - short, melodic, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F (tenor sax)
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=3.1875, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=3.9375, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.3125),  # Db
    pretty_midi.Note(velocity=90, pitch=43, start=4.3125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on 1 & 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # D
    # Bar 3: Fm7 on 3 & 4 (same chord)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # D
]
piano.notes.extend(piano_notes)

# Sax: continuation of the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
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
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=4.6875, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.0625),  # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=5.0625, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=5.4375, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=5.8125),  # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=5.8125, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on 1 & 3
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # D
    # Bar 4: Fm7 on 3 & 4 (same chord)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # D
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')


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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax starts the melody
# C7 -> E7 -> G7 -> Bb7 -> C7 (one bar)
# Tempo: 120 BPM = 0.5s per beat
note_lengths = 0.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.5 + note_lengths),  # C7
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.0 + note_lengths),  # E7
    pretty_midi.Note(velocity=100, pitch=78, start=2.5, end=2.5 + note_lengths),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.0 + note_lengths),  # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.5 + note_lengths),  # C7
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in C minor, chromatic approach
# C -> Bb -> B -> C -> D -> C -> Eb -> D -> C -> E -> D -> C -> F -> E -> D -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.5 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=1.75, end=1.75 + 0.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.0 + 0.25),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.25 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.5 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.75 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.0 + 0.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.25 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.5 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.75 + 0.25),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.0 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.25 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.5 + 0.25),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=4.75 + 0.25),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.0 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.25 + 0.25),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, C7 and Eb7
# C7 (C, E, Bb, B) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.0 + 0.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.0 + 0.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.0 + 0.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.0 + 0.25),  # B
    # Eb7 (Eb, G, Db, D) on beat 4
    pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=3.5 + 0.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.5 + 0.25),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.5 + 0.25),  # Db
    pretty_midi.Note(velocity=90, pitch=63, start=3.5, end=3.5 + 0.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues the motif
# G7 -> Bb7 -> C7 -> E7 -> G7
note_lengths = 0.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=3.5, end=3.5 + note_lengths),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.0 + note_lengths),  # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.5 + note_lengths),  # C7
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.0 + note_lengths),  # E7
    pretty_midi.Note(velocity=100, pitch=78, start=5.5, end=5.5 + note_lengths),  # G7
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in C minor, chromatic approach
# G -> F -> F# -> G -> A -> G -> Bb -> A -> G -> C -> B -> A -> D -> C -> B -> A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.5 + 0.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=3.75 + 0.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.0, end=4.0 + 0.25),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.25 + 0.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.5 + 0.25),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=4.75 + 0.25),  # G
    pretty_midi.Note(velocity=80, pitch=66, start=5.0, end=5.0 + 0.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.25 + 0.25),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.5 + 0.25),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=5.75, end=5.75 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=6.0, end=6.0 + 0.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=6.25, end=6.25 + 0.25),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=6.5, end=6.5 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=6.75, end=6.75 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=7.0, end=7.0 + 0.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=7.25, end=7.25 + 0.25),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, G7 and Bb7
# G7 (G, B, D, F) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.0 + 0.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.0 + 0.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.0 + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.0 + 0.25),  # F
    # Bb7 (Bb, D, F, Ab) on beat 4
    pretty_midi.Note(velocity=90, pitch=66, start=5.5, end=5.5 + 0.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.5 + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.5 + 0.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.5 + 0.25),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Sax finishes the motif
# C7 -> E7 -> G7 -> Bb7 -> C7
note_lengths = 0.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.5 + note_lengths),  # C7
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.0 + note_lengths),  # E7
    pretty_midi.Note(velocity=100, pitch=78, start=6.5, end=6.5 + note_lengths),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=7.0, end=7.0 + note_lengths),  # Bb7
    pretty_midi.Note(velocity=100, pitch=72, start=7.5, end=7.5 + note_lengths),  # C7
]
sax.notes.extend(sax_notes)

# Marcus: Walking bass line in C minor, chromatic approach
# C -> Bb -> B -> C -> D -> C -> Eb -> D -> C -> E -> D -> C -> F -> E -> D -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.5 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=5.75, end=5.75 + 0.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=6.0, end=6.0 + 0.25),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=6.25, end=6.25 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=6.5, end=6.5 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=6.75, end=6.75 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=7.0, end=7.0 + 0.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=7.25, end=7.25 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=7.5, end=7.5 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=7.75, end=7.75 + 0.25),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=8.0, end=8.0 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=8.25, end=8.25 + 0.25),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=8.5, end=8.5 + 0.25),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=8.75, end=8.75 + 0.25),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=9.0, end=9.0 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=9.25, end=9.25 + 0.25),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, C7 and Eb7
# C7 (C, E, Bb, B) on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.0 + 0.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.0 + 0.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.0 + 0.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=6.0, end=6.0 + 0.25),  # B
    # Eb7 (Eb, G, Db, D) on beat 4
    pretty_midi.Note(velocity=90, pitch=61, start=7.5, end=7.5 + 0.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=7.5, end=7.5 + 0.25),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=7.5, end=7.5 + 0.25),  # Db
    pretty_midi.Note(velocity=90, pitch=63, start=7.5, end=7.5 + 0.25),  # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

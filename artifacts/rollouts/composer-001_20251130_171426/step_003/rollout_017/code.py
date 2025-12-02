
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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
# Sax - motif: Fm7 -> Bbm7 -> Eb7 -> Abmaj7
# Start on F, chromatic approach to Bb, then pentatonic up to Eb, resolve to Ab
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.125),  # E
    pretty_midi.Note(velocity=100, pitch=50, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5),    # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.75),    # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),    # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),    # Db
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0)     # Eb
]
sax.notes.extend(sax_notes)

# Bass - walking line: F -> Gb -> G -> Ab (chromatic approach)
# Then Bb -> C -> Db -> Eb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=54, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5)    # Eb
]
bass.notes.extend(bass_notes)

# Piano - comping on 2 and 4 with F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125)   # Eb
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats motif but shifts up a 4th (Bb -> Eb -> Ab -> Db)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.625),  # A
    pretty_midi.Note(velocity=100, pitch=54, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.0),    # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=4.0, end=4.25),    # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),    # F
    pretty_midi.Note(velocity=100, pitch=63, start=4.25, end=4.5),    # F#
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5)     # G
]
sax.notes.extend(sax_notes)

# Bass - walking line: Bb -> C -> Db -> Eb (chromatic approach)
# Then F -> Gb -> G -> Ab
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=54, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0)    # Ab
]
bass.notes.extend(bass_notes)

# Piano - comping on 2 and 4 with Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625)   # Ab
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax resolves motif with Ab, then chromatic approach to Db, then pentatonic up to G, resolve to C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.125),  # Gb
    pretty_midi.Note(velocity=100, pitch=57, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5),    # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),    # Db
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),    # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),    # C#
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0)     # E
]
sax.notes.extend(sax_notes)

# Bass - walking line: Ab -> Bb -> B -> C (chromatic approach)
# Then Db -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=80, pitch=64, start=6.0, end=6.375),   # Db
    pretty_midi.Note(velocity=80, pitch=65, start=6.375, end=6.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=6.75, end=7.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=7.125, end=7.5)    # F
]
bass.notes.extend(bass_notes)

# Piano - comping on 2 and 4 with Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),  # Gb
    pretty_midi.Note(velocity=90, pitch=60, start=6.75, end=7.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=6.75, end=7.125),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=6.75, end=7.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=6.75, end=7.125)   # Gb
]
piano.notes.extend(piano_notes)

# Drums in bar 3 and 4
for i in range(2):
    offset = 1.5 + i * 3.0
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=offset + 0.0, end=offset + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=offset + 1.125, end=offset + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=offset + 0.75, end=offset + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=offset + 1.875, end=offset + 2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 0.0, end=offset + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 0.375, end=offset + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 0.75, end=offset + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 1.125, end=offset + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 1.5, end=offset + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 1.875, end=offset + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 2.25, end=offset + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=offset + 2.625, end=offset + 3.0)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

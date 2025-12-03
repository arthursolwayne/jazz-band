
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Start motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),   # Gb
]
bass.notes.extend(bass_notes)

# Piano: Bb7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: C7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for i in range(3):
    start = 1.5 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hi-hat on every eighth
    for j in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

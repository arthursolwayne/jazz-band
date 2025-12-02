
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s): Full quartet
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)   # G
]
sax.notes.extend(sax_notes)

# Bass (walking line in C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Db
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0)   # Eb
]
bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 2 chord: C7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0)    # B
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s): Full quartet
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5)   # G
]
sax.notes.extend(sax_notes)

# Bass (walking line in C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5)   # Db
]
bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 3 chord: C7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5)    # B
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s): Full quartet
# Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0)   # G
]
sax.notes.extend(sax_notes)

# Bass (walking line in C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0)   # Eb
]
bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 4 chord: C7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0)    # B
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    end = start + 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=end),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=end)

drums.notes.extend(drums.notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')


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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif in Dm
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
]

sax.notes.extend(sax_notes)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # D
]

bass.notes.extend(bass_notes)

# Piano: comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2 (Dm7)
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # D
    # Bar 2, beat 4 (Gm7)
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),   # F
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
]

sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),   # D
]

bass.notes.extend(bass_notes)

# Piano: comping
piano_notes = [
    # Bar 3, beat 2 (Dm7)
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # D
    # Bar 3, beat 4 (Gm7)
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),   # F
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
]

sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),   # D
]

bass.notes.extend(bass_notes)

# Piano: comping
piano_notes = [
    # Bar 4, beat 2 (Dm7)
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # D
    # Bar 4, beat 4 (Gm7)
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),   # F
]

piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
]

# Hi-hat on every eighth
for i in range(12):
    start = 1.5 + i * 0.375
    end = start + 0.375
    if end > 6.0:
        break
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")

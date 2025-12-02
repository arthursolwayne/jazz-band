
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    # 4th beat: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Melody (variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C
    # 4th beat: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Melody (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=48, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # 2nd beat: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # C
    # 4th beat: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
for i in range(2):
    start = 3.0 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),

# Bar 4 (4.5 - 6.0s)
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # C7
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C7
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax melody - short motif, sing, leave it hanging, come back
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick1)
    drums.notes.append(kick2)

# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

# Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")

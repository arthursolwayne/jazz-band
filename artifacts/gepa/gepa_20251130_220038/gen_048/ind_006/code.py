
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),   # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),   # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),   # A
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody (whisper -> cry)
# Motif: Dm7 -> G7 -> Cm7 -> F7
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=95, pitch=65, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=95, pitch=67, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=95, pitch=71, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=95, pitch=74, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=95, pitch=74, start=4.25, end=4.5),   # A
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=95, pitch=74, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=5.0, end=5.25),   # A
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=95, pitch=69, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=95, pitch=67, start=5.75, end=6.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

for note in drums.notes:
    pass  # Already added in the first bar

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_moment.mid")

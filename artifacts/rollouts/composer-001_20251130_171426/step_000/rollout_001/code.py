
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
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.1875, end=2.375), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.6875, end=2.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.625),    # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.625, end=1.75),   # C#
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.0),    # Eb
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.125),    # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.125, end=2.25),   # E
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.375),   # E
    pretty_midi.Note(velocity=80, pitch=53, start=2.375, end=2.5),    # F
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.625),    # F
    pretty_midi.Note(velocity=80, pitch=54, start=2.625, end=2.75),   # F#
    pretty_midi.Note(velocity=80, pitch=54, start=2.75, end=2.875),   # F#
    pretty_midi.Note(velocity=80, pitch=55, start=2.875, end=3.0),    # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 = D, F, A, C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    # Bar 3: G7 = G, B, D, F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    # Bar 4: Cm7 = C, Eb, G, Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.6875, end=3.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.1875, end=4.375), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.125),    # G
    pretty_midi.Note(velocity=80, pitch=54, start=3.125, end=3.25),   # F#
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.375),   # G
    pretty_midi.Note(velocity=80, pitch=56, start=3.375, end=3.5),    # Ab
    pretty_midi.Note(velocity=80, pitch=56, start=3.5, end=3.625),    # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=3.625, end=3.75),   # A
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=3.875),   # A
    pretty_midi.Note(velocity=80, pitch=58, start=3.875, end=4.0),    # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=4.0, end=4.125),    # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.25),   # B
    pretty_midi.Note(velocity=80, pitch=59, start=4.25, end=4.375),   # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.375, end=4.5),    # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: G7 = G, B, D, F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    # Bar 4: Cm7 = C, Eb, G, Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.1875, end=5.375), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.6875, end=5.875), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.875, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.625),    # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.625, end=4.75),   # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=4.875),   # C
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.0),    # C#
    pretty_midi.Note(velocity=80, pitch=61, start=5.0, end=5.125),    # C#
    pretty_midi.Note(velocity=80, pitch=62, start=5.125, end=5.25),   # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.375),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.375, end=5.5),    # D#
    pretty_midi.Note(velocity=80, pitch=63, start=5.5, end=5.625),    # D#
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=5.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=5.875),   # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.875, end=6.0),    # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Cm7 = C, Eb, G, Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")

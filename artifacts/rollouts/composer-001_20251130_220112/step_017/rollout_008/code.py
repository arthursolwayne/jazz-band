
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat on 1&2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat on 2&3
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3&4
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Bass line: Dm7 walking bass
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Dm
# Melody: D - Eb - F - D (1.5-2.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Dm7 walking bass
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Dm (repeat of first motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Dm7 walking bass
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in Dm (repeat of first motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),   # Hihat on 1&2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),   # Hihat on 2&3
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3&4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat on 1&2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),   # Hihat on 2&3
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3&4
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.5),    # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

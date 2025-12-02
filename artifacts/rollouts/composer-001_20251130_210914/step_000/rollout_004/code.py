
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
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    # F (1.5) -> Gb (1.625) -> G (1.75) -> A (2.0)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=70, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.125),
    # C (2.125) -> B (2.25) -> A (2.375) -> G (2.5)
    pretty_midi.Note(velocity=100, pitch=76, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=74, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.625),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # F7 (1.75 - 2.0)
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=2.0),
    # B7 (2.5 - 2.75)
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=85, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=86, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=88, start=2.5, end=2.75),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - F, G, Ab, Bb (1.5 - 1.875), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=74, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=73, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=74, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    # F (3.0) -> Gb (3.125) -> G (3.25) -> A (3.5)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=70, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.625),
    # C (3.625) -> B (3.75) -> A (3.875) -> G (4.0)
    pretty_midi.Note(velocity=100, pitch=76, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=74, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.125),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # F7 (3.25 - 3.5)
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=77, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.5),
    # B7 (4.0 - 4.25)
    pretty_midi.Note(velocity=100, pitch=81, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=85, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=86, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=88, start=4.0, end=4.25),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation - Bb, C, D, F (3.0 - 3.375), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    # F (4.5) -> Gb (4.625) -> G (4.75) -> A (5.0)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=70, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.125),
    # C (5.125) -> B (5.25) -> A (5.375) -> G (5.5)
    pretty_midi.Note(velocity=100, pitch=76, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=75, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=74, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.625),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # F7 (4.75 - 5.0)
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=77, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=79, start=4.75, end=5.0),
    # B7 (5.5 - 5.75)
    pretty_midi.Note(velocity=100, pitch=81, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=85, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=86, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=88, start=5.5, end=5.75),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation - F, G, Ab, Bb (4.5 - 4.875), then resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=74, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=73, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=74, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

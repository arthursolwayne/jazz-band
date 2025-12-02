
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875), # C (Dm7 root)
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625), # B (Dm7 b7)
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D (Dm7 b3)
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.375),  # D# (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D (Dm7 b3)
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125), # C (Dm7 root)
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.5),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # B (Dm7 b7)
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D (Dm7 b3)
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # D# (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D (Dm7 b3)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Theme: Dm7 -> G7 -> Cm7
# Motif: D (62), Bb (62-67?), F (65), C (60) -> but with some tension

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.125), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.5), # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875), # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=4.0), # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.375), # B
    pretty_midi.Note(velocity=100, pitch=65, start=4.375, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.5), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.875), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0), # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Fill the bar again
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

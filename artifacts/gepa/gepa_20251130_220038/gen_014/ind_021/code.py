
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.5),  # C#
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D - Eb - F - D (hanging), then later come back with F - G - A - C
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # D (hanging)
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.125),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.125, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.625),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0),

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_moment.mid")

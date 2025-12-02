
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),   # G#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=80, pitch=56, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # A
    # Bar 3: B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # B
    # Bar 3: Leave it hanging, then come back
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # B
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # B
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
# Snare on 2 and 4
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.5)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.25)
# Hi-hat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
                    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
                    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
                    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
                    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
                    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
                    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
                    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
                    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
                    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
                    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
                    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
                    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
                    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
                    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
                    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
                    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
                    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
                    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
                    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
                    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
                    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
                    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
                    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")

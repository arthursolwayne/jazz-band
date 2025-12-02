
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # B7
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # B7
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # F#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    kick_start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 0.75, end=kick_start + 1.125)
# Snare on 2 and 4
for bar in range(2, 5):
    snare_start = bar * 1.5 + 0.75
    pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=38, start=snare_start + 0.75, end=snare_start + 1.125)
# Hihat on every eighth
for bar in range(2, 5):
    for i in range(4):
        hihat_start = bar * 1.5 + i * 0.375
        pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.375)

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
                    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.25),
                    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
                    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
                    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
                    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
                    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
                    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
                    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
                    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
                    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
                    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
                    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
                    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
                    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
                    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
                    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
                    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
                    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
                    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
                    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
                    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
                    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
                    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

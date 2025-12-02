
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

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # Eb7: Eb, G, Bb, D
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Eb7: Eb, G, Bb, D
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # Eb7: Eb, G, Bb, D
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")

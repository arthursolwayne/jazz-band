
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
    # Hihat on every eighth
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
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),   # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D7: A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # D7: F#
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D7: A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D7: D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D7: F#
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D7: A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D7: F#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (start of motif)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B
    # Bar 3 (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    # Bar 4 (come back and finish it)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

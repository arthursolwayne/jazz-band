
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
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),  # Fm b9
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),  # Fm 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # Fm 5
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Fm 7
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # Fm b13
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Fm 5
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),   # Fm 3
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # Fm root
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.25),  # Fm b9
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # Fm 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Fm 5
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=60, start=1.875, end=2.25),  # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=3.0),
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.5),
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=95, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=95, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=95, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=95, pitch=69, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.6875, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.4375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.4375, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.8125),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0),  # E
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

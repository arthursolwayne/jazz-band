
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
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Ab
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=1.6875, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0625),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.4375, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.8125, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.1875, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.9375, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.3125),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.3125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0625, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.8125, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

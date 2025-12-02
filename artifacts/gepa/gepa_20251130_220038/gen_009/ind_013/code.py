
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

# Bass line (Marcus) - walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # G#
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # B
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F#
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.875),  # F
    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - short motif, make it sing, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.1875, end=2.375),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=2.375, end=2.5625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.9375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.9375, end=3.125),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.3125),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.3125, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.6875),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.6875, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0625, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.4375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.4375, end=4.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.8125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.8125, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.1875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.1875, end=5.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.5625, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=5.9375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.9375, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

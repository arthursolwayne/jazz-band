
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

# Bass line: Marcus (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    # Bar 3 (2.25 - 3.0)
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # F
    # Bar 4 (3.0 - 3.75)
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),   # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (melody: one short motif, make it sing)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.8125, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5625, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.9375, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.3125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.8125, end=6.0),   # D
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

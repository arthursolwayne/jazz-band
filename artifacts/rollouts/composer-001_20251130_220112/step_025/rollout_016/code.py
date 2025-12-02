
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # F

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # F#

    # Bar 3
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),  # F#

    # Bar 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # F#
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),  # Hihat

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),  # Hihat

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),  # Hihat
]
for note in drum_notes:
    drums.notes.append(note)

# Saxophone (Dante): One short motif, make it sing
# Start on D (62), play a triplet on 1 & 2, leave it hanging
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # A

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),   # D (half note)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625),  # D (half note)
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.75), # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),  # D

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),  # A
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

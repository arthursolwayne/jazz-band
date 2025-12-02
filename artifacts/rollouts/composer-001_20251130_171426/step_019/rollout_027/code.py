
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

# Bass line (Marcus): walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=35, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=34, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=33, start=2.625, end=3.0),   # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=32, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=31, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=30, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=35, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=34, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=33, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=32, start=5.625, end=6.0),   # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): 4-bar motif, Fm, one short phrase, leave it hanging
sax_notes = [
    # Start the motif on 2 of bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # G (Fm7)
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.125, end=2.25),  # A
    # Leave it hanging, come back on 2 of bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.625, end=3.75),  # A
    # End it on 2 of bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.125, end=5.25),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")

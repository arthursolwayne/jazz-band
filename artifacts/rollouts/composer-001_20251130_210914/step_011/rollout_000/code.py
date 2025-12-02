
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

# BASS: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # Ab

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # F

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=39, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),   # F7: F, A, C, Eb
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# SAX: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.6875),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0),    # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.1875),   # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.1875, end=2.375), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.5),    # A
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.6875),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.6875, end=2.875), # A

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.1875),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5),    # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.6875),   # A
    pretty_midi.Note(velocity=110, pitch=66, start=3.6875, end=3.875), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.875, end=4.0),    # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.1875),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.1875, end=4.375), # A

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.6875),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.0),    # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.1875),   # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.1875, end=5.375), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.375, end=5.5),    # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.6875),   # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.6875, end=5.875), # A
    pretty_midi.Note(velocity=110, pitch=66, start=5.875, end=6.0),    # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

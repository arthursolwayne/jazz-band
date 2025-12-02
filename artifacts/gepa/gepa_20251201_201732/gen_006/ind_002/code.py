
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): Walking line with roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2 - Fm7 (F, C, Ab, D)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=56, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # D

    # Bar 3 - Bb7 (Bb, F, Db, G)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G

    # Bar 4 - Eb7 (Eb, Bb, G, C)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2 - Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=3.0),
    # Bar 3 - Bb7 (Bb, D, F, G)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),
    # Bar 4 - Eb7 (Eb, G, Bb, C)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Gb, Ab, F (Fm scale)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=2.625, end=3.0),  # F
    # Repeat motif starting at bar 3
    pretty_midi.Note(velocity=110, pitch=48, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=63, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=4.125, end=4.5),  # F
    # Repeat motif starting at bar 4
    pretty_midi.Note(velocity=110, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=5.625, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

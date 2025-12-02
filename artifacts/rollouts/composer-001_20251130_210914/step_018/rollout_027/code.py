
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0),   # G#
    pretty_midi.Note(velocity=90, pitch=73, start=2.0, end=2.125),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.375, end=2.5),   # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),   # E
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),   # G#
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),  # G (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.625),  # E
    pretty_midi.Note(velocity=80, pitch=81, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.375),  # G (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=80, pitch=81, start=2.25, end=2.375),  # G

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.125),  # G (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=80, pitch=81, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=3.875),  # G (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=80, pitch=81, start=3.75, end=3.875),  # G

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.625),  # G (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.625),  # E
    pretty_midi.Note(velocity=80, pitch=81, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.375),  # G (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.375),  # C
    pretty_midi.Note(velocity=80, pitch=78, start=5.25, end=5.375),  # E
    pretty_midi.Note(velocity=80, pitch=81, start=5.25, end=5.375),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif (F, G#, A, F) - start, leave hanging, finish
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),   # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.125),   # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.25),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.375),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.375, end=2.5),   # G#
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.625),   # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=2.875),   # F
    pretty_midi.Note(velocity=100, pitch=70, start=2.875, end=3.0),    # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.125),    # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),    # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.375),    # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),     # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.625),     # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75),     # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875),     # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),      # G#
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.125),      # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.25),      # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.25, end=4.375),      # F
    pretty_midi.Note(velocity=100, pitch=70, start=4.375, end=4.5),       # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

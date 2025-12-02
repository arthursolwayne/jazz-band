
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.125, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.375),  # F#
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=2.875, end=3.0),  # F#

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=3.125, end=3.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.375),  # F#
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.5, end=3.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.875, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.25),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=4.25, end=4.375),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=4.375, end=4.5),  # G

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.375),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=5.375, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=5.5, end=5.625),  # Gb
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.75, end=5.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=5.875, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),  # Bb

    # Bar 3 (3.0 - 4.5s) - Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=46, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.0),  # Bb

    # Bar 4 (4.5 - 6.0s) - Comp on 2 and 4
    pretty_midi.Note(velocity=90, pitch=46, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.5),  # Bb
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 -> Bb7 -> Eb7 -> A7 -> F7
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - Start the motif
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F7
    pretty_midi.Note(velocity=110, pitch=60, start=1.625, end=1.75),  # Bb7
    pretty_midi.Note(velocity=110, pitch=57, start=1.75, end=1.875),  # Eb7
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # A7

    # Bar 3 (3.0 - 4.5s) - Leave it hanging, come back
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),  # F7
    pretty_midi.Note(velocity=110, pitch=60, start=3.125, end=3.25),  # Bb7
    pretty_midi.Note(velocity=110, pitch=57, start=3.25, end=3.375),  # Eb7
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),  # A7

    # Bar 4 (4.5 - 6.0s) - Finish it
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625),  # F7
    pretty_midi.Note(velocity=110, pitch=60, start=4.625, end=4.75),  # Bb7
    pretty_midi.Note(velocity=110, pitch=57, start=4.75, end=4.875),  # Eb7
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),  # A7
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.125),  # F7
    pretty_midi.Note(velocity=110, pitch=60, start=5.125, end=5.25),  # Bb7
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.375),  # Eb7
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5),  # A7
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.625),  # F7
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=5.75),  # Bb7
    pretty_midi.Note(velocity=110, pitch=57, start=5.75, end=5.875),  # Eb7
    pretty_midi.Note(velocity=110, pitch=62, start=5.875, end=6.0),  # A7
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_russo_intro.mid")

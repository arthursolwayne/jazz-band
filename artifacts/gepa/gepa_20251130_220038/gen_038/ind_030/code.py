
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.75),  # Fm7 - F
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=39, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.5),  # Gb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=3.25, end=3.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=39, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=4.25, end=4.5),  # F
    # Bar 4 continuation
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=41, start=5.5, end=5.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=40, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=59, start=1.75, end=2.0),  # E7 - B
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # F7 - C
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # F7 - E
    # Bar 2 - 4th beat
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # F7 - C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F7 - G
    # Bar 3 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # G7 - D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # G7 - E
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G7 - F#
    # Bar 3 - 4th beat
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # G7 - E
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G7 - F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # G7 - A
    # Bar 4 - 2nd beat
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # F7 - C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F7 - G
    # Bar 4 - 4th beat
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # F7 - G
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # F7 - Bb
    # Bar 4 - continuation
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F7 - G
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F7 - G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # F7 - Bb
]
piano.notes.extend(piano_notes)

# Tenor sax: Dante - one short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # F
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

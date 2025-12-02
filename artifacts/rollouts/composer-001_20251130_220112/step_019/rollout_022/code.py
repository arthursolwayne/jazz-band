
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.125),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.125),  # C
    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.125),  # B
    pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=83, start=3.0, end=3.125),  # F#
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=4.0, end=4.125),  # B
]
piano.notes.extend(piano_notes)

# Sax: Motif in D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # F#
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

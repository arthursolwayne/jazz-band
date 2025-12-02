
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Bb7
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Bb7
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)

# Sax (Dante): One short motif, make it sing
# Start at bar 2, first beat
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.4375, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.8125, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.625),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.9375),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.9375, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.375),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.375, end=4.625),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.125),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.375),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.375, end=5.625),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.875, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

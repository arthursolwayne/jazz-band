
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # D

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=4.125, end=4.5),  # F#

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # G

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # G

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)

drums.notes.extend(drum_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # A
]

# Bar 3: Leave it hanging (no notes)
# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # G
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

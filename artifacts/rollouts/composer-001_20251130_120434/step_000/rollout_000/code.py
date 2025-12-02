
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),  # D#
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.0),  # A#
    pretty_midi.Note(velocity=80, pitch=73, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=75, start=4.5, end=4.75),  # C#
    pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=5.0, end=5.25),  # D#
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=80, pitch=81, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=80, pitch=82, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),  # Bb

    # Bar 3 (2.5 - 3.0)
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),  # Bb

    # Bar 4 (3.5 - 4.0)
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=4.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 1.75)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # D
    # Bar 3 (2.5 - 2.75)
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # D
    # Bar 4 (3.5 - 3.75)
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # D
    # Bar 4 (4.0 - 4.25)
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # F
    # Bar 4 (4.5 - 4.75)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # G
    # Bar 4 (5.0 - 5.25)
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # A
    # Bar 4 (5.5 - 5.75)
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75),  # B
    # Bar 4 (6.0 - 6.25)
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.25),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 (1.5 - 3.0)
for i in range(2):
    offset = 1.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=offset + 0.0, end=offset + 0.375),
        pretty_midi.Note(velocity=110, pitch=38, start=offset + 0.75, end=offset + 0.875),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.0, end=offset + 0.125),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.125, end=offset + 0.25),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.25, end=offset + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.375, end=offset + 0.5),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.5, end=offset + 0.625),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.625, end=offset + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.75, end=offset + 0.875),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 0.875, end=offset + 1.0),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.0, end=offset + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.125, end=offset + 1.25),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.25, end=offset + 1.375),
        pretty_midi.Note(velocity=90, pitch=42, start=offset + 1.375, end=offset + 1.5)
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")

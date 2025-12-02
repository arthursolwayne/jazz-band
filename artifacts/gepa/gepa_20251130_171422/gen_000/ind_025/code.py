
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0),  # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.125, end=2.25),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=2.375, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=2.625, end=2.75),  # C#
    pretty_midi.Note(velocity=90, pitch=57, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=2.875, end=3.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # F7: F, A, C, E
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=1.6875, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.1875),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.1875, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),  # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.6875),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.6875, end=2.875),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")

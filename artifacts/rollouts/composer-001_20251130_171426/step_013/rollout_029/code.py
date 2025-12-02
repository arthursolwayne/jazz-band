
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

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Marcus on bass - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75), # G#
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),  # A#
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # E
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Dante on sax - motif over Dm
sax_notes = [
    # Bar 2 (start at 1.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25), # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

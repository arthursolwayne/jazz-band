
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
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=78, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # G7
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875),  # F
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=95, pitch=66, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)

# Sax: Melody - D, E, F, D - ascending and descending
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=105, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=105, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=105, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=105, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=105, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=105, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=105, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=105, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

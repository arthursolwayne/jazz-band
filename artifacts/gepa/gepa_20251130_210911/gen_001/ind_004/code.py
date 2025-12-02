
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=39, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # Fm7
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: Dante - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Motif starts in bar 2, ends in bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=57, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

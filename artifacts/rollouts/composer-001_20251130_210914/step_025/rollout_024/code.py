
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=54, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # A
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (with slight bends and syncopation)
sax_notes = [
    # Bar 2 (first part of motif)
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.9375),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.1875),   # C
    # Bar 3 (leave it hanging)
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),  # F
    # Bar 4 (come back and finish)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.9375),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.1875),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
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

midi.write("dante_intro.mid")


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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums for bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375),  # Hihat on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125), # Hihat on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),  # Hihat on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),  # Snare on 4
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875),  # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

# Bass line: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # F#
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # F#
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # F#
]
piano.notes.extend(piano_notes)

# Sax: D melody in 4 bars, motif and return
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # C#

    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D7 (F#)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # D7 (F#)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=3.0),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # D7 (F#)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
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

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

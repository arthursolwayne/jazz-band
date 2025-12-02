
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),  # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4.
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875),   # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.375),   # D7
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.875),   # D7
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 1 & 2
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.5)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.4375, end=2.625),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.8125, end=3.0),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),   # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.5625, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.3125), # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.3125, end=4.5),   # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.0625, end=5.25),  # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

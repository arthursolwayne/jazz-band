
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

# Bass line - walking line with chromatic approaches
# Bar 2: D (2.0) -> Eb (2.25) -> F (2.5) -> G (2.75)
# Bar 3: A (3.0) -> Bb (3.25) -> B (3.5) -> C (3.75)
# Bar 4: D (4.0) -> Eb (4.25) -> F (4.5) -> G (4.75)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
# Bar 2: D7 (2.25 - 2.5)
# Bar 3: A7 (3.25 - 3.5)
# Bar 4: D7 (4.25 - 4.5)
piano_notes = [
    # D7: D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),
    # A7: A, C#, E, G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=79, start=3.25, end=3.5),
    # D7: D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax - motif: D (1.5) -> Eb (1.875) -> F (2.25) -> G (2.625) -> D (3.0)
# Then leave it hanging at G (2.625) and return to D (4.0)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.375),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3 of each bar
# Snare on 2 and 4 of each bar
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

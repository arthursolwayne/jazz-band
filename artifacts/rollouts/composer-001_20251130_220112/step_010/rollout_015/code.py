
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=t, end=t+0.1) for t in kick_times])
drums.notes.extend([pretty_midi.Note(velocity=100, pitch=38, start=t, end=t+0.1) for t in snare_times])
drums.notes.extend([pretty_midi.Note(velocity=100, pitch=42, start=t, end=t+0.05) for t in hihat_times])

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=2.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=49, start=2.0, end=2.25)),  # C
    (pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5)),  # D
    (pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=2.75)),  # F
    (pretty_midi.Note(velocity=100, pitch=51, start=2.75, end=3.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=49, start=3.25, end=3.5)),  # C
    (pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.0)),  # F
    (pretty_midi.Note(velocity=100, pitch=51, start=4.0, end=4.25)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5)),  # D
    (pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.75)),  # C
    (pretty_midi.Note(velocity=100, pitch=50, start=4.75, end=5.0)),  # D
    (pretty_midi.Note(velocity=100, pitch=52, start=5.0, end=5.25)),  # F
    (pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.5)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=50, start=5.5, end=5.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=49, start=5.75, end=6.0)),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4 (1.5-6.0s)
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # D
    # Bar 3: G7
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.5),  # F#
    # Bar 4: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # Bb
    # Bar 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, come back and finish it
# Motif: D (62) -> F (65) -> Bb (67) -> D (69) -> D (62)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # F
]
# Bar 3: Leave it hanging
# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')

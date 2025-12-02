
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

# Marcus: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=72, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=76, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=95, pitch=79, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=81, start=1.75, end=2.0),  # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=72, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=95, pitch=76, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=95, pitch=79, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=95, pitch=81, start=3.25, end=3.5),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=95, pitch=72, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=95, pitch=76, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=95, pitch=79, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=81, start=4.75, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625),  # D (tenor sax C = piano D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=5.125, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for eighth in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + eighth * 0.375, end=start + eighth * 0.375 + 0.1875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')


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

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
    # Bar 2: comp on 2 and 4 (rests on 1 and 3)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.4375),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=2.4375, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.1875, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.9375, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.4375),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=5.4375, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=5.8125),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.8125, end=6.0),   # D
]
sax.notes.extend(sax_notes)

# Drums: Continue with hihat and kick/snare pattern for bars 2-4
for i in range(2, 4):
    start_time = i * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for j in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start_time + (j * 0.1875), end=start_time + (j * 0.1875) + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_4bar.mid")


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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (38) -> F# (41) -> G (43) -> B (46)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=3.0),
    # Bar 3: G (43) -> Bb (44) -> B (46) -> D (38)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Bar 4: D (38) -> F# (41) -> G (43) -> B (46)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5),
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62) -> B (67) -> C (60) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=110, pitch=60, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=110, pitch=60, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=110, pitch=60, start=3.875, end=4.0),
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=110, pitch=60, start=4.375, end=4.5),
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=110, pitch=60, start=5.375, end=5.5),
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=110, pitch=60, start=5.875, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')


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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> F#2 (41) -> G2 (43)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # Bar 3: A2 (45) -> B2 (46) -> C#3 (48)
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=46, start=2.8125, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=48, start=3.1875, end=3.5625),
    # Bar 4: F#2 (41) -> G2 (43) -> A2 (45)
    pretty_midi.Note(velocity=100, pitch=41, start=3.5625, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=43, start=3.9375, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=45, start=4.3125, end=4.6875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # C#4

    # Bar 3: Bm7 (B-D-F#-A)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # A4

    # Bar 4: D7 (D-F#-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5625, end=4.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5625, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5625, end=4.0),  # C4
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + (i * 0.375), end=start + (i * 0.375) + 0.1875)
    drums.notes.extend([  # Kick
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        # Snare
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
        # Hihat
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.5)
    ])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), E (64), F# (67), D (62)
sax_notes = [
    # First note at 1.5s
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Second note at 2.0s
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.375),
    # Third note at 2.5s
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875),
    # Return to D at 3.5s
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.875)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

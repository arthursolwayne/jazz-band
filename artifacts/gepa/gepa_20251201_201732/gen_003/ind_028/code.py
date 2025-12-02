
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # E2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # C#5
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F5
    # Bar 4: A7sus (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # C#5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G5
    # Bar 4: D7 (D, F#, A, C#) resolves back on beat 4
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a descending 3-note motif on beat 1 of bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.25),  # F4
    # Leave it hanging, then come back a half step higher
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # A#4
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.5),  # G#4
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.75),  # F#4
    # Finish it with the same pattern an octave higher
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # A6
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # G6
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25),  # F6
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar for bars 2-4
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
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

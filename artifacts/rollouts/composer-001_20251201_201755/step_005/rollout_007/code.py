
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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

# Bass: Marcus - Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (MIDI 38) with chromatic approach on 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.0),
    # Bar 2: G (MIDI 43) with chromatic approach on 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    # Bar 3: D (MIDI 38) with chromatic approach on 2
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=39, start=2.875, end=3.0),
    # Bar 3: G (MIDI 43) with chromatic approach on 3
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    # Bar 4: D (MIDI 38) with chromatic approach on 2
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=39, start=3.875, end=4.0),
    # Bar 4: G (MIDI 43) with chromatic approach on 3
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
    # Bar 4: D (MIDI 38) on beat 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
]
bass.notes.extend(bass_notes)

# Piano: Diane - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # C#
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=3.0),  # F
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=45, start=3.5, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=3.5, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (D, F#, G, A)
    pretty_midi.Note(velocity=110, pitch=45, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=47, start=1.75, end=2.0),  # F#
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it (G, A, Bb, D)
    pretty_midi.Note(velocity=110, pitch=49, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=50, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=51, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=45, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

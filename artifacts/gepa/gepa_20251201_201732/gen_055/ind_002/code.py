
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (38), F (41), G (43), E (40)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),

    # Bar 3: C (40), D (38), Bb (42), A (41)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),

    # Bar 4: D (38), F (41), G (43), C (40)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=3.0),

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5),

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0)
]
piano.notes.extend(piano_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (64), G (67), rest, then D (62), F (64), G (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

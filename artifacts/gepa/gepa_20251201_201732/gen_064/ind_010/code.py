
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

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),  # G (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # D (root)
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # G (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # F# (chromatic)
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),  # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # G (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D
]
# Bar 3: Bb7 (Bb, D, F, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # G
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb
])
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) - Ab (68) - C (72) - F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=68, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=68, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=68, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=72, start=3.625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=68, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=68, start=5.0, end=5.125),
    pretty_midi.Note(velocity=110, pitch=72, start=5.125, end=5.25),
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.375),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled


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
    # Hi-hats on every eighth
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

# Bass line (Fm, walking line with chromatic approaches)
# Bar 2: F (D2), Ab (E2), Bb (F2), D (G2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # Bb (F2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # D (G2)
    # Bar 3: C (A2), Eb (B2), F (C3), Ab (D3)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # C (A2)
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75),  # Eb (B2)
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),  # F (C3)
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # Ab (D3)
    # Bar 4: Bb (E2), D (G2), F (A2), C (B2)
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),  # Bb (E2)
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # D (G2)
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625),  # F (A2)
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # C (B2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.0),  # F (C3)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),  # Ab (D3)
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=2.0),  # C (E3)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # D (F3)
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.5),  # Bb (D3)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.5),  # D (E3)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5),  # F (F3)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),  # Ab (G3)
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=5.0),  # C (E3)
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=5.0),  # Eb (F3)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.0),  # G (G3)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=5.0),  # Bb (D3)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, Ab, Bb (Fm scale, but breathy and soulful)
# Bar 2: F (C3), G (D3), Ab (D#3), Bb (E3)
# Bar 3: rest
# Bar 4: F (C3), G (D3), Ab (D#3), Bb (E3)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=52, start=1.5, end=1.75),  # F (E3)
    pretty_midi.Note(velocity=110, pitch=53, start=1.75, end=2.0),   # G (F3)
    pretty_midi.Note(velocity=110, pitch=54, start=2.0, end=2.25),  # Ab (G3)
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.5),  # Bb (A3)
    # Bar 3: rest
    # Bar 4: repeat the motif
    pretty_midi.Note(velocity=110, pitch=52, start=4.5, end=4.75),  # F (E3)
    pretty_midi.Note(velocity=110, pitch=53, start=4.75, end=5.0),   # G (F3)
    pretty_midi.Note(velocity=110, pitch=54, start=5.0, end=5.25),  # Ab (G3)
    pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=5.5),  # Bb (A3)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
# Bar 3: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
])
# Bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.25, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled


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

# Bass line: walking line in F, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (D2), chromatic approach (C#2), F (D2)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Bar 3: C (G2), chromatic approach (B2), C (G2)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),
    # Bar 4: G (B2), chromatic approach (A#2), G (B2)
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),
    # Bar 4: Bb (D3), chromatic approach (C3), Bb (D3)
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # E
]
# Bar 3: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
])
# Bar 4: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F
])
# Bar 4: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Ab
])
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (G4), D (E4), Bb (F4), G (G4)
# Play F, D, Bb on beat 1, leave G hanging on beat 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # G
    # Repeat the motif slightly altered, but finish it
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # G
]
sax.notes.extend(sax_notes)

# Drums: continue in bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth
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
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

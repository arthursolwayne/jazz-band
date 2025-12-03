
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
    # Hi-hats on every eighth
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

# Bass line - Marcus: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (D2), chromatic approach to G (E2)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),
    # Bar 3: C (G2), chromatic approach to D (A2)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),
    # Bar 4: G (B2), chromatic approach to A (C3)
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),
    # Bar 2: G (E2)
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    # Bar 3: D (A2)
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),
    # Bar 4: A (C3)
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano - Diane: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Drums: continue the same pattern for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    # Hi-hats on every eighth
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
]
drums.notes.extend(drum_notes)

# Sax - Dante: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: A (C4) on beat 1, B (C#4) on beat 2
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=61, start=1.875, end=2.25),
    # Bar 3: Leave it hanging on D (D4)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),
    # Bar 4: Come back to A (C4) and B (C#4) to finish the motif
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=61, start=3.375, end=3.75),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

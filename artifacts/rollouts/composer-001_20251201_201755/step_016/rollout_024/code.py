
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
    # Hi-hat on every eighth
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

# Bass line (walking line in F, D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: F (D2), chromatic approach on E2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=37, start=1.5, end=1.6875),
    # Bar 3: C (G2), chromatic approach on B2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.4375),
    # Bar 4: G (D3), chromatic approach on F#2
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=49, start=3.0, end=3.1875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=2.0),  # E
]
# Bar 3: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=84, start=2.25, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.75),  # Bb
])
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=86, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.5),  # F
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (E), G, A, Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=76, start=3.25, end=3.5),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

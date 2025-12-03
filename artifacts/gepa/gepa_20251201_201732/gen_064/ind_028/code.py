
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) -> G (43) -> A (45) -> Bb (46)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0), # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875), # G (Fmaj7 3rd)
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25), # A (Fmaj7 5th)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625), # G (Fmaj7 3rd)
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0), # F (Fmaj7 root)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Cm7 (C, Eb, G, Bb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5), # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5), # Bb
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif but with variation (F, G, A, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=110, pitch=70, start=4.125, end=4.5), # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: G7 (G, B, D, F)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0), # B
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0), # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0), # F
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif, resolve on F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=6.0), # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

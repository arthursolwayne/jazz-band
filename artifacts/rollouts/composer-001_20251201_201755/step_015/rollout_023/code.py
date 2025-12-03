
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # F (17.3) -> F# (18) -> G (19) -> A (22)
    pretty_midi.Note(velocity=80, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=80, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=81, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=84, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, come back and finish it
# Motif: F (65), G (67), Ab (69), F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bb (20) -> B (21) -> C (22) -> D (24)
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=78, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=82, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: continue the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # E (16) -> F (17) -> F# (18) -> G (19)
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=75, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=77, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: finish the motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

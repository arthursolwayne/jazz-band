
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

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=47, start=1.5, end=1.6875),
    # Bar 3: C (fifth) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=54, start=2.25, end=2.4375),
    # Bar 4: Ab (flatted seventh) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=51, start=3.0, end=3.1875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0),
    # Bar 3: Bbm7 (Bb, Db, F, G)
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.5),
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.5),
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.5),
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.5),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=80, pitch=74, start=2.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif (F, Ab, C)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it (Ab, F)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),
]
sax.notes.extend(sax_notes)

# Drums: Continue for Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

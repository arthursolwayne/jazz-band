
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
    # Hi-hat on every eighth
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

# Bass: Walking line in Fm (F, Ab, D, Eb), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), Ab (fifth), chromatic approach up to D
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=52, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.0),
    # Bar 3: D (root), Eb (fifth), chromatic approach up to Ab
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=54, start=2.375, end=2.5),
    # Bar 4: Ab (root), Bb (fifth), chromatic approach up to F
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=53, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Dm7 (D, F, A, C)
# Bar 4: Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=3.0),
    # Bar 3: Dm7
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=4.5),
    # Bar 4: Ab7
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif start - F (49), Ab (52), D (53), leave it hanging on D
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=52, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=53, start=2.0, end=2.5),
    # Bar 3: Motif repeat (offset)
    pretty_midi.Note(velocity=100, pitch=49, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=52, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5),
    # Bar 4: Resolve, come back to F
    pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=49, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=53, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=49, start=5.5, end=6.0),
]
sax.notes.extend(sax_notes)

# Drum fill for bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

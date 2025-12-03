
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Bb3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # F2 (root)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # Db3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # F2 (root)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # C3 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Bb3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb5

    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # Db4
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Ab4

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # A5
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G5
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # A5
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # G5
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # F5

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=110, pitch=58, start=3.375, end=3.75), # E5
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125), # F5
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # G5

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # A5
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # G5
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625), # A5
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # G5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),  # Out of range, but added for timing
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled


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
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=54, start=1.875, end=2.125),
    # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=57, start=2.125, end=2.5),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=54, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif (F, Ab, C, Eb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.125, end=2.5),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),
    # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbm7 (Bb, Db, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # Db
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax: Motif (Bb, Db, F, G)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),
    # F2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=54, start=5.25, end=5.625),
    # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif (F, Ab, C, D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    # Bar 4: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.1875),
    # Hi-hat on every eighth
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

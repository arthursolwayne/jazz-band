
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
# Bass: Walking line (F2 - C3) with chromatic approaches
bass_notes = [
    # F2 (root) with chromatic approach from E#
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    # G2 (fifth) with chromatic approach from F#
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.25),
    # A2 (chromatic approach to Bb)
    pretty_midi.Note(velocity=90, pitch=80, start=2.25, end=2.625),
    # Bb2 (resolution)
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A (F7)
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),  # Bb (chromatic)
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # B (resolution)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2 - C3) with chromatic approaches
bass_notes = [
    # Bb2 (root) with chromatic approach from A#
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),
    # C3 (fifth) with chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=84, start=3.375, end=3.75),
    # D3 (chromatic approach to Eb)
    pretty_midi.Note(velocity=90, pitch=86, start=3.75, end=4.125),
    # Eb3 (resolution)
    pretty_midi.Note(velocity=90, pitch=87, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=91, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=81, start=3.0, end=3.375),  # Bb (Bb7)
    pretty_midi.Note(velocity=110, pitch=84, start=3.375, end=3.75),  # C (chromatic)
    pretty_midi.Note(velocity=110, pitch=86, start=3.75, end=4.125),  # D (resolution)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2 - C3) with chromatic approaches
bass_notes = [
    # Eb3 (root) with chromatic approach from D#
    pretty_midi.Note(velocity=90, pitch=87, start=4.5, end=4.875),
    # F3 (fifth) with chromatic approach from Eb
    pretty_midi.Note(velocity=90, pitch=89, start=4.875, end=5.25),
    # G3 (chromatic approach to Ab)
    pretty_midi.Note(velocity=90, pitch=91, start=5.25, end=5.625),
    # Ab3 (resolution)
    pretty_midi.Note(velocity=90, pitch=92, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb G Bb Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=92, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=94, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=96, start=4.5, end=6.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=87, start=4.5, end=4.875),  # Eb (Eb7)
    pretty_midi.Note(velocity=110, pitch=91, start=4.875, end=5.25),  # F (chromatic)
    pretty_midi.Note(velocity=110, pitch=92, start=5.25, end=5.625),  # G (resolution)
    pretty_midi.Note(velocity=110, pitch=94, start=5.625, end=6.0),  # Bb (finish)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
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

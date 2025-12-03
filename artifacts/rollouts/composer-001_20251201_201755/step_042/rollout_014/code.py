
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Root F (MIDI 53) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.6875),  # Fb
    pretty_midi.Note(velocity=100, pitch=53, start=1.6875, end=1.875),  # F
    # Fifth C (MIDI 60) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.0625),  # Cb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0625, end=2.25),  # C
    # Root F (MIDI 53) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.4375),  # Fb
    pretty_midi.Note(velocity=100, pitch=53, start=2.4375, end=2.625),  # F
    # Fifth C (MIDI 60) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=2.8125),  # Cb
    pretty_midi.Note(velocity=100, pitch=60, start=2.8125, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # G (Fm7)
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # E (Fm7)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # G (Fm7)
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0),  # E (Fm7)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Root Ab (MIDI 57) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.1875, end=3.375),  # Ab
    # Fifth Eb (MIDI 64) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.5625),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75),  # Eb
    # Root Ab (MIDI 57) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=3.9375),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.9375, end=4.125),  # Ab
    # Fifth Eb (MIDI 64) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.3125),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.3125, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Gb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # Ab (Ab7)
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # Gb (Ab7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # Ab (Ab7)
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # Gb (Ab7)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Root Eb (MIDI 64) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.6875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875),  # Eb
    # Fifth Bb (MIDI 71) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.0625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.0625, end=5.25),  # Bb
    # Root Eb (MIDI 64) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.4375),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625),  # Eb
    # Fifth Bb (MIDI 71) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=5.8125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.8125, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G (Eb7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # Eb (Eb7)
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # G (Eb7)
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # Eb (Eb7)
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 3: Full quartet (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
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

# Bar 4: Full quartet (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
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

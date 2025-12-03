
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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
# Bass: walking line in F (D2-G2, MIDI 38-43)
bass_notes = [
    # Root F (43) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),
    # Chromatic approach up to Bb (46)
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=46, start=2.125, end=2.5),
    # Root Bb (46)
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: short motif, one phrase, make it sing
# Dorian mode in F (F G A Bb C D E)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),   # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F (D2-G2, MIDI 38-43)
bass_notes = [
    # Root Bb (46)
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),
    # Chromatic approach down to F (43)
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=43, start=3.625, end=4.0),
    # Root F (43)
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb D F Ab) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F (D2-G2, MIDI 38-43)
bass_notes = [
    # Root F (43)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),
    # Chromatic approach up to Bb (46)
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.125),
    pretty_midi.Note(velocity=80, pitch=46, start=5.125, end=5.5),
    # Root Bb (46)
    pretty_midi.Note(velocity=90, pitch=46, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: Fmaj7 (F A C E) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0 - 4.5
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # End slightly beyond to be safe
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

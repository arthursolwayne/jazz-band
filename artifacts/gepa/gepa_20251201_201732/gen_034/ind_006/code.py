
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) - G2 (43)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),
    # Bar 3: D2 (38) - F2# (44)
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),
    # Bar 4: D2 (38) - G2 (43)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),
]

bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C#
]
# Bar 3: D7 (D-F#-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C
])
# Bar 4: Dm7 (D-F-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
])

piano.notes.extend(piano_notes)

# Sax: Dante (Motif, make it sing: D-F#-G-A, start it, leave it hanging, come back and finish it)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D (resolve)
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled


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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm (F2, Ab2, D2, G2, C2, Eb2, Bb2, E2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),   # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # Eb
]
# Bar 3: Bbm7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # D
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, leave it hanging
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F - Ab - Bb - C (half notes on beats 1, 2, 3, 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

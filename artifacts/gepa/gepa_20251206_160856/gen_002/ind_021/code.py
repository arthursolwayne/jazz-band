
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Ab
])
# Bar 4: E7 (E, G#, B, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (in Fm)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: End of motif, sustain and resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

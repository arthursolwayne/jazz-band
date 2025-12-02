
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on last bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # D5
]
# Bar 3: Bbm7 (Bb, Db, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # Db4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # Ab4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # C5
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Eb4
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),   # G5
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Bb4
])
piano.notes.extend(piano_notes)

# Sax: Motif in Fm
# Start with a short phrase: F, Ab, D, G (Fm motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Ab4
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=1.875),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.0),   # G5
]
# Leave it hanging, come back
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=74, start=2.875, end=3.0),   # D5
])
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Bar 3 (1.5 - 3.0s) - same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Drums continue
# Bar 4 (3.0 - 4.5s) - same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")

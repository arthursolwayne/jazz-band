
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),   # E2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),   # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),

    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # F7 (F, Ab, C, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),

    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),   # Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),   # E2
    pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # Ab2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F7 (F, Ab, C, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),

    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125),  # Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),

    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),   # Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),   # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # E2
    pretty_midi.Note(velocity=90, pitch=37, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0),   # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),

    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625),  # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),

    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),   # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=58, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax: finish the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=59, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0),   # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

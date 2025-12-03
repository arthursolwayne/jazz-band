
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm (F, Ab, D, C), with chromatic approaches
bass_notes = [
    # Bar 2: F (root), Ab (b9), D (5), C (b7)
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # Bb4 (Fm scale)
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75), # Bb4 again
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm (F, Ab, D, C), with chromatic approaches
bass_notes = [
    # Bar 3: F (root), Ab (b9), D (5), C (b7)
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),   # D
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # D5 (resolution)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),  # G4 (final note)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C), with chromatic approaches
bass_notes = [
    # Bar 4: F (root), Ab (b9), D (5), C (b7)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: End with a strong note, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # A4
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # D5 (resolution)
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

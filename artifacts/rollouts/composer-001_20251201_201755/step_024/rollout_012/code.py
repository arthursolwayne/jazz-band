
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line (F2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Diane: Piano comping
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # Eb5

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F5
]
piano.notes.extend(piano_notes)

# Little Ray: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line (Bb2 - F3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75), # C3
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125), # Db3
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),  # Eb3
]
bass.notes.extend(bass_notes)

# Diane: Piano comping
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # Ab5

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),  # Eb5
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5),  # G5
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.5),  # Bb5
]
piano.notes.extend(piano_notes)

# Little Ray: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line (Eb2 - Bb3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # F3
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625), # Gb3
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # G3
]
bass.notes.extend(bass_notes)

# Diane: Piano comping
piano_notes = [
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),  # G5
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.25),  # Bb5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # Db6

    # Resolution on the last chord
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=6.0),  # Eb6
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=6.0),  # G6
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=6.0),  # Bb6
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=6.0),  # D6
]
piano.notes.extend(piano_notes)

# Little Ray: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)  # Kick on 3
]
drums.notes.extend(drum_notes)

# Dante: Sax motif (start at bar 2)
# Motif: F4 (Ab4), Bb4, C5
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),  # C5
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled

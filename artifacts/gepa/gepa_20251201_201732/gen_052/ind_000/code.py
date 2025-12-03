
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # Ab2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Fm7 with open voicings, comp on 2 and 4
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # D5
    # Bar 3: Bbm7 (Bb, Db, F, G)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # Db4
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, haunting, incomplete
# Phrase: F - Ab - C - open (rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C5
    # Rest until the end of the bar
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.25),  # C5 (rest)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # Bb2 (root)
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
# Bar 3: Bbm7 (Bb, Db, F, G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Db4
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # Bb2 (root)
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),  # C2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625),  # D2 (fifth)
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # C#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Eb4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # D4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Snare on 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax: Return to complete the motif
# Phrase: F - Ab - C - Eb (briefly)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # Eb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

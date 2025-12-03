
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625), # C2 (fifth of Dm)
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0),  # Db2 (chromatic approach)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4 (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C4
]

# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # F4
])

# Bar 4: C7 (C E G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # Bb4
])

piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Sax: Bar 2-4
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - D4 (Dm scale, but with a question in the middle)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4 (end of bar 2)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4 (start of bar 3)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D4 (end of bar 3)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4 (start of bar 4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4 (end of bar 4)
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

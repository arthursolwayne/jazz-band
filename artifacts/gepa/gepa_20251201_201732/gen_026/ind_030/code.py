
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

# Marcus on bass: walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25), # F2 (fifth)
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C5

    # Bar 3: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F5

    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # G5
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=6.0),  # Bb5
]
piano.notes.extend(piano_notes)

# Little Ray on drums (Bar 2-4)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Dante on sax: start with a short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Eb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

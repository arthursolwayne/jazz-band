
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

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E flat)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # E flat4
]
piano.notes.extend(piano_notes)

# Bar 3: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
]
piano.notes.extend(piano_notes)

# Bar 4: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # F4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)   # Snare on 4
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F A Bb F (MIDI 69, 81, 80, 69)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=81, start=3.375, end=3.75), # A4
    pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=4.125), # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25), # A4
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

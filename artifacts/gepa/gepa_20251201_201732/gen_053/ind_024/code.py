
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # B (chromatic)
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),  # Bb (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),  # E4

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.25), # C5
    pretty_midi.Note(velocity=90, pitch=63, start=2.875, end=3.25), # Eb5
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.25), # G5
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.25), # Bb5
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)   # Snare on 4
]
drums.notes.extend(drum_notes)

# Sax: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.25), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.625), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=4.0)   # B4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

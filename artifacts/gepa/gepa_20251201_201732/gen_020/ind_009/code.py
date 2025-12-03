
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # F2
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # Bb2
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),  # Bb2
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=5.25, end=5.625), # Eb2
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # C4
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # F4
    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes.extend([
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
])
drums.notes.extend(drum_notes)

# Dante on sax: Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

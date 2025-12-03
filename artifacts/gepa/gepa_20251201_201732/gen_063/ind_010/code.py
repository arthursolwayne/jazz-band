
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Fm (F, Ab, D, Eb, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),   # Eb2
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),   # Eb2
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),   # Eb2
]
bass.notes.extend(bass_notes)

# Diane - Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # D5
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # F4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # Eb5
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Bb5
])
piano.notes.extend(piano_notes)

# Dante - Tenor sax melody (4-bar motif)
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=110, pitch=63, start=2.625, end=3.0),   # G4
]
# Bar 3: Continue the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=110, pitch=63, start=4.125, end=4.5),   # G4
])
# Bar 4: Resolution
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # Ab4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=110, pitch=61, start=5.625, end=6.0),   # Eb4
])
sax.notes.extend(sax_notes)

# Add drum fills for bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

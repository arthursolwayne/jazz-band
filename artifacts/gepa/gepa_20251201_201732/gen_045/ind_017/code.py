
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bass (Marcus) - Walking line in D minor (D2-G2, MIDI 38-43)
# Bar 2: D2 (root), F#2 (chromatic approach), G2 (fifth), C#2 (chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=70, pitch=40, start=1.875, end=2.25),  # F#2 on 2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2 on 3
    pretty_midi.Note(velocity=70, pitch=41, start=2.625, end=3.0),   # C#2 on 4
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, resolve on the last bar
# Bar 2: D7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C#4
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: C7 (C-E-G-B)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B4
]
piano.notes.extend(piano_notes)

# Sax (Dante) - One short motif, make it sing
# Start with a high D (D5), then a grace note (C#5), then a G5 (fifth), then resolve to Bb5
# Bar 2-4: Start on 1.5, end on 3.0
# D5 (62), grace C#5 (61), G5 (67), Bb5 (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D5
    pretty_midi.Note(velocity=60, pitch=61, start=1.625, end=1.6875), # Grace C#5
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # G5
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # D5
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G5
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),   # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled

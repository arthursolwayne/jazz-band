
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line - D2 (38), G2 (43), chromatic approaches, roots and fifths
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),    # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),   # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),   # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),    # F2
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),    # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),   # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),   # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),    # F2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),    # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),   # Eb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),   # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),    # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last chord of each bar
# Bar 2: Dm7 - D F A C
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 - G B D F
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F5
])

# Bar 4: Cm7 - C Eb G Bb
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Bb4
])

# Add resolution on last beat of each bar
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.625, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.625, end=3.75),  # C5
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - C5 (Dm7) then rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),   # A4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),   # C5
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),   # A4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),   # C5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

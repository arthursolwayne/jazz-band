
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=75, start=1.875, end=2.25), # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),  # F2 (root)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=3.375, end=3.75), # C3
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=75, start=4.125, end=4.5),  # C3

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=4.875, end=5.25), # C3
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.625), # D2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last bar
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),   # A4
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=3.0),   # C5
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=3.0),   # E5
]

# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),   # B4
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=4.5),   # D5
    pretty_midi.Note(velocity=95, pitch=78, start=3.0, end=4.5),   # F#5
])

# Bar 4: C7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),   # E4
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=6.0),   # G4
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=6.0),   # B4
])
piano.notes.extend(piano_notes)

# Sax (Dante): Melody in F, one short motif, sing it, leave it hanging
# Start with a short motive: F (65) - A (69) - F (65) - G (67) - F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")


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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=70, pitch=37, start=1.125, end=1.5),  # C#2 (chromatic approach)
    # Bar 3: G2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=70, pitch=44, start=1.875, end=2.25),  # A2 (chromatic approach)
    # Bar 4: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=70, pitch=37, start=2.625, end=3.0),  # C#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.875),  # C#4
    # Bar 3: G7sus4 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # F#4
    # Bar 4: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # C#4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth for Bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

# Sax: Motif (D4, E4, F#4, G4) - short, singable, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # G4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

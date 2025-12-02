
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Dm)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # F2 (fifth of Dm)
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),   # D2
    # Bar 3 (Dm)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),   # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),   # Eb2
    # Bar 4 (Dm)
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),   # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),   # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 - C (rootless)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F4 (3rd of Dm)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A4 (5th of Dm)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C4 (root of Dm)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # C#4 (7th of Dm)
    # Bar 3: Gm7 - F (rootless)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb4 (3rd of Gm)
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.375),  # D4 (5th of Gm)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F4 (root of Gm)
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # F#4 (7th of Gm)
    # Bar 4: Cm7 - Bb (rootless)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # Eb4 (3rd of Cm)
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=4.875),  # G4 (5th of Cm)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Bb4 (root of Cm)
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),  # B4 (7th of Cm)
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm scale fragment: D - E - F - Eb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.0),   # Eb4 (hanging)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D4 (return)
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.5),   # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D4 (final return)
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.0),   # Eb4
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Bars 2-3: Full pattern
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hi-hat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # F#2
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)   # F#2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F4
    # Bar 3: G7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # F#4
    # Bar 4: Cm7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    # Bar 4: Resolve to Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F4
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, sing it, leave it hanging, come back
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),   # D4
    # Bar 3: Continue the motif, leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),   # G4
    # Bar 4: Resolve the motif
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),   # E4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),   # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.25),   # E4
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),   # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),   # E4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),   # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),   # E4
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),   # G4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare1, snare2])

# Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

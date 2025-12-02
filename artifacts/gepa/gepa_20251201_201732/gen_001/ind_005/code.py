
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on all eighths
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # B2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625), # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Bb2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Db)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # Db5
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),  # F4
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # Bb5
    # Bar 4: resolve on Cm7
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=6.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=6.0),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=6.0),  # Bb5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue hihat and kicks/snare
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Hihat on all eighths
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)

midi.instruments.extend([sax, bass, piano, drums])
midi.dump()

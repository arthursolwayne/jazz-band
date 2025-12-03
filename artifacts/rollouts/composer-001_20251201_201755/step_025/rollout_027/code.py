
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, Ab2, Bb2, Db2, etc.)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=100, pitch=49, start=2.625, end=3.0),  # Db2
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # Db2
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625), # Bb2
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # Db2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.75),  # Db4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Ab4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (Fm chord, but with a chromatic approach to Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=1.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),   # F4
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.375), # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=2.375, end=2.5),  # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.625),  # F4
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.625),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75), # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=4.75, end=4.875), # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

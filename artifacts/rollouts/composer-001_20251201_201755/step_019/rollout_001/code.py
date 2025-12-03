
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm7 (F, C, Ab, D)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # Ab3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # D3
    # Bar 3: Bb7 (Bb, F, Db, Ab)
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=39, start=3.75, end=4.125), # Db3
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # Ab3
    # Bar 4: Eb7 (Eb, Bb, G, D)
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Ab5
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif (F4, Ab4, G4)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25), # Ab4
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625), # G4
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Return and finish (F4, G4, Ab4)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=61, start=4.875, end=5.25), # G4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625), # Ab4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

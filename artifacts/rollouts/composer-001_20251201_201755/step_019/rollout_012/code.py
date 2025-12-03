
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
    # Hihat on every 8th
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

# Bass: Marcus (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: Fm7 - F (root), C (fifth), Eb (b3), Ab (dim 7)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),  # Eb3
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # Ab3
    # Bar 3: Bb7 - Bb (root), F (fifth), Ab (b3), Db (dim 7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # F3
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625), # Ab3
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # Db3
    # Bar 4: Eb7 - Eb (root), Bb (fifth), Db (b3), F (dim 7)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Bb3
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # Db3
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F3
]
bass.notes.extend(bass_notes)

# Piano: Diane (Open voicings, resolve on the last beat)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Db)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # Ab3
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # Db4
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # Ab4
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # Eb3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Db4
]
piano.notes.extend(piano_notes)

# Sax: Dante (One short motif, make it sing)
sax_notes = [
    # Bar 2: Start the motif (F, Ab, Bb, F)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # F3
    pretty_midi.Note(velocity=110, pitch=72, start=1.6875, end=1.875), # Ab3
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # Bb3
    pretty_midi.Note(velocity=110, pitch=71, start=2.0625, end=2.25), # F3
    # Bar 3: Leave it hanging (Rest)
    # Bar 4: Come back and finish it (F, G, Ab, F)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),  # F3
    pretty_midi.Note(velocity=110, pitch=72, start=3.1875, end=3.375), # G3
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.5625), # Ab3
    pretty_midi.Note(velocity=110, pitch=71, start=3.5625, end=3.75), # F3
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

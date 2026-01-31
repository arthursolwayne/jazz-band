
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, G2, D2, C2, etc.)
bass_notes = [
    # Bar 2: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=1.5, end=1.5 + 0.1875),  # Eb2
    # Bar 3: G2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=78, start=2.25, end=2.25 + 0.1875),  # Ab2
    # Bar 4: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.0 + 0.1875),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),  # Ab2
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=1.875),  # D3
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.625),  # Ab2
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=100, pitch=89, start=3.0, end=3.375),  # E3
    pretty_midi.Note(velocity=100, pitch=92, start=3.0, end=3.375),  # G3
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),  # Bb3
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75),  # Bb2
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),   # F2
    pretty_midi.Note(velocity=110, pitch=79, start=2.0, end=2.25),  # G2
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.5),  # F2
    pretty_midi.Note(velocity=110, pitch=79, start=2.5, end=2.75),  # G2
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=3.0),  # Bb2
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.25),  # F2
    pretty_midi.Note(velocity=110, pitch=79, start=3.25, end=3.5),  # G2
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.75),  # F2
    pretty_midi.Note(velocity=110, pitch=79, start=3.75, end=4.0),  # G2
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

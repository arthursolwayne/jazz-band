
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Root (F2) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=52, start=1.6875, end=1.875), # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),  # F2
    # Bar 3: Fifth (C3) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1875),  # C3
    pretty_midi.Note(velocity=80, pitch=59, start=2.1875, end=2.375), # B2
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # C3
    # Bar 4: Root (F2) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=52, start=2.6875, end=2.875), # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=2.875, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # A2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # E3
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.375),  # G2
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.375),  # D3
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.375),  # F3
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.875),  # C3
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875),  # E3
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.875),  # G3
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.875),  # Bb3
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F - G - Eb - F (bar 2), then repeat with a slight variation (bar 3), then resolve on F (bar 4)
sax_notes = [
    # Bar 2: F (F3)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    # Bar 2: G (G3)
    pretty_midi.Note(velocity=110, pitch=73, start=1.875, end=2.0),
    # Bar 2: Eb (Eb3)
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.1875),
    # Bar 2: F (F3)
    pretty_midi.Note(velocity=110, pitch=71, start=2.1875, end=2.375),
    # Bar 3: F (F3)
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.6875),
    # Bar 3: G (G3)
    pretty_midi.Note(velocity=110, pitch=73, start=2.6875, end=2.875),
    # Bar 3: Eb (Eb3)
    pretty_midi.Note(velocity=110, pitch=68, start=2.875, end=3.0),
    # Bar 4: F (F3)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums continue same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: Root (F2) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=52, start=4.6875, end=4.875), # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.0),  # F2
    # Bar 4: Root (F2) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=5.0, end=5.1875),  # F2
    pretty_midi.Note(velocity=80, pitch=52, start=5.1875, end=5.375), # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=5.375, end=5.5),  # F2
    # Bar 4: Root (F2) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=5.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=52, start=5.6875, end=5.875), # Eb2
    pretty_midi.Note(velocity=100, pitch=53, start=5.875, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # E3
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F - G - Eb - F (bar 2), then repeat with a slight variation (bar 3), then resolve on F (bar 4)
sax_notes = [
    # Bar 4: F (F3)
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.1875),
    # Bar 4: G (G3)
    pretty_midi.Note(velocity=110, pitch=73, start=5.1875, end=5.375),
    # Bar 4: Eb (Eb3)
    pretty_midi.Note(velocity=110, pitch=68, start=5.375, end=5.5),
    # Bar 4: F (F3)
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.6875),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

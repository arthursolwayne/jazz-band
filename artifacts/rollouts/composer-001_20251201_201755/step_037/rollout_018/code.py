
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
# Bass: Walking line (F2 - A2, MIDI 38 - 43), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # E2 (chromatic approach) on 2
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.125),
    # A2 (fifth) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # G2 (chromatic approach) on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # A (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # E (MIDI 64)
    
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # G (MIDI 55)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # Bb (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F (MIDI 53)
    
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # Bb (MIDI 57)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (F, G, A)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=1.875, end=2.125),  # G
    pretty_midi.Note(velocity=110, pitch=57, start=2.125, end=2.5),  # A
    
    # Bar 3: Leave it hanging (Bb)
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.375),  # A (repeat)
    pretty_midi.Note(velocity=110, pitch=55, start=3.375, end=3.75),  # G
    
    # Bar 4: Come back and finish it (F, G, A, F)
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=55, start=4.875, end=5.125),  # G
    pretty_midi.Note(velocity=110, pitch=57, start=5.125, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=53, start=5.5, end=5.875),  # F
]
sax.notes.extend(sax_notes)

# Bar 2: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
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

# Bar 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

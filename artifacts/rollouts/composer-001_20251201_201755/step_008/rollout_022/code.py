
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Root (F2) on 1, chromatic approach (E2) on 2, root (F2) on 3, chromatic approach (G2) on 4
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=72, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, D) on 1, Bbm7 (Bb, D, F, Ab) on 2, Ab7 (Ab, C, Eb, G) on 3, C7 (C, E, G, Bb) on 4
piano_notes = [
    # Bar 2 - Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),
    # Bar 3 - Bbm7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0),
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.0),
    # Bar 4 - Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.5),
    # Bar 5 - C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Bar 2 - Motif
# F (71), Ab (68), C (72), D (74)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=74, start=2.0625, end=2.25),
    # Repeat motif with slight variation
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=110, pitch=68, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=110, pitch=74, start=2.8125, end=3.0),
    # Repeat with different rhythm
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=68, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=74, start=3.5625, end=3.75),
    # End on Ab (68) for tension
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Piano: Bar 3 and 4
piano_notes = [
    # Bar 3 - Bbm7 (Bb, D, F, Ab) with comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),
    # Bar 4 - Ab7 (Ab, C, Eb, G) with comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),
    # Bar 5 - C7 (C, E, G, Bb) with comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=72, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=76, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=76, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=67, start=6.75, end=7.125),
]
piano.notes.extend(piano_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

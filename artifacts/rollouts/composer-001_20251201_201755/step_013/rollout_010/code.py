
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
# Marcus: Walking line (F2 - C3) with chromatic approaches, rooted in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=54, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on last
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),   # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),   # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),   # C5
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),   # E5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.625),  # Ab5
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # E5
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),   # G5
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),   # B5
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
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

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),   # B4
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=2.4375, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # B4
    pretty_midi.Note(velocity=100, pitch=64, start=2.8125, end=3.0),   # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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

# Bass line (F7, Bb7, C7, G7)
# Roots and fifths with chromatic approaches
# Bar 2: F7 (F, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.5 + 0.375),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=1.5 + 0.375, end=1.5 + 0.75),  # E (chromatic approach)
]
# Bar 3: Bb7 (Bb, F)
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=1.875 + 0.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=1.875 + 0.375),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.875 + 0.375, end=1.875 + 0.75),  # A (chromatic approach)
])
# Bar 4: C7 (C, G)
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.25 + 0.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.25 + 0.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.25 + 0.375, end=2.25 + 0.75),  # D (chromatic approach)
])
# Bar 5: G7 (G, D)
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=2.625 + 0.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.625 + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=73, start=2.625 + 0.375, end=2.625 + 0.75),  # E (chromatic approach)
])
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.5 + 0.375),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.5 + 0.375),  # E
]
# Bar 3: Bb7 (Bb, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + 0.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=1.875 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=1.875 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=78, start=1.875, end=1.875 + 0.375),  # A
])
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.25 + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.25 + 0.375),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.25 + 0.375),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.25 + 0.375),  # B
])
# Bar 5: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.625 + 0.375),  # G
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=2.625 + 0.375),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.625 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.625 + 0.375),  # F
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.5 + 0.1875),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 0.1875, end=1.5 + 0.375),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 0.375, end=1.5 + 0.5625),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 0.5625, end=1.5 + 0.75),  # A
]
# Bar 3: Repeat motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=1.875 + 0.1875),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=1.875 + 0.1875, end=1.875 + 0.375),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.875 + 0.375, end=1.875 + 0.5625),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=1.875 + 0.5625, end=1.875 + 0.75),  # A
])
# Bar 4: End of motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.25 + 0.1875),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=2.25 + 0.1875, end=2.25 + 0.375),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.25 + 0.375, end=2.25 + 0.5625),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.25 + 0.5625, end=2.25 + 0.75),  # G
])
# Bar 5: End with a descending run to F
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.625 + 0.1875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.625 + 0.1875, end=2.625 + 0.375),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.625 + 0.375, end=2.625 + 0.5625),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=2.625 + 0.5625, end=2.625 + 0.75),  # A
])
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.5 + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.5 + 0.75, end=1.5 + 0.875),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.5 + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.1875, end=1.5 + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.375, end=1.5 + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.5625, end=1.5 + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.75, end=1.5 + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.9375, end=1.5 + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 1.125, end=1.5 + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 1.3125, end=1.5 + 1.5)
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=1.875 + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875 + 0.75, end=1.875 + 0.875),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=1.875 + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875 + 0.1875, end=1.875 + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875 + 0.375, end=1.875 + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875 + 0.5625, end=1.875 + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875 + 0.75, end=1.875 + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875 + 0.9375, end=1.875 + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875 + 1.125, end=1.875 + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875 + 1.3125, end=1.875 + 1.5)
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.25 + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25 + 0.75, end=2.25 + 0.875),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.25 + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 0.1875, end=2.25 + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 0.375, end=2.25 + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 0.5625, end=2.25 + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 0.75, end=2.25 + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 0.9375, end=2.25 + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 1.125, end=2.25 + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25 + 1.3125, end=2.25 + 1.5)
])
# Bar 5
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.625 + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.625 + 0.75, end=2.625 + 0.875),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.625 + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625 + 0.1875, end=2.625 + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625 + 0.375, end=2.625 + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625 + 0.5625, end=2.625 + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625 + 0.75, end=2.625 + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625 + 0.9375, end=2.625 + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625 + 1.125, end=2.625 + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625 + 1.3125, end=2.625 + 1.5)
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled

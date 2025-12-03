
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.0),
    # Bar 3: C (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.375),
    pretty_midi.Note(velocity=90, pitch=56, start=2.375, end=2.5),
    # Bar 4: F (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=47, start=2.875, end=3.0),
    # Bar 5: Bb (flat seventh) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5),
    # Bar 6: F (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=47, start=3.875, end=4.0),
    # Bar 7: C (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=55, start=4.0, end=4.375),
    pretty_midi.Note(velocity=90, pitch=56, start=4.375, end=4.5),
    # Bar 8: F (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.0),
    # Bar 9: Bb (flat seventh) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=50, start=5.0, end=5.375),
    pretty_midi.Note(velocity=90, pitch=51, start=5.375, end=5.5),
    # Bar 10: F (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=5.5, end=5.875),
    pretty_midi.Note(velocity=90, pitch=47, start=5.875, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=52, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.5),
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=3.0),
])
# Bar 5: F7 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5),
])
# Bar 6: Bbm7 (Bb, Db, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=51, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=4.0),
])
# Bar 7: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=4.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=50, start=4.0, end=4.5),
])
# Bar 8: Fm7 (F, Ab, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=5.0),
])
# Bar 9: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=52, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=55, start=5.0, end=5.5),
    pretty_midi.Note(velocity=100, pitch=50, start=5.0, end=5.5),
])
# Bar 10: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=5.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=50, start=5.5, end=6.0),
])
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (48), Ab (50), C (55), rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=48, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=50, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=55, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=48, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=50, start=2.75, end=3.0),
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=48, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=50, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=55, start=4.0, end=4.25),
    pretty_midi.Note(velocity=110, pitch=48, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=50, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=55, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=48, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=50, start=5.75, end=6.0),
    pretty_midi.Note(velocity=110, pitch=55, start=6.0, end=6.25),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 5
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
]
drums.notes.extend(drum_notes)

# Bar 6
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
]
drums.notes.extend(drum_notes)

# Bar 7
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 8
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

# Bar 9
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
]
drums.notes.extend(drum_notes)

# Bar 10
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

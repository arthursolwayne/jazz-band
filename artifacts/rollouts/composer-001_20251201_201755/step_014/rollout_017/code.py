
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
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
# Bass: D2 (D2) -> F2 (F2) -> G2 (G2) -> C2 (C2) with chromatic approach
# D2 (38), F2 (41), G2 (43), C2 (36)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.625),  # chromatic approach to F2
    pretty_midi.Note(velocity=100, pitch=41, start=1.625, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.125),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=1.9375),  # chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=36, start=2.125, end=2.5),  # C2
    pretty_midi.Note(velocity=100, pitch=37, start=2.125, end=2.1875),  # chromatic approach to C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # F
]
# Bar 3: Cm7 (E, G, C, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5),  # F
])
# Bar 4: Bm7 (D, F#, B, E)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.25),  # E
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Dm -> F -> G -> D (D, F, G, D)
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Dm
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # Dm
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
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
# Bass: D2 (D2) -> F2 (F2) -> G2 (G2) -> C2 (C2) with chromatic approach
# D2 (38), F2 (41), G2 (43), C2 (36)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.625),  # chromatic approach to F2
    pretty_midi.Note(velocity=100, pitch=41, start=4.625, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.125),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=4.9375),  # chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=36, start=5.125, end=5.5),  # C2
    pretty_midi.Note(velocity=100, pitch=37, start=5.125, end=5.1875),  # chromatic approach to C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last
# Bar 4: Dm7 (F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),  # F
]
piano.notes.extend(piano_notes)

# Sax: End the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # Dm
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # Dm
]
sax.notes.extend(sax_notes)

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

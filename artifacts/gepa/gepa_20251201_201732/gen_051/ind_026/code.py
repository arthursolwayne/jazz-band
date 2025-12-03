
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: D2 (38) on 1, G2 (43) on 2, D2 (38) on 3, C2 (36) on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # G2 on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # D2 on 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # C2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Am7 (A, C, E, G)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F (71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A (76)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # C (74)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # E (79),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # G (77)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # Bb (71)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # D (74)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F (71)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),  # A (76)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # C (74)
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),  # E (79)
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=3.0),  # G (81)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Bar 2 (start at 1.5)
# Motif: F (71) -> Bb (74) -> F (71) -> D (74) -> F (71) -> Bb (74) -> F (71) -> C (72)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Bass line: G2 (77) on 1, Bb2 (71) on 2, G2 (77) on 3, F2 (71) on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # G2 on 1
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # Bb2 on 2
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Bar 3: Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Bass line: A2 (76) on 1, C2 (74) on 2, A2 (76) on 3, G2 (77) on 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # A2 on 1
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # C2 on 2
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),  # G2 on 4
]
bass.notes.extend(bass_notes)

# Bar 4: Piano: Am7 (A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=5.25),  # G
]
piano.notes.extend(piano_notes)

# Sax: Bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=6.25, end=6.5),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

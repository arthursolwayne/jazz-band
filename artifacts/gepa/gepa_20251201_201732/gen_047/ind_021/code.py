
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D2) -> E2 (E2) -> F#2 (F#2) -> G2 (G2)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875))  # D2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25))  # E2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625))  # F#2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0))  # G2

# Piano: Dm7 -> G7 -> Cmaj7 -> F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # D

piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25))  # F

piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625))  # B

piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0))  # F

# Sax: D (D4) -> F# (F#4) -> D (D4) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25))  # F#4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0))  # D4

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: A2 (A2) -> B2 (B2) -> C#3 (C#3) -> D3 (D3)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375))  # A2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75))  # B2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125))  # C#3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5))  # D3

# Piano: Am7 -> D7 -> Gmaj7 -> C7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # C#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))  # G

piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75))  # C

piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125))  # F#

piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5))  # C

# Sax: A (A4) -> C# (C#5) -> A (A4) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375))  # A4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=73, start=3.375, end=3.75))  # C#5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125))  # A4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5))  # A4

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F#2 (F#2) -> G2 (G2) -> A2 (A2) -> B2 (B2)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875))  # F#2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25))  # G2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625))  # A2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0))  # B2

# Piano: F#m7 -> B7 -> Emaj7 -> A7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))  # C#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875))  # E

piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25))  # A

piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625))  # D

piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0))  # A

# Sax: F# (F#4) -> B (B4) -> E (E5) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875))  # F#4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25))  # B4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625))  # E5
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0))  # E5

# Drums: Bar 3 and Bar 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [3.0, 4.5]:
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

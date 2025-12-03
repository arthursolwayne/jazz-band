
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth note
for i in range(0, 4):
    hihat_start = i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: D2 (38) -> Eb2 (39) chromatic approach to F2 (41)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625))
bass.notes.append(pretty_midi.Note(velocity=85, pitch=39, start=1.625, end=1.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=1.75, end=2.0))

# Diane on piano: F7 (77) - Bb7 (76) - D7 (72) - F7 (77)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.5))

# Dante on sax: F4 (65) -> Ab4 (68) -> F4 (65) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: F2 (41) -> E2 (40) -> D2 (38) -> F2 (41)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.125))
bass.notes.append(pretty_midi.Note(velocity=85, pitch=40, start=3.125, end=3.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.5))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=3.5, end=3.75))

# Diane on piano: Bb7 (76) - D7 (72) - F7 (77) - Eb7 (76)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0))

# Dante on sax: Rest -> Eb4 (67) -> F4 (65) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: F2 (41) -> E2 (40) -> D2 (38) -> F2 (41)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.625))
bass.notes.append(pretty_midi.Note(velocity=85, pitch=40, start=4.625, end=4.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=5.0))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=41, start=5.0, end=5.25))

# Diane on piano: F7 (77) - Bb7 (76) - D7 (72) - F7 (77)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.5))

# Dante on sax: Rest -> Ab4 (68) -> F4 (65) -> rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5))

# Drums for bar 4
# Kick on 1 and 3 (4.5 and 5.625)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4 (5.25 and 6.0)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0))

# Hihat on every eighth note
for i in range(10, 14):
    hihat_start = 4.5 + (i - 10) * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

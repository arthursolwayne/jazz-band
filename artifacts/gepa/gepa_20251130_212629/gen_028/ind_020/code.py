
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in D, chromatic approach to G
# D (D4), E (E4), F# (F#4), G (G4), F# (F#4), E (E4), D (D4), C# (C#4)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.6875, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.0625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.0625, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.4375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.4375, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.8125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=2.8125, end=3.0))

# Diane: 7th chords on 2 and 4
# D7 (D4, F#4, A4, C#5) on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125))

# D7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=2.875, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.0))

# Dante: Tenor sax motif - D (D4), F# (F#4), G (G4), rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Chromatic approach to A
# D4, C#4, B3, A3, B3, C#4, D4, E4
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=3.1875, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=58, start=3.5625, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.9375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=3.9375, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.3125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.3125, end=4.5))

# Diane: 7th chords on 2 and 4
# A7 (A4, C#5, E5, G5)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=3.875))

# A7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.625))

# Dante: Tenor sax motif continuation - A (A4), G (G4), F# (F#4), rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line in D, chromatic approach to G
# D (D4), E (E4), F# (F#4), G (G4), F# (F#4), E (E4), D (D4), C# (C#4)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.6875, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.0625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.0625, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.4375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.4375, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.8125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=5.8125, end=6.0))

# Diane: 7th chords on 2 and 4
# D7 (D4, F#4, A4, C#5) on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125))

# Diane: 7th chords on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.875, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.875, end=6.0))

# Dante: Tenor sax motif - D (D4), F# (F#4), G (G4), rest
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.625, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0))

# Drums: Bar 4 (4.5 - 6.0s)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0))

# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('intro.mid')


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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75))  # Hihat on 1 & 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5))  # Hihat on 2 & 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))  # Kick on 3

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Tenor line
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75))  # C4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0))  # D4

# Bass: Walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75))  # D3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0))  # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.25))  # C#3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5))  # D3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.75))  # E3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=2.75, end=3.0))  # F#3

# Piano: 7th chords on 2 & 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75))  # D4 (root)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75))  # A4 (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75))  # G4 (3rd)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75))  # C#5 (5th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5))  # D4 (root)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5))  # A4 (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5))  # G4 (3rd)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5))  # C#5 (5th)

# Drums: same pattern as bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25))  # Hihat on 1 & 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0))  # Hihat on 2 & 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0))  # Kick on 3

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75))  # G4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25))  # C4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5))  # D4

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.25))  # F#3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5))  # G#3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75))  # F3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0))  # F#3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=4.0, end=4.25))  # G#3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=4.25, end=4.5))  # A3

# Piano: 7th chords on 2 & 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25))  # D4 (root)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25))  # A4 (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25))  # G4 (3rd)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25))  # C#5 (5th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0))  # D4 (root)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0))  # A4 (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0))  # G4 (3rd)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0))  # C#5 (5th)

# Drums: same pattern as bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75))  # Hihat on 1 & 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5))  # Hihat on 2 & 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5))  # Kick on 3

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Ending the motif with a cry
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25))  # A4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5))  # G#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0))  # C4

# Bass: walking line
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75))  # A3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0))  # B3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25))  # G3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5))  # A3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=55, start=5.5, end=5.75))  # B3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=6.0))  # C#4

# Piano: 7th chords on 2 & 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75))  # D4 (root)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75))  # A4 (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75))  # G4 (3rd)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75))  # C#5 (5th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5))  # D4 (root)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5))  # A4 (7th)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5))  # G4 (3rd)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5))  # C#5 (5th)

# Drums: same pattern as bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25))  # Hihat on 1 & 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0))  # Hihat on 2 & 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))  # Kick on 3

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

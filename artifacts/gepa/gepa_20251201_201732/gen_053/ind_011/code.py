
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

# Kicks on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snares on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hats on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: 1.5 - 3.0s
# Bass: walking line in D, roots and fifths, with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=2, start=1.5, end=1.75))  # D2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=5, start=1.75, end=2.0))  # F#2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=4, start=2.0, end=2.25))  # E2 (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=7, start=2.25, end=2.5))  # A2

# Piano: open voicing, D7sus4 (D, G, A, C#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75))  # C#4

# Sax: motif starts, short and lyrical
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0))  # F#4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5))  # G4

# Bar 3: 3.0 - 4.5s
# Bass: walking line in D, roots and fifths, with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=7, start=3.0, end=3.25))  # A2
bass.notes.append(pretty_midi.Note(velocity=90, pitch=10, start=3.25, end=3.5))  # C#3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=9, start=3.5, end=3.75))  # C3 (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=12, start=3.75, end=4.0))  # D3

# Piano: open voicing, G7sus4 (G, C, D, F#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25))  # C5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25))  # F#4

# Sax: motif continues, lyrical and suspended
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5))  # A4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0))  # C5

# Bar 4: 4.5 - 6.0s
# Bass: walking line in D, roots and fifths, with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=12, start=4.5, end=4.75))  # D3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=15, start=4.75, end=5.0))  # F#3
bass.notes.append(pretty_midi.Note(velocity=90, pitch=14, start=5.0, end=5.25))  # E3 (chromatic approach)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=17, start=5.25, end=5.5))  # A3

# Piano: open voicing, D7sus4 (D, G, A, C#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75))  # C#4

# Sax: motif resolves
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5))  # G4

# Drums: kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375))

# Hi-hats on every eighth
for i in range(10, 14):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

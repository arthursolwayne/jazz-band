
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
# Dm: D, F, G, C
bass_notes = [
    (1.5, 50),  # D
    (1.875, 51),  # Eb (chromatic approach)
    (2.25, 52),  # F
    (2.625, 53),  # Gb (chromatic approach)
    (3.0, 53),  # G
    (3.375, 52),  # F
    (3.75, 51),  # Eb
    (4.125, 50),  # D
    (4.5, 50),  # D
    (4.875, 49),  # C# (chromatic approach)
    (5.25, 48),  # C
    (5.625, 49),  # C#
    (6.0, 50)  # D
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords on 2 and 4, comping
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

# Bar 2 (1.5 - 2.25)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=2.25))  # C

# Bar 3 (2.25 - 3.0)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=3.0))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=3.0))  # B
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=3.0))  # F

# Bar 4 (3.0 - 3.75)
piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.75))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.75))  # Eb
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.75))  # Bb

# Bar 4 (3.75 - 4.5) - F7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.5))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.5))  # C
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.5))  # Eb

# Bar 4 (4.5 - 5.25) - comping
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=5.25))  # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=5.25))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=5.25))  # C

# Bar 4 (5.25 - 6.0) - comping
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=6.0))  # G
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=6.0))  # B
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=6.0))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=6.0))  # F

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5 - 2.25): Dm7 - motif starts
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25))  # F

# Bar 3 (2.25 - 3.0): G7 - leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # G

# Bar 4 (3.0 - 3.75): Cm7 - return with resolution
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375))  # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))  # D

# Bar 4 (4.5 - 5.25): Dm7 - return with variation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25))  # F

# Bar 4 (5.25 - 6.0): G7 - resolve again
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0))  # A

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches, no repeated notes
# Bar 2: D - Eb - F - G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0))  # G

# Bar 3: A - Bb - B - C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75))  # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125))  # B
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5))  # C

# Bar 4: D - Eb - F - G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0))  # G

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25))  # F# (7th)

# Bar 3: G7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75))  # B (7th)

# Bar 4: D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25))  # F# (7th)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: D (62) on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))

# Bar 2: F (65) on beat 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875))

# Bar 3: B (71) on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375))

# Bar 3: D (62) on beat 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))

# Bar 4: G (67) on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))

# Bar 4: D (62) on beat 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))

# Bar 4: F (65) on beat 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0))

# Drums: Bar 2-4
# Kick on 1 and 3
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))

# Snare on 2 and 4
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))

# Hihat on every eighth
for i in range(2, 4):
    for j in range(0, 4):
        start = i * 1.5 + j * 0.375
        end = start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")

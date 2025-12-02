
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

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
# Walking line in D Dorian: D Eb F G A Bb B C
# Bar 2: D Eb F G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0))  # G

# Bar 3: A Bb B C
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125))  # A
bass.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=2.125, end=2.25))  # Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375))  # B
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.375, end=2.5))  # C

# Bar 4: D Eb F G
bass.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=2.75))  # Eb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=2.875))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0))  # G

# Diane: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Bar 2, beat 2: Dm7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0))  # C

# Bar 3, beat 2: Dm7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=2.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75))  # C

# Bar 4, beat 2: Dm7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5))  # C

# Sax: Dm motif - D Eb G Bb
# Bar 2, beat 1: D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625))
# Bar 2, beat 2: Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.0))
# Bar 3, beat 1: G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125))
# Bar 3, beat 2: Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.375, end=2.5))
# Bar 4, beat 1: D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625))
# Bar 4, beat 2: Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=2.875, end=3.0))

# Drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))

# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0))

# Hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(0, 4):
        hihat_start = start + i * 0.375
        hihat_end = hihat_start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")

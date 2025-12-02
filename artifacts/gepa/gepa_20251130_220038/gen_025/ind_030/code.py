
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

# Kick on beats 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on beats 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
# D Dm7 G7 Cmaj7 in D
# D - Eb - F# - G - A - Bb - B - C - D
bass_notes = [62, 63, 66, 67, 69, 70, 71, 72, 62]
for i, note in enumerate(bass_notes[:-1]):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: Diane, 7th chords on 2 and 4
# Dmaj7 on beat 2, G7 on beat 4, Bm7b5 on beat 2, E7 on beat 4
# Bar 2: Dmaj7 on beat 2, G7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5))  # D

piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0))  # F

# Bar 3: Bm7b5 on beat 2, E7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75))  # A

piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.25))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=6.0, end=6.25))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=6.0, end=6.25))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=83, start=6.0, end=6.25))  # D

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - F# - A - D - G - D
# Play on beats 1, 2, 3, 4 of bar 2
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625))  # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0))  # D

sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75))  # D

# Drums: Continue pattern from bar 1
# Kick on 1 and 3 of bars 2 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4 of bars 2 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=6.25, end=6.375))

# Hihat on every eighth note in bars 2-4
for i in range(4, 12):
    start = 1.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

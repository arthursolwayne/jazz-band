
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in F (F, G, A, Bb)
bass_notes = [78, 79, 80, 77]
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=start, end=end))

# Piano: 7th chords on 2 and 4 (F7 and Bb7)
# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab

# F7 on beat 2 (start=2.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=2.0, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=82, start=2.0, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=86, start=2.0, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=2.0, end=2.125))

# Bb7 on beat 4 (start=3.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.125))

# Sax: Short motif (F, Ab, Bb, F)
sax_notes = [78, 80, 82, 78]
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=sax_notes[i], start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line in F (F, G, A, Bb)
bass_notes = [78, 79, 80, 77]
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=start, end=end))

# Piano: 7th chords on 2 and 4 (F7 and Bb7)
# F7 on beat 2 (start=3.75)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=86, start=3.75, end=3.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=3.75, end=3.875))

# Bb7 on beat 4 (start=4.5)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=4.5, end=4.625))

# Sax: Repeat and finish the motif
sax_notes = [78, 80, 82, 78]
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=sax_notes[i], start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line in F (F, G, A, Bb)
bass_notes = [78, 79, 80, 77]
for i in range(4):
    start = 4.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=start, end=end))

# Piano: 7th chords on 2 and 4 (F7 and Bb7)
# F7 on beat 2 (start=5.25)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=86, start=5.25, end=5.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=5.25, end=5.375))

# Bb7 on beat 4 (start=6.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=80, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=6.0, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=6.0, end=6.125))

# Sax: Repeat motif and end with a held note
sax_notes = [78, 80, 82, 78]
for i in range(4):
    start = 4.5 + i * 0.375
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=sax_notes[i], start=start, end=end))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125))

# Hihat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])


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
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time signature: 4/4, 160 BPM, 4 bars = 6.0 seconds

# Bass line: walking line, chromatic approaches, never the same note twice
# F7 = F, A, C, E
# Bass line: F, Gb, G, A, Bb, B, C, Db, D, Eb, E, F#, G, Ab, A, Bb
bass_notes = [77, 76, 78, 79, 77, 78, 80, 79, 78, 77, 81, 79, 80, 79, 81, 79]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E
# F7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=80, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=1.5, end=1.875))

# F7 on beat 3
piano.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=80, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=3.0, end=3.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, Ab, Bb (F7 in 8th notes)
# Start on beat 1, leave it hanging on beat 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=1.875, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=3.0))

# Repeat motif starting on beat 3, finish on beat 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=80, start=4.125, end=4.5))

# Drums continue for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5))

# Hi-hat on every eighth
for i in range(4, 16):
    start = 1.5 + (i * 0.375)
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

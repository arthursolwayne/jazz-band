
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
for i in range(4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [34, 32, 30, 29, 28, 27, 25, 24, 22, 20, 19, 17, 15, 14, 12, 10]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.25
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: 7th chords on 2 and 4, Fm7, Bbm7, Fm7, Gm7
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (1.5 + 0.375, 53, 0.25), (1.5 + 0.375, 50, 0.25), (1.5 + 0.375, 60, 0.25), (1.5 + 0.375, 57, 0.25),
    # Bar 3: Bbm7 (Bb, Db, F, Ab)
    (1.5 + 0.375 * 2, 58, 0.25), (1.5 + 0.375 * 2, 55, 0.25), (1.5 + 0.375 * 2, 53, 0.25), (1.5 + 0.375 * 2, 50, 0.25),
    # Bar 4: Fm7 (F, Ab, C, Eb)
    (1.5 + 0.375 * 3, 53, 0.25), (1.5 + 0.375 * 3, 50, 0.25), (1.5 + 0.375 * 3, 60, 0.25), (1.5 + 0.375 * 3, 57, 0.25),
    # Bar 4: Gm7 (G, Bb, D, F)
    (1.5 + 0.375 * 3, 67, 0.25), (1.5 + 0.375 * 3, 58, 0.25), (1.5 + 0.375 * 3, 62, 0.25), (1.5 + 0.375 * 3, 53, 0.25)
]
for start, pitch, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Sax: Melody, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    (1.5, 62, 0.25),  # D
    (1.5 + 0.5, 60, 0.25),  # Bb
    (1.5 + 0.75, 58, 0.25),  # G
    # Bar 3: Return and finish
    (1.5 + 1.5, 62, 0.25),  # D
    (1.5 + 1.75, 60, 0.25),  # Bb
    (1.5 + 2.0, 58, 0.25),  # G
    (1.5 + 2.25, 55, 0.25)  # Eb
]
for start, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration))

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(6):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

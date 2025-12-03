
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 100), # Hihat on 2
    (0.75, 38, 100),  # Snare on 2
    (1.125, 42, 100), # Hihat on 3
    (1.5, 36, 100),   # Kick on 3
    (1.875, 42, 100), # Hihat on 4
    (2.25, 38, 100),  # Snare on 4
    (2.625, 42, 100)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 53, 100),  # F2
    (1.875, 55, 100), # F#2 (chromatic approach)
    (2.25, 57, 100),  # G2 (F to G)
    (2.625, 53, 100), # F2
    (3.0, 55, 100),   # F#2
    (3.375, 57, 100), # G2
    (3.75, 59, 100),  # A2 (G to A)
    (4.125, 57, 100)  # G2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375))

# Piano: open voicings, each bar has a different chord
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    # Bar 2
    (1.5, 53, 100),  # F
    (1.5, 64, 100),  # A
    (1.5, 60, 100),  # C
    (1.5, 65, 100),  # E
    # Bar 3: Gm7 (G, Bb, D, F)
    (2.25, 57, 100),  # G
    (2.25, 62, 100),  # Bb
    (2.25, 65, 100),  # D
    (2.25, 53, 100),  # F
    # Bar 4: C7 (C, E, G, Bb)
    (3.0, 60, 100),  # C
    (3.0, 65, 100),  # E
    (3.0, 67, 100),  # G
    (3.0, 62, 100),  # Bb
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G#, A, F
sax_notes = [
    (1.5, 72, 100),  # F4
    (1.75, 76, 100),  # G#4
    (1.875, 77, 100),  # A4
    (2.0, 72, 100),   # F4
    (2.25, 72, 100),  # F4 (restate)
    (2.5, 76, 100),   # G#4
    (2.625, 77, 100),  # A4
    (2.75, 72, 100)   # F4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 53, 100),  # F2
    (3.375, 55, 100), # F#2 (chromatic approach)
    (3.75, 57, 100),  # G2 (F to G)
    (4.125, 53, 100), # F2
    (4.5, 55, 100),   # F#2
    (4.875, 57, 100), # G2
    (5.25, 59, 100),  # A2 (G to A)
    (5.625, 57, 100)  # G2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375))

# Piano: open voicings, each bar has a different chord
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    (3.0, 57, 100),  # G
    (3.0, 62, 100),  # Bb
    (3.0, 65, 100),  # D
    (3.0, 53, 100),  # F
    (3.375, 62, 100),  # Bb (comp on 2)
    (3.375, 57, 100),  # G
    (3.75, 65, 100),  # D
    (3.75, 53, 100),  # F
    (4.125, 62, 100),  # Bb (comp on 4)
    (4.125, 57, 100),  # G
    (4.5, 65, 100),  # D
    (4.5, 53, 100)  # F
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375))

# Sax: Continue motif, build tension
# F, G#, A, Bb, A, G#, F
sax_notes = [
    (3.0, 72, 100),  # F4
    (3.25, 76, 100),  # G#4
    (3.375, 77, 100),  # A4
    (3.5, 71, 100),  # Bb4
    (3.625, 77, 100),  # A4
    (3.75, 76, 100),  # G#4
    (3.875, 72, 100),  # F4
    (4.0, 72, 100)    # F4 (resolve)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 53, 100),  # F2
    (4.875, 55, 100), # F#2 (chromatic approach)
    (5.25, 57, 100),  # G2 (F to G)
    (5.625, 53, 100), # F2
    (6.0, 55, 100),   # F#2
    (6.375, 57, 100), # G2
    (6.75, 59, 100),  # A2 (G to A)
    (7.125, 57, 100)  # G2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375))

# Piano: open voicings, each bar has a different chord
# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    (4.5, 60, 100),  # C
    (4.5, 65, 100),  # E
    (4.5, 67, 100),  # G
    (4.5, 62, 100),  # Bb
    (4.875, 62, 100),  # Bb (comp on 2)
    (4.875, 60, 100),  # C
    (5.25, 67, 100),  # G
    (5.25, 62, 100),  # Bb
    (5.625, 62, 100),  # Bb (comp on 4)
    (5.625, 60, 100),  # C
    (6.0, 67, 100),  # G
    (6.0, 62, 100)  # Bb
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375))

# Sax: Finish the motif, resolve with clarity
# F, G#, A, Bb, A, G#, F
sax_notes = [
    (4.5, 72, 100),  # F4
    (4.75, 76, 100),  # G#4
    (4.875, 77, 100),  # A4
    (5.0, 71, 100),  # Bb4
    (5.125, 77, 100),  # A4
    (5.25, 76, 100),  # G#4
    (5.375, 72, 100),  # F4
    (5.5, 72, 100)    # F4 (resolve)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 100), # Hihat on 2
    (5.25, 38, 100),  # Snare on 2
    (5.625, 42, 100), # Hihat on 3
    (6.0, 36, 100),   # Kick on 3
    (6.375, 42, 100), # Hihat on 4
    (6.75, 38, 100),  # Snare on 4
    (7.125, 42, 100)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

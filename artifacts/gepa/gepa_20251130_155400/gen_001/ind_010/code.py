
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
for bar in range(1):
    time = bar * 1.5
    # Kick on beat 1 and 3 (0.0 and 0.75s)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.05))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 0.8))
    # Snare on beat 2 and 4 (0.375 and 1.125s)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.4))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.2))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.05))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
# D minor key: D, Eb, F, G, Ab, Bb, B
bass_notes = [62, 63, 65, 67, 68, 70, 71]
bass_pattern = [62, 63, 65, 67, 68, 70, 71, 67, 68, 70, 71, 68, 70, 71, 72, 71]
for i, note in enumerate(bass_pattern):
    time = 1.5 + (i * 0.375)
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (1.5 + 0.375, 62), (1.5 + 0.375, 66), (1.5 + 0.375, 69), (1.5 + 0.375, 67),
    (1.5 + 1.125, 62), (1.5 + 1.125, 66), (1.5 + 1.125, 69), (1.5 + 1.125, 67),
    # Bar 3: G7 on 2 and 4
    (1.5 + 1.875, 67), (1.5 + 1.875, 71), (1.5 + 1.875, 69), (1.5 + 1.875, 67),
    (1.5 + 2.625, 67), (1.5 + 2.625, 71), (1.5 + 2.625, 69), (1.5 + 2.625, 67),
    # Bar 4: Cm7 on 2 and 4
    (1.5 + 3.525, 60), (1.5 + 3.525, 63), (1.5 + 3.525, 67), (1.5 + 3.525, 71),
    (1.5 + 4.275, 60), (1.5 + 4.275, 63), (1.5 + 4.275, 67), (1.5 + 4.275, 71)
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time = 1.5 + (bar - 2) * 1.5
    # Kick on beat 1 and 3 (0.0 and 0.75s)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.05))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 0.8))
    # Snare on beat 2 and 4 (0.375 and 1.125s)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.4))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.2))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.05))

# Dante on sax: short motif, make it sing
# Dm scale: D, Eb, F, G, Ab, Bb, B
# Motif: D - Eb - F - G (descending)
sax_notes = [
    (1.5, 62), (1.5 + 0.25, 63), (1.5 + 0.5, 65), (1.5 + 0.75, 67)
]
for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.1))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')


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
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Everyone in. Sax takes the melody
# F7 - G7 - A7 - Bb7 (F7 is F A C Eb)
# Start with F, then G, then A, then Bb
# Short motif, leave it hanging at Bb
sax_notes = [
    (1.5, 77), (1.625, 79), (1.75, 82), (1.875, 83)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Marcus: Walking bass line in F (F, G, Ab, A), repeat
# F (48), G (49), Ab (50), A (51)
bass_notes = [
    (1.5, 48), (1.625, 49), (1.75, 50), (1.875, 51),
    (2.0, 48), (2.125, 49), (2.25, 50), (2.375, 51),
    (2.5, 48), (2.625, 49), (2.75, 50), (2.875, 51)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Diane: 7th chords on 2 and 4
# F7 on 2 (beat 2), Bb7 on 4 (beat 4)
# F7 = F A C Eb (77, 79, 81, 83)
# Bb7 = Bb D F Ab (74, 76, 77, 79)
piano_notes = [
    (2.0, 77), (2.0, 79), (2.0, 81), (2.0, 83),
    (2.875, 74), (2.875, 76), (2.875, 77), (2.875, 79)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 3: Continue the motif, leave it hanging again
sax_notes = [
    (2.0, 77), (2.125, 79), (2.25, 82), (2.375, 83)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Marcus: Walking line continues
bass_notes = [
    (2.5, 48), (2.625, 49), (2.75, 50), (2.875, 51),
    (3.0, 48), (3.125, 49), (3.25, 50), (3.375, 51),
    (3.5, 48), (3.625, 49), (3.75, 50), (3.875, 51)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (3.0, 77), (3.0, 79), (3.0, 81), (3.0, 83),
    (3.875, 74), (3.875, 76), (3.875, 77), (3.875, 79)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 4: Finish the motif, resolve it
sax_notes = [
    (3.0, 77), (3.125, 79), (3.25, 82), (3.375, 83),
    (3.5, 81), (3.625, 79), (3.75, 77)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Marcus: Walking line continues
bass_notes = [
    (3.5, 48), (3.625, 49), (3.75, 50), (3.875, 51)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (3.5, 77), (3.5, 79), (3.5, 81), (3.5, 83),
    (4.375, 74), (4.375, 76), (4.375, 77), (4.375, 79)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

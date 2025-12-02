
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, Dm7
# Dm7: D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D etc.
bass_notes = [
    (1.5, 2), (1.875, 3), (2.25, 4), (2.625, 5),
    (3.0, 6), (3.375, 7), (3.75, 8), (4.125, 9),
    (4.5, 10), (4.875, 11), (5.25, 12), (5.625, 13)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# D7 = D F# A C
# Gm7 = G Bb D F
# G7 = G B D F#
piano_notes = [
    # Bar 2: Dm7 on beat 2
    (2.25, 64), (2.25, 67), (2.25, 71), (2.25, 74),
    # Bar 3: G7 on beat 2
    (3.75, 76), (3.75, 79), (3.75, 82), (3.75, 85),
    # Bar 4: Dm7 on beat 2
    (5.25, 64), (5.25, 67), (5.25, 71), (5.25, 74),
    # Bar 4: G7 on beat 4
    (6.0, 76), (6.0, 79), (6.0, 82), (6.0, 85)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax, short motif, make it sing
# Dm scale: D, Eb, F, G, A, Bb, B, C
# Motif: D to F to Bb to C
# Start it, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 62), (1.5, 64), (1.5, 67), (1.5, 69),
    (2.25, 62), (2.25, 64), (2.25, 67), (2.25, 69),
    (3.0, 62), (3.0, 64), (3.0, 67), (3.0, 69),
    (3.75, 62), (3.75, 64), (3.75, 67), (3.75, 69),
    (4.5, 62), (4.5, 64), (4.5, 67), (4.5, 69),
    (5.25, 62), (5.25, 64), (5.25, 67), (5.25, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_shorter_moment.mid")

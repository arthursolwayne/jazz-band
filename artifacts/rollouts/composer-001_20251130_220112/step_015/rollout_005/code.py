
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
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.375), (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375), (38, 1.875, 0.375),
    # Hi-hat on every eighth
    (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F7 (F, A, C, E), then Bb7 (Bb, D, F, Ab) - short motif

sax_notes = [
    # F7 (F, A, C, E)
    (79, 1.5, 0.25), (82, 1.75, 0.25), (87, 2.0, 0.25), (91, 2.25, 0.25),
    # Bb7 (Bb, D, F, Ab)
    (82, 2.5, 0.25), (87, 2.75, 0.25), (91, 3.0, 0.25), (85, 3.25, 0.25)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line, chromatic approaches
bass_notes = [
    # F -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
    (48, 1.5, 0.25), (50, 1.75, 0.25), (51, 2.0, 0.25), (52, 2.25, 0.25),
    (53, 2.5, 0.25), (55, 2.75, 0.25), (57, 3.0, 0.25), (59, 3.25, 0.25),
    (60, 3.5, 0.25)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # F7 on 2: F, A, C, E
    (79, 1.75, 0.25), (82, 1.75, 0.25), (87, 1.75, 0.25), (91, 1.75, 0.25),
    # Bb7 on 4: Bb, D, F, Ab
    (82, 2.25, 0.25), (87, 2.25, 0.25), (91, 2.25, 0.25), (85, 2.25, 0.25)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but with a half-step twist (F7 -> G7)
sax_notes = [
    (82, 3.0, 0.25), (87, 3.25, 0.25), (91, 3.5, 0.25), (96, 3.75, 0.25),
    (89, 4.0, 0.25), (92, 4.25, 0.25), (96, 4.5, 0.25), (95, 4.75, 0.25)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line, chromatic approaches
bass_notes = [
    # G -> A -> Bb -> B -> C -> D -> Eb -> E -> F -> G
    (50, 3.0, 0.25), (52, 3.25, 0.25), (53, 3.5, 0.25), (55, 3.75, 0.25),
    (57, 4.0, 0.25), (59, 4.25, 0.25), (61, 4.5, 0.25), (62, 4.75, 0.25),
    (64, 5.0, 0.25)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # G7 on 2: G, B, D, F
    (80, 3.25, 0.25), (84, 3.25, 0.25), (87, 3.25, 0.25), (91, 3.25, 0.25),
    # C7 on 4: C, E, G, B
    (72, 3.75, 0.25), (76, 3.75, 0.25), (80, 3.75, 0.25), (84, 3.75, 0.25)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a descending line, leave it hanging

sax_notes = [
    # Descend from G7 to F7
    (80, 4.5, 0.25), (79, 4.75, 0.25), (82, 5.0, 0.25), (87, 5.25, 0.25), (91, 5.5, 0.25)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line, chromatic approaches
bass_notes = [
    # F -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
    (48, 4.5, 0.25), (50, 4.75, 0.25), (51, 5.0, 0.25), (52, 5.25, 0.25),
    (53, 5.5, 0.25), (55, 5.75, 0.25), (57, 6.0, 0.25)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2: F, A, C, E
    (79, 4.75, 0.25), (82, 4.75, 0.25), (87, 4.75, 0.25), (91, 4.75, 0.25),
    # Bb7 on 4: Bb, D, F, Ab
    (82, 5.25, 0.25), (87, 5.25, 0.25), (91, 5.25, 0.25), (85, 5.25, 0.25)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Bar 3 and 4 (3.0 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    (36, 3.0, 0.375), (36, 4.125, 0.375),
    (36, 4.5, 0.375), (36, 5.625, 0.375),
    # Snare on 2 and 4
    (38, 3.75, 0.375), (38, 4.875, 0.375),
    (38, 5.25, 0.375), (38, 6.375, 0.375),
    # Hi-hat on every eighth
    (42, 3.0, 0.1875), (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875), (42, 4.3125, 0.1875),
    (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875), (42, 5.8125, 0.1875),
    (42, 6.0, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")

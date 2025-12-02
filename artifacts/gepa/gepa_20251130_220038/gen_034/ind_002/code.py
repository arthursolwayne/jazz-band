
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 64), (2.25, 62),  # D -> Eb -> E -> D
    (2.5, 60), (2.75, 61), (3.0, 62), (3.25, 60),  # B -> C -> D -> B
    (3.5, 63), (3.75, 64), (4.0, 65), (4.25, 63),  # Eb -> E -> F -> Eb
    (4.5, 62), (4.75, 63), (5.0, 64), (5.25, 62),  # D -> Eb -> E -> D
    (5.5, 60), (5.75, 61), (6.0, 62), (6.25, 60)   # B -> C -> D -> B
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    (2.0, 67), (2.0, 69), (2.0, 71), (2.0, 72),  # D, F#, A, C
    (2.25, 67), (2.25, 69), (2.25, 71), (2.25, 72),
    # Bar 3: G7 on 2 and 4
    (3.5, 71), (3.5, 73), (3.5, 75), (3.5, 76),  # G, B, D, F
    (3.75, 71), (3.75, 73), (3.75, 75), (3.75, 76),
    # Bar 4: C7 on 2 and 4
    (5.0, 67), (5.0, 69), (5.0, 71), (5.0, 72),  # C, E, G, B
    (5.25, 67), (5.25, 69), (5.25, 71), (5.25, 72)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax - melody: whisper at first, then a cry (D, E, B, F#, D)
sax_notes = [
    (1.5, 62), (1.5 + 0.75, 64), (1.5 + 1.5, 67), (1.5 + 2.25, 69), (1.5 + 3.0, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    kick_times = [start, start + 0.75]
    snare_times = [start + 0.375, start + 1.125]
    hihat_times = [start + 0.125 * i for i in range(8)]
    
    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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

# Bass line (Marcus): Walking line in Dm, chromatic approaches, 16th notes
bass_notes = [
    (1.5, 50), (1.75, 49), (2.0, 50), (2.25, 51),
    (2.5, 52), (2.75, 51), (3.0, 50), (3.25, 49),
    (3.5, 50), (3.75, 51), (4.0, 52), (4.25, 53),
    (4.5, 52), (4.75, 51), (5.0, 50), (5.25, 49)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4, Dm7, Gm7, Cm7, Fm7
piano_notes = [
    # Bar 2
    (2.0, 71), (2.0, 69), (2.0, 67), (2.0, 64),  # Dm7
    # Bar 3
    (3.5, 70), (3.5, 68), (3.5, 66), (3.5, 62),  # Gm7
    # Bar 4
    (5.0, 72), (5.0, 70), (5.0, 69), (5.0, 65),  # Cm7
    (5.5, 67), (5.5, 65), (5.5, 62), (5.5, 59)   # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 -> G7 -> Cm7 -> F7
# Bar 2: D (62), F (65), A (69), Bb (71)
sax_notes = [
    (2.0, 62), (2.25, 65), (2.5, 69), (2.75, 71),
    (3.25, 67), (3.5, 71), (3.75, 69), (4.0, 67),
    (4.25, 62), (4.5, 65), (4.75, 69), (5.0, 71),
    (5.25, 67), (5.5, 71), (5.75, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums continue for full 6 bars
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 6):
    bar_start = bar * 1.5
    kick_times = [bar_start, bar_start + 0.75]
    snare_times = [bar_start + 0.375, bar_start + 1.125]
    hihat_times = [bar_start + x * 0.125 for x in range(12)]
    for time in kick_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    for time in snare_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

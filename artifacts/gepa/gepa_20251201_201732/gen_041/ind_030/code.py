
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (43, 1.5), (44, 1.75), (42, 2.0), (41, 2.25),
    (43, 2.5), (44, 2.75), (42, 3.0), (41, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, comp on 2 and 4
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (66, 1.75), (77, 1.75), (79, 1.75), (83, 1.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    (71, 2.25), (76, 2.25), (79, 2.25), (79, 2.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    (72, 2.75), (83, 2.75), (79, 2.75), (76, 2.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F - G - A - F
sax_notes = [
    (87, 1.5), (88, 1.75), (89, 2.0), (87, 2.25),
    (87, 2.75), (88, 3.0), (89, 3.25), (87, 3.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums continue in bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    drum_notes = [
        (36, start_time), (38, start_time + 0.375), (42, start_time + 0.375),
        (36, start_time + 0.75), (38, start_time + 1.125), (42, start_time + 1.125),
        (36, start_time + 1.5), (38, start_time + 1.875), (42, start_time + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

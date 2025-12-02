
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.125), (42, 1.25),
    (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    (62, 1.5), (61, 1.875), (63, 2.25), (62, 2.625),  # Dm7
    (67, 2.625), (66, 2.875), (68, 3.125), (67, 3.375),  # G7
    (60, 3.375), (59, 3.75), (61, 4.125), (60, 4.5),  # Cm7
    (65, 4.5), (64, 4.875), (66, 5.25), (65, 5.5)   # F7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),  # Dm7
    (74, 2.5), (76, 2.5), (78, 2.5), (80, 2.5),  # G7
    # Bar 3
    (60, 3.0), (63, 3.0), (65, 3.0), (67, 3.0),  # Cm7
    (69, 3.5), (71, 3.5), (73, 3.5), (75, 3.5),  # F7
    # Bar 4
    (64, 4.0), (67, 4.0), (69, 4.0), (71, 4.0),  # Dm7
    (74, 4.5), (76, 4.5), (78, 4.5), (80, 4.5)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (62, 1.5), (65, 1.875), (67, 2.25), (65, 2.625),  # Dm7 motif
    # Bar 3
    (62, 3.375), (65, 3.75), (67, 4.125), (65, 4.5),  # Repeat motif
    # Bar 4
    (62, 4.875), (65, 5.25), (67, 5.5), (65, 5.875)   # Final resolution
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = (36, start)
    snare2 = (38, start + 0.375)
    hihat = [
        (42, start), (42, start + 0.125), (42, start + 0.25), (42, start + 0.375),
        (42, start + 0.75), (42, start + 0.875), (42, start + 1.125), (42, start + 1.25),
        (42, start + 1.375), (42, start + 1.5)
    ]
    kick3 = (36, start + 0.75)
    snare4 = (38, start + 1.125)
    for note, time in [kick1, kick3, snare2, snare4] + hihat:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

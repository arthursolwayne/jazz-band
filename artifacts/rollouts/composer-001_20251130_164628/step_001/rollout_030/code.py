
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Dm7 = D F A C (1st bar), chromatic lines
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625),  # D -> E -> C -> D
    (62, 3.0), (63, 3.375), (60, 3.75), (62, 4.125),  # D -> E -> C -> D
    (62, 4.5), (63, 4.875), (60, 5.25), (62, 5.625)   # D -> E -> C -> D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
# Dm7 on 1, F7 on 2, Am7 on 3, C7 on 4
piano_notes = [
    # Bar 2
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),  # Dm7
    (65, 1.875), (67, 1.875), (71, 1.875), (72, 1.875),  # F7
    (62, 2.25), (64, 2.25), (67, 2.25), (72, 2.25),  # Am7
    (69, 2.625), (71, 2.625), (74, 2.625), (76, 2.625),  # C7

    # Bar 3
    (62, 3.0), (64, 3.0), (67, 3.0), (69, 3.0),  # Dm7
    (65, 3.375), (67, 3.375), (71, 3.375), (72, 3.375),  # F7
    (62, 3.75), (64, 3.75), (67, 3.75), (72, 3.75),  # Am7
    (69, 4.125), (71, 4.125), (74, 4.125), (76, 4.125),  # C7

    # Bar 4
    (62, 4.5), (64, 4.5), (67, 4.5), (69, 4.5),  # Dm7
    (65, 4.875), (67, 4.875), (71, 4.875), (72, 4.875),  # F7
    (62, 5.25), (64, 5.25), (67, 5.25), (72, 5.25),  # Am7
    (69, 5.625), (71, 5.625), (74, 5.625), (76, 5.625)   # C7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor saxophone, short motif, make it sing
# Dm melody: D -> F -> A -> D (1st bar), then leave it hanging
sax_notes = [
    (62, 1.5), (64, 1.875), (67, 2.25), (62, 2.625),  # D -> F -> A -> D
    (64, 3.0), (67, 3.375), (62, 3.75), (64, 4.125),  # F -> A -> D -> F
    (67, 4.5), (62, 4.875), (64, 5.25), (67, 5.625)   # A -> D -> F -> A
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start), (42, start + 0.125), (42, start + 0.25), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 0.75), (42, start + 0.875), (42, start + 1.0), (42, start + 1.125)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

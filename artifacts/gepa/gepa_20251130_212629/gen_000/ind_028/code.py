
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F
# F -> G -> A -> Bb -> C -> D -> Eb -> F (chromatic approach)
bass_notes = [
    (53, 1.5, 0.375), (55, 1.875, 0.375), (57, 2.25, 0.375),
    (58, 2.625, 0.375), (60, 2.75, 0.375), (62, 3.125, 0.375),
    (63, 3.5, 0.375), (53, 3.875, 0.375),
    (55, 4.25, 0.375), (57, 4.625, 0.375), (58, 5.0, 0.375),
    (60, 5.375, 0.375), (62, 5.75, 0.375), (63, 6.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 (F7, Bb7, F7, Bb7)
piano_notes = [
    # F7 (F, A, C, E) on beat 2 of bar 2
    (65, 2.25, 0.1875), (68, 2.25, 0.1875), (72, 2.25, 0.1875), (69, 2.25, 0.1875),
    # Bb7 (Bb, D, F, Ab) on beat 4 of bar 2
    (62, 2.625, 0.1875), (65, 2.625, 0.1875), (69, 2.625, 0.1875), (67, 2.625, 0.1875),
    # F7 on beat 2 of bar 3
    (65, 4.25, 0.1875), (68, 4.25, 0.1875), (72, 4.25, 0.1875), (69, 4.25, 0.1875),
    # Bb7 on beat 4 of bar 3
    (62, 4.625, 0.1875), (65, 4.625, 0.1875), (69, 4.625, 0.1875), (67, 4.625, 0.1875),
    # F7 on beat 2 of bar 4
    (65, 5.75, 0.1875), (68, 5.75, 0.1875), (72, 5.75, 0.1875), (69, 5.75, 0.1875),
    # Bb7 on beat 4 of bar 4
    (62, 6.125, 0.1875), (65, 6.125, 0.1875), (69, 6.125, 0.1875), (67, 6.125, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Motif in F (Bb, D, F, Ab) - a question that sings, leaves it hanging
sax_notes = [
    (62, 1.5, 0.375), (66, 1.875, 0.375), (69, 2.25, 0.375), (67, 2.625, 0.375),
    (62, 3.5, 0.375), (66, 3.875, 0.375), (69, 4.25, 0.375), (67, 4.625, 0.375),
    (62, 5.75, 0.375), (66, 6.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drum fills for bar 4
drum_notes = [
    (36, 5.0, 0.375), (38, 5.375, 0.375), (42, 5.0, 0.1875),
    (36, 5.75, 0.375), (38, 6.125, 0.375), (42, 5.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

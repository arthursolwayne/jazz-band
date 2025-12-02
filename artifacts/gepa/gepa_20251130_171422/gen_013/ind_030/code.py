
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
    (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in F, chromatic approaches
bass_notes = [
    # Bar 2: F -> G -> Ab -> A -> Bb -> B -> C -> Db
    (53, 1.5, 0.375), (55, 1.875, 0.375), (56, 2.25, 0.375), (57, 2.625, 0.375),
    (58, 3.0, 0.375), (59, 3.375, 0.375), (60, 3.75, 0.375), (61, 4.125, 0.375),
    # Bar 3: C -> Db -> D -> Eb -> E -> F -> G -> Ab
    (60, 4.5, 0.375), (61, 4.875, 0.375), (62, 5.25, 0.375), (63, 5.625, 0.375),
    (64, 6.0, 0.375), (53, 6.375, 0.375), (55, 6.75, 0.375), (56, 7.125, 0.375),
    # Bar 4: Ab -> A -> Bb -> B -> C -> Db -> D -> Eb
    (56, 7.5, 0.375), (57, 7.875, 0.375), (58, 8.25, 0.375), (59, 8.625, 0.375),
    (60, 9.0, 0.375), (61, 9.375, 0.375), (62, 9.75, 0.375), (63, 10.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (64, 2.25, 0.375), (67, 2.25, 0.375), (69, 2.25, 0.375), (71, 2.25, 0.375),
    (64, 2.625, 0.375), (67, 2.625, 0.375), (69, 2.625, 0.375), (71, 2.625, 0.375),
    # Bar 3: Bb7 on 2 and 4
    (71, 5.25, 0.375), (74, 5.25, 0.375), (76, 5.25, 0.375), (78, 5.25, 0.375),
    (71, 5.625, 0.375), (74, 5.625, 0.375), (76, 5.625, 0.375), (78, 5.625, 0.375),
    # Bar 4: D7 on 2 and 4
    (67, 8.25, 0.375), (70, 8.25, 0.375), (72, 8.25, 0.375), (74, 8.25, 0.375),
    (67, 8.625, 0.375), (70, 8.625, 0.375), (72, 8.625, 0.375), (74, 8.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875),
    (36, 6.75, 0.375), (38, 7.125, 0.375), (42, 6.75, 0.1875),
    (42, 6.9375, 0.1875), (42, 7.125, 0.1875),
    (36, 7.5, 0.375), (38, 7.875, 0.375), (42, 7.5, 0.1875),
    (36, 8.25, 0.375), (38, 8.625, 0.375), (42, 8.25, 0.1875),
    (42, 8.4375, 0.1875), (42, 8.625, 0.1875),
    (36, 9.0, 0.375), (38, 9.375, 0.375), (42, 9.0, 0.1875),
    (36, 9.75, 0.375), (38, 10.125, 0.375), (42, 9.75, 0.1875),
    (42, 9.9375, 0.1875), (42, 10.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Tenor sax motif: F, Bb, D, F (melodic minor) with a bend on the Bb
sax_notes = [
    (64, 1.5, 0.375), (67, 1.875, 0.375), (71, 2.25, 0.375), (64, 2.625, 0.375),
    (64, 3.0, 0.375), (67, 3.375, 0.375), (71, 3.75, 0.375), (64, 4.125, 0.375),
    (64, 4.5, 0.375), (67, 4.875, 0.375), (71, 5.25, 0.375), (64, 5.625, 0.375),
    (64, 6.0, 0.375), (67, 6.375, 0.375), (71, 6.75, 0.375), (64, 7.125, 0.375),
    (64, 7.5, 0.375), (67, 7.875, 0.375), (71, 8.25, 0.375), (64, 8.625, 0.375),
    (64, 9.0, 0.375), (67, 9.375, 0.375), (71, 9.75, 0.375), (64, 10.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add a bend on the Bb (67) in bar 2
sax.pitch_bends.append(pretty_midi.Pitch Bend(time=1.875, pitch_bend=0x2000))
sax.pitch_bends.append(pretty_midi.Pitch Bend(time=2.25, pitch_bend=0x0000))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")

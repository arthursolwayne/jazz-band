
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
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125),
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),
    # Bar 3: G7 (G B D F)
    (71, 3.0), (73, 3.0), (76, 3.0), (78, 3.0),
    # Bar 4: Cm7 (C Eb G Bb)
    (60, 4.5), (62, 4.5), (67, 4.5), (69, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Sax - Motif: Dm7 -> G7 -> Cm7
# Start on D (62), move to F (64), then to A (67), then to C (69) - leave it hanging
# Come back on D (62) in bar 3 to pick it up again

# Bar 2: D -> F -> A -> C
sax_notes = [
    (62, 1.5), (64, 1.75), (67, 2.0), (69, 2.25)
]
# Bar 3: G -> B -> D -> F
sax_notes += [
    (71, 3.0), (73, 3.25), (76, 3.5), (78, 3.75)
]
# Bar 4: C -> Eb -> G -> Bb
sax_notes += [
    (60, 4.5), (62, 4.75), (67, 5.0), (69, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add drum fill for bar 4
drum_fill_notes = [
    (36, 5.25), (38, 5.375), (42, 5.25),
    (42, 5.375), (42, 5.5), (42, 5.625)
]
for note, time in drum_fill_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line with chromatic approaches, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    # Bar 2: Dm7 -> G7
    (62, 1.5), (60, 1.875), (59, 2.25), (62, 2.625),
    # Bar 3: Cm7 -> F7
    (60, 3.0), (58, 3.375), (57, 3.75), (60, 4.125),
    # Bar 4: Dm7 -> G7
    (62, 4.5), (60, 4.875), (59, 5.25), (62, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (beat 2)
    (62, 1.875), (67, 1.875), (65, 1.875),
    # Bar 3: Cm7 (beat 2)
    (60, 3.375), (65, 3.375), (63, 3.375),
    # Bar 4: Dm7 (beat 2)
    (62, 4.875), (67, 4.875), (65, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 -> G7 -> Cm7 -> F7
sax_notes = [
    # Bar 2: Start motif on D (62)
    (62, 1.5), (65, 1.875), (67, 2.25), (65, 2.625),
    # Bar 3: Leave it hanging with a G
    (67, 3.0), (65, 3.375), (67, 3.75), (69, 4.125),
    # Bar 4: Come back and finish on F
    (65, 4.5), (67, 4.875), (69, 5.25), (67, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

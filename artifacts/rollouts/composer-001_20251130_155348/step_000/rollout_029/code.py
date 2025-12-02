
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7 = D F A C
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (62, 2.5), (63, 2.75), (60, 3.0), (62, 3.25),
    (62, 3.5), (63, 3.75), (60, 4.0), (62, 4.25),
    (62, 4.5), (63, 4.75), (60, 5.0), (62, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
piano_notes = [
    (62, 2.0), (65, 2.0), (67, 2.0), (69, 2.0),
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0),
    (62, 4.0), (65, 4.0), (67, 4.0), (69, 4.0),
    (62, 5.0), (65, 5.0), (67, 5.0), (69, 5.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D E F G A Bb C
# Motif: D -> F -> G -> A -> rest -> D -> F -> G -> A
sax_notes = [
    (62, 1.5), (65, 1.75), (67, 2.0), (69, 2.25),
    (62, 2.75), (65, 3.0), (67, 3.25), (69, 3.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

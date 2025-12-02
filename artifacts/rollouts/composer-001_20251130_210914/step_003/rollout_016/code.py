
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

# Marcus on bass: walking line, chromatic approaches, Dm7 chord
bass_notes = [
    (62, 1.5), (63, 1.875), (60, 2.25), (62, 2.625),  # Dm7 walk
    (62, 3.0), (63, 3.375), (60, 3.75), (62, 4.125),  # Dm7 walk
    (62, 4.5), (63, 4.875), (60, 5.25), (62, 5.625)   # Dm7 walk
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 2.0), (64, 2.0), (62, 2.0), (60, 2.0),  # Dm7
    (67, 3.0), (64, 3.0), (62, 3.0), (60, 3.0),  # Dm7
    (67, 4.0), (64, 4.0), (62, 4.0), (60, 4.0)   # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante on sax: short motif, one phrase, leave it hanging
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0),  # D -> F -> D
    (60, 2.25), (62, 2.5), (64, 2.75), (62, 3.0),  # C -> D -> F -> D
    (60, 3.25), (62, 3.5), (64, 3.75), (62, 4.0),  # C -> D -> F -> D
    (60, 4.25), (62, 4.5), (64, 4.75), (62, 5.0)   # C -> D -> F -> D
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

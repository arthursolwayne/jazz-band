
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
# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.75), (65, 2.0), (64, 2.25),
    (62, 2.5), (63, 2.75), (65, 3.0), (64, 3.25),
    (62, 3.5), (63, 3.75), (65, 4.0), (64, 4.25),
    (62, 4.5), (63, 4.75), (65, 5.0), (64, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 2.0), (71, 2.0), (69, 2.0), (73, 2.0),  # D7
    (67, 3.0), (71, 3.0), (69, 3.0), (73, 3.0),  # D7
    (67, 4.0), (71, 4.0), (69, 4.0), (73, 4.0),  # D7
    (67, 5.0), (71, 5.0), (69, 5.0), (73, 5.0)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.0), (38, 2.375), (42, 2.375),
    (36, 2.5), (38, 2.875), (42, 2.875),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.5), (38, 3.875), (42, 3.875),
    (36, 4.0), (38, 4.375), (42, 4.375),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.0), (38, 5.375), (42, 5.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: motif in D, start it, leave it hanging, come back and finish it
# D F# A D (start), then leave it hanging on F#
sax_notes = [
    (62, 1.5), (66, 1.75), (69, 2.0), (62, 2.25),
    (62, 3.5), (66, 3.75), (69, 4.0), (62, 4.25),
    (62, 5.0), (66, 5.25), (69, 5.5), (62, 5.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

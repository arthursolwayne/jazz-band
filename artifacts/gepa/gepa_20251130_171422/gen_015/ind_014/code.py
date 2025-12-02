
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
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (63, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),
    (59, 3.5), (60, 3.75), (62, 4.0), (63, 4.25),
    (64, 4.5), (65, 4.75), (64, 5.0), (62, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.75), (64, 1.75), (67, 1.75), (71, 1.75),  # Dm7
    (62, 2.25), (66, 2.25), (69, 2.25), (72, 2.25),  # F7
    (60, 3.25), (64, 3.25), (67, 3.25), (71, 3.25),  # Dm7
    (62, 3.75), (66, 3.75), (69, 3.75), (72, 3.75),  # F7
    (60, 4.75), (64, 4.75), (67, 4.75), (71, 4.75)   # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (60, 1.5), (64, 1.875), (62, 2.25),  # Motif start
    (60, 2.75), (64, 3.125), (62, 3.5),  # Motif repeat
    (60, 4.5), (64, 4.875), (62, 5.25)   # Motif finish
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Continue full pattern
for i in range(2):
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 1.5 + i * 1.5, end=time + 1.5 + i * 1.5 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (61, 2.625),
    (62, 3.0), (64, 3.375), (63, 3.75), (61, 4.125),
    (62, 4.5), (64, 4.875), (63, 5.25), (61, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875), (64, 1.875), (67, 1.875), (71, 1.875),  # Dm7
    (64, 3.0), (67, 3.0), (69, 3.0), (73, 3.0),  # G7
    # Bar 3
    (62, 3.75), (64, 3.75), (67, 3.75), (71, 3.75),  # Dm7
    (64, 4.875), (67, 4.875), (69, 4.875), (73, 4.875)  # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - start on D, move to F, G, A, leave it hanging, come back to finish
sax_notes = [
    (62, 1.5), (64, 1.875), (65, 2.25), (67, 2.625),
    (67, 3.0), (65, 3.375), (64, 3.75), (62, 4.125),
    (62, 5.25), (64, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums continue: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start_time), (38, start_time + 0.375), (42, start_time + 0.375),
        (36, start_time + 1.125), (38, start_time + 1.5), (42, start_time + 1.5)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

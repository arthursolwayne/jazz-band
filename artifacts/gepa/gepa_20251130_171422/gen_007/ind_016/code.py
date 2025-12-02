
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

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    (62, 2.75), (64, 3.125), (63, 3.5), (60, 3.875),
    (62, 4.0), (64, 4.375), (63, 4.75), (60, 5.125),
    (62, 5.25), (64, 5.625), (63, 6.0), (60, 6.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (67, 1.5), (71, 1.5), (69, 1.5), (72, 1.5),  # D7
    (69, 2.0), (73, 2.0), (71, 2.0), (72, 2.0),  # F#7
    # Bar 3 (3.0 - 4.5s)
    (67, 3.0), (71, 3.0), (69, 3.0), (72, 3.0),  # D7
    (71, 3.5), (75, 3.5), (73, 3.5), (72, 3.5),  # A7
    # Bar 4 (4.5 - 6.0s)
    (67, 4.5), (71, 4.5), (69, 4.5), (72, 4.5),  # D7
    (69, 5.0), (73, 5.0), (71, 5.0), (72, 5.0),  # F#7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing (D, F#, B, D)
sax_notes = [
    (62, 1.5), (66, 1.75), (67, 2.0), (62, 2.25),
    (62, 3.0), (66, 3.25), (67, 3.5), (62, 3.75),
    (62, 4.5), (66, 4.75), (67, 5.0), (62, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

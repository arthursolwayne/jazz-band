
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5), (63, 1.75), (64, 2.0), (65, 2.25),
    # Bar 3
    (65, 2.5), (66, 2.75), (67, 3.0), (68, 3.25),
    # Bar 4
    (68, 3.5), (67, 3.75), (66, 4.0), (65, 4.25),
]

for note, time in bass_notes:
    b = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(b)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.0), (67, 2.0), (71, 2.0), (72, 2.0),  # D7
    # Bar 3
    (65, 3.0), (68, 3.0), (72, 3.0), (73, 3.0),  # E7
    # Bar 4
    (64, 4.0), (67, 4.0), (71, 4.0), (72, 4.0),  # D7
]

for note, time in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(p)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (67, 1.5), (71, 1.5), (69, 1.75), (67, 2.0),  # D G Bb D
    # Bar 3
    (67, 2.25), (71, 2.25), (69, 2.5),  # D G Bb (leave hanging)
    # Bar 4
    (67, 3.0), (71, 3.0), (69, 3.25), (67, 3.5),  # D G Bb D
]

for note, time in sax_notes:
    s = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(s)

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

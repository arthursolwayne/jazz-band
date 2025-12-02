
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

# Bass line: Walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (64, 2.5), (65, 2.75), (62, 3.0), (64, 3.25),
    (67, 3.5), (68, 3.75), (65, 4.0), (67, 4.25),
    (69, 4.5), (70, 4.75), (67, 5.0), (69, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 2.0), (71, 2.0), (69, 2.0), (72, 2.0),  # D7
    # Bar 3
    (72, 3.0), (76, 3.0), (74, 3.0), (77, 3.0),  # G7
    # Bar 4
    (67, 4.0), (71, 4.0), (69, 4.0), (72, 4.0)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (65, 1.5), (67, 1.75), (65, 2.0),
    (67, 3.0), (65, 3.25),
    (67, 4.0), (69, 4.25), (67, 4.5), (65, 4.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

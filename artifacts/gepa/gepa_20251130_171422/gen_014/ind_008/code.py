
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875), (36, 1.125), (38, 1.5),
    (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875), (42, 2.0), (42, 2.125),
    (42, 2.25), (42, 2.375)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5s)
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    # Bar 3 (2.5s)
    (64, 2.5), (65, 2.75), (62, 3.0), (64, 3.25),
    # Bar 4 (3.5s)
    (65, 3.5), (67, 3.75), (64, 4.0), (65, 4.25)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    (67, 1.75), (69, 1.75), (71, 1.75), (72, 1.75),  # D7 on beat 2
    (67, 2.25), (69, 2.25), (71, 2.25), (72, 2.25),  # D7 on beat 4
    # Bar 3 (2.5s)
    (67, 2.75), (69, 2.75), (71, 2.75), (72, 2.75),  # D7 on beat 2
    (67, 3.25), (69, 3.25), (71, 3.25), (72, 3.25),  # D7 on beat 4
    # Bar 4 (3.5s)
    (67, 3.75), (69, 3.75), (71, 3.75), (72, 3.75),  # D7 on beat 2
    (67, 4.25), (69, 4.25), (71, 4.25), (72, 4.25)   # D7 on beat 4
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5s) - Start the motif
    (62, 1.5), (64, 1.625), (65, 1.75),
    # Bar 3 (2.5s) - Leave it hanging
    (64, 2.5),
    # Bar 4 (3.5s) - Come back and finish it
    (65, 3.5), (64, 3.625), (62, 3.75)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (62, 2.25),
    (65, 2.5), (66, 2.75), (64, 3.0), (63, 3.25),
    (62, 3.5), (63, 3.75), (64, 4.0), (65, 4.25),
    (67, 4.5), (66, 4.75), (65, 5.0), (64, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 2.0), (71, 2.0), (74, 2.0), (69, 2.0), # D7
    # Bar 3
    (67, 3.5), (71, 3.5), (76, 3.5), (70, 3.5), # G7
    # Bar 4
    (67, 5.0), (71, 5.0), (74, 5.0), (69, 5.0)  # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (67, 1.5), (69, 1.75), (71, 2.0), # D, F#, A (motif start)
    (67, 2.5), (69, 2.75), (71, 3.0), # D, F#, A (motif repeat)
    (74, 3.5), (71, 3.75), (69, 4.0), # C#, A, F#
    (74, 4.5), (71, 4.75), (67, 5.0)  # C#, A, D (resolution)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (47, 1.875), (46, 2.25), (44, 2.625),
    (45, 3.0), (47, 3.375), (46, 3.75), (44, 4.125),
    (45, 4.5), (47, 4.875), (46, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (59, 2.0), (57, 2.0), (60, 2.0), (62, 2.0),
    (59, 3.0), (57, 3.0), (60, 3.0), (62, 3.0),
    # Bar 3: Bb7 on 2 and 4
    (62, 4.0), (60, 4.0), (63, 4.0), (65, 4.0),
    (62, 5.0), (60, 5.0), (63, 5.0), (65, 5.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif
    (62, 1.5), (64, 1.75), (62, 2.0),
    # Bar 3: Leave it hanging
    (62, 3.5),
    # Bar 4: Come back and finish it
    (64, 4.5), (62, 4.75), (60, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

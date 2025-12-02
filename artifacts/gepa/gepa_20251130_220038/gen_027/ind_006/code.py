
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),
    (67, 3.0), (69, 3.375), (68, 3.75), (70, 4.125),
    (72, 4.5), (74, 4.875), (73, 5.25), (75, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    (60, 2.25), (64, 2.25), (67, 2.25), (69, 2.25),
    # Bar 3: F7 on beat 2
    (53, 3.75), (57, 3.75), (60, 3.75), (62, 3.75),
    # Bar 4: Bb7 on beat 2
    (62, 5.25), (65, 5.25), (69, 5.25), (71, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (65, 1.875), (62, 2.25),
    (65, 2.625), (67, 2.75), (65, 3.0),
    (62, 3.375), (65, 3.75), (67, 4.125),
    (69, 4.5), (67, 4.875), (65, 5.25),
    (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")

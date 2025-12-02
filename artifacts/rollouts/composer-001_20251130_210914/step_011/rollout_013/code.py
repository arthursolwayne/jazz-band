
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

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (53, 1.5), (54, 1.75), (52, 2.0), (51, 2.25),
    (53, 2.5), (54, 2.75), (52, 3.0), (51, 3.25),
    (53, 3.5), (54, 3.75), (52, 4.0), (51, 4.25),
    (53, 4.5), (54, 4.75), (52, 5.0), (51, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (64, 2.0), (67, 2.0), (69, 2.0), (71, 2.0),
    # Bar 3: Bb7 on beat 2
    (71, 3.0), (74, 3.0), (76, 3.0), (78, 3.0),
    # Bar 4: E7 on beat 2
    (69, 4.0), (72, 4.0), (74, 4.0), (76, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (64) - Bb (67) - E (69) - F (64) -> leave it on the Bb
sax_notes = [
    (64, 1.5), (67, 1.75), (69, 2.0), (64, 2.25),
    (67, 4.5), (69, 4.75), (64, 5.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

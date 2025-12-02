
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (43, 2.25),
    (45, 2.5), (46, 2.75), (44, 3.0), (43, 3.25),
    (45, 3.5), (46, 3.75), (44, 4.0), (43, 4.25),
    (45, 4.5), (46, 4.75), (44, 5.0), (43, 5.25)
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
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Melody - one short motif, make it sing
# F (65), G (67), Bb (69), D (71)
sax_notes = [
    (65, 1.5), (67, 1.5), (69, 1.5), (71, 1.5),
    (65, 2.5), (67, 2.5), (69, 2.5), (71, 2.5),
    (65, 3.5), (67, 3.5), (69, 3.5), (71, 3.5),
    (65, 4.5), (67, 4.5), (69, 4.5), (71, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("dante_intro.mid")

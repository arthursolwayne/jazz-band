
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, F7 chord (F A C Eb)
bass_notes = [
    (44, 1.5), (45, 1.875), (43, 2.25), (42, 2.625),  # F, F#, E, D
    (44, 3.0), (45, 3.375), (43, 3.75), (42, 4.125),  # F, F#, E, D
    (44, 4.5), (45, 4.875), (43, 5.25), (42, 5.625)   # F, F#, E, D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
# F7 = F A C Eb
# Bb7 = Bb D F Ab
# D7 = D F# A C
# G7 = G B D F
piano_notes = [
    # Bar 2 - F7 on 2 and 4
    (65, 2.25), (68, 2.25), (69, 2.25), (67, 2.25),  # F A C Eb
    (65, 3.0), (68, 3.0), (69, 3.0), (67, 3.0),     # F A C Eb
    # Bar 3 - Bb7 on 2 and 4
    (62, 3.75), (65, 3.75), (69, 3.75), (66, 3.75),  # Bb D F Ab
    (62, 4.5), (65, 4.5), (69, 4.5), (66, 4.5),     # Bb D F Ab
    # Bar 4 - D7 on 2 and 4
    (62, 5.25), (64, 5.25), (67, 5.25), (69, 5.25),  # D F# A C
    (62, 6.0), (64, 6.0), (67, 6.0), (69, 6.0)      # D F# A C
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 chord (F A C Eb) with a chromatic approach
# Bar 2: F (65), Eb (67), C (69), A (68)
# Bar 3: F (65), D (67), C (69), B (71)
# Bar 4: F (65), Eb (67), C (69), A (68), then resolution to F (65)
sax_notes = [
    (65, 1.5), (67, 1.5), (69, 1.5), (68, 1.5),  # F Eb C A
    (65, 3.0), (67, 3.0), (69, 3.0), (71, 3.0),  # F D C B
    (65, 4.5), (67, 4.5), (69, 4.5), (68, 4.5),  # F Eb C A
    (65, 6.0)                                    # F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375), (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875), (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

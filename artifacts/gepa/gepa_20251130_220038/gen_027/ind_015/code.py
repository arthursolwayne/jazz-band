
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F, G, A, Bb, C, D, Eb, F)
bass_notes = [
    (78, 1.5), (79, 1.875), (81, 2.25), (82, 2.625),
    (84, 3.0), (86, 3.375), (87, 3.75), (78, 4.125),
    (79, 4.5), (81, 4.875), (82, 5.25), (84, 5.625),
    (86, 6.0), (87, 6.375), (78, 6.75), (79, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords on 2 and 4. F7 on 2, Bb7 on 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (78, 1.5), (82, 1.5), (84, 1.5), (87, 1.5),
    # Bar 2: Rest
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (82, 3.0), (86, 3.0), (78, 3.0), (89, 3.0),
    # Bar 3: Rest
    # Bar 4: F7 again
    (78, 4.5), (82, 4.5), (84, 4.5), (87, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Dante: Melody starts on F, goes to A, Bb, C, then ends on F
# Bar 2: F (78) at 1.5s
# Bar 2: A (82) at 1.875s
# Bar 2: Bb (82) at 2.25s
# Bar 2: C (84) at 2.625s
# Bar 3: Leave it hanging
# Bar 4: Come back with F (78) at 4.5s

sax_notes = [
    (78, 1.5), (82, 1.875), (82, 2.25), (84, 2.625),
    (78, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

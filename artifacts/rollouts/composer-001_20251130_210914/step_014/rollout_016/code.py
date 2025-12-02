
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

# Marcus - Walking bass line in F (F, G, Ab, A, Bb, B, C, Db)
bass_notes = [
    (78, 1.5), (79, 1.875), (77, 2.25), (80, 2.625),
    (76, 3.0), (77, 3.375), (78, 3.75), (79, 4.125),
    (78, 4.5), (79, 4.875), (77, 5.25), (80, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane - 7th chords on 2 and 4, F7, Bb7, F7, Bb7
piano_notes = [
    # Bar 2
    (65, 1.875), (69, 1.875), (72, 1.875), (76, 1.875),  # F7
    # Bar 3
    (71, 3.375), (75, 3.375), (78, 3.375), (82, 3.375),  # Bb7
    # Bar 4
    (65, 4.875), (69, 4.875), (72, 4.875), (76, 4.875)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante - Tenor sax: One short motif, make it sing. F, G, Bb, F
sax_notes = [
    (87, 1.5), (89, 1.875), (84, 2.25), (87, 2.625),
    (87, 3.0), (89, 3.375), (84, 3.75), (87, 4.125),
    (87, 4.5), (89, 4.875), (84, 5.25), (87, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

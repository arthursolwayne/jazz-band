
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

# Marcus - Walking bass line in Dm
bass_notes = [
    (62, 1.5), (60, 1.875), (62, 2.25), (64, 2.625),
    (65, 3.0), (64, 3.375), (62, 3.75), (60, 4.125),
    (62, 4.5), (60, 4.875), (62, 5.25), (64, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane - Piano comping on 2 and 4 with 7th chords
# Dm7 = C, D, F, G
piano_notes = [
    # Bar 2
    (60, 2.0), (62, 2.0), (65, 2.0), (67, 2.0),  # Dm7
    # Bar 3
    (60, 3.5), (62, 3.5), (65, 3.5), (67, 3.5),  # Dm7
    # Bar 4
    (60, 5.0), (62, 5.0), (65, 5.0), (67, 5.0)   # Dm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

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

# Dante - Tenor sax motif
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62), Eb (63), F (65) - then leave it hanging
sax_notes = [
    (62, 1.5), (63, 1.625), (65, 1.75), # Motif
    (62, 2.5), (63, 2.625), (65, 2.75), # Repeat motif
    (62, 3.5), (63, 3.625), (65, 3.75), # Repeat motif
    (62, 4.5), (63, 4.625), (65, 4.75)  # Repeat motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

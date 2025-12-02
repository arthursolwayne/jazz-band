
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (F, G, A, Bb, B, C, D, Eb)
# Chromatic approaches, no repeated notes
bass_notes = [
    (70, 1.5), (71, 1.875), (72, 2.25), (70, 2.625),  # F, G, A, F
    (71, 3.0), (72, 3.375), (74, 3.75), (72, 4.125),  # G, A, B, A
    (74, 4.5), (76, 4.875), (77, 5.25), (76, 5.625)   # B, C, D, C
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
# F7, Bb7, C7, Eb7
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (65, 1.75), (67, 1.75), (70, 1.75), (72, 1.75),  # F7
    (62, 2.25), (64, 2.25), (67, 2.25), (69, 2.25),  # Bb7
    # Bar 3 (3.0 - 4.5s)
    (65, 3.25), (67, 3.25), (70, 3.25), (72, 3.25),  # F7
    (62, 3.75), (64, 3.75), (67, 3.75), (69, 3.75),  # Bb7
    # Bar 4 (4.5 - 6.0s)
    (65, 4.75), (67, 4.75), (70, 4.75), (72, 4.75),  # F7
    (62, 5.25), (64, 5.25), (67, 5.25), (69, 5.25)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax, short motif, sing it, leave it hanging
# F, A, Bb, F (Motif)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    (65, 1.5), (68, 1.75), (69, 2.0), (65, 2.25),  # Start motif
    (65, 3.0)                                       # Return to start
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

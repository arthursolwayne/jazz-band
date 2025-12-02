
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),
    (67, 3.0), (69, 3.375), (68, 3.75), (70, 4.125),
    (72, 4.5), (74, 4.875), (73, 5.25), (75, 5.625)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 2.0), (67, 2.0), (71, 2.0), (72, 2.0),  # D7
    (64, 2.5), (67, 2.5), (71, 2.5), (72, 2.5),  # D7
    # Bar 3
    (69, 3.0), (72, 3.0), (76, 3.0), (77, 3.0),  # G7
    (69, 3.5), (72, 3.5), (76, 3.5), (77, 3.5),  # G7
    # Bar 4
    (62, 4.0), (65, 4.0), (69, 4.0), (70, 4.0),  # Bm7
    (62, 4.5), (65, 4.5), (69, 4.5), (70, 4.5)   # Bm7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Saxophone - motif: D, E, F#, D
# Start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5), (64, 1.75), (66, 2.0), (62, 2.25),
    (62, 4.5), (64, 4.75), (66, 5.0), (62, 5.25)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


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

# Bass line: walking with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (65, 2.625),
    (67, 3.0), (69, 3.375), (68, 3.75), (70, 4.125),
    (72, 4.5), (74, 4.875), (73, 5.25), (75, 5.625)
]
for note, time in bass_notes:
    b = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(b)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.0), (67, 2.0), (71, 2.0), (72, 2.0),  # D7
    (62, 3.0), (65, 3.0), (69, 3.0), (70, 3.0),  # Bm7
    (64, 4.0), (67, 4.0), (71, 4.0), (72, 4.0),  # D7
    (62, 5.0), (65, 5.0), (69, 5.0), (70, 5.0)   # Bm7
]
for note, time in piano_notes:
    p = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(p)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5), (65, 1.875), (69, 2.25), (72, 2.625),
    (69, 3.0), (65, 3.375), (62, 3.75),
    (65, 4.5), (69, 4.875), (72, 5.25)
]
for note, time in sax_notes:
    s = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(s)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

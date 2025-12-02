
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif starting on D (D4) with a chromatic descent
sax_notes = [
    (62, 1.5), (60, 1.75), (59, 2.0), (62, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach to D
bass_notes = [
    (45, 1.5), (46, 1.75), (47, 2.0), (49, 2.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (1.75s)
    (62, 1.75), (67, 1.75), (64, 1.75), (69, 1.75),
    # G7 on 4 (2.25s)
    (67, 2.25), (72, 2.25), (69, 2.25), (74, 2.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif repeats, then ascends
sax_notes = [
    (62, 3.0), (60, 3.25), (59, 3.5), (62, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach to G
bass_notes = [
    (49, 3.0), (50, 3.25), (51, 3.5), (53, 3.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # G7 on 2 (3.25s)
    (67, 3.25), (72, 3.25), (69, 3.25), (74, 3.25),
    # C7 on 4 (3.75s)
    (60, 3.75), (65, 3.75), (62, 3.75), (67, 3.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif, resolve to D
sax_notes = [
    (62, 4.5), (60, 4.75), (59, 5.0), (62, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach to D
bass_notes = [
    (53, 4.5), (54, 4.75), (55, 5.0), (57, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 on 2 (4.75s)
    (60, 4.75), (65, 4.75), (62, 4.75), (67, 4.75),
    # F7 on 4 (5.25s)
    (58, 5.25), (63, 5.25), (60, 5.25), (65, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

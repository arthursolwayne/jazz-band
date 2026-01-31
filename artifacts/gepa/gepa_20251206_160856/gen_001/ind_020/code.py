
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    (71, 1.5), (70, 1.75), (67, 2.0), (69, 2.25),
    (71, 2.5), (70, 2.75), (67, 3.0), (69, 3.25)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (71, 1.5), (70, 1.5), (69, 1.5), (73, 1.5)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(n)

# Sax: Start motif
sax_notes = [
    (72, 1.5), (76, 1.75), (74, 2.0)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    (70, 3.0), (67, 3.25), (69, 3.5), (68, 3.75),
    (70, 4.0), (67, 4.25), (69, 4.5), (68, 4.75)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: Bbm7 (Bb, Db, F, Ab)
piano_notes = [
    (70, 3.0), (68, 3.0), (71, 3.0), (70, 3.0)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(n)

# Sax: Continue motif
sax_notes = [
    (72, 3.0), (76, 3.25), (74, 3.5), (72, 3.75)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass_notes = [
    (68, 4.5), (67, 4.75), (69, 5.0), (71, 5.25),
    (68, 5.5), (67, 5.75), (69, 6.0), (71, 6.25)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: C7 (C, E, G, B)
piano_notes = [
    (69, 4.5), (72, 4.5), (74, 4.5), (77, 4.5)
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5)
    piano.notes.append(n)

# Sax: Finish motif
sax_notes = [
    (72, 4.5), (76, 4.75), (74, 5.0), (72, 5.25)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

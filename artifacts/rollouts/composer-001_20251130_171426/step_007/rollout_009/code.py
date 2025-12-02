
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (45, 1.5), (44, 1.875), (43, 2.25), (42, 2.625),
    (41, 3.0), (40, 3.375), (39, 3.75), (38, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (45, 1.875), (43, 1.875), (40, 1.875), (38, 1.875),
    (45, 3.375), (43, 3.375), (40, 3.375), (38, 3.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Sax: Motif starts here
sax_notes = [
    (50, 1.5), (53, 1.875), (55, 2.25), (53, 2.625),
    (50, 3.0), (48, 3.375), (50, 3.75), (52, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (45, 3.0), (44, 3.375), (43, 3.75), (42, 4.125),
    (41, 4.5), (40, 4.875), (39, 5.25), (38, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (45, 3.375), (43, 3.375), (40, 3.375), (38, 3.375),
    (45, 4.875), (43, 4.875), (40, 4.875), (38, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Sax: continue motif
sax_notes = [
    (50, 3.0), (53, 3.375), (55, 3.75), (53, 4.125),
    (50, 4.5), (48, 4.875), (50, 5.25), (52, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (45, 4.5), (44, 4.875), (43, 5.25), (42, 5.625),
    (41, 6.0), (40, 6.375), (39, 6.75), (38, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (45, 4.875), (43, 4.875), (40, 4.875), (38, 4.875),
    (45, 6.375), (43, 6.375), (40, 6.375), (38, 6.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Sax: finish motif
sax_notes = [
    (50, 4.5), (53, 4.875), (55, 5.25), (53, 5.625),
    (50, 6.0), (48, 6.375), (50, 6.75), (52, 7.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

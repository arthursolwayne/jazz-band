
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
# Bass: Walking line, chromatic approaches, Fm7 -> Bb7 -> Eb7 -> Ab7
bass_notes = [
    (53, 1.5), (52, 1.75), (51, 2.0), (50, 2.25),
    (53, 2.5), (52, 2.75), (51, 3.0), (50, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.75), (67, 1.75), (69, 1.75), (71, 1.75),  # Fm7
    (67, 2.25), (71, 2.25), (74, 2.25), (76, 2.25),  # Bb7
    (64, 2.75), (67, 2.75), (69, 2.75), (71, 2.75),  # Fm7
    (67, 3.25), (71, 3.25), (74, 3.25), (76, 3.25)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - F (65), Ab (67), Bb (69), D (71) - start on 1, leave it hanging
sax_notes = [
    (65, 1.5), (67, 1.75), (69, 2.0), (71, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches, Fm7 -> Bb7 -> Eb7 -> Ab7
bass_notes = [
    (53, 3.0), (52, 3.25), (51, 3.5), (50, 3.75),
    (53, 4.0), (52, 4.25), (51, 4.5), (50, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.25), (67, 3.25), (69, 3.25), (71, 3.25),  # Fm7
    (67, 3.75), (71, 3.75), (74, 3.75), (76, 3.75),  # Bb7
    (64, 4.25), (67, 4.25), (69, 4.25), (71, 4.25),  # Fm7
    (67, 4.75), (71, 4.75), (74, 4.75), (76, 4.75)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif again, but now finished
sax_notes = [
    (65, 3.0), (67, 3.25), (69, 3.5), (71, 3.75), (69, 4.0), (67, 4.25), (65, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches, Fm7 -> Bb7 -> Eb7 -> Ab7
bass_notes = [
    (53, 4.5), (52, 4.75), (51, 5.0), (50, 5.25),
    (53, 5.5), (52, 5.75), (51, 6.0), (50, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 4.75), (67, 4.75), (69, 4.75), (71, 4.75),  # Fm7
    (67, 5.25), (71, 5.25), (74, 5.25), (76, 5.25),  # Bb7
    (64, 5.75), (67, 5.75), (69, 5.75), (71, 5.75),  # Fm7
    (67, 6.25), (71, 6.25), (74, 6.25), (76, 6.25)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Finale - return to motif
sax_notes = [
    (65, 4.5), (67, 4.75), (69, 5.0), (71, 5.25), (69, 5.5), (67, 5.75), (65, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

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

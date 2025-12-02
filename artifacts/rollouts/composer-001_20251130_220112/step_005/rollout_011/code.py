
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

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (43, 2.25),  # F -> Gb -> Eb -> D
    (45, 2.5), (46, 2.75), (44, 3.0), (43, 3.25)   # F -> Gb -> Eb -> D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (1.875s)
    (53, 1.875), (57, 1.875), (60, 1.875), (62, 1.875),
    # Bb7 on beat 4 (3.125s)
    (59, 3.125), (63, 3.125), (65, 3.125), (67, 3.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif starting on F, ascending chromatic line to Gb, resolving to Eb
sax_notes = [
    (53, 1.5), (54, 1.75), (55, 2.0), (57, 2.25),  # F -> F# -> G -> G#
    (59, 2.5), (60, 2.75), (62, 3.0)               # A -> A# -> B -> Bb
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (45, 3.0), (46, 3.25), (44, 3.5), (43, 3.75),  # F -> Gb -> Eb -> D
    (45, 4.0), (46, 4.25), (44, 4.5), (43, 4.75)   # F -> Gb -> Eb -> D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (3.875s)
    (53, 3.875), (57, 3.875), (60, 3.875), (62, 3.875),
    # Bb7 on beat 4 (5.125s)
    (59, 5.125), (63, 5.125), (65, 5.125), (67, 5.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (45, 4.5), (46, 4.75), (44, 5.0), (43, 5.25),  # F -> Gb -> Eb -> D
    (45, 5.5), (46, 5.75), (44, 6.0), (43, 6.25)   # F -> Gb -> Eb -> D
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (5.875s)
    (53, 5.875), (57, 5.875), (60, 5.875), (62, 5.875),
    # Bb7 on beat 4 (6.125s)
    (59, 6.125), (63, 6.125), (65, 6.125), (67, 6.125)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Final resolution, return to F, end on Eb
sax_notes = [
    (53, 4.5), (57, 4.75), (60, 5.0), (62, 5.25),  # F -> G -> A -> Bb
    (62, 5.5), (60, 5.75), (57, 6.0), (53, 6.25)   # Bb -> A -> G -> F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

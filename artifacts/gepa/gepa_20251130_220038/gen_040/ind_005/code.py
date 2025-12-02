
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.0),
    (36, 0.75), (38, 1.125), (42, 0.75),
    (36, 1.5), (38, 1.875), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - walking in Fm, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.875), (50, 2.25), (51, 2.625),
    (52, 3.0), (53, 3.375), (54, 3.75), (55, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano - 7th chords on 2 and 4
piano_notes = [
    (47, 1.875), (50, 1.875), (53, 1.875), (55, 1.875),  # Fm7
    (45, 3.375), (48, 3.375), (50, 3.375), (53, 3.375)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax melody - start with a whisper, build to a cry
sax_notes = [
    (48, 1.5), (51, 1.875), (48, 2.25), (50, 2.625),
    (51, 3.0), (53, 3.375), (51, 3.75), (50, 4.125),
    (48, 4.5), (51, 4.875), (53, 5.25), (55, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - walking in Fm, chromatic approaches
bass_notes = [
    (52, 3.0), (53, 3.375), (54, 3.75), (55, 4.125),
    (56, 4.5), (57, 4.875), (58, 5.25), (59, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano - 7th chords on 2 and 4
piano_notes = [
    (47, 3.375), (50, 3.375), (53, 3.375), (55, 3.375),  # Fm7
    (45, 4.875), (48, 4.875), (50, 4.875), (53, 4.875)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax melody - build to a cry
sax_notes = [
    (53, 3.0), (55, 3.375), (53, 3.75), (51, 4.125),
    (53, 4.5), (55, 4.875), (57, 5.25), (55, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line - walking in Fm, chromatic approaches
bass_notes = [
    (56, 4.5), (57, 4.875), (58, 5.25), (59, 5.625),
    (60, 6.0), (61, 6.375), (62, 6.75), (63, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano - 7th chords on 2 and 4
piano_notes = [
    (47, 4.875), (50, 4.875), (53, 4.875), (55, 4.875),  # Fm7
    (45, 6.375), (48, 6.375), (50, 6.375), (53, 6.375)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax melody - resolution with a whisper
sax_notes = [
    (55, 4.5), (53, 4.875), (51, 5.25), (48, 5.625),
    (51, 6.0), (53, 6.375), (55, 6.75), (53, 7.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.5),
    (36, 5.25), (38, 5.625), (42, 5.25),
    (36, 6.0), (38, 6.375), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')

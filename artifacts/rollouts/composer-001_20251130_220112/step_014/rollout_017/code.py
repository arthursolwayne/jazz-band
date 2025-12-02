
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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm7 motif starting on D (62), Bb (60), F (58), C (60)
sax_notes = [
    (62, 1.5), (60, 1.75), (58, 2.0), (60, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in Dm
bass_notes = [
    (62, 1.5), (60, 1.75), (58, 2.0), (60, 2.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Dm7 on 2 and 4
piano_notes = [
    (62, 1.75), (58, 1.75), (60, 1.75), (64, 1.75),
    (62, 2.25), (58, 2.25), (60, 2.25), (64, 2.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for time in [1.5, 1.875, 2.25, 2.625]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
for time in [1.75, 2.125]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
for time in [1.5, 1.625, 1.75, 1.875, 2.0, 2.125, 2.25, 2.375]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but end on C (60)
sax_notes = [
    (62, 3.0), (60, 3.25), (58, 3.5), (60, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in Dm
bass_notes = [
    (62, 3.0), (60, 3.25), (58, 3.5), (60, 3.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Dm7 on 2 and 4
piano_notes = [
    (62, 3.25), (58, 3.25), (60, 3.25), (64, 3.25),
    (62, 3.75), (58, 3.75), (60, 3.75), (64, 3.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for time in [3.0, 3.375, 3.75, 4.125]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
for time in [3.25, 3.625]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
for time in [3.0, 3.125, 3.25, 3.375, 3.5, 3.625, 3.75, 3.875]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a resolution to Cm7 (C, Eb, G, Bb)
sax_notes = [
    (60, 4.5), (64, 4.75), (67, 5.0), (64, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in Dm
bass_notes = [
    (62, 4.5), (60, 4.75), (58, 5.0), (60, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Dm7 on 2 and 4
piano_notes = [
    (62, 4.75), (58, 4.75), (60, 4.75), (64, 4.75),
    (62, 5.25), (58, 5.25), (60, 5.25), (64, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for time in [4.5, 4.875, 5.25, 5.625]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
for time in [4.75, 5.125]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
for time in [4.5, 4.625, 4.75, 4.875, 5.0, 5.125, 5.25, 5.375]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

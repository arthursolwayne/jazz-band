
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
# Sax: motif starting on Fm7 (F, Ab, Bb, D)
sax_notes = [
    (84, 1.5), (80, 1.75), (82, 2.0), (86, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line in Fm, chromatic approach
bass_notes = [
    (53, 1.5), (51, 1.75), (52, 2.0), (50, 2.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: comping on 2 and 4 with F7 chords (F, A, C, E)
piano_notes = [
    (53, 1.75), (58, 1.75), (60, 1.75), (64, 1.75),
    (53, 2.25), (58, 2.25), (60, 2.25), (64, 2.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif with slight variation
sax_notes = [
    (84, 3.0), (80, 3.25), (82, 3.5), (86, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach
bass_notes = [
    (53, 3.0), (51, 3.25), (52, 3.5), (50, 3.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: comping on 2 and 4 with F7 chords
piano_notes = [
    (53, 3.25), (58, 3.25), (60, 3.25), (64, 3.25),
    (53, 3.75), (58, 3.75), (60, 3.75), (64, 3.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolution, with a half-step descent at the end
sax_notes = [
    (84, 4.5), (80, 4.75), (82, 5.0), (81, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach
bass_notes = [
    (53, 4.5), (51, 4.75), (52, 5.0), (50, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: comping on 2 and 4 with F7 chords
piano_notes = [
    (53, 4.75), (58, 4.75), (60, 4.75), (64, 4.75),
    (53, 5.25), (58, 5.25), (60, 5.25), (64, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

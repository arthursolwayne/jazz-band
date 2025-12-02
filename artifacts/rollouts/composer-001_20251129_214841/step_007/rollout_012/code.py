
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    (36, 0.75), (38, 1.125), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.5), (42, 1.625), (42, 1.75), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C (60), E (64), Bb (62), D (65) - short motif
sax_notes = [
    (60, 1.5, 1.75), (64, 1.75, 2.0), (62, 2.0, 2.25), (65, 2.25, 2.5)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bass: Walking line in C - C, D, Eb, F, G, Ab, Bb, B
bass_notes = [
    (60, 1.5, 1.75), (62, 1.75, 2.0), (63, 2.0, 2.25), (65, 2.25, 2.5),
    (67, 2.5, 2.75), (68, 2.75, 3.0), (69, 3.0, 3.25), (70, 3.25, 3.5)
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 1.75, 2.0), (64, 1.75, 2.0), (67, 1.75, 2.0), (71, 1.75, 2.0),  # C7
    (62, 2.25, 2.5), (65, 2.25, 2.5), (68, 2.25, 2.5), (72, 2.25, 2.5)   # D7
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but with variation
sax_notes = [
    (60, 3.0, 3.25), (64, 3.25, 3.5), (62, 3.5, 3.75), (65, 3.75, 4.0)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bass: Walking line in C
bass_notes = [
    (60, 3.0, 3.25), (62, 3.25, 3.5), (63, 3.5, 3.75), (65, 3.75, 4.0),
    (67, 4.0, 4.25), (68, 4.25, 4.5), (69, 4.5, 4.75), (70, 4.75, 5.0)
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 3.25, 3.5), (65, 3.25, 3.5), (68, 3.25, 3.5), (72, 3.25, 3.5),  # D7
    (60, 3.75, 4.0), (64, 3.75, 4.0), (67, 3.75, 4.0), (71, 3.75, 4.0)   # C7
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Drums: Same pattern
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 1.5, end=time + 1.625))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif with a resolution
sax_notes = [
    (60, 4.5, 4.75), (64, 4.75, 5.0), (62, 5.0, 5.25), (65, 5.25, 5.5),
    (60, 5.5, 5.75), (64, 5.75, 6.0)
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bass: Walking line in C
bass_notes = [
    (60, 4.5, 4.75), (62, 4.75, 5.0), (63, 5.0, 5.25), (65, 5.25, 5.5),
    (67, 5.5, 5.75), (68, 5.75, 6.0), (69, 6.0, 6.25), (70, 6.25, 6.5)
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (62, 4.75, 5.0), (65, 4.75, 5.0), (68, 4.75, 5.0), (72, 4.75, 5.0),  # D7
    (60, 5.25, 5.5), (64, 5.25, 5.5), (67, 5.25, 5.5), (71, 5.25, 5.5),  # C7
    (60, 5.75, 6.0), (64, 5.75, 6.0), (67, 5.75, 6.0), (71, 5.75, 6.0)   # C7
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Drums: Same pattern
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 3.0, end=time + 3.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")

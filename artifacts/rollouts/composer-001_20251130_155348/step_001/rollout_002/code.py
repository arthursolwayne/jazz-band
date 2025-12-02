
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

# Bass line: walking line, chromatic approaches
bass_notes = [
    (37, 1.5), (38, 1.75), (39, 2.0), (41, 2.25),
    (41, 2.5), (40, 2.75), (39, 3.0), (37, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (65, 1.75), (69, 1.75), (67, 1.75), (68, 1.75),
    # Bar 2: C7 on beat 4
    (72, 2.25), (76, 2.25), (74, 2.25), (75, 2.25),
    # Bar 3: F7 on beat 2
    (65, 2.75), (69, 2.75), (67, 2.75), (68, 2.75),
    # Bar 3: C7 on beat 4
    (72, 3.25), (76, 3.25), (74, 3.25), (75, 3.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Melody motif
sax_notes = [
    (66, 1.5), (69, 1.75), (67, 2.0), (66, 2.25),  # First 4 notes of motif
    (66, 2.5), (69, 2.75), (67, 3.0), (66, 3.25)   # Repeat motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking line, chromatic approaches
bass_notes = [
    (41, 3.0), (40, 3.25), (39, 3.5), (37, 3.75),
    (37, 4.0), (38, 4.25), (39, 4.5), (41, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    (65, 3.25), (69, 3.25), (67, 3.25), (68, 3.25),
    # Bar 3: C7 on beat 4
    (72, 3.75), (76, 3.75), (74, 3.75), (75, 3.75),
    # Bar 4: F7 on beat 2
    (65, 4.25), (69, 4.25), (67, 4.25), (68, 4.25),
    # Bar 4: C7 on beat 4
    (72, 4.75), (76, 4.75), (74, 4.75), (75, 4.75)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Melody motif
sax_notes = [
    (66, 3.0), (69, 3.25), (67, 3.5), (66, 3.75),  # First 4 notes of motif
    (66, 4.0), (69, 4.25), (67, 4.5), (66, 4.75)   # Repeat motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass line: walking line, chromatic approaches
bass_notes = [
    (41, 4.5), (40, 4.75), (39, 5.0), (37, 5.25),
    (37, 5.5), (38, 5.75), (39, 6.0), (37, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    (65, 4.75), (69, 4.75), (67, 4.75), (68, 4.75),
    # Bar 4: C7 on beat 4
    (72, 5.25), (76, 5.25), (74, 5.25), (75, 5.25)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Melody motif
sax_notes = [
    (66, 4.5), (69, 4.75), (67, 5.0), (66, 5.25),  # First 4 notes of motif
    (66, 5.5), (69, 5.75), (67, 6.0), (66, 6.25)   # Repeat motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

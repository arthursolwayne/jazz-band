
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

# Bass line: walking line in F minor, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.75), (44, 2.0), (42, 2.25),
    (45, 2.5), (46, 2.75), (44, 3.0), (42, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2, beat 1: leave empty
    # Bar 2, beat 2: F7
    (59, 2.0), (60, 2.0), (62, 2.0), (64, 2.0),
    # Bar 2, beat 3: leave empty
    # Bar 2, beat 4: C7
    (67, 3.0), (68, 3.0), (70, 3.0), (72, 3.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif
sax_notes = [
    (62, 1.5), (65, 1.75), (62, 2.0), (60, 2.25),
    (62, 2.5), (65, 2.75), (62, 3.0), (60, 3.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in F minor, chromatic approaches
bass_notes = [
    (45, 3.0), (46, 3.25), (44, 3.5), (42, 3.75),
    (45, 4.0), (46, 4.25), (44, 4.5), (42, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 3, beat 1: leave empty
    # Bar 3, beat 2: F7
    (59, 3.5), (60, 3.5), (62, 3.5), (64, 3.5),
    # Bar 3, beat 3: leave empty
    # Bar 3, beat 4: C7
    (67, 4.5), (68, 4.5), (70, 4.5), (72, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif repetition
sax_notes = [
    (62, 3.0), (65, 3.25), (62, 3.5), (60, 3.75),
    (62, 4.0), (65, 4.25), (62, 4.5), (60, 4.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking line in F minor, chromatic approaches
bass_notes = [
    (45, 4.5), (46, 4.75), (44, 5.0), (42, 5.25),
    (45, 5.5), (46, 5.75), (44, 6.0), (42, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 4, beat 1: leave empty
    # Bar 4, beat 2: F7
    (59, 5.0), (60, 5.0), (62, 5.0), (64, 5.0),
    # Bar 4, beat 3: leave empty
    # Bar 4, beat 4: C7
    (67, 6.0), (68, 6.0), (70, 6.0), (72, 6.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif repetition and resolution
sax_notes = [
    (62, 4.5), (65, 4.75), (62, 5.0), (60, 5.25),
    (62, 5.5), (65, 5.75), (62, 6.0), (60, 6.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starting on D (62), Bb (60), F# (66), D (62)
sax_notes = [
    (62, 1.5), (60, 1.75), (66, 2.0), (62, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (62, 2.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (F#7 on beat 2, B7 on beat 4)
piano_notes = [
    (66, 1.75), (69, 1.75), (71, 1.75), (73, 1.75),  # F#7
    (71, 2.25), (73, 2.25), (76, 2.25), (78, 2.25)   # B7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but with a slight variation
sax_notes = [
    (62, 3.0), (60, 3.25), (66, 3.5), (62, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (62, 3.0), (63, 3.25), (64, 3.5), (62, 3.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (F#7 on beat 2, B7 on beat 4)
piano_notes = [
    (66, 3.25), (69, 3.25), (71, 3.25), (73, 3.25),  # F#7
    (71, 3.75), (73, 3.75), (76, 3.75), (78, 3.75)   # B7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 4.125), (38, 4.5), (42, 4.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif, but end on D (62)
sax_notes = [
    (62, 4.5), (60, 4.75), (66, 5.0), (62, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (62, 4.5), (63, 4.75), (64, 5.0), (62, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4 (F#7 on beat 2, B7 on beat 4)
piano_notes = [
    (66, 4.75), (69, 4.75), (71, 4.75), (73, 4.75),  # F#7
    (71, 5.25), (73, 5.25), (76, 5.25), (78, 5.25)   # B7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.625), (38, 6.0), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

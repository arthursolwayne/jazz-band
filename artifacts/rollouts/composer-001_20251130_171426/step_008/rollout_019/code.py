
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
# Sax: motif in D minor, starting on Eb (D is root, Eb is 9)
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (60, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach to D
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (62, 2.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: comp on 2 and 4, 7th chords
piano_notes = [
    (67, 1.75), (70, 1.75), (72, 1.75),  # D7 on 2
    (67, 2.25), (70, 2.25), (72, 2.25)   # D7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but with slight variation
sax_notes = [
    (62, 3.0), (64, 3.25), (62, 3.5), (60, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach to D
bass_notes = [
    (62, 3.0), (63, 3.25), (64, 3.5), (62, 3.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: comp on 2 and 4, 7th chords
piano_notes = [
    (67, 3.25), (70, 3.25), (72, 3.25),  # D7 on 2
    (67, 3.75), (70, 3.75), (72, 3.75)   # D7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: complete the motif, resolving to D
sax_notes = [
    (62, 4.5), (64, 4.75), (62, 5.0), (65, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bass: walking line, chromatic approach to D
bass_notes = [
    (62, 4.5), (63, 4.75), (64, 5.0), (62, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: comp on 2 and 4, 7th chords
piano_notes = [
    (67, 4.75), (70, 4.75), (72, 4.75),  # D7 on 2
    (67, 5.25), (70, 5.25), (72, 5.25)   # D7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")

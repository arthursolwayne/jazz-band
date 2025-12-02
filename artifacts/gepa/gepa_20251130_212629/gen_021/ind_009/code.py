
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
    (36, 0.0), (38, 0.375), (42, 0.0),
    (36, 1.125), (38, 1.5), (42, 0.375),
    (42, 0.75), (42, 1.125), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Everyone in (1.5 - 3.0s)

## Drums: same pattern
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 1.5, end=time + 1.625))

## Bass: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (64, 2.0), (63, 2.25),
    (62, 2.5), (61, 2.75), (60, 3.0), (61, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

## Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.0), (67, 2.0), (71, 2.0), (72, 2.0),  # D7
    (64, 2.75), (67, 2.75), (71, 2.75), (72, 2.75)  # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

## Sax: Motif, start it and leave it hanging
sax_notes = [
    (69, 1.5), (71, 1.75), (69, 2.0),
    (71, 2.25), (69, 2.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: (3.0 - 4.5s)

## Drums: same pattern
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 3.0, end=time + 3.125))

## Bass: Walking line, chromatic approaches
bass_notes = [
    (63, 3.0), (62, 3.25), (61, 3.5), (62, 3.75),
    (63, 4.0), (64, 4.25), (65, 4.5), (64, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

## Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.25), (67, 3.25), (71, 3.25), (72, 3.25),  # D7
    (64, 4.0), (67, 4.0), (71, 4.0), (72, 4.0)        # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

## Sax: Continue the motif, build tension
sax_notes = [
    (67, 3.0), (69, 3.25), (67, 3.5),
    (69, 3.75), (67, 4.0), (65, 4.25), (67, 4.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: (4.5 - 6.0s)

## Drums: same pattern
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 4.5, end=time + 4.625))

## Bass: Walking line, chromatic approaches
bass_notes = [
    (62, 4.5), (61, 4.75), (60, 5.0), (61, 5.25),
    (62, 5.5), (63, 5.75), (64, 6.0)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

## Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 4.75), (67, 4.75), (71, 4.75), (72, 4.75),  # D7
    (64, 5.5), (67, 5.5), (71, 5.5), (72, 5.5)        # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

## Sax: End the motif with a question
sax_notes = [
    (65, 4.5), (67, 4.75), (65, 5.0),
    (67, 5.25), (65, 5.5), (64, 5.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")

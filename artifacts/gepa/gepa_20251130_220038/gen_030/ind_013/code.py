
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
    (36, 2.25), (38, 2.625), (42, 2.625),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5), (63, 1.75), (60, 2.0), (62, 2.25),
    (64, 2.5), (62, 2.75), (60, 3.0), (62, 3.25),
    (63, 3.5), (62, 3.75), (60, 4.0), (62, 4.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 2.0), (67, 2.0), (70, 2.0), (72, 2.0),
    (67, 3.0), (70, 3.0), (72, 3.0), (69, 3.0),
    (64, 4.0), (67, 4.0), (70, 4.0), (72, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Melody - motif in Dm, short and singing
sax_notes = [
    (62, 1.5), (64, 1.75), (62, 2.0), (60, 2.25),
    (62, 2.5), (64, 2.75), (62, 3.0), (60, 3.25),
    (62, 3.5), (64, 3.75), (62, 4.0), (60, 4.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 3.0), (63, 3.25), (60, 3.5), (62, 3.75),
    (64, 4.0), (62, 4.25), (60, 4.5), (62, 4.75),
    (63, 5.0), (62, 5.25), (60, 5.5), (62, 5.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.5), (67, 3.5), (70, 3.5), (72, 3.5),
    (67, 4.5), (70, 4.5), (72, 4.5), (69, 4.5),
    (64, 5.5), (67, 5.5), (70, 5.5), (72, 5.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Melody continuation
sax_notes = [
    (62, 3.0), (64, 3.25), (62, 3.5), (60, 3.75),
    (62, 4.0), (64, 4.25), (62, 4.5), (60, 4.75),
    (62, 5.0), (64, 5.25), (62, 5.5), (60, 5.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: same pattern
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 4.5), (63, 4.75), (60, 5.0), (62, 5.25),
    (64, 5.5), (62, 5.75), (60, 6.0), (62, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 5.0), (67, 5.0), (70, 5.0), (72, 5.0),
    (67, 6.0), (70, 6.0), (72, 6.0), (69, 6.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Melody resolution
sax_notes = [
    (62, 4.5), (64, 4.75), (62, 5.0), (60, 5.25),
    (62, 5.5), (64, 5.75), (62, 6.0), (60, 6.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: same pattern
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

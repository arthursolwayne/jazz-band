
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
    (36, 0.0), (38, 0.375), (42, 0.375), (42, 0.75),
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: F - G - A - Bb
sax_notes = [
    (84, 1.5), (87, 1.875), (89, 2.25), (88, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in F (F - G - Ab - A - Bb - B - C - D)
bass_notes = [
    (84, 1.5), (87, 1.875), (88, 2.25), (90, 2.625),
    (88, 3.0), (91, 3.375), (92, 3.75), (95, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4, F7, Bb7
piano_notes = [
    (84, 1.875), (87, 1.875), (91, 1.875), (92, 1.875),
    (88, 3.375), (91, 3.375), (96, 3.375), (97, 3.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with variation
sax_notes = [
    (84, 3.0), (87, 3.375), (89, 3.75), (86, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in F
bass_notes = [
    (84, 3.0), (87, 3.375), (88, 3.75), (90, 4.125),
    (88, 4.5), (91, 4.875), (92, 5.25), (95, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4, F7, Bb7
piano_notes = [
    (84, 3.375), (87, 3.375), (91, 3.375), (92, 3.375),
    (88, 4.875), (91, 4.875), (96, 4.875), (97, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif, but resolve it
sax_notes = [
    (84, 4.5), (87, 4.875), (89, 5.25), (88, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line in F
bass_notes = [
    (84, 4.5), (87, 4.875), (88, 5.25), (90, 5.625),
    (88, 6.0), (91, 6.375), (92, 6.75), (95, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4, F7, Bb7
piano_notes = [
    (84, 4.875), (87, 4.875), (91, 4.875), (92, 4.875),
    (88, 6.375), (91, 6.375), (96, 6.375), (97, 6.375)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875), (42, 5.25),
    (36, 5.625), (38, 6.0), (42, 6.0)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

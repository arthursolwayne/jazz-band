
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
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (61, 2.25), (63, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (65, 1.5), (67, 1.5), (69, 1.5), (71, 1.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Motif starts here, incomplete
sax_notes = [
    (62, 1.5), (65, 1.875), (67, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    (64, 3.0), (62, 3.375), (66, 3.75), (64, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Bb7 (D, F, A, C)
piano_notes = [
    (62, 3.0), (65, 3.0), (67, 3.0), (69, 3.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Continue motif, leave it hanging
sax_notes = [
    (67, 3.0), (64, 3.375), (66, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    (64, 4.5), (62, 4.875), (63, 5.25), (61, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Gm7 (Bb, D, G, B)
piano_notes = [
    (62, 4.5), (65, 4.5), (69, 4.5), (71, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Continue motif, finish it
sax_notes = [
    (64, 4.5), (67, 5.25), (69, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375),
    (36, 6.75), (38, 7.125), (42, 7.125)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

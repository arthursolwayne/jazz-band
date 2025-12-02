
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.375), (42, 0.75), (42, 1.125), (42, 1.5),
    (36, 1.5), (38, 1.875), (42, 1.875), (42, 2.25), (42, 2.625), (42, 3.0),
]
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Whispering motif, start on D (62), then Bb (60), then A (57), then G (67), then D (62) again
sax_notes = [
    (62, 1.5), (60, 1.875), (57, 2.25), (67, 2.625), (62, 3.0)
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bass: Walking line in Dm, with chromatic approaches
bass_notes = [
    (62, 1.5), (60, 1.875), (59, 2.25), (62, 2.625), (64, 3.0), (62, 3.375), (60, 3.75), (59, 4.125)
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Dm7 on 1
    (62, 1.5), (64, 1.5), (67, 1.5), (71, 1.5),
    # Bar 2 - F7 on 2
    (65, 1.875), (67, 1.875), (71, 1.875), (76, 1.875),
    # Bar 3 - Gm7 on 1
    (67, 2.625), (69, 2.625), (72, 2.625), (76, 2.625),
    # Bar 3 - Bb7 on 2
    (69, 3.0), (71, 3.0), (74, 3.0), (79, 3.0)
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Let the motif continue with a cry, descending from D to Bb to A to G to D
sax_notes = [
    (62, 3.0), (60, 3.375), (57, 3.75), (67, 4.125), (62, 4.5)
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bass: Walking line in Dm, with chromatic approaches
bass_notes = [
    (62, 3.0), (60, 3.375), (59, 3.75), (62, 4.125), (64, 4.5), (62, 4.875), (60, 5.25), (59, 5.625)
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 - Gm7 on 1
    (67, 3.0), (69, 3.0), (72, 3.0), (76, 3.0),
    # Bar 3 - Bb7 on 2
    (69, 3.375), (71, 3.375), (74, 3.375), (79, 3.375),
    # Bar 4 - C7 on 1
    (60, 4.125), (62, 4.125), (67, 4.125), (71, 4.125),
    # Bar 4 - Dm7 on 2
    (62, 4.5), (64, 4.5), (67, 4.5), (71, 4.5)
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Let the motif finish with a cry in D, then a breath of silence
sax_notes = [
    (62, 4.5), (60, 4.875), (57, 5.25), (67, 5.625)
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bass: Walking line in Dm, with chromatic approaches
bass_notes = [
    (62, 4.5), (60, 4.875), (59, 5.25), (62, 5.625)
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4 - C7 on 1
    (60, 4.5), (62, 4.5), (67, 4.5), (71, 4.5),
    # Bar 4 - Dm7 on 2
    (62, 4.875), (64, 4.875), (67, 4.875), (71, 4.875)
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    piano.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.375), (42, 3.75), (42, 4.125), (42, 4.5),
    (36, 4.5), (38, 4.875), (42, 4.875), (42, 5.25), (42, 5.625), (42, 6.0),
]
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

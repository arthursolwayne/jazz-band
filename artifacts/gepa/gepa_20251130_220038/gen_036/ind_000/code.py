
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
    (36, 0.0), (38, 0.375), (42, 0.375), (36, 0.75), (38, 1.125), (42, 1.125), (36, 1.5)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (53, 1.5), (52, 1.875), (51, 2.25), (50, 2.625),
    (53, 2.875), (52, 3.25), (51, 3.625), (50, 4.0),
    (53, 4.25), (52, 4.625), (51, 5.0), (50, 5.375),
    (53, 5.625), (52, 6.0)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4 of each bar
piano_notes = [
    (65, 2.0), (62, 2.0), (60, 2.0), (58, 2.0),  # F7 at bar 2
    (68, 3.0), (65, 3.0), (63, 3.0), (61, 3.0),  # Bb7 at bar 3
    (69, 4.0), (66, 4.0), (64, 4.0), (62, 4.0),  # Eb7 at bar 4
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Sax: Short motif starting at bar 2, leave it hanging, return at bar 4
sax_notes = [
    (60, 1.5), (62, 1.875), (64, 2.25), (62, 2.625),  # First phrase
    (60, 4.5), (62, 4.875), (64, 5.25), (62, 5.625)   # Return phrase
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

# Drums for bars 2-4
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (36, 2.25), (38, 2.625), (42, 2.625), (36, 3.0),
    (36, 3.5), (38, 3.875), (42, 3.875), (36, 4.25), (38, 4.625), (42, 4.625), (36, 5.0),
    (36, 5.5), (38, 5.875), (42, 5.875), (36, 6.0)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

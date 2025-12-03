
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
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (66, 2.625),
    (67, 3.0), (69, 3.375), (68, 3.75), (71, 4.125),
    (72, 4.5), (74, 4.875), (73, 5.25), (76, 5.625)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    (62, 1.5), (67, 1.5), (69, 1.5), (64, 1.5),
    (62, 1.875), (67, 1.875), (69, 1.875), (64, 1.875),
    (62, 2.25), (67, 2.25), (69, 2.25), (64, 2.25)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Bar 3: Bm7 (B D F# A)
piano_notes = [
    (66, 3.0), (69, 3.0), (71, 3.0), (69, 3.0),
    (66, 3.375), (69, 3.375), (71, 3.375), (69, 3.375),
    (66, 3.75), (69, 3.75), (71, 3.75), (69, 3.75)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Bar 4: G7 (G B D F)
piano_notes = [
    (67, 4.5), (72, 4.5), (69, 4.5), (67, 4.5),
    (67, 4.875), (72, 4.875), (69, 4.875), (67, 4.875),
    (67, 5.25), (72, 5.25), (69, 5.25), (67, 5.25)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Sax: short motif, start it, leave it hanging, come back to finish it
# Motif: D (62), F# (67), A (69), G (67)
sax_notes = [
    (62, 1.5), (67, 1.5), (69, 1.5), (67, 1.5),  # Bar 2
    (62, 2.25), (67, 2.25), (69, 2.25), (67, 2.25),  # Bar 3
    (62, 3.75), (67, 3.75), (69, 3.75), (67, 3.75),  # Bar 4
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Drums: continue the pattern
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

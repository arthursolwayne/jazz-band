
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
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (36, 1.5), (38, 1.875), (37, 2.25), (34, 2.625),
    (36, 3.0), (38, 3.375), (37, 3.75), (34, 4.125),
    (36, 4.5), (38, 4.875), (37, 5.25), (34, 5.625)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano (Diane): 7th chords, comp on 2 and 4
# Fm7 (F, Ab, C, Eb)
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (53, 3.0), (51, 3.0), (58, 3.0), (55, 3.0),
    # Bar 3: Fm7 on beat 2
    (53, 4.5), (51, 4.5), (58, 4.5), (55, 4.5),
    # Bar 4: Fm7 on beat 2
    (53, 6.0), (51, 6.0), (58, 6.0), (55, 6.0)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Saxophone (Dante): One short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F -> Ab -> Bb -> F
sax_notes = [
    (53, 1.5), (55, 1.5), (57, 1.5), (53, 1.5),
    (53, 3.0), (55, 3.0), (57, 3.0), (53, 3.0),
    (53, 4.5), (55, 4.5), (57, 4.5), (53, 4.5)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

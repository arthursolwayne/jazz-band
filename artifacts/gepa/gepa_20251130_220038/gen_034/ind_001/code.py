
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

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    # Bar 3
    (45, 3.0), (46, 3.375), (47, 3.75), (45, 4.125),
    # Bar 4
    (45, 4.5), (46, 4.875), (44, 5.25), (43, 5.625)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 chord on beat 2
    (59, 2.25), (61, 2.25), (64, 2.25), (62, 2.25),
    # Bar 3: Bb7 chord on beat 2
    (62, 3.375), (64, 3.375), (67, 3.375), (65, 3.375),
    # Bar 4: F7 chord on beat 2
    (59, 4.375), (61, 4.375), (64, 4.375), (62, 4.375)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Saxophone (Dante): One short motif, make it sing
# Motif: F (59) -> G (60) -> E (57) -> D (55)
# Start on beat 1 of bar 2 (1.5s), leave it hanging on beat 2 (1.875s)
# Come back on beat 3 (2.625s) to finish it
sax_notes = [
    (59, 1.5), (60, 1.875), (57, 2.625), (55, 3.0)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")

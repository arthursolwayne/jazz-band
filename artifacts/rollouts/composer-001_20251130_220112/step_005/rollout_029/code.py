
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (47, 2.25), (49, 2.625),
    (50, 3.0), (51, 3.375), (52, 3.75), (53, 4.125),
    (55, 4.5), (56, 4.875), (57, 5.25), (59, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (60, 2.0), (64, 2.0), (67, 2.0), (71, 2.0),  # F7 on beat 2
    (60, 3.5), (64, 3.5), (67, 3.5), (71, 3.5),  # F7 on beat 4
    (60, 5.0), (64, 5.0), (67, 5.0), (71, 5.0)   # F7 on beat 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax (Dante): One short motif, starts on bar 2, leaves it hanging, returns in bar 4
sax_notes = [
    (62, 1.5), (64, 1.875), (66, 2.25), (64, 2.625),  # Start of motif
    (62, 4.5), (64, 4.875), (66, 5.25), (64, 5.625)   # Return and finish
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.625), (38, 3.0), (42, 3.0),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.875), (38, 5.25), (42, 5.25)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

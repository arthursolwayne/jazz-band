
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

# Bars 2-4 (1.5 - 6.0s)
# Sax: Motif in F major, with chromatic approach
sax_notes = [
    (60, 1.5), (62, 1.875), (60, 2.25), (62, 2.625),
    (64, 3.0), (62, 3.375), (60, 3.75), (62, 4.125),
    (64, 4.5), (65, 4.875), (64, 5.25), (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bass: Walking line, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.875), (50, 2.25), (51, 2.625),
    (52, 3.0), (51, 3.375), (50, 3.75), (49, 4.125),
    (48, 4.5), (47, 4.875), (48, 5.25), (49, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.875), (67, 1.875), (69, 1.875), (71, 1.875),  # D7
    (64, 3.375), (67, 3.375), (69, 3.375), (71, 3.375),  # D7
    (65, 4.875), (68, 4.875), (70, 4.875), (72, 4.875)   # E7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums: Full bar
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875), (42, 2.25),
    (36, 2.625), (38, 3.0), (42, 3.0), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125), (42, 4.5),
    (36, 4.875), (38, 5.25), (42, 5.25), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

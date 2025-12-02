
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
    (36, 1.125), (38, 1.5), (42, 1.5),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.375), (38, 3.75), (42, 3.75)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    (45, 2.75), (46, 3.125), (44, 3.5), (43, 3.875),
    (45, 4.25), (46, 4.625), (44, 5.0), (43, 5.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (59, 2.0), (61, 2.0), (62, 2.0), (64, 2.0),  # F7
    (57, 3.0), (59, 3.0), (60, 3.0), (62, 3.0),  # D7
    (59, 4.0), (61, 4.0), (62, 4.0), (64, 4.0)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.5), (65, 2.0, 0.5), (62, 2.5, 0.5),  # Motif
    (62, 3.0, 0.25), (65, 3.25, 0.25), (62, 3.5, 0.25),  # Repeat motif
    (67, 4.0, 0.5), (65, 4.5, 0.5), (62, 5.0, 0.5)   # Resolution
]
for note, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

midi.instruments.extend([sax, bass, piano, drums])

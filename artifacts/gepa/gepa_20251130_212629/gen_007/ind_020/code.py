
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (44, 1.5), (46, 1.875), (45, 2.25), (43, 2.625),
    (44, 2.75), (46, 3.125), (45, 3.5), (43, 3.875),
    (44, 4.0), (46, 4.375), (45, 4.75), (43, 5.125),
    (44, 5.25), (46, 5.625), (45, 6.0), (43, 6.375)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (42, 2.0), (45, 2.0), (48, 2.0), (50, 2.0),  # F7
    (47, 2.375), (50, 2.375), (53, 2.375), (55, 2.375),  # Bb7
    # Bar 3
    (42, 3.0), (45, 3.0), (48, 3.0), (50, 3.0),  # F7
    (47, 3.375), (50, 3.375), (53, 3.375), (55, 3.375),  # Bb7
    # Bar 4
    (42, 4.0), (45, 4.0), (48, 4.0), (50, 4.0),  # F7
    (47, 4.375), (50, 4.375), (53, 4.375), (55, 4.375)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax: Motif in Fm, one short phrase, leave it hanging
sax_notes = [
    (44, 1.5), (46, 1.75), (45, 2.0), (43, 2.25),
    (44, 2.5), (46, 2.75), (45, 3.0), (42, 3.25),
    (44, 3.5), (46, 3.75), (45, 4.0), (42, 4.25),
    (44, 4.5), (46, 4.75), (45, 5.0), (43, 5.25),
    (44, 5.5), (46, 5.75), (45, 6.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.125))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    # Bar 3
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    # Bar 4
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

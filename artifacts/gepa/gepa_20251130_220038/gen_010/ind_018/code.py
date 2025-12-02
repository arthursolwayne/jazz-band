
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

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (47, 2.625),
    (48, 3.0), (49, 3.375), (47, 3.75), (50, 4.125),
    (51, 4.5), (52, 4.875), (50, 5.25), (53, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (57, 1.5), (60, 1.5), (62, 1.5), (64, 1.5),  # F7
    (59, 2.0), (62, 2.0), (64, 2.0), (66, 2.0),  # Bb7
    # Bar 3 (3.0 - 4.5s)
    (57, 3.0), (60, 3.0), (62, 3.0), (64, 3.0),  # F7
    (59, 3.5), (62, 3.5), (64, 3.5), (66, 3.5),  # Bb7
    # Bar 4 (4.5 - 6.0s)
    (57, 4.5), (60, 4.5), (62, 4.5), (64, 4.5),  # F7
    (59, 5.0), (62, 5.0), (64, 5.0), (66, 5.0)   # Bb7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Drums: Bars 2-4 (1.5 - 6.0s)
for bar in [2, 3, 4]:
    start_time = (bar - 1) * 1.5
    drum_notes = [
        (36, start_time), (38, start_time + 0.375), (42, start_time + 0.375),
        (36, start_time + 1.125), (38, start_time + 1.5), (42, start_time + 1.5)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Melody in F, short motif, leave it hanging
sax_notes = [
    (65, 1.5),    # F
    (67, 1.875),  # G
    (64, 2.25),   # E
    (66, 2.625),  # F#
    (65, 3.0),    # F
    (67, 3.375),  # G
    (64, 3.75),   # E
    (66, 4.125),  # F#
    (65, 4.5),    # F
    (67, 4.875),  # G
    (64, 5.25),   # E
    (66, 5.625)   # F#
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

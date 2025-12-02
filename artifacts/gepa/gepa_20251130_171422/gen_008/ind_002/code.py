
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

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    (65, 1.5), (66, 1.875), (67, 2.25), (69, 2.625),
    (67, 3.0), (65, 3.375), (63, 3.75), (62, 4.125),
    (60, 4.5), (61, 4.875), (63, 5.25), (64, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4, comp on bars 2-4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5), (67, 1.5), (72, 1.5), (74, 1.5),  # D7
    (60, 2.25), (65, 2.25), (70, 2.25), (72, 2.25),  # Bm7
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0), (67, 3.0), (72, 3.0), (74, 3.0),  # D7
    (64, 3.75), (69, 3.75), (74, 3.75), (76, 3.75),  # F#m7
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5), (67, 4.5), (72, 4.5), (74, 4.5),  # D7
    (60, 5.25), (65, 5.25), (70, 5.25), (72, 5.25)   # Bm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Drums: Bars 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 1.125),
        (36, start + 1.5), (38, start + 1.875), (42, start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Melody in bars 2-4
# Motif: D -> F# -> B -> D (1.5s)
sax_notes = [
    (62, 1.5), (67, 1.875), (72, 2.25), (62, 2.625),  # D -> F# -> B -> D
    (62, 3.0), (65, 3.375), (68, 3.75), (72, 4.125),  # D -> E -> F# -> B
    (62, 4.5), (67, 4.875), (72, 5.25), (62, 5.625)   # D -> F# -> B -> D
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_moment.mid")

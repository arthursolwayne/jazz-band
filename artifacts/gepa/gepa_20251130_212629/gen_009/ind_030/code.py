
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
    (39, 1.5), (40, 1.875), (41, 2.25), (42, 2.625),
    (39, 3.0), (40, 3.375), (41, 3.75), (42, 4.125),
    (39, 4.5), (40, 4.875), (41, 5.25), (42, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (57, 1.5), (60, 1.5), (62, 1.5), (64, 1.5),  # F7
    (57, 2.0), (60, 2.0), (62, 2.0), (64, 2.0),  # F7
    # Bar 3
    (57, 3.0), (60, 3.0), (62, 3.0), (64, 3.0),  # F7
    (57, 3.5), (60, 3.5), (62, 3.5), (64, 3.5),  # F7
    # Bar 4
    (57, 4.5), (60, 4.5), (62, 4.5), (64, 4.5),  # F7
    (57, 5.0), (60, 5.0), (62, 5.0), (64, 5.0)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 1.125),
        (36, start + 1.5), (38, start + 1.875), (42, start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F - Ab - Bb - C (Fm triad + chromatic approach)
sax_notes = [
    (53, 1.5), (55, 1.875), (57, 2.25), (59, 2.625),  # Start of motif
    (53, 3.0), (55, 3.375), (57, 3.75), (59, 4.125),  # Repeat motif
    (53, 4.5), (55, 4.875), (57, 5.25), (59, 5.625)   # Finish motif
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")

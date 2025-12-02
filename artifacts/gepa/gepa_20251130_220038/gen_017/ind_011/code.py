
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

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5), (64, 1.875), (63, 2.25), (60, 2.625),
    (62, 3.0), (64, 3.375), (63, 3.75), (60, 4.125),
    (62, 4.5), (64, 4.875), (63, 5.25), (60, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.875), (69, 1.875), (71, 1.875), (74, 1.875),
    # Bar 3
    (67, 3.375), (69, 3.375), (71, 3.375), (74, 3.375),
    # Bar 4
    (67, 4.875), (69, 4.875), (71, 4.875), (74, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing
# Start on D, then Bb, then G, then F# (half step resolution)
sax_notes = [
    (62, 1.5), (60, 1.75), (67, 2.0), (66, 2.25),
    (62, 3.0), (60, 3.25), (67, 3.5), (66, 3.75),
    (62, 4.5), (60, 4.75), (67, 5.0), (66, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums: continue kick, snare, hihat
for bar in range(2, 4):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 1.125),
        (36, start + 1.5), (38, start + 1.875), (42, start + 1.875)
    ]
    for note, time in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_moment.mid')


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
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (36, 0.75), (38, 0.875), (42, 0.75), (42, 0.875), (42, 1.0), (42, 1.125),
    (42, 1.25), (42, 1.375), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5), (40, 1.875), (39, 2.25), (41, 2.625),
    (42, 3.0), (43, 3.375), (42, 3.75), (40, 4.125),
    (41, 4.5), (42, 4.875), (43, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2
    (57, 1.5), (60, 1.5), (62, 1.5), (64, 1.5),  # Fm7
    (60, 1.875), (62, 1.875), (64, 1.875), (67, 1.875),  # C7
    # Bar 3
    (57, 3.0), (60, 3.0), (62, 3.0), (64, 3.0),  # Fm7
    (62, 3.375), (64, 3.375), (67, 3.375), (69, 3.375),  # E7
    # Bar 4
    (57, 4.5), (60, 4.5), (62, 4.5), (64, 4.5),  # Fm7
    (64, 4.875), (67, 4.875), (69, 4.875), (71, 4.875)   # G7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Sax: Motif in Fm, one short phrase, leave it hanging
sax_notes = [
    (57, 1.5), (60, 1.875), (62, 2.25), (64, 2.625),
    (62, 3.0), (60, 3.375), (57, 3.75), (57, 4.125),
    (57, 4.5), (60, 4.875)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

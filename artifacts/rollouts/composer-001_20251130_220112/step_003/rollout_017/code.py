
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (36, 1.5), (37, 1.875), (35, 2.25), (36, 2.625),
    (37, 3.0), (38, 3.375), (36, 3.75), (35, 4.125),
    (34, 4.5), (35, 4.875), (33, 5.25), (34, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    (59, 1.5), (60, 1.5), (62, 1.5), (64, 1.5),  # F7
    # Bar 3 (2.625 - 3.375)
    (62, 2.625), (64, 2.625), (66, 2.625), (68, 2.625),  # Ab7
    # Bar 4 (3.75 - 4.5)
    (65, 3.75), (67, 3.75), (69, 3.75), (71, 3.75),  # C7
    # Bar 4 (4.875 - 5.625)
    (66, 4.875), (68, 4.875), (70, 4.875), (72, 4.875)   # Db7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625),
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: Fm7 -> Gb -> Ab -> Bb -> Fm7
sax_notes = [
    (59, 1.5), (60, 1.875), (62, 2.25), (64, 2.625),  # Fm7
    (61, 3.0), (63, 3.375), (65, 3.75), (67, 4.125),  # Gb -> Ab -> Bb -> Fm7
    (59, 4.5), (60, 4.875), (62, 5.25), (64, 5.625)   # Reprise Fm7
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('fm_intro.mid')

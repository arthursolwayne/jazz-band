
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    # Bar 2
    (45, 1.5), (46, 1.875), (44, 2.25), (43, 2.625),
    # Bar 3
    (42, 3.0), (43, 3.375), (44, 3.75), (45, 4.125),
    # Bar 4
    (46, 4.5), (47, 4.875), (45, 5.25), (44, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (57, 1.5), (60, 1.5), (62, 1.5), (64, 1.5),  # F7
    # Bar 3
    (57, 3.0), (60, 3.0), (62, 3.0), (64, 3.0),  # F7
    # Bar 4
    (57, 4.5), (60, 4.5), (62, 4.5), (64, 4.5)   # F7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (65), Ab (67), Bb (62), G (67) — Motif: F Ab Bb G
# Play on beat 1, leave it open, return on beat 4
sax_notes = [
    (65, 1.5), (67, 1.875), (62, 2.25), (67, 2.625),
    (65, 4.5), (67, 4.875), (62, 5.25), (67, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

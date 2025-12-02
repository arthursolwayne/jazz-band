
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches, no same note twice
bass_notes = [
    (43, 1.5, 0.375), (44, 1.875, 0.375), (42, 2.25, 0.375), (40, 2.625, 0.375),
    (41, 3.0, 0.375), (43, 3.375, 0.375), (44, 3.75, 0.375), (42, 4.125, 0.375),
    (40, 4.5, 0.375), (41, 4.875, 0.375), (43, 5.25, 0.375), (44, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (53, 2.25, 0.375), (50, 2.25, 0.375), (57, 2.25, 0.375), (60, 2.25, 0.375),
    # Bar 3: Fm7 on beat 2
    (53, 3.75, 0.375), (50, 3.75, 0.375), (57, 3.75, 0.375), (60, 3.75, 0.375),
    # Bar 4: Fm7 on beat 2
    (53, 5.25, 0.375), (50, 5.25, 0.375), (57, 5.25, 0.375), (60, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (62, 2.25, 0.375),  # Start the motif
    (60, 2.625, 0.375), (62, 3.0, 0.375), (65, 3.375, 0.375),  # Continue, leave it hanging
    (62, 4.5, 0.375), (60, 4.875, 0.375), (62, 5.25, 0.375)    # Come back and finish it
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")

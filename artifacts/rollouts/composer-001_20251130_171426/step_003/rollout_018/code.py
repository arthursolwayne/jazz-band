
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.125),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.125)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm, chromatic approaches
bass_notes = [
    (64, 1.5, 0.375), (65, 1.875, 0.375), (63, 2.25, 0.375), (61, 2.625, 0.375),  # Fm -> Bb -> Eb -> Ab
    (64, 3.0, 0.375), (65, 3.375, 0.375), (63, 3.75, 0.375), (61, 4.125, 0.375),
    (64, 4.5, 0.375), (65, 4.875, 0.375), (63, 5.25, 0.375), (61, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane: 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, C), Bb7 (Bb, D, F, Ab)
piano_notes = [
    (53, 2.25, 0.125), (60, 2.25, 0.125), (58, 2.25, 0.125), (57, 2.25, 0.125),  # Fm7 on 2
    (58, 3.0, 0.125), (65, 3.0, 0.125), (62, 3.0, 0.125), (60, 3.0, 0.125),     # Bb7 on 4
    (53, 4.5, 0.125), (60, 4.5, 0.125), (58, 4.5, 0.125), (57, 4.5, 0.125),     # Fm7 on 2
    (58, 5.25, 0.125), (65, 5.25, 0.125), (62, 5.25, 0.125), (60, 5.25, 0.125)   # Bb7 on 4
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Dante: Tenor sax motif
# Fm -> G -> Ab -> Bb -> Fm (hanging on Ab)
# Bar 2 (1.5 - 2.25s): F (65), G (67), Ab (68)
# Bar 3 (2.25 - 3.0s): Bb (62), F (65), Ab (68)
# Bar 4 (3.0 - 3.75s): Bb (62), F (65), Ab (68)
# Bar 4 (3.75 - 4.5s): F (65), rest
sax_notes = [
    (65, 1.5, 0.25), (67, 1.75, 0.25), (68, 2.0, 0.25),  # F -> G -> Ab
    (62, 2.25, 0.25), (65, 2.5, 0.25), (68, 2.75, 0.25),  # Bb -> F -> Ab
    (62, 3.0, 0.25), (65, 3.25, 0.25), (68, 3.5, 0.25),   # Bb -> F -> Ab
    (65, 3.75, 0.25)                                     # F, hanging on Ab
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")

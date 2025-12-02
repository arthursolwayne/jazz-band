
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.0, 0.125), (42, 0.125, 0.125),
    (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125),
    (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (F, G, Ab, A, Bb, B, C, D), chromatic approach
bass_notes = [
    (65, 1.5, 0.375),  # F
    (67, 1.875, 0.375), # G
    (68, 2.25, 0.375),  # Ab
    (69, 2.625, 0.375), # A
    (67, 2.875, 0.375), # Bb (chromatic approach)
    (69, 3.25, 0.375),  # B
    (71, 3.625, 0.375), # C
    (72, 4.0, 0.375),   # D
    (71, 4.375, 0.375), # Eb (chromatic approach)
    (72, 4.75, 0.375),  # E
    (69, 5.125, 0.375), # F
    (67, 5.5, 0.375),   # G
    (65, 5.875, 0.375)  # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7: D, F, A, C
# Gm7: G, Bb, D, F
# Cm7: C, Eb, G, Bb
# Fm7: F, Ab, C, Eb
piano_notes = [
    # Bar 2
    (52, 1.5, 0.375), (55, 1.5, 0.375), (57, 1.5, 0.375), (60, 1.5, 0.375),  # Dm7
    (55, 2.25, 0.375), (57, 2.25, 0.375), (60, 2.25, 0.375), (62, 2.25, 0.375),  # Gm7
    # Bar 3
    (60, 3.0, 0.375), (63, 3.0, 0.375), (65, 3.0, 0.375), (67, 3.0, 0.375),  # Cm7
    (52, 3.75, 0.375), (55, 3.75, 0.375), (57, 3.75, 0.375), (60, 3.75, 0.375),  # Dm7
    # Bar 4
    (55, 4.5, 0.375), (57, 4.5, 0.375), (60, 4.5, 0.375), (62, 4.5, 0.375),  # Gm7
    (60, 5.25, 0.375), (63, 5.25, 0.375), (65, 5.25, 0.375), (67, 5.25, 0.375)  # Cm7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: G, A, Bb, G (Dm scale: F, G, A, Bb, C, D, Eb)
sax_notes = [
    (67, 1.5, 0.375),  # G
    (69, 1.875, 0.375), # A
    (67, 2.25, 0.375),  # Bb
    (67, 2.625, 0.375), # G
    (67, 3.0, 0.375),   # G
    (69, 3.375, 0.375), # A
    (67, 3.75, 0.375),  # Bb
    (67, 4.125, 0.375), # G
    (67, 4.5, 0.375),   # G
    (69, 4.875, 0.375), # A
    (67, 5.25, 0.375),  # Bb
    (67, 5.625, 0.375)  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

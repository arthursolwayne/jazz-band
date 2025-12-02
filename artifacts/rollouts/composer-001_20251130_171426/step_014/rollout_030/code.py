
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
    (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (65, 1.5, 0.375), (66, 1.875, 0.375), (64, 2.25, 0.375), (63, 2.625, 0.375),
    (65, 3.0, 0.375), (66, 3.375, 0.375), (64, 3.75, 0.375), (63, 4.125, 0.375),
    (65, 4.5, 0.375), (66, 4.875, 0.375), (64, 5.25, 0.375), (63, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), (64, 1.875, 0.375), (67, 1.875, 0.375), (71, 1.875, 0.375),
    # Bar 3
    (62, 3.375, 0.375), (64, 3.375, 0.375), (67, 3.375, 0.375), (71, 3.375, 0.375),
    # Bar 4
    (62, 4.875, 0.375), (64, 4.875, 0.375), (67, 4.875, 0.375), (71, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    drum_notes = [
        (36, bar_start + 0.0, 0.375), (38, bar_start + 0.375, 0.375), (42, bar_start + 0.0, 0.1875),
        (36, bar_start + 0.75, 0.375), (38, bar_start + 1.125, 0.375), (42, bar_start + 0.75, 0.1875),
        (42, bar_start + 1.5, 0.1875)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), A (68), B (70), F (65) — leave B hanging, come back with F
sax_notes = [
    (65, 1.5, 0.375), (68, 1.875, 0.375), (70, 2.25, 0.375),  # First phrase
    (65, 3.0, 0.375), (68, 3.375, 0.375), (70, 3.75, 0.375),  # Second phrase
    (65, 4.5, 0.375), (68, 4.875, 0.375), (70, 5.25, 0.375),  # Third phrase
    (65, 5.625, 0.375)  # Final note
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

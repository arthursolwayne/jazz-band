
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
    (36, 0.0, 0.375), (42, 0.0, 0.125), # Kick and hihat on 1
    (38, 0.375, 0.375), (42, 0.375, 0.125), # Snare and hihat on 2
    (36, 0.75, 0.375), (42, 0.75, 0.125), # Kick and hihat on 3
    (38, 1.125, 0.375), (42, 1.125, 0.125) # Snare and hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (61, 2.625, 0.375), # Bar 2: Dm7
    (62, 3.0, 0.375), (63, 3.375, 0.375), (60, 3.75, 0.375), (61, 4.125, 0.375), # Bar 3: Dm7
    (62, 4.5, 0.375), (63, 4.875, 0.375), (60, 5.25, 0.375), (61, 5.625, 0.375)  # Bar 4: Dm7
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.125), (67, 1.5, 0.125), (64, 1.5, 0.125), (69, 1.5, 0.125), # Dm7
    (62, 2.25, 0.125), (67, 2.25, 0.125), (64, 2.25, 0.125), (69, 2.25, 0.125), # Dm7
    # Bar 3
    (62, 3.0, 0.125), (67, 3.0, 0.125), (64, 3.0, 0.125), (69, 3.0, 0.125), # Dm7
    (62, 3.75, 0.125), (67, 3.75, 0.125), (64, 3.75, 0.125), (69, 3.75, 0.125), # Dm7
    # Bar 4
    (62, 4.5, 0.125), (67, 4.5, 0.125), (64, 4.5, 0.125), (69, 4.5, 0.125), # Dm7
    (62, 5.25, 0.125), (67, 5.25, 0.125), (64, 5.25, 0.125), (69, 5.25, 0.125)  # Dm7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62) -> F (65) -> Eb (63) -> D (62) -> F (65) -> G (67)
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (63, 2.25, 0.375), (62, 2.625, 0.375), # Bar 2
    (65, 3.0, 0.375), (67, 3.375, 0.375), (62, 3.75, 0.375), (65, 4.125, 0.375), # Bar 3
    (63, 4.5, 0.375), (62, 4.875, 0.375), (65, 5.25, 0.375), (67, 5.625, 0.375)  # Bar 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums continue in bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (42, 1.5, 0.125),
    (38, 1.875, 0.375), (42, 1.875, 0.125),
    (36, 2.25, 0.375), (42, 2.25, 0.125),
    (38, 2.625, 0.375), (42, 2.625, 0.125),
    # Bar 3
    (36, 3.0, 0.375), (42, 3.0, 0.125),
    (38, 3.375, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (42, 3.75, 0.125),
    (38, 4.125, 0.375), (42, 4.125, 0.125),
    # Bar 4
    (36, 4.5, 0.375), (42, 4.5, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125),
    (36, 5.25, 0.375), (42, 5.25, 0.125),
    (38, 5.625, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

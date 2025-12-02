
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Fm, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5, 0.375), (37, 1.875, 0.375), (35, 2.25, 0.375), (36, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (38, 3.0, 0.375), (39, 3.375, 0.375), (37, 3.75, 0.375), (38, 4.125, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (40, 4.5, 0.375), (41, 4.875, 0.375), (39, 5.25, 0.375), (40, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (40, 1.875, 0.375), (43, 1.875, 0.375), (44, 1.875, 0.375),
    (40, 2.625, 0.375), (43, 2.625, 0.375), (44, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (40, 3.375, 0.375), (43, 3.375, 0.375), (44, 3.375, 0.375),
    (40, 4.125, 0.375), (43, 4.125, 0.375), (44, 4.125, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (40, 4.875, 0.375), (43, 4.875, 0.375), (44, 4.875, 0.375),
    (40, 5.625, 0.375), (43, 5.625, 0.375), (44, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (56, 1.5, 0.375), (58, 1.875, 0.375), (57, 2.25, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (56, 3.0, 0.375), (58, 3.375, 0.375), (57, 3.75, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (56, 4.5, 0.375), (58, 4.875, 0.375), (57, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = (36, start, 0.375)
    kick2 = (36, start + 0.75, 0.375)
    # Snare on 2 and 4
    snare1 = (38, start + 0.375, 0.375)
    snare2 = (38, start + 1.125, 0.375)
    # Hihat on every eighth
    hihat1 = (42, start, 0.1875)
    hihat2 = (42, start + 0.1875, 0.1875)
    hihat3 = (42, start + 0.375, 0.1875)
    hihat4 = (42, start + 0.5625, 0.1875)
    hihat5 = (42, start + 0.75, 0.1875)
    hihat6 = (42, start + 0.9375, 0.1875)
    hihat7 = (42, start + 1.125, 0.1875)
    hihat8 = (42, start + 1.3125, 0.1875)
    # Add all the notes
    for note, start, duration in [kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')


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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.75),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.75),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    (43, 1.5, 0.375), (41, 1.875, 0.375), (43, 2.25, 0.375), (42, 2.625, 0.375),
    # Bar 3
    (44, 3.0, 0.375), (42, 3.375, 0.375), (44, 3.75, 0.375), (43, 4.125, 0.375),
    # Bar 4
    (43, 4.5, 0.375), (41, 4.875, 0.375), (43, 5.25, 0.375), (42, 5.625, 0.375),
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    (60, 1.5, 0.375), (64, 1.5, 0.375), (67, 1.5, 0.375), (70, 1.5, 0.375),
    # Bar 3: Gm7
    (62, 3.0, 0.375), (65, 3.0, 0.375), (67, 3.0, 0.375), (71, 3.0, 0.375),
    # Bar 4: C7
    (60, 4.5, 0.375), (64, 4.5, 0.375), (67, 4.5, 0.375), (71, 4.5, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (60) - G (62) - F (60) - D (62), then rest on the beat
sax_notes = [
    (60, 1.5, 0.375), (62, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    # Leave it hanging
    (60, 3.0, 0.375), (62, 3.375, 0.375),
    # Come back and finish it
    (60, 4.5, 0.375), (62, 4.875, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    (36, 0.75, 0.375), (38, 1.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    (42, 1.5, 0.375), (43, 1.875, 0.375), (44, 2.25, 0.375), (45, 2.625, 0.375),
    (41, 2.999, 0.375), (42, 3.375, 0.375), (43, 3.75, 0.375), (44, 4.125, 0.375),
    (45, 4.5, 0.375), (46, 4.875, 0.375), (47, 5.25, 0.375), (48, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (40, 1.5, 0.375), (43, 1.5, 0.375), (45, 1.5, 0.375), (47, 1.5, 0.375),
    (41, 1.875, 0.375), (44, 1.875, 0.375), (46, 1.875, 0.375), (48, 1.875, 0.375),
    # Bar 3
    (39, 2.25, 0.375), (42, 2.25, 0.375), (44, 2.25, 0.375), (46, 2.25, 0.375),
    (40, 2.625, 0.375), (43, 2.625, 0.375), (45, 2.625, 0.375), (47, 2.625, 0.375),
    # Bar 4
    (40, 3.0, 0.375), (43, 3.0, 0.375), (45, 3.0, 0.375), (47, 3.0, 0.375),
    (41, 3.375, 0.375), (44, 3.375, 0.375), (46, 3.375, 0.375), (48, 3.375, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kicks on 1 and 3, snares on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick1 = (36, bar_start + 0.0, 0.375)
    snare1 = (38, bar_start + 0.375, 0.375)
    kick2 = (36, bar_start + 0.75, 0.375)
    snare2 = (38, bar_start + 1.125, 0.375)
    for i in range(0, 4):
        hihat = (42, bar_start + i * 0.375, 0.375)
        drum_notes.append(hihat)
    drum_notes.extend([kick1, snare1, kick2, snare2])

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: short motif, starts on 1.5s, leaves it hanging, comes back to finish
sax_notes = [
    (42, 1.5, 0.375), (44, 1.875, 0.375), (45, 2.25, 0.375),
    (42, 2.625, 0.375), (44, 2.999, 0.375), (45, 3.375, 0.375),
    (47, 3.75, 0.375), (45, 4.125, 0.375), (43, 4.5, 0.375),
    (42, 4.875, 0.375), (44, 5.25, 0.375), (45, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_shorter.mid')

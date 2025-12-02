
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (30, 1.5, 0.375), (31, 1.875, 0.375), (32, 2.25, 0.375), (33, 2.625, 0.375),
    # Bar 3
    (34, 3.0, 0.375), (35, 3.375, 0.375), (36, 3.75, 0.375), (37, 4.125, 0.375),
    # Bar 4
    (38, 4.5, 0.375), (39, 4.875, 0.375), (40, 5.25, 0.375), (41, 5.625, 0.375),
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (43, 1.875, 0.375), (48, 1.875, 0.375), (50, 1.875, 0.375),
    (53, 1.875, 0.375),
    # Bar 3
    (43, 3.375, 0.375), (48, 3.375, 0.375), (50, 3.375, 0.375),
    (53, 3.375, 0.375),
    # Bar 4
    (43, 4.875, 0.375), (48, 4.875, 0.375), (50, 4.875, 0.375),
    (53, 4.875, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody in Fm (F, Ab, Bb, C, Eb)
sax_notes = [
    # Bar 2
    (61, 1.5, 0.375), (60, 1.875, 0.375), (58, 2.25, 0.375),
    # Bar 3
    (59, 3.0, 0.375), (60, 3.375, 0.375), (59, 3.75, 0.375),
    # Bar 4
    (61, 4.5, 0.375), (60, 4.875, 0.375), (58, 5.25, 0.375),
    (59, 5.625, 0.375),
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Fill in the drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875),
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (42, 4.5, 0.1875),
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")

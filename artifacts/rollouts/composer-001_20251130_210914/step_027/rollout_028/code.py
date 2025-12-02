
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
    
    # Bar 2
    (38, 1.875, 0.375), (36, 2.25, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875),
    
    # Bar 3
    (36, 3.375, 0.375), (38, 3.75, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875), (42, 4.5, 0.1875),
    
    # Bar 4
    (38, 4.875, 0.375), (36, 5.25, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Gb, Ab, Bb, C, Db, Eb, F)
# Chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5s)
    (64, 1.5, 0.375), (65, 1.875, 0.375), (66, 2.25, 0.375), (67, 2.625, 0.375),
    # Bar 3 (2.875s)
    (68, 2.875, 0.375), (69, 3.25, 0.375), (70, 3.625, 0.375), (71, 4.0, 0.375),
    # Bar 4 (4.375s)
    (72, 4.375, 0.375), (73, 4.75, 0.375), (74, 5.125, 0.375), (75, 5.5, 0.375)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    (43, 1.5, 0.375), (46, 1.5, 0.375), (48, 1.5, 0.375), (50, 1.5, 0.375),
    (51, 1.875, 0.375), (54, 1.875, 0.375), (56, 1.875, 0.375), (58, 1.875, 0.375),
    # Bar 3 (2.875s)
    (43, 2.875, 0.375), (46, 2.875, 0.375), (48, 2.875, 0.375), (50, 2.875, 0.375),
    (51, 3.25, 0.375), (54, 3.25, 0.375), (56, 3.25, 0.375), (58, 3.25, 0.375),
    # Bar 4 (4.375s)
    (43, 4.375, 0.375), (46, 4.375, 0.375), (48, 4.375, 0.375), (50, 4.375, 0.375),
    (51, 4.75, 0.375), (54, 4.75, 0.375), (56, 4.75, 0.375), (58, 4.75, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Fm motif: F, Ab, Bb, Eb (hanging on Eb)
sax_notes = [
    (65, 1.5, 0.375), (68, 1.875, 0.375), (67, 2.25, 0.375), (61, 2.625, 0.375),
    (65, 3.0, 0.375), (68, 3.375, 0.375), (67, 3.75, 0.375), (61, 4.125, 0.375),
    (65, 4.5, 0.375), (68, 4.875, 0.375), (67, 5.25, 0.375), (61, 5.625, 0.375)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

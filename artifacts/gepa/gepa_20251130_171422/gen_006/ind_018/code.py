
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
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (36, 1.125, 0.375),
    (38, 1.5, 0.375), (42, 1.5, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (52, 1.5, 0.375), (53, 1.875, 0.375), (51, 2.25, 0.375), (52, 2.625, 0.375),
    # Bar 3
    (54, 3.0, 0.375), (53, 3.375, 0.375), (52, 3.75, 0.375), (51, 4.125, 0.375),
    # Bar 4
    (50, 4.5, 0.375), (51, 4.875, 0.375), (52, 5.25, 0.375), (53, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375),
    # Bar 3
    (62, 3.375, 0.375), (64, 3.375, 0.375), (67, 3.375, 0.375), (69, 3.375, 0.375),
    # Bar 4
    (62, 4.875, 0.375), (64, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: motif in F, one short phrase, sing it, leave it hanging
sax_notes = [
    (66, 1.5, 0.375), (68, 1.875, 0.375), (67, 2.25, 0.375), (66, 2.625, 0.375),
    (64, 3.0, 0.375), (66, 3.375, 0.375), (68, 3.75, 0.375), (67, 4.125, 0.375),
    (66, 4.5, 0.375), (68, 4.875, 0.375), (67, 5.25, 0.375), (66, 5.625, 0.375)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 (start) and 3 (start + 0.75)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 (start + 0.375) and 4 (start + 1.125)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

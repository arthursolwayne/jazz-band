
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &2
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &3
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &4
    (36, 1.5, 0.375)    # Kick on 3
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375), # F
    (67, 3.0, 0.375),   # G
    (69, 3.375, 0.375), # A
    (70, 3.75, 0.375),  # Bb
    (71, 4.125, 0.375), # B
    (72, 4.5, 0.375),   # C
    (73, 4.875, 0.375), # C#
    (74, 5.25, 0.375),  # D
    (76, 5.625, 0.375)  # E
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 2.25, 0.375),  # G7 (G, B, D, F)
    (67, 2.25, 0.375),
    (72, 2.25, 0.375),
    (69, 2.25, 0.375),
    (67, 3.75, 0.375),  # G7 on 4
    (67, 3.75, 0.375),
    (72, 3.75, 0.375),
    (69, 3.75, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing
# D, Eb, E, G (Dorian flavor)
sax_notes = [
    (62, 1.5, 0.25),   # D
    (63, 1.75, 0.25),  # Eb
    (64, 2.0, 0.25),   # E
    (67, 2.25, 0.25),  # G
    (62, 2.5, 0.25),   # D
    (63, 2.75, 0.25),  # Eb
    (64, 3.0, 0.25),   # E
    (67, 3.25, 0.25),  # G
    (62, 3.5, 0.25),   # D
    (63, 3.75, 0.25),  # Eb
    (64, 4.0, 0.25),   # E
    (67, 4.25, 0.25)   # G
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

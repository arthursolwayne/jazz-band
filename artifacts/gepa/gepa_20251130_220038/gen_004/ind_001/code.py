
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
    # Bar 1 (0.0 - 1.5s)
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),    # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 3 & 4
    (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: motif starts here, Dm7 -> F7 -> Bb7 -> C7 (motif)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375),  # F
    (60, 2.25, 0.375),  # Bb
    (64, 2.625, 0.375),  # C
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in Dm (root, 7, b3, 5)
bass_notes = [
    (62, 1.5, 0.375),  # D
    (60, 1.875, 0.375),  # Bb
    (64, 2.25, 0.375),  # C
    (67, 2.625, 0.375),  # Eb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7, G7, C7)
piano_notes = [
    # Dm7 (1.875)
    (62, 1.875, 0.375),  # D
    (67, 1.875, 0.375),  # Eb
    (67, 1.875, 0.375),  # Eb (duplicate for 7th)
    (64, 1.875, 0.375),  # F (not in Dm7, but in G7)
    (74, 2.625, 0.375),  # C
    (77, 2.625, 0.375),  # E
    (76, 2.625, 0.375),  # Eb
    (72, 2.625, 0.375),  # G
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: motif repeats but ends on G
sax_notes = [
    (62, 3.0, 0.375),  # D
    (65, 3.375, 0.375),  # F
    (60, 3.75, 0.375),  # Bb
    (67, 4.125, 0.375),  # G
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in Dm
bass_notes = [
    (62, 3.0, 0.375),  # D
    (60, 3.375, 0.375),  # Bb
    (64, 3.75, 0.375),  # C
    (67, 4.125, 0.375),  # Eb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    # Dm7 (3.375)
    (62, 3.375, 0.375),  # D
    (67, 3.375, 0.375),  # Eb
    (67, 3.375, 0.375),  # Eb
    (64, 3.375, 0.375),  # F
    (74, 4.125, 0.375),  # C
    (77, 4.125, 0.375),  # E
    (76, 4.125, 0.375),  # Eb
    (72, 4.125, 0.375),  # G
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: motif ends with a chromatic approach to Bb
sax_notes = [
    (62, 4.5, 0.375),  # D
    (65, 4.875, 0.375),  # F
    (60, 5.25, 0.375),  # Bb
    (59, 5.625, 0.375),  # A (chromatic approach)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in Dm
bass_notes = [
    (62, 4.5, 0.375),  # D
    (60, 4.875, 0.375),  # Bb
    (64, 5.25, 0.375),  # C
    (67, 5.625, 0.375),  # Eb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7)
piano_notes = [
    # Dm7 (4.875)
    (62, 4.875, 0.375),  # D
    (67, 4.875, 0.375),  # Eb
    (67, 4.875, 0.375),  # Eb
    (64, 4.875, 0.375),  # F
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = (36, bar_start, 0.375)
    kick2 = (36, bar_start + 1.125, 0.375)
    # Snare on 2 and 4
    snare1 = (38, bar_start + 0.375, 0.375)
    snare2 = (38, bar_start + 1.5, 0.375)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = (42, bar_start + (i * 0.1875), 0.1875)
        drum_notes.append(hihat)

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

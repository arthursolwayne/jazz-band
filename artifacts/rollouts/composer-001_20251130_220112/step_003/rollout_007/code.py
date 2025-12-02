
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
    # Bar 1 (0.0 to 1.5s)
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &1
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &2
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &3
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.1875),  # Hihat on 3
    (42, 1.3125, 0.1875),  # Hihat on &3
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.5, 0.1875),  # Hihat on 4
    (42, 1.6875, 0.1875),  # Hihat on &4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Dm (D F A C)
bass_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (67, 2.25, 0.375),  # A
    (69, 2.625, 0.375),  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7 on 2, Gm7 on 4)
piano_notes = [
    # Dm7 on 2 (1.875)
    (62, 1.875, 0.375),  # D
    (67, 1.875, 0.375),  # A
    (69, 1.875, 0.375),  # C
    (72, 1.875, 0.375),  # F
    # Gm7 on 4 (2.625)
    (67, 2.625, 0.375),  # G
    (72, 2.625, 0.375),  # Bb
    (74, 2.625, 0.375),  # D
    (76, 2.625, 0.375),  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - short phrase, singable, leaves it hanging
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375),  # F
    (67, 2.25, 0.375),  # A
    (65, 2.625, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D F A C)
bass_notes = [
    (62, 3.0, 0.375),  # D
    (64, 3.375, 0.375),  # F
    (67, 3.75, 0.375),  # A
    (69, 4.125, 0.375),  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7 on 2, Gm7 on 4)
piano_notes = [
    # Dm7 on 2 (3.375)
    (62, 3.375, 0.375),  # D
    (67, 3.375, 0.375),  # A
    (69, 3.375, 0.375),  # C
    (72, 3.375, 0.375),  # F
    # Gm7 on 4 (4.125)
    (67, 4.125, 0.375),  # G
    (72, 4.125, 0.375),  # Bb
    (74, 4.125, 0.375),  # D
    (76, 4.125, 0.375),  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif (repeat with a slight variation)
sax_notes = [
    (62, 3.0, 0.375),  # D
    (65, 3.375, 0.375),  # F
    (67, 3.75, 0.375),  # A
    (65, 4.125, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D F A C)
bass_notes = [
    (62, 4.5, 0.375),  # D
    (64, 4.875, 0.375),  # F
    (67, 5.25, 0.375),  # A
    (69, 5.625, 0.375),  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7 on 2, Gm7 on 4)
piano_notes = [
    # Dm7 on 2 (4.875)
    (62, 4.875, 0.375),  # D
    (67, 4.875, 0.375),  # A
    (69, 4.875, 0.375),  # C
    (72, 4.875, 0.375),  # F
    # Gm7 on 4 (5.625)
    (67, 5.625, 0.375),  # G
    (72, 5.625, 0.375),  # Bb
    (74, 5.625, 0.375),  # D
    (76, 5.625, 0.375),  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif (finish the phrase)
sax_notes = [
    (62, 4.5, 0.375),  # D
    (65, 4.875, 0.375),  # F
    (67, 5.25, 0.375),  # A
    (65, 5.625, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 to 3.0s)
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.5, 0.1875),  # Hihat on 1
    (42, 1.6875, 0.1875),  # Hihat on &1
    (42, 1.875, 0.1875),  # Hihat on 2
    (42, 2.0625, 0.1875),  # Hihat on &2
    (42, 2.25, 0.1875),  # Hihat on 3
    (42, 2.4375, 0.1875),  # Hihat on &3
    (36, 2.625, 0.375),  # Kick on 3
    (42, 2.625, 0.1875),  # Hihat on 3
    (42, 2.8125, 0.1875),  # Hihat on &3
    (38, 3.0, 0.375),  # Snare on 4
    (42, 3.0, 0.1875),  # Hihat on 4
    (42, 3.1875, 0.1875),  # Hihat on &4
    # Bar 3 (3.0 to 4.5s)
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875),  # Hihat on &1
    (42, 3.375, 0.1875),  # Hihat on 2
    (42, 3.5625, 0.1875),  # Hihat on &2
    (42, 3.75, 0.1875),  # Hihat on 3
    (42, 3.9375, 0.1875),  # Hihat on &3
    (36, 4.125, 0.375),  # Kick on 3
    (42, 4.125, 0.1875),  # Hihat on 3
    (42, 4.3125, 0.1875),  # Hihat on &3
    (38, 4.5, 0.375),  # Snare on 4
    (42, 4.5, 0.1875),  # Hihat on 4
    (42, 4.6875, 0.1875),  # Hihat on &4
    # Bar 4 (4.5 to 6.0s)
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),  # Hihat on &1
    (42, 4.875, 0.1875),  # Hihat on 2
    (42, 5.0625, 0.1875),  # Hihat on &2
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),  # Hihat on &3
    (36, 5.625, 0.375),  # Kick on 3
    (42, 5.625, 0.1875),  # Hihat on 3
    (42, 5.8125, 0.1875),  # Hihat on &3
    (38, 6.0, 0.375),  # Snare on 4
    (42, 6.0, 0.1875),  # Hihat on 4
    (42, 6.1875, 0.1875),  # Hihat on &4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

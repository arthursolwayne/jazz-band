
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
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    (52, 1.5, 0.375),     # F
    (50, 1.875, 0.375),   # Eb
    (49, 2.25, 0.375),    # D
    (52, 2.625, 0.375)    # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    (52, 1.5, 0.1875),    # F
    (60, 1.5, 0.1875),    # A
    (59, 1.5, 0.1875),    # G
    (50, 1.5, 0.1875),    # Eb

    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 2.25, 0.1875),   # Bb
    (62, 2.25, 0.1875),   # D
    (52, 2.25, 0.1875),   # F
    (55, 2.25, 0.1875),   # Ab

    # Bar 4: F7 again
    (52, 3.0, 0.1875),    # F
    (60, 3.0, 0.1875),    # A
    (59, 3.0, 0.1875),    # G
    (50, 3.0, 0.1875)     # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm
# Start with a short phrase: F, Ab, Bb, F
sax_notes = [
    (52, 1.5, 0.1875),    # F
    (55, 1.6875, 0.1875), # Ab
    (58, 1.875, 0.1875),  # Bb
    (52, 2.0625, 0.1875)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    (50, 3.0, 0.375),     # Eb
    (49, 3.375, 0.375),   # D
    (52, 3.75, 0.375),    # F
    (55, 4.125, 0.375)    # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (58, 3.0, 0.1875),    # Bb
    (62, 3.0, 0.1875),    # D
    (52, 3.0, 0.1875),    # F
    (55, 3.0, 0.1875),    # Ab

    # Bar 4: Cm7 (C, Eb, G, Bb)
    (59, 3.75, 0.1875),   # C
    (50, 3.75, 0.1875),   # Eb
    (52, 3.75, 0.1875),   # G
    (58, 3.75, 0.1875)    # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Continue motif, leave it hanging
sax_notes = [
    (52, 3.0, 0.1875),    # F
    (55, 3.1875, 0.1875), # Ab
    (58, 3.375, 0.1875),  # Bb
    (52, 3.5625, 0.1875)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    (55, 4.5, 0.375),     # G
    (52, 4.875, 0.375),   # F
    (50, 5.25, 0.375),    # Eb
    (49, 5.625, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 again
    (52, 4.5, 0.1875),    # F
    (60, 4.5, 0.1875),    # A
    (59, 4.5, 0.1875),    # G
    (50, 4.5, 0.1875)     # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif, resolve
sax_notes = [
    (52, 4.5, 0.1875),    # F
    (55, 4.6875, 0.1875), # Ab
    (58, 4.875, 0.1875),  # Bb
    (52, 5.0625, 0.1875)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.1875),    # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.1875),  # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.1875),   # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.1875)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

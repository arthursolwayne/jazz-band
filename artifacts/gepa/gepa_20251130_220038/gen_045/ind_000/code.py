
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Fm walking bass line
bass_notes = [35, 33, 31, 29, 28, 27, 25, 24, 22, 20, 19, 17, 16, 15, 13, 12]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane: F7 chords on 2 and 4
# F7 = F, A, C, Eb
# Comp on 2 and 4 (beat 2 and 4 of bar 2)
# Bar 2: 2 = 2.25s, 4 = 3.0s
piano_notes = [
    # Beat 2 (2.25s)
    (2.25, 77),  # F
    (2.25, 82),  # A
    (2.25, 79),  # C
    (2.25, 74),  # Eb
    # Beat 4 (3.0s)
    (3.0, 77),   # F
    (3.0, 82),   # A
    (3.0, 79),   # C
    (3.0, 74),   # Eb
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Dante: Melody in Fm
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 65),   # Ab
    (1.75, 64),  # G
    (2.0, 62),   # E
    (2.25, 65),  # Ab
    (2.5, 60),   # D
    (2.75, 62),  # E
    (3.0, 60),   # D
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Fm walking bass line (same pattern)
bass_notes = [35, 33, 31, 29, 28, 27, 25, 24, 22, 20, 19, 17, 16, 15, 13, 12]
for i, note in enumerate(bass_notes):
    start = 3.0 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane: F7 chords on 2 and 4
# Bar 3: 2 = 3.75s, 4 = 4.5s
piano_notes = [
    # Beat 2 (3.75s)
    (3.75, 77),  # F
    (3.75, 82),  # A
    (3.75, 79),  # C
    (3.75, 74),  # Eb
    # Beat 4 (4.5s)
    (4.5, 77),   # F
    (4.5, 82),   # A
    (4.5, 79),   # C
    (4.5, 74),   # Eb
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Dante: Melody continues
sax_notes = [
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62),   # E
    (3.25, 64),  # G
    (3.5, 67),   # Bb
    (3.75, 65),  # Ab
    (4.0, 60),   # D
    (4.25, 62),  # E
    (4.5, 64),   # G
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Fm walking bass line
bass_notes = [35, 33, 31, 29, 28, 27, 25, 24, 22, 20, 19, 17, 16, 15, 13, 12]
for i, note in enumerate(bass_notes):
    start = 4.5 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane: F7 chords on 2 and 4
# Bar 4: 2 = 5.25s, 4 = 6.0s
piano_notes = [
    # Beat 2 (5.25s)
    (5.25, 77),  # F
    (5.25, 82),  # A
    (5.25, 79),  # C
    (5.25, 74),  # Eb
    # Beat 4 (6.0s)
    (6.0, 77),   # F
    (6.0, 82),   # A
    (6.0, 79),   # C
    (6.0, 74),   # Eb
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Dante: Melody (final bar, resolves)
sax_notes = [
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62),   # E
    (4.75, 64),  # G
    (5.0, 67),   # Bb
    (5.25, 65),  # Ab
    (5.5, 60),   # D
    (5.75, 62),  # E
    (6.0, 62),   # E (rest on 6.0)
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Drums: same pattern for bar 3 and 4
for bar in [3.0, 4.5]:
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar + 0.0, end=bar + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar + 1.875, end=bar + 2.0))
    
    # Hi-hat on every eighth
    for i in range(0, 4):
        start = bar + (i * 0.375)
        end = start + 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

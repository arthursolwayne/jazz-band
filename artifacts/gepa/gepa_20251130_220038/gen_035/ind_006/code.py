
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

bar1_start = 0.0
bar1_end = 1.5

# Kick on beats 0 and 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 1.125))

# Snare on beats 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.5))

# Hihat on every eighth note
for i in range(0, 4):
    start = bar1_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (1.5, 60),  # D
    (1.875, 61), # Eb
    (2.25, 62),  # E
    (2.625, 63), # F
    (2.875, 62), # E
    (3.25, 61),  # Eb
    (3.625, 60), # D
    (4.0, 59),   # C
    (4.375, 60), # D
    (4.75, 61),  # Eb
    (5.125, 62), # E
    (5.5, 63),   # F
    (5.75, 62),  # E
    (6.0, 61)    # Eb
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (2.25, 62, 67, 70),  # E7 (Dmaj7) -> E, G#, B, D
    (3.625, 60, 65, 69), # D7 (D7) -> D, F#, A, C
    (4.75, 62, 67, 70),  # E7 (Dmaj7) -> E, G#, B, D
    (6.0, 60, 65, 69)    # D7 (D7) -> D, F#, A, C
]
for start, root, third, seventh in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=root, start=start, end=start + 0.375))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=third, start=start, end=start + 0.375))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=seventh, start=start, end=start + 0.375))

# Sax: One short motif, start it, leave it hanging, then finish it
# Motif: D, F#, B, D (Dmaj7) on 1, E, G#, B, E (Emaj7) on 2, D, F#, B on 3, D on 4

sax_notes = [
    (1.5, 62),  # D
    (1.875, 66), # F#
    (2.25, 67),  # B
    (2.625, 62), # D (end of first phrase)
    (2.875, 64), # E
    (3.25, 68),  # G#
    (3.625, 67), # B
    (4.0, 64),   # E (end of second phrase)
    (4.375, 62), # D
    (4.75, 66),  # F#
    (5.125, 67), # B
    (5.5, 62)    # D
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Drums: Continue in bars 2-4
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.375, end=bar2_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 0.75, end=bar2_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 1.125, end=bar2_start + 1.5))
for i in range(0, 4):
    start = bar2_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.375, end=bar3_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 0.75, end=bar3_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.125, end=bar3_start + 1.5))
for i in range(0, 4):
    start = bar3_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.375, end=bar4_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 0.75, end=bar4_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.125, end=bar4_start + 1.5))
for i in range(0, 4):
    start = bar4_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

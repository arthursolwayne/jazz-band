
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (21, 1.5, 0.375),  # Fm root (F)
    (20, 1.875, 0.375), # Eb
    (19, 2.25, 0.375),  # D
    (21, 2.625, 0.375), # F
    (22, 3.0, 0.375),   # G
    (21, 3.375, 0.375), # F
    (20, 3.75, 0.375),  # Eb
    (19, 4.125, 0.375), # D
    (21, 4.5, 0.375),   # F
    (22, 4.875, 0.375), # G
    (23, 5.25, 0.375),  # Ab
    (21, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (28, 1.875, 0.375), # Bb7 (Bb)
    (31, 1.875, 0.375), # D
    (33, 1.875, 0.375), # F
    (35, 1.875, 0.375), # Ab
    # Bar 3
    (28, 3.375, 0.375), # Bb7 (Bb)
    (31, 3.375, 0.375), # D
    (33, 3.375, 0.375), # F
    (35, 3.375, 0.375), # Ab
    # Bar 4
    (28, 4.875, 0.375), # Bb7 (Bb)
    (31, 4.875, 0.375), # D
    (33, 4.875, 0.375), # F
    (35, 4.875, 0.375)  # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Full bar with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.375, end=start_time + 0.75))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.1875))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.5625))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 0.9375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.3125))

# Sax: Melody (starting at 1.5s)
# Motif: F - G - Ab - F (half note, half note, half note, half note)
sax_notes = [
    (21, 1.5, 1.5),     # F (half note)
    (22, 3.0, 1.5),     # G (half note)
    (23, 4.5, 1.5),     # Ab (half note)
    (21, 6.0, 1.5)      # F (half note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

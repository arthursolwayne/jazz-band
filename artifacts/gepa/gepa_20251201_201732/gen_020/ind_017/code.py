
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start, end=bar1_start + 1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.5, end=bar1_start + 1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.75, end=bar1_start + 1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C, Bb, Eb, A, G
bass_notes = [
    (1.5, 43),   # F2
    (1.875, 41),  # Eb2
    (2.25, 50),   # D2
    (2.625, 48),  # C2
    (3.0, 46),    # Bb2
    (3.375, 44),  # Ab2
    (3.75, 53),   # A2
    (4.125, 51),  # G2
    (4.5, 43),    # F2
    (4.875, 41),  # Eb2
    (5.25, 50),   # D2
    (5.625, 48),  # C2
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875))

# Bar 3: Bb7 (Bb, D, F, Ab)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625))

# Bar 4: Eb7 (Eb, G, Bb, D)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it
# Motif: F, Ab, Bb, F (8th notes)
sax_notes = [
    (1.5, 64, 0.375),  # F4
    (1.875, 62, 0.375), # Ab4
    (2.25, 60, 0.375),  # Bb4
    (2.625, 64, 0.375), # F4
    (3.0, 64, 0.375),   # F4 (return)
]
for start, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Drums continue with the same pattern for bars 2-4
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 1.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

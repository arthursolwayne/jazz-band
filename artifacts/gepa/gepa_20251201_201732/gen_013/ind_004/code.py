
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.75),   # Hihat on 2
    (36, 0.75, 1.125),   # Kick on 3
    (42, 1.125, 1.5)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2-G2 range), walking line with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),    # F2 on 1
    (40, 1.875, 0.375),  # F#2 on 2
    (39, 2.25, 0.375),   # G2 on 3
    (38, 2.625, 0.375)   # F2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on last
piano_notes = [
    (44, 1.5, 0.375),    # F7 (F A C E) on 1
    (45, 1.875, 0.375),  # Dm7 (D F A C) on 2
    (47, 2.25, 0.375),   # Bb7 (Bb D F A) on 3
    (46, 2.625, 0.375)   # Gm7 (G Bb D F) on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - F, Bb, C, Eb (hanging on Eb)
sax_notes = [
    (53, 1.5, 0.375),    # F
    (57, 1.875, 0.375),  # Bb
    (55, 2.25, 0.375),   # C
    (59, 2.625, 0.375)   # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2, D2, Bb2, A2
bass_notes = [
    (38, 3.0, 0.375),    # F2 on 1
    (40, 3.375, 0.375),  # D2 on 2
    (42, 3.75, 0.375),   # Bb2 on 3
    (41, 4.125, 0.375)   # A2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on last
piano_notes = [
    (46, 3.0, 0.375),    # Gm7 (G Bb D F) on 1
    (48, 3.375, 0.375),  # C7 (C E G B) on 2
    (50, 3.75, 0.375),   # Eb7 (Eb G Bb D) on 3
    (49, 4.125, 0.375)   # Dm7 (D F A C) on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif variation, F, Bb, C, Eb again (hanging on Eb)
sax_notes = [
    (53, 3.0, 0.375),    # F
    (57, 3.375, 0.375),  # Bb
    (55, 3.75, 0.375),   # C
    (59, 4.125, 0.375)   # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2, D2, Bb2, A2
bass_notes = [
    (38, 4.5, 0.375),    # F2 on 1
    (40, 4.875, 0.375),  # D2 on 2
    (42, 5.25, 0.375),   # Bb2 on 3
    (41, 5.625, 0.375)   # A2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on last
piano_notes = [
    (46, 4.5, 0.375),    # Gm7 (G Bb D F) on 1
    (48, 4.875, 0.375),  # C7 (C E G B) on 2
    (50, 5.25, 0.375),   # Eb7 (Eb G Bb D) on 3
    (49, 5.625, 0.375)   # Dm7 (D F A C) on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif variation, F, Bb, C, Eb again (hanging on Eb)
sax_notes = [
    (53, 4.5, 0.375),    # F
    (57, 4.875, 0.375),  # Bb
    (55, 5.25, 0.375),   # C
    (59, 5.625, 0.375)   # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")


import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.375, 0.125), # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125), # Hihat on &2
    (36, 1.125, 0.375), # Kick on 3
    (42, 1.5, 0.125)    # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, F-Ab-C-Eb
bass_notes = [
    (43, 1.5, 0.375),   # F2
    (40, 1.875, 0.375), # Ab2
    (45, 2.25, 0.375),  # C3
    (43, 2.625, 0.375)  # F2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (43, 1.5, 0.375),   # F
    (40, 1.5, 0.375),   # Ab
    (45, 1.5, 0.375),   # C
    (43, 1.5, 0.375),   # Eb
    (47, 1.875, 0.375)  # D (chromatic approach)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: First motif (F, Ab, Bb, C)
sax_notes = [
    (43, 1.5, 0.375),   # F
    (40, 1.875, 0.375), # Ab
    (42, 2.25, 0.375),  # Bb
    (45, 2.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm, F-Ab-C-Eb
bass_notes = [
    (43, 3.0, 0.375),   # F2
    (40, 3.375, 0.375), # Ab2
    (45, 3.75, 0.375),  # C3
    (43, 4.125, 0.375)  # F2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Fm7 -> Bb7 (F, Ab, C, Eb -> Bb, D, F, Ab)
piano_notes = [
    (43, 3.0, 0.375),   # F
    (40, 3.0, 0.375),   # Ab
    (45, 3.0, 0.375),   # C
    (43, 3.0, 0.375),   # Eb
    (42, 3.375, 0.375), # Bb
    (45, 3.75, 0.375),  # D
    (43, 4.125, 0.375)  # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Second motif (Ab, Bb, C, F)
sax_notes = [
    (40, 3.0, 0.375),   # Ab
    (42, 3.375, 0.375), # Bb
    (45, 3.75, 0.375),  # C
    (43, 4.125, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.875, 0.125), # Hihat on &1
    (38, 5.25, 0.375),  # Snare on 2
    (42, 5.375, 0.125), # Hihat on &2
    (36, 5.625, 0.375), # Kick on 3
    (42, 5.999, 0.125)  # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm, F-Ab-C-Eb
bass_notes = [
    (43, 4.5, 0.375),   # F2
    (40, 4.875, 0.375), # Ab2
    (45, 5.25, 0.375),  # C3
    (43, 5.625, 0.375)  # F2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Fm7 -> Eb7 (F, Ab, C, Eb -> Eb, G, Bb, D)
piano_notes = [
    (43, 4.5, 0.375),   # F
    (40, 4.5, 0.375),   # Ab
    (45, 4.5, 0.375),   # C
    (43, 4.5, 0.375),   # Eb
    (41, 4.875, 0.375), # Eb
    (44, 5.25, 0.375),  # G
    (42, 5.625, 0.375)  # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Final motif (Bb, C, F, Ab)
sax_notes = [
    (42, 4.5, 0.375),   # Bb
    (45, 4.875, 0.375), # C
    (43, 5.25, 0.375),  # F
    (40, 5.625, 0.375)  # Ab
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

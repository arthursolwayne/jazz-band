
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C - E - G - C (Motif)
sax_notes = [
    (60, 1.5, 0.375),   # C
    (64, 1.875, 0.375), # E
    (67, 2.25, 0.375),  # G
    (60, 2.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: Walking line in C
bass_notes = [
    (60, 1.5, 0.375),   # C
    (62, 1.875, 0.375), # D
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 1.875, 0.375), # C7: C, E, B
    (62, 1.875, 0.375),
    (67, 1.875, 0.375),
    (60, 2.625, 0.375), # C7: C, E, B
    (62, 2.625, 0.375),
    (67, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.1875),  # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with slight variation
sax_notes = [
    (60, 3.0, 0.375),   # C
    (64, 3.375, 0.375), # E
    (67, 3.75, 0.375),  # G
    (60, 4.125, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: Walking line in C
bass_notes = [
    (60, 3.0, 0.375),   # C
    (62, 3.375, 0.375), # D
    (64, 3.75, 0.375),  # E
    (65, 4.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 3.375, 0.375), # C7: C, E, B
    (62, 3.375, 0.375),
    (67, 3.375, 0.375),
    (60, 4.125, 0.375), # C7: C, E, B
    (62, 4.125, 0.375),
    (67, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif with slight variation
sax_notes = [
    (60, 4.5, 0.375),   # C
    (64, 4.875, 0.375), # E
    (67, 5.25, 0.375),  # G
    (60, 5.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bass: Walking line in C
bass_notes = [
    (60, 4.5, 0.375),   # C
    (62, 4.875, 0.375), # D
    (64, 5.25, 0.375),  # E
    (65, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 4.875, 0.375), # C7: C, E, B
    (62, 4.875, 0.375),
    (67, 4.875, 0.375),
    (60, 5.625, 0.375), # C7: C, E, B
    (62, 5.625, 0.375),
    (67, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("four_bar_intro.mid")

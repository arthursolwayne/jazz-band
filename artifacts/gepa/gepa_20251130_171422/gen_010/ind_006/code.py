
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: 0.0 - 1.5s (Little Ray alone)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BAR 2: 1.5 - 3.0s (Full quartet)
# Sax: Motif starts here
sax_notes = [
    (62, 1.5, 0.375),  # Dm7
    (64, 1.875, 0.375),  # F
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line
bass_notes = [
    (50, 1.5, 0.375),  # D
    (51, 1.875, 0.375),  # Eb
    (49, 2.25, 0.375),  # C
    (50, 2.625, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.875, 0.375),  # F7 (F, A, C, Eb)
    (62, 1.875, 0.375),
    (60, 1.875, 0.375),
    (58, 1.875, 0.375),
    (64, 2.625, 0.375),  # F7 again
    (62, 2.625, 0.375),
    (60, 2.625, 0.375),
    (58, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Full bar
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BAR 3: 3.0 - 4.5s
# Sax: Repeat motif with slight variation
sax_notes = [
    (62, 3.0, 0.375),  # Dm7
    (64, 3.375, 0.375),  # F
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line
bass_notes = [
    (50, 3.0, 0.375),  # D
    (51, 3.375, 0.375),  # Eb
    (49, 3.75, 0.375),  # C
    (50, 4.125, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.375, 0.375),  # F7
    (62, 3.375, 0.375),
    (60, 3.375, 0.375),
    (58, 3.375, 0.375),
    (64, 4.125, 0.375),  # F7
    (62, 4.125, 0.375),
    (60, 4.125, 0.375),
    (58, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Full bar
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# BAR 4: 4.5 - 6.0s
# Sax: Finish the motif
sax_notes = [
    (62, 4.5, 0.375),  # Dm7
    (64, 4.875, 0.375),  # F
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line
bass_notes = [
    (50, 4.5, 0.375),  # D
    (51, 4.875, 0.375),  # Eb
    (49, 5.25, 0.375),  # C
    (50, 5.625, 0.375)   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 4.875, 0.375),  # F7
    (62, 4.875, 0.375),
    (60, 4.875, 0.375),
    (58, 4.875, 0.375),
    (64, 5.625, 0.375),  # F7
    (62, 5.625, 0.375),
    (60, 5.625, 0.375),
    (58, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Full bar
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

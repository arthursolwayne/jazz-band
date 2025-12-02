
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1 &
    (42, 0.1875, 0.1875), # Hihat on 2 &
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2 &
    (42, 0.5625, 0.1875), # Hihat on 3 &
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3 &
    (42, 0.9375, 0.1875), # Hihat on 4 &
    (38, 1.125, 0.375),   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (65, 1.875, 0.375), # F#4
    (67, 2.25, 0.375),  # A4
    (65, 2.625, 0.375), # F#4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking)
bass_notes = [
    (50, 1.5, 0.375),   # D3
    (51, 1.875, 0.375), # Eb3
    (52, 2.25, 0.375),  # E3
    (53, 2.625, 0.375), # F3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    (62, 1.875, 0.375),  # D7 - D, F#, A, C
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (62, 2.625, 0.375),
    (64, 2.625, 0.375),
    (67, 2.625, 0.375),
    (69, 2.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.1875),    # Hihat on 1 &
    (42, 1.6875, 0.1875), # Hihat on 2 &
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.1875),  # Hihat on 2 &
    (42, 2.0625, 0.1875), # Hihat on 3 &
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.1875),   # Hihat on 3 &
    (42, 2.4375, 0.1875), # Hihat on 4 &
    (38, 2.625, 0.375),   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats the motif, but with a variation
sax_notes = [
    (62, 3.0, 0.375),  # D4
    (65, 3.375, 0.375), # F#4
    (67, 3.75, 0.375),  # A4
    (69, 4.125, 0.375), # B4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking)
bass_notes = [
    (53, 3.0, 0.375),   # F3
    (55, 3.375, 0.375), # G3
    (57, 3.75, 0.375),  # A3
    (58, 4.125, 0.375), # Bb3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    (62, 3.375, 0.375),  # D7 - D, F#, A, C
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (62, 4.125, 0.375),
    (64, 4.125, 0.375),
    (67, 4.125, 0.375),
    (69, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.1875),    # Hihat on 1 &
    (42, 3.1875, 0.1875), # Hihat on 2 &
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.1875),  # Hihat on 2 &
    (42, 3.5625, 0.1875), # Hihat on 3 &
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.1875),   # Hihat on 3 &
    (42, 3.9375, 0.1875), # Hihat on 4 &
    (38, 4.125, 0.375),   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax resolves the motif
sax_notes = [
    (62, 4.5, 0.375),  # D4
    (65, 4.875, 0.375), # F#4
    (67, 5.25, 0.375),  # A4
    (62, 5.625, 0.375), # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking)
bass_notes = [
    (58, 4.5, 0.375),   # Bb3
    (60, 4.875, 0.375), # B3
    (62, 5.25, 0.375),  # C4
    (64, 5.625, 0.375), # D4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    (62, 4.875, 0.375),  # D7 - D, F#, A, C
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    (62, 5.625, 0.375),
    (64, 5.625, 0.375),
    (67, 5.625, 0.375),
    (69, 5.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.1875),    # Hihat on 1 &
    (42, 4.6875, 0.1875), # Hihat on 2 &
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.1875),  # Hihat on 2 &
    (42, 5.0625, 0.1875), # Hihat on 3 &
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.1875),   # Hihat on 3 &
    (42, 5.4375, 0.1875), # Hihat on 4 &
    (38, 5.625, 0.375),   # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

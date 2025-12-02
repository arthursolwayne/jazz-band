
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    (42, 0.0, 0.1875),    # Hihat on 1&
    (42, 0.1875, 0.1875), # Hihat on 2&
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2&
    (42, 0.5625, 0.1875), # Hihat on 3&
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3&
    (42, 0.9375, 0.1875), # Hihat on 4&
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 4&
    (42, 1.3125, 0.1875)  # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    (62, 1.5, 0.375),    # E4
    (64, 1.875, 0.375),  # F#4
    (65, 2.25, 0.375),   # G4
    (62, 2.625, 0.375)   # E4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: walking, chromatic
bass_notes = [
    (49, 1.5, 0.375),    # C3
    (50, 1.875, 0.375),  # C#3
    (51, 2.25, 0.375),   # D3
    (52, 2.625, 0.375)   # D#3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    (64, 1.875, 0.375),  # F#4 (7th chord on 2)
    (60, 1.875, 0.375),  # C4
    (67, 1.875, 0.375),  # G4
    (62, 1.875, 0.375),  # E4
    (64, 2.625, 0.375),  # F#4 (7th chord on 4)
    (60, 2.625, 0.375),  # C4
    (67, 2.625, 0.375),  # G4
    (62, 2.625, 0.375)   # E4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1&
    (42, 1.6875, 0.1875),# Hihat on 2&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2&
    (42, 2.0625, 0.1875),# Hihat on 3&
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3&
    (42, 2.4375, 0.1875),# Hihat on 4&
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4&
    (42, 2.8125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif (reprise)
sax_notes = [
    (62, 3.0, 0.375),    # E4
    (64, 3.375, 0.375),  # F#4
    (65, 3.75, 0.375),   # G4
    (62, 4.125, 0.375)   # E4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: walking, chromatic
bass_notes = [
    (53, 3.0, 0.375),    # E3
    (54, 3.375, 0.375),  # F3
    (55, 3.75, 0.375),   # F#3
    (57, 4.125, 0.375)   # A3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    (64, 3.375, 0.375),  # F#4 (7th chord on 2)
    (60, 3.375, 0.375),  # C4
    (67, 3.375, 0.375),  # G4
    (62, 3.375, 0.375),  # E4
    (64, 4.125, 0.375),  # F#4 (7th chord on 4)
    (60, 4.125, 0.375),  # C4
    (67, 4.125, 0.375),  # G4
    (62, 4.125, 0.375)   # E4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1&
    (42, 3.1875, 0.1875),# Hihat on 2&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2&
    (42, 3.5625, 0.1875),# Hihat on 3&
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3&
    (42, 3.9375, 0.1875),# Hihat on 4&
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4&
    (42, 4.3125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif (end)
sax_notes = [
    (62, 4.5, 0.375),    # E4
    (64, 4.875, 0.375),  # F#4
    (65, 5.25, 0.375),   # G4
    (62, 5.625, 0.375)   # E4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line: walking, chromatic
bass_notes = [
    (58, 4.5, 0.375),    # G3
    (59, 4.875, 0.375),  # G#3
    (60, 5.25, 0.375),   # A3
    (62, 5.625, 0.375)   # B3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    (64, 4.875, 0.375),  # F#4 (7th chord on 2)
    (60, 4.875, 0.375),  # C4
    (67, 4.875, 0.375),  # G4
    (62, 4.875, 0.375),  # E4
    (64, 5.625, 0.375),  # F#4 (7th chord on 4)
    (60, 5.625, 0.375),  # C4
    (67, 5.625, 0.375),  # G4
    (62, 5.625, 0.375)   # E4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums continue
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1&
    (42, 4.6875, 0.1875),# Hihat on 2&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2&
    (42, 5.0625, 0.1875),# Hihat on 3&
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3&
    (42, 5.4375, 0.1875),# Hihat on 4&
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4&
    (42, 5.8125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

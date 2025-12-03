
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5, 0.375),  # D2 on 1
    (40, 1.875, 0.375),  # F2 on 2
    (42, 2.25, 0.375),  # A2 on 3
    (43, 2.625, 0.375),  # Bb2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Piano chords (open voicings, each bar a different chord)
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    (62, 1.5, 0.375),  # D4
    (67, 1.5, 0.375),  # F#4
    (69, 1.5, 0.375),  # A4
    (71, 1.5, 0.375),  # C#5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Diane plays on 2 and 4
# Bar 2: D7 on 2 and 4
piano_notes = [
    (62, 1.875, 0.375),  # D4
    (67, 1.875, 0.375),  # F#4
    (69, 1.875, 0.375),  # A4
    (71, 1.875, 0.375),  # C#5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    (67, 2.25, 0.375),  # G4
    (71, 2.25, 0.375),  # Bb4
    (69, 2.25, 0.375),  # D4
    (66, 2.25, 0.375),  # F4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Diane plays on 2 and 4
# Bar 3: Gm7 on 2 and 4
piano_notes = [
    (67, 2.625, 0.375),  # G4
    (71, 2.625, 0.375),  # Bb4
    (69, 2.625, 0.375),  # D4
    (66, 2.625, 0.375),  # F4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Cmaj7 (C, E, G, B)
piano_notes = [
    (60, 3.0, 0.375),  # C4
    (64, 3.0, 0.375),  # E4
    (67, 3.0, 0.375),  # G4
    (71, 3.0, 0.375),  # B4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Diane plays on 2 and 4
# Bar 4: Cmaj7 on 2 and 4
piano_notes = [
    (60, 3.375, 0.375),  # C4
    (64, 3.375, 0.375),  # E4
    (67, 3.375, 0.375),  # G4
    (71, 3.375, 0.375),  # B4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif (start at bar 2, 1.5s)
# Motif: D5 (62), E5 (64), F5 (65), G5 (67)
# Play it on 1 and 3 (1.5 and 2.25s)
sax_notes = [
    (62, 1.5, 0.375),  # D5
    (64, 2.25, 0.375),  # E5
    (65, 2.625, 0.375),  # F5
    (67, 3.0, 0.375),  # G5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=120, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=120, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

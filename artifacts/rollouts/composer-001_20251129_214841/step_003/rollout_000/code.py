
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
    (36, 0.0, 1.0),     # Kick on beat 1
    (38, 0.5, 1.0),     # Snare on beat 2
    (42, 0.0, 1.0),     # Hihat on every 8th
    (42, 0.25, 1.0),
    (42, 0.5, 1.0),
    (42, 0.75, 1.0),
    (36, 1.0, 1.0),     # Kick on beat 3
    (38, 1.5, 1.0),     # Snare on beat 4
    (42, 1.0, 1.0),
    (42, 1.25, 1.0),
    (42, 1.5, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet starts
# Sax melody
sax_notes = [
    (62, 1.5, 0.5),  # D4 (start of motif)
    (67, 2.0, 0.5),  # G4
    (64, 2.5, 0.5),  # E4
    (62, 3.0, 0.5),  # D4 again
    (69, 3.5, 0.5),  # B4
    (67, 4.0, 0.5),  # G4
    (64, 4.5, 0.5),  # E4
    (62, 5.0, 0.5)   # D4 (ending the motif)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass line (walking line, chromatic approaches)
bass_notes = [
    (48, 1.5, 0.5),  # C4
    (49, 2.0, 0.5),  # C#4
    (50, 2.5, 0.5),  # D4
    (51, 3.0, 0.5),  # D#4
    (52, 3.5, 0.5),  # E4
    (53, 4.0, 0.5),  # F4
    (54, 4.5, 0.5),  # F#4
    (55, 5.0, 0.5)   # G4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (7th chords, comp on 2 and 4)
piano_notes = [
    (60, 2.0, 0.5),  # Cmaj7 (C, E, B, G)
    (64, 2.0, 0.5),
    (67, 2.0, 0.5),
    (69, 2.0, 0.5),
    (60, 4.0, 0.5),
    (64, 4.0, 0.5),
    (67, 4.0, 0.5),
    (69, 4.0, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Drums continue
drum_notes = [
    (36, 1.5, 1.0),     # Kick on beat 1
    (38, 2.0, 1.0),     # Snare on beat 2
    (42, 1.5, 1.0),     # Hihat on every 8th
    (42, 1.75, 1.0),
    (42, 2.0, 1.0),
    (42, 2.25, 1.0),
    (36, 2.5, 1.0),     # Kick on beat 3
    (38, 3.0, 1.0),     # Snare on beat 4
    (42, 2.5, 1.0),
    (42, 2.75, 1.0),
    (42, 3.0, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Drums continue
drum_notes = [
    (36, 3.0, 1.0),     # Kick on beat 1
    (38, 3.5, 1.0),     # Snare on beat 2
    (42, 3.0, 1.0),     # Hihat on every 8th
    (42, 3.25, 1.0),
    (42, 3.5, 1.0),
    (42, 3.75, 1.0),
    (36, 4.0, 1.0),     # Kick on beat 3
    (38, 4.5, 1.0),     # Snare on beat 4
    (42, 4.0, 1.0),
    (42, 4.25, 1.0),
    (42, 4.5, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Sax continues with motif
sax_notes = [
    (62, 5.5, 0.5),  # D4 (repeat motif)
    (67, 6.0, 0.5),  # G4
    (64, 6.5, 0.5),  # E4
    (62, 7.0, 0.5),  # D4 again
    (69, 7.5, 0.5),  # B4
    (67, 8.0, 0.5),  # G4
    (64, 8.5, 0.5),  # E4
    (62, 9.0, 0.5)   # D4 (ending the motif)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Bass continues
bass_notes = [
    (56, 5.0, 0.5),  # G4
    (57, 5.5, 0.5),  # G#4
    (58, 6.0, 0.5),  # A4
    (59, 6.5, 0.5),  # A#4
    (60, 7.0, 0.5),  # B4
    (61, 7.5, 0.5),  # C5
    (62, 8.0, 0.5),  # C#5
    (63, 8.5, 0.5)   # D5
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 3: Piano continues
piano_notes = [
    (60, 5.0, 0.5),  # Cmaj7
    (64, 5.0, 0.5),
    (67, 5.0, 0.5),
    (69, 5.0, 0.5),
    (60, 7.0, 0.5),
    (64, 7.0, 0.5),
    (67, 7.0, 0.5),
    (69, 7.0, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Sax ends with a resolution
sax_notes = [
    (62, 9.5, 0.5),  # D4
    (67, 10.0, 0.5), # G4
    (69, 10.5, 0.5), # B4
    (67, 11.0, 0.5), # G4
    (64, 11.5, 0.5), # E4
    (62, 12.0, 0.5)  # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Bass ends
bass_notes = [
    (64, 9.0, 0.5),  # D5
    (65, 9.5, 0.5),  # D#5
    (66, 10.0, 0.5), # E5
    (67, 10.5, 0.5), # F5
    (68, 11.0, 0.5), # F#5
    (69, 11.5, 0.5), # G5
    (70, 12.0, 0.5)  # G#5
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Bar 4: Piano ends
piano_notes = [
    (60, 9.0, 0.5),  # Cmaj7
    (64, 9.0, 0.5),
    (67, 9.0, 0.5),
    (69, 9.0, 0.5),
    (60, 11.0, 0.5),
    (64, 11.0, 0.5),
    (67, 11.0, 0.5),
    (69, 11.0, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Drums end
drum_notes = [
    (36, 6.0, 1.0),     # Kick on beat 1
    (38, 6.5, 1.0),     # Snare on beat 2
    (42, 6.0, 1.0),     # Hihat on every 8th
    (42, 6.25, 1.0),
    (42, 6.5, 1.0),
    (42, 6.75, 1.0),
    (36, 7.0, 1.0),     # Kick on beat 3
    (38, 7.5, 1.0),     # Snare on beat 4
    (42, 7.0, 1.0),
    (42, 7.25, 1.0),
    (42, 7.5, 1.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add time signature and tempo
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=120)]
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

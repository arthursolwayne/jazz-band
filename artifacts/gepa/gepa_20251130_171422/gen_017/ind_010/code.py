
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts on D (D4), E (E4), F# (F#4), G (G4) - short motif
sax_notes = [
    (62, 1.5, 0.1875), # D4
    (64, 1.6875, 0.1875), # E4
    (66, 1.875, 0.1875), # F#4
    (67, 2.0625, 0.1875) # G4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in D minor
bass_notes = [
    (45, 1.5, 0.375), # D3
    (46, 1.875, 0.375), # Eb3
    (47, 2.25, 0.375), # E3
    (49, 2.625, 0.375) # G3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    (62, 1.6875, 0.375), # D4
    (67, 1.6875, 0.375), # G4
    (64, 1.6875, 0.375), # E4
    (69, 1.6875, 0.375), # B4
    (67, 2.25, 0.375), # G4
    (71, 2.25, 0.375), # D5
    (72, 2.25, 0.375), # E5
    (76, 2.25, 0.375) # A5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif repeats, but with a half-step shift up
sax_notes = [
    (63, 3.0, 0.1875), # D#4
    (65, 3.1875, 0.1875), # F4
    (67, 3.375, 0.1875), # G4
    (68, 3.5625, 0.1875) # A4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in D minor
bass_notes = [
    (48, 3.0, 0.375), # F3
    (49, 3.375, 0.375), # G3
    (50, 3.75, 0.375), # A3
    (52, 4.125, 0.375) # C4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    (62, 3.1875, 0.375), # D4
    (67, 3.1875, 0.375), # G4
    (64, 3.1875, 0.375), # E4
    (69, 3.1875, 0.375), # B4
    (67, 3.75, 0.375), # G4
    (71, 3.75, 0.375), # D5
    (72, 3.75, 0.375), # E5
    (76, 3.75, 0.375) # A5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif ends on G (G4), resolves upward
sax_notes = [
    (67, 4.5, 0.1875), # G4
    (69, 4.6875, 0.1875), # A4
    (71, 4.875, 0.1875), # B4
    (72, 5.0625, 0.1875) # C5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: walking line in D minor
bass_notes = [
    (53, 4.5, 0.375), # C#4
    (55, 4.875, 0.375), # E4
    (57, 5.25, 0.375), # G4
    (59, 5.625, 0.375) # A#4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Dm7, G7)
piano_notes = [
    (62, 4.6875, 0.375), # D4
    (67, 4.6875, 0.375), # G4
    (64, 4.6875, 0.375), # E4
    (69, 4.6875, 0.375), # B4
    (67, 5.25, 0.375), # G4
    (71, 5.25, 0.375), # D5
    (72, 5.25, 0.375), # E5
    (76, 5.25, 0.375) # A5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

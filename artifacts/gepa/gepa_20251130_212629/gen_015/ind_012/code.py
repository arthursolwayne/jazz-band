
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on &1
    (1.125, 42, 100),# Hihat on &2
    (1.5, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on &3
    (2.125, 42, 100),# Hihat on &4
    (2.5, 36, 100),  # Kick on beat 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.25, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full ensemble enters (1.5 - 3.0s)
# Saxophone: F4 (F), G4 (G), A4 (A), F4 (F)
sax_notes = [
    (1.5, 65, 100),  # F4
    (1.75, 67, 100), # G4
    (2.0, 69, 100),  # A4
    (2.25, 65, 100), # F4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass: walking line in F minor (F, G, Ab, A)
bass_notes = [
    (1.5, 64, 100),  # F3
    (1.75, 66, 100), # G3
    (2.0, 67, 100),  # Ab3
    (2.25, 69, 100), # A3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4 (F7 on beat 2, Bb7 on beat 4)
piano_notes = [
    (1.75, 58, 100), # F3
    (1.75, 60, 100), # A3
    (1.75, 62, 100), # C4
    (1.75, 64, 100), # Eb4
    (2.25, 62, 100), # Bb3
    (2.25, 65, 100), # D4
    (2.25, 67, 100), # F4
    (2.25, 69, 100), # Ab4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Continue the motif (3.0 - 4.5s)
# Saxophone: E4 (E), F4 (F), G4 (G), F4 (F)
sax_notes = [
    (3.0, 64, 100),  # E4
    (3.25, 65, 100), # F4
    (3.5, 67, 100),  # G4
    (3.75, 65, 100), # F4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass: walking line in F minor (Bb3, B3, C4, D4)
bass_notes = [
    (3.0, 62, 100),  # Bb3
    (3.25, 63, 100), # B3
    (3.5, 64, 100),  # C4
    (3.75, 65, 100), # D4
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4 (Bb7 on beat 2, C7 on beat 4)
piano_notes = [
    (3.25, 62, 100), # Bb3
    (3.25, 65, 100), # D4
    (3.25, 67, 100), # F4
    (3.25, 69, 100), # Ab4
    (3.75, 64, 100), # C4
    (3.75, 67, 100), # F4
    (3.75, 69, 100), # G4
    (3.75, 71, 100), # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),  # Kick on beat 1
    (3.25, 42, 100), # Hihat on &1
    (3.5, 42, 100),  # Hihat on &2
    (3.75, 38, 100), # Snare on beat 2
    (4.0, 42, 100),  # Hihat on &3
    (4.25, 42, 100), # Hihat on &4
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100), # Hihat on &4
    (5.0, 38, 100),  # Snare on beat 4
    (5.25, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 4: Final resolution (4.5 - 6.0s)
# Saxophone: D4 (D), C4 (C), B4 (B), A4 (A)
sax_notes = [
    (4.5, 62, 100),  # D4
    (4.75, 60, 100), # C4
    (5.0, 61, 100),  # B4
    (5.25, 69, 100), # A4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass: walking line in F minor (Eb3, F3, G3, Ab3)
bass_notes = [
    (4.5, 61, 100),  # Eb3
    (4.75, 64, 100), # F3
    (5.0, 66, 100),  # G3
    (5.25, 67, 100), # Ab3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4 (C7 on beat 2, Ab7 on beat 4)
piano_notes = [
    (4.75, 64, 100), # C4
    (4.75, 67, 100), # F4
    (4.75, 69, 100), # G4
    (4.75, 71, 100), # Bb4
    (5.25, 67, 100), # F4
    (5.25, 69, 100), # G4
    (5.25, 71, 100), # Bb4
    (5.25, 72, 100), # B4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on beat 1
    (4.75, 42, 100), # Hihat on &1
    (5.0, 42, 100),  # Hihat on &2
    (5.25, 38, 100), # Snare on beat 2
    (5.5, 42, 100),  # Hihat on &3
    (5.75, 42, 100), # Hihat on &4
    (6.0, 36, 100),  # Kick on beat 3
    (6.25, 42, 100), # Hihat on &4
    (6.5, 38, 100),  # Snare on beat 4
    (6.75, 42, 100), # Hihat on &4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('intro.mid')

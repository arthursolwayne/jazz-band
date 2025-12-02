
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(note)
    # Snare on 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(note)
    # Hihat on every eighth
    for i in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 62),   # C3
    (1.875, 63), # C#3
    (2.25, 64),  # D3
    (2.625, 62), # C3
    (2.875, 61), # B2
    (3.25, 60),  # Bb2
    (3.625, 62), # C3
    (4.0, 63),   # C#3
    (4.375, 64), # D3
    (4.75, 62),  # C3
    (5.125, 61), # B2
    (5.5, 60),   # Bb2
    (5.875, 62), # C3
    (6.25, 63),  # C#3
    (6.625, 64), # D3
    (7.0, 62)    # C3
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (2.25, 60), (2.25, 64), (2.25, 67), (2.25, 69),  # C7
    (3.0, 60), (3.0, 64), (3.0, 67), (3.0, 69),   # C7
    (4.25, 60), (4.25, 64), (4.25, 67), (4.25, 69), # C7
    (5.0, 60), (5.0, 64), (5.0, 67), (5.0, 69),    # C7
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: Motif
sax_notes = [
    (1.5, 64), # D4
    (1.875, 67), # F4
    (2.25, 69), # G4
    (2.625, 67), # F4
    (2.875, 64), # D4
    (3.25, 62), # C4
    (3.625, 64), # D4
    (4.0, 67), # F4
    (4.375, 69), # G4
    (4.75, 67), # F4
    (5.125, 64), # D4
    (5.5, 62), # C4
    (5.875, 64), # D4
    (6.25, 67), # F4
    (6.625, 69), # G4
    (7.0, 67) # F4
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(note)
    # Snare on 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(note)
    # Hihat on every eighth
    for i in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")

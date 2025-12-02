
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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on &1
    (1.0, 38, 100),  # Snare on 2
    (1.25, 42, 100), # Hihat on &2
    (1.5, 36, 100)   # Kick on 3
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 45, 100),  # F3
    (1.875, 46, 100), # Gb3
    (2.25, 47, 100),  # G3
    (2.625, 48, 100), # Ab3
    (3.0, 49, 100),   # A3
    (3.375, 50, 100), # Bb3
    (3.75, 51, 100),  # B3
    (4.125, 52, 100), # C4
    (4.5, 53, 100),   # C#4
    (4.875, 54, 100), # D4
    (5.25, 55, 100),  # Eb4
    (5.625, 56, 100), # E4
    (6.0, 57, 100)    # F4
]
for start, note, velocity in bass_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
# Bar 2 - F7 (F A C E)
piano_notes = [
    (1.875, 71, 100), # E4
    (1.875, 69, 100), # C4
    (1.875, 67, 100), # A3
    (1.875, 65, 100), # F3
    (2.25, 71, 100),  # E4
    (2.25, 69, 100),  # C4
    (2.25, 67, 100),  # A3
    (2.25, 65, 100),  # F3
    (3.0, 76, 100),   # E5
    (3.0, 74, 100),   # C5
    (3.0, 72, 100),   # A4
    (3.0, 70, 100),   # F4
    (3.375, 76, 100), # E5
    (3.375, 74, 100), # C5
    (3.375, 72, 100), # A4
    (3.375, 70, 100)  # F4
]
for start, note, velocity in piano_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66, 100), # F4
    (1.75, 68, 100), # G4
    (2.0, 66, 100),  # F4
    (2.5, 66, 100),  # F4
    (2.75, 68, 100), # G4
    (3.0, 66, 100),  # F4
    (3.5, 68, 100),  # G4
    (3.75, 66, 100)  # F4
]
for start, note, velocity in sax_notes:
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(note_obj)

# Drums: Bar 2
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &1
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &2
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &3
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100)  # Hihat on &4
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 3
drum_notes = [
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &1
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100)  # Hihat on &4
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bar 4
drum_notes = [
    (5.5, 36, 100),  # Kick on 1
    (5.75, 42, 100), # Hihat on &1
    (6.0, 38, 100),  # Snare on 2
    (6.25, 42, 100), # Hihat on &2
]
for start, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.5, 38, 100),  # Snare on 3
    (2.25, 42, 100), # Hihat on 4
    (3.0, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on 2
    (4.5, 38, 100),  # Snare on 3
    (5.25, 42, 100), # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 62, 100),  # D4
    (1.875, 61, 100), # C#4 (chromatic approach)
    (2.25, 63, 100),  # E4
    (2.625, 64, 100), # F4
    (3.0, 62, 100),   # D4
    (3.375, 61, 100), # C#4
    (3.75, 63, 100),  # E4
    (4.125, 64, 100), # F4
    (4.5, 62, 100),   # D4
    (4.875, 61, 100), # C#4
    (5.25, 63, 100),  # E4
    (5.625, 64, 100), # F4
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67, 100),  # B4 (D7: D, F#, A, C#)
    (1.5, 64, 100),  # F#4
    (1.5, 62, 100),  # A4
    (1.5, 60, 100),  # C#4
    (2.25, 67, 100), # B4 (D7)
    (2.25, 64, 100), # F#4
    (2.25, 62, 100), # A4
    (2.25, 60, 100), # C#4
    (3.0, 67, 100),  # B4 (D7)
    (3.0, 64, 100),  # F#4
    (3.0, 62, 100),  # A4
    (3.0, 60, 100),  # C#4
    (3.75, 67, 100), # B4 (D7)
    (3.75, 64, 100), # F#4
    (3.75, 62, 100), # A4
    (3.75, 60, 100), # C#4
    (4.5, 67, 100),  # B4 (D7)
    (4.5, 64, 100),  # F#4
    (4.5, 62, 100),  # A4
    (4.5, 60, 100),  # C#4
    (5.25, 67, 100), # B4 (D7)
    (5.25, 64, 100), # F#4
    (5.25, 62, 100), # A4
    (5.25, 60, 100), # C#4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.875, 42, 100), # Hihat on 2
    (2.25, 38, 100),  # Snare on 3
    (2.625, 42, 100), # Hihat on 4
    (3.0, 36, 100),   # Kick on 1
    (3.375, 42, 100), # Hihat on 2
    (3.75, 38, 100),  # Snare on 3
    (4.125, 42, 100), # Hihat on 4
    (4.5, 36, 100),   # Kick on 1
    (4.875, 42, 100), # Hihat on 2
    (5.25, 38, 100),  # Snare on 3
    (5.625, 42, 100), # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante on sax: Motif that sings, starts, leaves it hanging, returns
sax_notes = [
    (1.5, 65, 100),  # E4
    (1.875, 67, 100), # G4
    (2.25, 69, 100),  # A4
    (2.625, 67, 100), # G4
    (3.0, 65, 100),   # E4
    (3.375, 62, 100), # D4
    (3.75, 60, 100),  # C4
    (4.125, 62, 100), # D4
    (4.5, 65, 100),   # E4
    (4.875, 67, 100), # G4
    (5.25, 69, 100),  # A4
    (5.625, 67, 100), # G4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

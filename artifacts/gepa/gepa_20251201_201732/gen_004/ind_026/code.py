
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
    (0.0, 36, 100),   # Kick on beat 1
    (0.75, 42, 100),  # Hihat on beat 2
    (1.25, 38, 100),  # Snare on beat 3
    (1.5, 42, 100),   # Hihat on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 43, 100),   # D2 (root)
    (1.875, 41, 100), # C#2 (chromatic approach)
    (2.25, 46, 100),  # A2 (fifth of D)
    (2.625, 44, 100), # G2 (root of next chord)
    (3.0, 48, 100),   # D3 (root)
    (3.375, 46, 100), # C#3 (chromatic approach)
    (3.75, 51, 100),  # A3 (fifth of D)
    (4.125, 49, 100), # G3 (root of next chord)
    (4.5, 52, 100),   # E3 (root of next chord)
    (4.875, 50, 100), # D#3 (chromatic approach)
    (5.25, 55, 100),  # B3 (fifth of E)
    (5.625, 53, 100), # E4 (root of next chord)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane on piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D F# A C)
    (1.5, 62, 100), # D4
    (1.5, 67, 100), # F#4
    (1.5, 71, 100), # A4
    (1.5, 67, 100), # C5

    # Bar 3: G7 (G B D F)
    (2.25, 67, 100), # G4
    (2.25, 71, 100), # B4
    (2.25, 69, 100), # D4
    (2.25, 65, 100), # F4

    # Bar 4: C7 (C E G B)
    (3.0, 60, 100), # C4
    (3.0, 64, 100), # E4
    (3.0, 67, 100), # G4
    (3.0, 71, 100), # B4

    # Bar 4: Resolve (A7)
    (3.75, 65, 100), # A4
    (3.75, 69, 100), # C#5
    (3.75, 72, 100), # E5
    (3.75, 76, 100), # G5
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_pattern = [
    (1.5, 36, 100), (1.5 + 0.375, 42, 100),
    (1.875, 38, 100), (1.875 + 0.375, 42, 100),
    (2.25, 36, 100), (2.25 + 0.375, 42, 100),
    (2.625, 38, 100), (2.625 + 0.375, 42, 100),
    (3.0, 36, 100), (3.0 + 0.375, 42, 100),
    (3.375, 38, 100), (3.375 + 0.375, 42, 100),
    (3.75, 36, 100), (3.75 + 0.375, 42, 100),
    (4.125, 38, 100), (4.125 + 0.375, 42, 100),
    (4.5, 36, 100), (4.5 + 0.375, 42, 100),
    (4.875, 38, 100), (4.875 + 0.375, 42, 100),
    (5.25, 36, 100), (5.25 + 0.375, 42, 100),
    (5.625, 38, 100), (5.625 + 0.375, 42, 100)
]
for time, note, velocity in drum_pattern:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 67, 100),  # D4
    (1.75, 72, 100),  # G4
    (2.25, 67, 100),  # D4
    (2.5, 74, 100),   # A4
    (3.0, 67, 100),   # D4
    (3.25, 72, 100),  # G4
    (3.5, 74, 100),   # A4
    (3.75, 69, 100),  # B4
    (4.25, 67, 100),  # D4
    (4.5, 72, 100),   # G4
    (4.75, 74, 100),  # A4
    (5.0, 67, 100)    # D4
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

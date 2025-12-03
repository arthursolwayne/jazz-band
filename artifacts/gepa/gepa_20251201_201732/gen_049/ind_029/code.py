
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
bar_length = 1.5
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 80), # Hihat on 2
    (0.75, 38, 110), # Snare on 3
    (1.125, 42, 80), # Hihat on 4
    (1.375, 36, 100) # Kick on 4 (slightly off-grid)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# Walking line with chromatic approaches, F2 (F3 in MIDI)
bass_notes = [
    (1.5, 72, 80),  # F3
    (1.75, 71, 80), # E3 (chromatic approach)
    (2.0, 74, 80),  # G3
    (2.25, 72, 80), # F3
    (2.5, 76, 80),  # A3
    (2.75, 74, 80), # G3
    (3.0, 72, 80),  # F3
    (3.25, 71, 80), # E3
    (3.5, 76, 80),  # A3
    (3.75, 74, 80), # G3
    (4.0, 72, 80),  # F3
    (4.25, 71, 80), # E3
    (4.5, 76, 80),  # A3
    (4.75, 74, 80), # G3
    (5.0, 72, 80),  # F3
    (5.25, 71, 80), # E3
    (5.5, 72, 80),  # F3
    (5.75, 76, 80)  # A3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano (Diane)
# Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E) - open voicing
piano_notes = [
    (1.5, 76, 90),  # A3
    (1.5, 72, 85),  # F3
    (1.5, 79, 85),  # C4
    (1.5, 84, 80),  # E4
    # Bar 3: A7 (A C# E G#) borrowed from C minor
    (2.0, 81, 95),  # A4
    (2.0, 85, 90),  # C#4
    (2.0, 88, 85),  # E4
    (2.0, 91, 80),  # G#4
    # Bar 4: D7 (D F# A C) - chromatic passing chord
    (2.5, 69, 95),  # D3
    (2.5, 76, 90),  # F#3
    (2.5, 82, 85),  # A3
    (2.5, 72, 80),  # C3
    # Resolve on F7
    (3.0, 76, 90),  # A3
    (3.0, 72, 85),  # F3
    (3.0, 79, 85),  # C4
    (3.0, 84, 80),  # E4
    # Add tension in bar 4
    (3.5, 86, 100), # Bb4
    (3.5, 82, 95),  # A3
    (3.5, 79, 90),  # C4
    (3.5, 72, 85),  # F3
    (3.5, 67, 80),  # D3 (chromatic passing tone)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth, with fills
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.625, 42, 80), # Hihat
    (1.75, 38, 110), # Snare on 2
    (1.875, 42, 80), # Hihat
    (2.0, 36, 100),  # Kick on 3
    (2.125, 42, 80), # Hihat
    (2.25, 38, 110), # Snare on 4
    (2.375, 42, 80), # Hihat
    # Fill before bar 3
    (2.5, 36, 100),  # Kick
    (2.625, 42, 80), # Hihat
    (2.75, 38, 110), # Snare
    (2.875, 42, 80), # Hihat
    (3.0, 36, 100),  # Kick on 1
    (3.125, 42, 80), # Hihat
    (3.25, 38, 110), # Snare on 2
    (3.375, 42, 80), # Hihat
    (3.5, 36, 100),  # Kick on 3
    (3.625, 42, 80), # Hihat
    (3.75, 38, 110), # Snare on 4
    (3.875, 42, 80), # Hihat
    # Final fill before bar 4
    (4.0, 36, 100),  # Kick
    (4.125, 42, 80), # Hihat
    (4.25, 38, 110), # Snare
    (4.375, 42, 80), # Hihat
    (4.5, 36, 100),  # Kick on 1
    (4.625, 42, 80), # Hihat
    (4.75, 38, 110), # Snare on 2
    (4.875, 42, 80), # Hihat
    (5.0, 36, 100),  # Kick on 3
    (5.125, 42, 80), # Hihat
    (5.25, 38, 110), # Snare on 4
    (5.375, 42, 80), # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Sax (Dante)
# One short motif, haunting, incomplete
sax_notes = [
    (1.5, 73, 100),  # G3
    (1.625, 76, 100), # A3
    (1.75, 71, 100), # E3
    (1.875, 73, 100), # G3
    (2.0, 79, 100),  # C4
    (2.125, 82, 100), # D4
    (2.25, 79, 100), # C4
    (2.375, 76, 100), # A3
    (2.5, 73, 100),  # G3
    (2.625, 76, 100), # A3
    (2.75, 71, 100), # E3
    (2.875, 73, 100), # G3
    (3.0, 79, 100),  # C4
    (3.125, 76, 100), # A3
    (3.25, 73, 100),  # G3
    (3.375, 76, 100), # A3
    (3.5, 71, 100),  # E3
    (3.625, 73, 100), # G3
    (3.75, 76, 100),  # A3
    (3.875, 82, 100), # D4
    (4.0, 79, 100),  # C4
    (4.125, 76, 100), # A3
    (4.25, 73, 100),  # G3
    (4.375, 71, 100), # E3
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Add some rests and space
# Leave the last bar open, incomplete

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

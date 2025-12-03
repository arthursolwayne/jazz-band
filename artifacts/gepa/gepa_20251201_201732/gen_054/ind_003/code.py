
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums, with a syncopated, tense pattern
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    (0.0, 36, 100),   # Kick on 1
    (0.375, 42, 100), # Hi-hat on & of 1
    (0.5, 38, 110),   # Snare on 2
    (0.875, 42, 100), # Hi-hat on & of 2
    (1.0, 36, 100),   # Kick on 3
    (1.375, 42, 100), # Hi-hat on & of 3
    (1.5, 38, 110)    # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 80),   # D2 (root)
    (1.75, 39, 90),  # Eb2 (chromatic approach)
    (2.0, 43, 80),   # A2 (fifth)
    (2.25, 42, 90),  # G2 (chromatic approach)
    (2.5, 38, 80),   # D2 (root)
    (2.75, 39, 90),  # Eb2 (chromatic approach)
    (3.0, 43, 80),   # A2 (fifth)
    (3.25, 42, 90)   # G2 (chromatic approach)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: open voicings, different chord each bar, comp on 2 and 4
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (1.5, 62, 90),   # D4
    (1.5, 64, 90),   # F4
    (1.5, 69, 90),   # A4
    (1.5, 72, 90),   # C5
    # Bar 3: Gm7 (G Bb D F)
    (2.5, 71, 90),   # G4
    (2.5, 73, 90),   # Bb4
    (2.5, 69, 90),   # D4
    (2.5, 64, 90),   # F4
    # Bar 4: Cm7 (C Eb G Bb)
    (3.5, 60, 90),   # C4
    (3.5, 63, 90),   # Eb4
    (3.5, 67, 90),   # G4
    (3.5, 62, 90)    # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: short, haunting motif, incomplete
# Motif: D4 (beat 1), F4 (beat 2), A4 (beat 3), rest on beat 4
sax_notes = [
    (1.5, 62, 100),   # D4 on beat 1
    (2.0, 64, 100),   # F4 on beat 2
    (2.5, 69, 100),   # A4 on beat 3
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: Dm7 -> Gm7 -> Cm7

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (already played)
    # Bar 3: Gm7 (already played)
    # Bar 4: Cm7 (already played)
    # Comp on 2 and 4
    (2.0, 62, 90),   # Comp on beat 2
    (2.0, 64, 90),
    (2.0, 69, 90),
    (2.0, 72, 90),
    (3.0, 60, 90),   # Comp on beat 4
    (3.0, 63, 90),
    (3.0, 67, 90),
    (3.0, 62, 90)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: continue the pattern from bar 1
drum_notes = [
    (3.0, 36, 100),   # Kick on 1
    (3.375, 42, 100), # Hi-hat on & of 1
    (3.5, 38, 110),   # Snare on 2
    (3.875, 42, 100), # Hi-hat on & of 2
    (4.0, 36, 100),   # Kick on 3
    (4.375, 42, 100), # Hi-hat on & of 3
    (4.5, 38, 110)    # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax completes the motif
sax_notes = [
    (4.5, 62, 100)    # D4 on beat 1 (completes the motif)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass line: resolves on C
bass_notes = [
    (4.5, 60, 80)     # C3
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: resolves on Cm7
piano_notes = [
    (4.5, 60, 90),    # C4
    (4.5, 63, 90),    # Eb4
    (4.5, 67, 90),    # G4
    (4.5, 62, 90)     # Bb4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: final beat
drum_notes = [
    (4.5, 36, 100),   # Kick on 1
    (4.875, 42, 100), # Hi-hat on & of 1
    (5.0, 38, 120),   # Snare on 2
    (5.375, 42, 100), # Hi-hat on & of 2
    (5.5, 36, 100),   # Kick on 3
    (5.875, 42, 100), # Hi-hat on & of 3
    (6.0, 38, 120)    # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

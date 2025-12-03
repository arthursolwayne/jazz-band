
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
    (0.5, 42, 100),  # Hihat on beat 2
    (1.0, 38, 100),  # Snare on beat 3
    (1.5, 42, 100),  # Hihat on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 50, 100),  # D2 (root)
    (1.875, 51, 100), # Eb2 (chromatic approach)
    (2.25, 52, 100),  # E2 (fifth)
    (2.625, 50, 100), # D2 (root)
    
    (3.0, 50, 100),  # D2
    (3.375, 51, 100), # Eb2
    (3.75, 52, 100),  # E2
    (4.125, 50, 100), # D2
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    (1.5, 62, 100),  # D4
    (1.5, 67, 100),  # F#4
    (1.5, 71, 100),  # A4
    (1.5, 72, 100),  # C#4

    # Bar 3: Bm7 (B, D, F#, A)
    (3.0, 69, 100),  # B4
    (3.0, 62, 100),  # D4
    (3.0, 67, 100),  # F#4
    (3.0, 71, 100),  # A4

    # Bar 4: G7 (G, B, D, F)
    (4.5, 67, 100),  # G4
    (4.5, 71, 100),  # B4
    (4.5, 69, 100),  # D4
    (4.5, 65, 100),  # F4
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Drums: continue pattern
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (2.0, 42, 100),  # Hihat on beat 2
    (2.5, 38, 100),  # Snare on beat 3
    (3.0, 42, 100),  # Hihat on beat 4

    (3.0, 36, 100),  # Kick on beat 1
    (3.5, 42, 100),  # Hihat on beat 2
    (4.0, 38, 100),  # Snare on beat 3
    (4.5, 42, 100),  # Hihat on beat 4

    (4.5, 36, 100),  # Kick on beat 1
    (5.0, 42, 100),  # Hihat on beat 2
    (5.5, 38, 100),  # Snare on beat 3
    (6.0, 42, 100),  # Hihat on beat 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 74, 100),  # E5
    (1.75, 72, 100), # D5 (half note)
    (2.25, 74, 100), # E5 (half note)
    (2.75, 72, 100), # D5 (half note)
    
    (3.5, 74, 100),  # E5
    (3.75, 72, 100), # D5
    (4.25, 74, 100), # E5
    (4.75, 76, 100), # F#5
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

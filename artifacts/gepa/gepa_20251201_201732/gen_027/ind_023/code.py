
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.5, 36, 100),  # Kick on beat 3
    (1.75, 42, 100), # Hihat on & of 3
    (2.0, 38, 100),  # Snare on beat 4
    (2.5, 42, 100),  # Hihat on & of 4
    (3.0, 36, 100)   # Kick on beat 1 of next bar
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100),  # D2
    (1.75, 41, 100), # F#2 (chromatic approach)
    (2.0, 43, 100),  # A2
    (2.25, 41, 100), # F#2
    (2.5, 38, 100),  # D2
    (2.75, 40, 100), # E2 (chromatic approach)
    (3.0, 43, 100),  # A2
    (3.25, 40, 100), # E2
    (3.5, 38, 100),  # D2
    (3.75, 41, 100), # F#2
    (4.0, 43, 100),  # A2
    (4.25, 41, 100), # F#2
    (4.5, 38, 100),  # D2
    (4.75, 40, 100), # E2
    (5.0, 43, 100),  # A2
    (5.25, 40, 100), # E2
    (5.5, 38, 100),  # D2
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (1.5, 50, 100), # D4
    (1.5, 53, 100), # F4
    (1.5, 57, 100), # A4
    (1.5, 60, 100), # C5
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    (2.5, 55, 100), # G4
    (2.5, 59, 100), # B4
    (2.5, 62, 100), # D5
    (2.5, 65, 100), # F5
])
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes.extend([
    (3.5, 60, 100), # C5
    (3.5, 64, 100), # E5
    (3.5, 67, 100), # G5
    (3.5, 71, 100), # B5
])
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - D5 (D, F#, A, D)
sax_notes = [
    (1.5, 62, 100), # D4
    (1.75, 66, 100), # F#4
    (2.0, 67, 100), # A4
    (2.25, 69, 100), # Bb4 (chromatic approach)
    (2.5, 62, 100), # D4
    (2.75, 66, 100), # F#4
    (3.0, 67, 100), # A4
    (3.25, 69, 100), # Bb4
    (3.5, 62, 100), # D4
    (3.75, 66, 100), # F#4
    (4.0, 67, 100), # A4
    (4.25, 72, 100), # D5
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Drums: continue for bars 2-4
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (1.75, 42, 100), # Hihat on & of 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.5, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.5, 36, 100),  # Kick on beat 1
    (3.75, 42, 100), # Hihat on & of 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.5, 36, 100),  # Kick on beat 3
    (4.75, 42, 100), # Hihat on & of 3
    (5.0, 38, 100),  # Snare on beat 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

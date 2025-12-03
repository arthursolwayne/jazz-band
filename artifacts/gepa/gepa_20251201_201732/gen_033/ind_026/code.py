
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
    (1.5, 42, 100),  # Hihat on &2
    (1.75, 36, 100), # Kick on 3
    (2.25, 42, 100), # Hihat on &3
    (2.5, 38, 100),  # Snare on 4
    (3.0, 42, 100)   # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (1.5, 50, 100), # D2 (root)
    (1.875, 49, 100), # C#2 (chromatic approach)
    (2.25, 55, 100), # A2 (fifth)
    (2.625, 56, 100) # Bb2 (chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (1.5, 62, 100), # D4
    (1.5, 65, 100), # F4
    (1.5, 69, 100), # A4
    (1.5, 72, 100), # C5
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax: motif - start it, leave it hanging
sax_notes = [
    (1.5, 76, 100), # D5
    (1.75, 78, 100), # F5
    (2.0, 76, 100), # D5
    (2.25, 78, 100), # F5
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (3.0, 57, 100), # Bb2 (chromatic approach)
    (3.375, 55, 100), # A2 (fifth)
    (3.75, 52, 100), # G2 (root)
    (4.125, 51, 100) # F#2 (chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Cm7 (C, Eb, G, Bb)
piano_notes = [
    (3.0, 72, 100), # C5
    (3.0, 69, 100), # Eb4
    (3.0, 76, 100), # G4
    (3.0, 74, 100), # Bb4
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax: continue motif, come back and finish it
sax_notes = [
    (3.0, 76, 100), # D5
    (3.25, 78, 100), # F5
    (3.5, 76, 100), # D5
    (3.75, 78, 100), # F5
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    (4.5, 51, 100), # F#2 (chromatic approach)
    (4.875, 52, 100), # G2 (root)
    (5.25, 55, 100), # A2 (fifth)
    (5.625, 56, 100) # Bb2 (chromatic approach)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes = [
    (4.5, 78, 100), # G5
    (4.5, 74, 100), # Bb4
    (4.5, 76, 100), # D5
    (4.5, 72, 100), # F5
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax: finish the motif
sax_notes = [
    (4.5, 76, 100), # D5
    (4.75, 78, 100), # F5
    (5.0, 76, 100), # D5
    (5.25, 78, 100), # F5
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),  # Kick on 1
    (5.0, 38, 100),  # Snare on 2
    (5.25, 42, 100), # Hihat on &2
    (5.5, 36, 100),  # Kick on 3
    (6.0, 38, 100),  # Snare on 4
    (6.25, 42, 100)  # Hihat on &4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

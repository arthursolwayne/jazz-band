
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
    (0.375, 42, 100),  # Hihat on &1
    (0.75, 38, 100),  # Snare on 2
    (1.125, 42, 100),  # Hihat on &2
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 100),  # Hihat on &3
    (2.25, 38, 100),  # Snare on 4
    (2.625, 42, 100)   # Hihat on &4
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line - D2-G2 with chromatic approaches
bass_notes = [
    (1.5, 38, 100),  # D2
    (1.75, 40, 100),  # Eb2 (chromatic approach)
    (2.0, 43, 100),  # G2
    (2.25, 41, 100),  # F2 (chromatic approach)
    (2.5, 38, 100),  # D2
    (2.75, 40, 100),  # Eb2
    (3.0, 43, 100),  # G2
    (3.25, 41, 100)  # F2
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    (1.5, 62, 100),  # D4
    (1.5, 67, 100),  # F4
    (1.5, 71, 100),  # A4
    (1.5, 72, 100),  # C5
    (2.0, 62, 100),  # D4
    (2.0, 67, 100),  # F4
    (2.0, 71, 100),  # A4
    (2.0, 72, 100),  # C5
    (2.5, 62, 100),  # D4
    (2.5, 67, 100),  # F4
    (2.5, 71, 100),  # A4
    (2.5, 72, 100),  # C5
    (3.0, 62, 100),  # D4
    (3.0, 67, 100),  # F4
    (3.0, 71, 100),  # A4
    (3.0, 72, 100)   # C5
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Dante: Saxophone line - one short motif
# Motif: D4, F4, E4, D4 (half note, half note, eighth note, eighth note)
sax_notes = [
    (1.5, 62, 100),  # D4
    (2.0, 62, 100),  # D4 (half note)
    (2.5, 67, 100),  # F4
    (2.75, 65, 100),  # E4
    (3.0, 62, 100),  # D4
    (3.25, 62, 100)  # D4
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line - D2-G2 with chromatic approaches
bass_notes = [
    (3.0, 38, 100),  # D2
    (3.25, 40, 100),  # Eb2
    (3.5, 43, 100),  # G2
    (3.75, 41, 100),  # F2
    (4.0, 38, 100),  # D2
    (4.25, 40, 100),  # Eb2
    (4.5, 43, 100),  # G2
    (4.75, 41, 100)  # F2
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane: Open voicings - Gm7 (G-Bb-D-F)
piano_notes = [
    (3.0, 67, 100),  # G4
    (3.0, 71, 100),  # Bb4
    (3.0, 74, 100),  # D5
    (3.0, 76, 100),  # F5
    (3.5, 67, 100),  # G4
    (3.5, 71, 100),  # Bb4
    (3.5, 74, 100),  # D5
    (3.5, 76, 100),  # F5
    (4.0, 67, 100),  # G4
    (4.0, 71, 100),  # Bb4
    (4.0, 74, 100),  # D5
    (4.0, 76, 100),  # F5
    (4.5, 67, 100),  # G4
    (4.5, 71, 100),  # Bb4
    (4.5, 74, 100),  # D5
    (4.5, 76, 100)   # F5
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Dante: Saxophone line - continuation of motif
# Continue: G4, F4, E4, D4 (half note, half note, eighth note, eighth note)
sax_notes = [
    (3.0, 67, 100),  # G4
    (3.5, 67, 100),  # G4 (half note)
    (4.0, 67, 100),  # G4
    (4.25, 65, 100),  # F4
    (4.5, 62, 100),  # E4
    (4.75, 62, 100)  # D4
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line - D2-G2 with chromatic approaches
bass_notes = [
    (4.5, 38, 100),  # D2
    (4.75, 40, 100),  # Eb2
    (5.0, 43, 100),  # G2
    (5.25, 41, 100),  # F2
    (5.5, 38, 100),  # D2
    (5.75, 40, 100),  # Eb2
    (6.0, 43, 100),  # G2
    (6.25, 41, 100)  # F2
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane: Open voicings - Cm7 (C-Eb-G-Bb)
piano_notes = [
    (4.5, 60, 100),  # C4
    (4.5, 64, 100),  # Eb4
    (4.5, 67, 100),  # G4
    (4.5, 71, 100),  # Bb4
    (5.0, 60, 100),  # C4
    (5.0, 64, 100),  # Eb4
    (5.0, 67, 100),  # G4
    (5.0, 71, 100),  # Bb4
    (5.5, 60, 100),  # C4
    (5.5, 64, 100),  # Eb4
    (5.5, 67, 100),  # G4
    (5.5, 71, 100),  # Bb4
    (6.0, 60, 100),  # C4
    (6.0, 64, 100),  # Eb4
    (6.0, 67, 100),  # G4
    (6.0, 71, 100)   # Bb4
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Dante: Saxophone line - resolution of motif
# End with a D4 on beat 4
sax_notes = [
    (4.5, 62, 100),  # D4
    (5.0, 62, 100),  # D4
    (5.5, 62, 100),  # D4
    (6.0, 62, 100)   # D4
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Drums: continue the pattern for the full 4 bars
for i in range(3):
    for time, note, velocity in drum_notes:
        new_time = time + 3.0 * i
        drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=new_time, end=new_time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

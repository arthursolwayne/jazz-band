
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.375, 42, 90), # Hihat
    (0.75, 38, 100), # Snare on 2
    (1.125, 42, 90), # Hihat
    (1.5, 36, 100),  # Kick on 3
    (1.875, 42, 90), # Hihat
    (2.25, 38, 100), # Snare on 4
    (2.625, 42, 90)  # Hihat
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 38, 100),  # D2 (root)
    (1.875, 40, 80), # Eb2 (chromatic approach)
    (2.25, 43, 100), # G2 (fifth)
    (2.625, 41, 80), # F2 (chromatic)
    # Bar 3 (3.0 - 4.5s)
    (3.0, 40, 100),  # Eb2 (root)
    (3.375, 42, 80), # F2 (chromatic)
    (3.75, 45, 100), # A2 (fifth)
    (4.125, 44, 80), # Ab2 (chromatic)
    # Bar 4 (4.5 - 6.0s)
    (4.5, 38, 100),  # D2 (root)
    (4.875, 40, 80), # Eb2 (chromatic)
    (5.25, 43, 100), # G2 (fifth)
    (5.625, 41, 80)  # F2 (chromatic)
]
for note in bass_notes:
    bass_note = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (1.5, 62, 100),  # D4
    (1.5, 65, 100),  # F4
    (1.5, 67, 100),  # A4
    (1.5, 69, 100),  # C5
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    (3.0, 71, 100),  # G4
    (3.0, 70, 100),  # Bb4
    (3.0, 67, 100),  # D4
    (3.0, 65, 100),  # F4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    (4.5, 60, 100),  # C4
    (4.5, 63, 100),  # Eb4
    (4.5, 67, 100),  # G4
    (4.5, 69, 100),  # Bb4
])
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - Ab4 (half note, then rest)
sax_notes = [
    (1.5, 62, 100),  # D4
    (1.5, 65, 100),  # F4
    (1.5, 67, 100),  # Ab4
    (2.25, 67, 100), # Ab4 (rest until 2.25)
    (3.0, 62, 100),  # D4
    (3.0, 65, 100),  # F4
    (3.0, 67, 100),  # Ab4
    (3.75, 67, 100), # Ab4 (rest until 3.75)
    (4.5, 62, 100),  # D4
    (4.5, 65, 100),  # F4
    (4.5, 67, 100)   # Ab4
]
for note in sax_notes:
    sax_note = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    sax.notes.append(sax_note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    time = 1.5 + i * 0.375
    if i % 2 == 0:
        dr = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    elif i % 2 == 1:
        dr = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    time = 3.0 + i * 0.375
    if i % 2 == 0:
        dr = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    elif i % 2 == 1:
        dr = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(dr)

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    time = 4.5 + i * 0.375
    if i % 2 == 0:
        dr = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    elif i % 2 == 1:
        dr = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375)
    drums.notes.append(dr)
    dr = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

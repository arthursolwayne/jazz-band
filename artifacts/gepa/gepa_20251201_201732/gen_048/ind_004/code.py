
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 4):
    time = i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line in Fm (F - Ab - D - C), chromatic approaches
bass_notes = [
    (1.5, 53, 100),  # F2
    (1.75, 51, 100), # Eb2 (chromatic approach)
    (2.0, 50, 100),  # D2
    (2.25, 48, 100), # C2
    (2.5, 50, 100),  # D2
    (2.75, 51, 100), # Eb2
    (3.0, 53, 100),  # F2
    (3.25, 55, 100)  # G2 (chromatic approach)
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (1.5, 71, 100),  # F4
    (1.5, 69, 100),  # Eb4
    (1.5, 67, 100),  # C4
    (1.5, 64, 100),  # Ab3
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.0, 73, 100),  # Bb4
    (2.0, 71, 100),  # D4
    (2.0, 69, 100),  # F4
    (2.0, 66, 100),  # Ab3
    # Bar 4: Am7 (A, C, E, G)
    (2.5, 77, 100),  # A4
    (2.5, 75, 100),  # C4
    (2.5, 72, 100),  # E4
    (2.5, 71, 100),  # G4
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.5)
    piano.notes.append(note)

# Dante on sax: short motif, start it, leave it hanging, finish it
# Motif: F, Ab, Bb, F (F - Ab - Bb - F)
sax_notes = [
    (1.5, 65, 100),  # F4
    (1.75, 63, 100), # Ab4
    (2.0, 62, 100),  # Bb4
    (2.5, 65, 100),  # F4 (come back and finish)
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for i in range(0, 4):
        time = bar * 1.5 + i * 0.375
        if i % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125)
            drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

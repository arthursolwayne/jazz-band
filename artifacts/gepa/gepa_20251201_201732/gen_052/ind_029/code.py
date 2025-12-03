
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus (walking line with chromatic approaches, roots and fifths)
# Bar 2: F - E - F - G
bass_notes = [
    (0.0, 38, 100),  # F2
    (0.375, 37, 90), # E2
    (0.75, 38, 100), # F2
    (1.125, 40, 100) # G2
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + time, end=1.5 + time + 0.125)
    bass.notes.append(note)

# Bar 3: C - B - C - D
bass_notes = [
    (0.0, 43, 100),  # C3
    (0.375, 42, 90), # B2
    (0.75, 43, 100), # C3
    (1.125, 45, 100) # D3
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + 1.5 + time, end=1.5 + 1.5 + time + 0.125)
    bass.notes.append(note)

# Bar 4: G - F# - G - A
bass_notes = [
    (0.0, 40, 100),  # G2
    (0.375, 39, 90), # F#2
    (0.75, 40, 100), # G2
    (1.125, 42, 100) # A2
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + 3.0 + time, end=1.5 + 3.0 + time + 0.125)
    bass.notes.append(note)

# Piano: Diane (open voicings, different chord each bar, resolve on the last)
# Bar 2: F7sus4 (F, Bb, C, D)
for time, pitch, vel in [(0.0, 64, 100), (0.0, 76, 100), (0.0, 72, 100), (0.0, 69, 100)]:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + time, end=1.5 + time + 0.25)
    piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab)
for time, pitch, vel in [(0.0, 68, 100), (0.0, 72, 100), (0.0, 64, 100), (0.0, 60, 100)]:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + 1.5 + time, end=1.5 + 1.5 + time + 0.25)
    piano.notes.append(note)

# Bar 4: Gm7 (G, Bb, D, F)
for time, pitch, vel in [(0.0, 72, 100), (0.0, 68, 100), (0.0, 69, 100), (0.0, 64, 100)]:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + 3.0 + time, end=1.5 + 3.0 + time + 0.25)
    piano.notes.append(note)

# Sax: Dante (haunting motif, incomplete, leave it hanging)
# Bar 2: F - Eb - F - rest
sax_notes = [
    (0.0, 72, 100), # F4
    (0.375, 70, 100), # Eb4
    (0.75, 72, 100), # F4
    (1.125, 72, 0)   # rest
]
for time, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + time, end=1.5 + time + 0.125)
    sax.notes.append(note)

# Bar 3: Bb - A - Bb - rest
sax_notes = [
    (0.0, 76, 100), # Bb4
    (0.375, 74, 100), # A4
    (0.75, 76, 100), # Bb4
    (1.125, 76, 0)   # rest
]
for time, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + 1.5 + time, end=1.5 + 1.5 + time + 0.125)
    sax.notes.append(note)

# Bar 4: G - F - G - rest
sax_notes = [
    (0.0, 72, 100), # G4
    (0.375, 70, 100), # F4
    (0.75, 72, 100), # G4
    (1.125, 72, 0)   # rest
]
for time, pitch, vel in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=1.5 + 3.0 + time, end=1.5 + 3.0 + time + 0.125)
    sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 5):
    for beat in range(4):
        time = 1.5 + (bar - 2) * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Add drum notes for each bar
for bar in range(2, 5):
    for beat in range(4):
        time = 1.5 + (bar - 2) * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled

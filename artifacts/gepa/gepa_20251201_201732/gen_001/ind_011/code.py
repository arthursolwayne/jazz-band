
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 0.25),   # D2
    (1.875, 40, 0.25), # Eb2 (chromatic approach)
    (2.25, 43, 0.25),  # G2
    (2.625, 41, 0.25), # F2 (chromatic approach)
    (2.875, 38, 0.25), # D2
    (3.25, 40, 0.25),  # Eb2
    (3.625, 43, 0.25), # G2
    (4.0, 41, 0.25),   # F2
    (4.25, 38, 0.25),  # D2
    (4.625, 40, 0.25), # Eb2
    (5.0, 43, 0.25),   # G2
    (5.375, 41, 0.25)  # F2
]
for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    (1.5, 62, 0.5), # D4
    (1.5, 65, 0.5), # F4
    (1.5, 69, 0.5), # A4
    (1.5, 72, 0.5), # C5
]
for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Bar 3: G7 (G B D F)
piano_notes = [
    (2.25, 67, 0.5), # G4
    (2.25, 71, 0.5), # B4
    (2.25, 69, 0.5), # D4
    (2.25, 65, 0.5), # F4
]
for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    (3.0, 60, 0.5), # C4
    (3.0, 63, 0.5), # Eb4
    (3.0, 67, 0.5), # G4
    (3.0, 62, 0.5), # Bb4
]
for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - Eb4 - F4 - D4 (suspending on the third)
sax_notes = [
    (1.5, 62, 0.375), # D4
    (1.875, 64, 0.375), # Eb4
    (2.25, 65, 0.375), # F4
    (2.625, 62, 0.375), # D4
    (2.875, 62, 0.375), # D4 (hold)
    (3.25, 62, 0.375), # D4
    (3.625, 62, 0.375), # D4
    (4.0, 62, 0.375), # D4
    (4.375, 62, 0.375), # D4
    (4.75, 62, 0.375), # D4
    (5.125, 62, 0.375), # D4
    (5.5, 62, 0.375) # D4
]
for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")


import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 60),   # C3
    (1.875, 61), # C#3
    (2.25, 62),  # D3
    (2.625, 63), # D#3
    (3.0, 64),   # E3
    (3.375, 65), # F3
    (3.75, 66),  # F#3
    (4.125, 67), # G3
    (4.5, 68),   # G#3
    (4.875, 69), # A3
    (5.25, 70),  # A#3
    (5.625, 71), # B3
    (6.0, 72)    # C4
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
# Bar 2: C7 on beat 2, E7 on beat 4
piano_notes = [
    (2.25, 60), # C4
    (2.25, 67), # G4 (C7)
    (2.25, 64), # E4
    (2.25, 69), # B4 (C7)
    (2.625, 64), # E4
    (2.625, 71), # B4 (E7)
    (2.625, 67), # G4
    (2.625, 72), # C5 (E7)
    (3.75, 60), # C4
    (3.75, 67), # G4 (C7)
    (3.75, 64), # E4
    (3.75, 69), # B4 (C7)
    (4.125, 64), # E4
    (4.125, 71), # B4 (E7)
    (4.125, 67), # G4
    (4.125, 72), # C5 (E7)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - E - B - C (C E B C), then rest
sax_notes = [
    (1.5, 60), # C4
    (1.625, 64), # E4
    (1.75, 67), # G4
    (1.875, 60), # C4
    (2.25, 60), # C4
    (2.375, 64), # E4
    (2.5, 67), # G4
    (2.625, 60), # C4
    (3.0, 60), # C4
    (3.125, 64), # E4
    (3.25, 67), # G4
    (3.375, 60)  # C4
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: continue with same pattern in bars 2-4
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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")

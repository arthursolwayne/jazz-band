
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F minor, chromatic approaches
bass_notes = [
    (1.5, 69, 100),  # F3
    (1.875, 70, 100), # Gb3
    (2.25, 71, 100),  # G3
    (2.625, 72, 100), # Ab3
    (3.0, 69, 100),   # F3
    (3.375, 70, 100), # Gb3
    (3.75, 71, 100),  # G3
    (4.125, 72, 100), # Ab3
    (4.5, 69, 100),   # F3
    (4.875, 70, 100), # Gb3
    (5.25, 71, 100),  # G3
    (5.625, 72, 100)  # Ab3
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, F7, Bb7, Eb7
# Bar 2: F7 (F, A, C, Eb) on beat 2
# Bar 3: Bb7 (Bb, D, F, Ab) on beat 2
# Bar 4: Eb7 (Eb, G, Bb, Db) on beat 2
piano_notes = [
    # Bar 2 - Beat 2 (F7)
    (2.25, 65, 100), # F3
    (2.25, 68, 100), # A3
    (2.25, 69, 100), # C4
    (2.25, 67, 100), # Eb4
    # Bar 3 - Beat 2 (Bb7)
    (3.75, 62, 100), # Bb3
    (3.75, 65, 100), # D4
    (3.75, 69, 100), # F4
    (3.75, 67, 100), # Ab4
    # Bar 4 - Beat 2 (Eb7)
    (5.25, 60, 100), # Eb3
    (5.25, 63, 100), # G4
    (5.25, 66, 100), # Bb4
    (5.25, 64, 100), # Db5
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Dante: Tenor sax melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (65), Ab (67), Bb (62), C (69)
# Bar 2: F (65) on beat 1
# Bar 2: Ab (67) on beat 2
# Bar 3: Bb (62) on beat 1
# Bar 3: C (69) on beat 2
# Bar 4: F (65) on beat 1
# Bar 4: C (69) on beat 2
sax_notes = [
    (2.0, 65, 100), # F3
    (2.25, 67, 100), # Ab3
    (3.0, 62, 100), # Bb3
    (3.25, 69, 100), # C4
    (4.0, 65, 100), # F3
    (4.25, 69, 100)  # C4
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)
    
# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")

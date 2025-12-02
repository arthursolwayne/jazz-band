
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
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 50, 100),  # F
    (1.875, 49, 100), # Eb
    (2.25, 51, 100),  # G
    (2.625, 50, 100), # F
    (2.625, 48, 100), # D
    (3.0, 49, 100),   # Eb
    (3.375, 50, 100), # F
    (3.75, 51, 100),  # G
    (3.75, 53, 100),  # A
    (4.125, 51, 100), # G
    (4.5, 50, 100),   # F
    (4.875, 49, 100), # Eb
    (5.25, 50, 100),  # F
    (5.625, 48, 100), # D
    (6.0, 50, 100)    # F
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62, 100), # F7
    (1.5, 67, 100), # Bb
    (1.875, 64, 100), # D
    (1.875, 69, 100), # F
    (2.25, 62, 100), # F7
    (2.25, 67, 100), # Bb
    (2.625, 64, 100), # D
    (2.625, 69, 100), # F
    (3.0, 62, 100), # F7
    (3.0, 67, 100), # Bb
    (3.375, 64, 100), # D
    (3.375, 69, 100), # F
    (3.75, 62, 100), # F7
    (3.75, 67, 100), # Bb
    (4.125, 64, 100), # D
    (4.125, 69, 100), # F
    (4.5, 62, 100), # F7
    (4.5, 67, 100), # Bb
    (4.875, 64, 100), # D
    (4.875, 69, 100), # F
    (5.25, 62, 100), # F7
    (5.25, 67, 100), # Bb
    (5.625, 64, 100), # D
    (5.625, 69, 100), # F
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Drums: continue pattern
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5s)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0)  # A
sax.notes.append(note)

# Bar 3 (2.25s)
note = pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75)  # A
sax.notes.append(note)

# Bar 4 (3.0s)
note = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5)  # A
sax.notes.append(note)

# Final note to hang
note = pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75)  # F
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

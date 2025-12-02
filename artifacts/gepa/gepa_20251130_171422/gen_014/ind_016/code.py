
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
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 50, 100),   # Fm7: F, Ab, C, D
    (1.875, 49, 100), # chromatic to Eb
    (2.25, 50, 100),
    (2.625, 48, 100), # chromatic to D
    (3.0, 50, 100),
    (3.375, 49, 100),
    (3.75, 50, 100),
    (4.125, 48, 100),
    (4.5, 50, 100),
    (4.875, 49, 100),
    (5.25, 50, 100),
    (5.625, 48, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60, 100),   # F7: F, Ab, C, E
    (1.5, 64, 100),
    (1.5, 67, 100),
    (1.5, 71, 100),
    (2.25, 60, 100),
    (2.25, 64, 100),
    (2.25, 67, 100),
    (2.25, 71, 100),
    (3.0, 60, 100),
    (3.0, 64, 100),
    (3.0, 67, 100),
    (3.0, 71, 100),
    (3.75, 60, 100),
    (3.75, 64, 100),
    (3.75, 67, 100),
    (3.75, 71, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Eb - D - F (hanging on D)
sax_notes = [
    (1.5, 77, 100),   # F
    (1.875, 76, 100), # Eb
    (2.25, 75, 100),  # D
    (2.625, 77, 100), # F
    (3.0, 77, 100),   # F (repeat)
    (3.375, 76, 100), # Eb
    (3.75, 75, 100),  # D
    (4.125, 77, 100), # F
    (4.5, 77, 100),   # F
    (4.875, 76, 100), # Eb
    (5.25, 75, 100),  # D
    (5.625, 77, 100)  # F
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])


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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass - walking line with chromatic approaches
bass_notes = [
    (1.5, 62, 100),     # D
    (1.875, 63, 90),    # Eb
    (2.25, 60, 100),    # C
    (2.625, 62, 90),    # D
    (2.875, 63, 100),   # Eb
    (3.25, 64, 90),     # F
    (3.625, 62, 100),   # D
    (4.0, 63, 90),      # Eb
    (4.375, 65, 100),   # G
    (4.75, 62, 90),     # D
    (5.125, 63, 100),   # Eb
    (5.5, 64, 90),      # F
    (5.875, 62, 100)    # D
]

for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane on piano - 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67, 90),      # D7: G
    (1.5, 69, 90),      # D7: B
    (1.5, 64, 90),      # D7: F
    (1.5, 62, 90),      # D7: D

    (2.25, 67, 90),     # D7: G
    (2.25, 69, 90),     # D7: B
    (2.25, 64, 90),     # D7: F
    (2.25, 62, 90),     # D7: D

    (3.0, 67, 90),      # D7: G
    (3.0, 69, 90),      # D7: B
    (3.0, 64, 90),      # D7: F
    (3.0, 62, 90),      # D7: D

    (3.75, 67, 90),     # D7: G
    (3.75, 69, 90),     # D7: B
    (3.75, 64, 90),     # D7: F
    (3.75, 62, 90),     # D7: D

    (4.5, 67, 90),      # D7: G
    (4.5, 69, 90),      # D7: B
    (4.5, 64, 90),      # D7: F
    (4.5, 62, 90),      # D7: D

    (5.25, 67, 90),     # D7: G
    (5.25, 69, 90),     # D7: B
    (5.25, 64, 90),     # D7: F
    (5.25, 62, 90),     # D7: D
]

for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Dante on tenor sax - sparse, expressive melody
sax_notes = [
    (1.5, 65, 100),     # E
    (1.75, 62, 90),     # D
    (2.0, 67, 100),     # G
    (2.25, 65, 90),     # E
    (2.5, 62, 100),     # D
    (2.75, 64, 90),     # F
    (3.0, 65, 100),     # E
    (3.25, 67, 90),     # G
    (3.5, 69, 100),     # B
    (3.75, 67, 90),     # G
    (4.0, 65, 100),     # E
    (4.25, 62, 90),     # D
    (4.5, 67, 100),     # G
    (4.75, 65, 90),     # E
    (5.0, 64, 100),     # F
    (5.25, 62, 90),     # D
    (5.5, 65, 100),     # E
    (5.75, 67, 90),     # G
]

for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")

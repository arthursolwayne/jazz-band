
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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches
bass_notes = [
    (1.5, 70),  # F
    (1.875, 69),  # E
    (2.25, 71),  # F#
    (2.625, 72),  # G
    (2.625, 70),  # F
    (2.875, 69),  # E
    (3.25, 71),  # F#
    (3.625, 72),  # G
    (3.625, 70),  # F
    (3.875, 69),  # E
    (4.25, 71),  # F#
    (4.625, 72),  # G
    (4.625, 70),  # F
    (4.875, 69),  # E
    (5.25, 71),  # F#
    (5.625, 72),  # G
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
# F7 on beat 2, D7 on beat 4
piano_notes = [
    (1.875, 65, 100),  # F
    (1.875, 69, 100),  # A
    (1.875, 72, 100),  # C
    (1.875, 71, 100),  # Bb
    (2.625, 62, 100),  # D
    (2.625, 67, 100),  # F
    (2.625, 71, 100),  # A
    (2.625, 72, 100),  # B
    (3.875, 65, 100),  # F
    (3.875, 69, 100),  # A
    (3.875, 72, 100),  # C
    (3.875, 71, 100),  # Bb
    (4.625, 62, 100),  # D
    (4.625, 67, 100),  # F
    (4.625, 71, 100),  # A
    (4.625, 72, 100),  # B
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
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Dante: Tenor sax motif
# F (65), G (67), A (69), leave it hanging on A (69)
sax_notes = [
    (1.5, 65, 100, 0.25),
    (1.75, 67, 100, 0.25),
    (2.0, 69, 100, 0.25),
    (2.25, 69, 100, 0.75)
]
for time, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

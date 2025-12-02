
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 60),     # C
    (1.875, 61),   # C#
    (2.25, 62),    # D
    (2.625, 63),   # D#
    (3.0, 64),     # E
    (3.375, 65),   # F
    (3.75, 66),    # F#
    (4.125, 67),   # G
    (4.5, 68),     # G#
    (4.875, 69),   # A
    (5.25, 70),    # A#
    (5.625, 71),   # B
    (6.0, 72),     # C
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 71),  # C7
    (2.25, 62), (2.25, 66), (2.25, 69), (2.25, 73),  # D7
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 74),  # E7
    (3.75, 65), (3.75, 69), (3.75, 72), (3.75, 76),  # F7
    (4.5, 67), (4.5, 71), (4.5, 74), (4.5, 77),  # G7
    (5.25, 69), (5.25, 72), (5.25, 76), (5.25, 79),  # A7
    (6.0, 71), (6.0, 74), (6.0, 77), (6.0, 81),  # B7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: motif
# C - E - Bb - D (melody)
sax_notes = [
    (1.5, 60),     # C
    (1.875, 64),   # E
    (2.25, 62),    # Bb
    (2.625, 67),   # D
    (3.0, 60),     # C (return)
    (3.375, 64),   # E
    (3.75, 62),    # Bb
    (4.125, 67),   # D
    (4.5, 60),     # C (return)
    (4.875, 64),   # E
    (5.25, 62),    # Bb
    (5.625, 67),   # D
    (6.0, 60),     # C (resolve)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")

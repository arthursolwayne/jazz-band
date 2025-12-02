
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
    (1.5, 60),   # C
    (1.875, 61), # C#
    (2.25, 62),  # D
    (2.625, 64), # D#
    (3.0, 65),   # E
    (3.375, 67), # F#
    (3.75, 69),  # G
    (4.125, 70), # G#
    (4.5, 71),   # A
    (4.875, 72), # A#
    (5.25, 74),  # B
    (5.625, 76), # C
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 60), (1.75, 64), (1.75, 67), (1.75, 71),  # C7
    (2.25, 60), (2.25, 64), (2.25, 67), (2.25, 71),  # C7
    # Bar 3 (3.0 - 4.5s)
    (3.25, 62), (3.25, 67), (3.25, 71), (3.25, 76),  # D7
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 76),  # D7
    # Bar 4 (4.5 - 6.0s)
    (4.75, 64), (4.75, 67), (4.75, 71), (4.75, 76),  # E7
    (5.25, 64), (5.25, 67), (5.25, 71), (5.25, 76),  # E7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Sax: short motif, start it, leave it hanging, come back and finish it
# C E Bb G (C minor 7) -> leave it hanging on Bb for 1 bar, come back on G
sax_notes = [
    (1.5, 60), (1.5 + 0.375, 64), (1.5 + 0.75, 62), (1.5 + 1.125, 67),
    (1.5 + 1.5, 62), (1.5 + 1.875, 62), (1.5 + 2.25, 62), (1.5 + 2.625, 62),
    (1.5 + 3.0, 67), (1.5 + 3.375, 67), (1.5 + 3.75, 67), (1.5 + 4.125, 67),
    (1.5 + 4.5, 60), (1.5 + 4.875, 64), (1.5 + 5.25, 62), (1.5 + 5.625, 67)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')

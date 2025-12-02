
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
# Bar 2
# Bass: Walking line, chromatic approaches
# C7 chord: C E G B
bass_notes = [60, 61, 62, 64, 65, 67, 68, 69, 71, 72, 73, 75]
for i in range(4):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=bass_notes[i % len(bass_notes)], start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# C7: C E G Bb
# F7: F A C Eb
# Bb7: Bb D F Ab
# E7: E G# B D
for bar in range(2, 5):
    time = bar * 1.5
    if bar % 2 == 0:
        # 7th chord on 2
        for pitch in [60, 64, 67, 69]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + 0.5, end=time + 0.75)
            piano.notes.append(note)
    else:
        # 7th chord on 4
        for pitch in [65, 69, 72, 74]:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + 0.5, end=time + 0.75)
            piano.notes.append(note)

# Sax: One short motif, make it sing.
# Start with C (60), Bb (62), B (62), A (60), G (67), F (65)
sax_notes = [
    (60, 0.0, 0.25),  # C
    (62, 0.25, 0.5),  # Bb
    (62, 0.5, 0.75),  # B
    (60, 0.75, 1.0),  # A
    (67, 1.0, 1.25),  # G
    (65, 1.25, 1.5)   # F
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + 1.5, end=end + 1.5)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
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

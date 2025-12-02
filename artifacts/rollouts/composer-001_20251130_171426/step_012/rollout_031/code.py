
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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches
# Fm7 = F, Ab, C, Eb
# Walking bass line: F, Gb, G, Ab, A, Bb, B, C, C#, Db, D, Eb, etc.
bass_notes = [
    # Bar 2
    (1.5, 72), # F
    (1.875, 70), # Gb
    (2.25, 71), # G
    (2.625, 72), # Ab
    # Bar 3
    (2.875, 74), # A
    (3.25, 73), # Bb
    (3.625, 75), # B
    (4.0, 72), # C
    # Bar 4
    (4.25, 73), # C#
    (4.625, 70), # Db
    (5.0, 72), # D
    (5.375, 72), # Eb
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bars 2-4, comp on 2 and 4
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    for beat in [1, 3]:
        start = time + beat * 0.375
        # Fm7 chord: F, Ab, C, Eb
        for pitch in [72, 76, 76, 70]:  # F, Ab, C, Eb
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
            piano.notes.append(note)

# Dante: Motif in Fm, 4 bars
# Start with a short motif, leave it hanging, then return to finish it
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
# Motif: F, Ab, Bb, F (hanging on Bb), then return with G, Ab, Bb, F

# Bar 2: Start motif
sax_notes = [
    (1.5, 72),   # F
    (1.875, 76), # Ab
    (2.25, 71),  # Bb
    (2.625, 72), # F
]

# Bar 3: Leave it hanging (no note)
# Bar 4: Return and finish motif
sax_notes += [
    (4.0, 74),   # G
    (4.375, 76), # Ab
    (4.75, 71),  # Bb
    (5.125, 72), # F
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Little Ray: Fill the bar with kicks, snares, and hi-hats
for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 2) * 1.5 + beat * 0.375
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

# Save the MIDI file
midi.write("dante_intro.mid")

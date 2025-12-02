
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
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time starts at 1.5s

# Marcus: Walking line, chromatic approaches, no repeated notes
# Fm7: F, Ab, Bb, D
# Walking line in Fm: F, Gb, G, Ab, A, Bb, B, C, etc.

# Bass line
bass_notes = [77, 76, 78, 79, 80, 79, 78, 77, 76, 75, 77, 76, 78, 79, 80, 79]
bass_times = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25]
for i, time in enumerate(bass_times):
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Bbm7 = Bb, Db, Eb, G
# Abm7 = Ab, B, Db, F
# Dm7 = D, F, G, A
# Chords on beat 2 and 4

chord_notes = {
    1.5: [77, 80, 81, 74],   # Fm7
    2.0: [81, 84, 85, 78],   # Bbm7
    2.5: [80, 82, 84, 77],   # Abm7
    3.0: [78, 80, 82, 76],   # Dm7
    3.5: [77, 80, 81, 74],   # Fm7
    4.0: [81, 84, 85, 78],   # Bbm7
    4.5: [80, 82, 84, 77],   # Abm7
    5.0: [78, 80, 82, 76]    # Dm7
}

for time, pitches in chord_notes.items():
    for pitch in pitches:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: F, Ab, Bb, F (over 2 bars)
# Start on beat 2 of bar 2
# End on beat 4 of bar 2, leave it hanging
# Come back on beat 1 of bar 3 to finish

# First instance (bar 2, beats 2-4)
sax_notes = [77, 80, 81, 77]
sax_times = [2.0, 2.375, 2.75, 3.125]
for i, time in enumerate(sax_times):
    note = pretty_midi.Note(velocity=100, pitch=sax_notes[i], start=time, end=time + 0.25)
    sax.notes.append(note)

# Second instance (bar 3, beat 1)
note = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")

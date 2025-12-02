
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

# Marcus: Walking line, chromatic approaches
# Key: Fm7 (F, Ab, Bb, D)
# Bass line: F - Gb - G - Ab - Bb - B - C - Db - D - Eb - F - Gb - G - Ab - Bb - B
bass_notes = [77, 75, 76, 78, 75, 77, 79, 74, 76, 77, 77, 75, 76, 78, 75, 77]
for i, pitch in enumerate(bass_notes):
    time = 1.5 + (i * 0.375)
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Bb7 = Bb, D, F, Ab
# E7 = E, G#, B, D
# Am7 = A, C, E, G
chords = [
    [77, 80, 81, 84],  # Fm7
    [81, 84, 77, 80],  # Bb7
    [82, 85, 87, 84],  # E7
    [83, 85, 87, 89],  # Am7
]
for bar in range(2, 5):
    for chord in chords[bar - 2]:
        time = bar * 1.5
        note = pretty_midi.Note(velocity=95, pitch=chord, start=time, end=time + 0.25)
        piano.notes.append(note)

# You: Tenor sax - one short motif, make it sing.
# Motif: F (77) - Bb (81) - Ab (80) - F (77) - D (84) - Ab (80)
# Start on beat 2 of bar 2, leave it hanging, come back on bar 4
note1 = pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.5)
note2 = pretty_midi.Note(velocity=115, pitch=81, start=2.5, end=2.75)
note3 = pretty_midi.Note(velocity=110, pitch=80, start=2.75, end=3.0)
note4 = pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.25)
note5 = pretty_midi.Note(velocity=115, pitch=84, start=4.5, end=4.75)
note6 = pretty_midi.Note(velocity=110, pitch=80, start=4.75, end=5.0)

sax.notes.extend([note1, note2, note3, note4, note5, note6])

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

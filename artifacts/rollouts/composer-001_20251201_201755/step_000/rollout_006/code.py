
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 (38), F2 (41), G2 (43), Eb2 (40)
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        notes = [38, 41, 43, 40]
    elif bar == 3:
        notes = [40, 43, 45, 42]
    elif bar == 4:
        notes = [42, 45, 47, 44]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
# Bar 3: G7 (G-B-D-F)
# Bar 4: Cm7 (C-Eb-G-Bb)
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        chords = [62, 64, 67, 69]
    elif bar == 3:
        chords = [67, 71, 69, 64]
    elif bar == 4:
        chords = [60, 63, 67, 69]
    for i, pitch in enumerate(chords):
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + i * 0.375, end=time + i * 0.375 + 0.25)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (64), Eb (63), D (62)
# Bar 2: play first two notes
# Bar 3: leave it hanging
# Bar 4: finish it
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        notes = [62, 64]
    elif bar == 4:
        notes = [63, 62]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=110, pitch=pitch, start=time + i * 0.375, end=time + i * 0.375 + 0.25)
        sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

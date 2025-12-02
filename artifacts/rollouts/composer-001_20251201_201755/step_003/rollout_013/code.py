
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
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line
# Fm7 to Bbm7 to Ebm7 to Abm7 (root, root + 5, chromatic approach)
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        # Fm7: F, C, Bb, Eb
        for pitch in [37, 43, 41, 47]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
            bass.notes.append(note)
        # Chromatic approach to Bb
        note = pretty_midi.Note(velocity=80, pitch=40, start=time + 0.25, end=time + 0.375)
        bass.notes.append(note)
    elif bar == 3:
        # Bbm7: Bb, F, Eb, Ab
        for pitch in [41, 37, 47, 51]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
            bass.notes.append(note)
        # Chromatic approach to Eb
        note = pretty_midi.Note(velocity=80, pitch=46, start=time + 0.25, end=time + 0.375)
        bass.notes.append(note)
    elif bar == 4:
        # Ebm7: Eb, Bb, Ab, Db
        for pitch in [47, 41, 51, 54]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
            bass.notes.append(note)
        # Chromatic approach to Ab
        note = pretty_midi.Note(velocity=80, pitch=50, start=time + 0.25, end=time + 0.375)
        bass.notes.append(note)

# Diane: Open voicings, each bar different chord
# Bar 2: Fm7 (F, Ab, C, Eb)
for pitch in [37, 41, 43, 47]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=1.5, end=1.5 + 0.375)
    piano.notes.append(note)

# Bar 3: Bbm7 (Bb, Db, F, Ab)
for pitch in [41, 43, 37, 41]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=3.0, end=3.0 + 0.375)
    piano.notes.append(note)

# Bar 4: Ebm7 (Eb, Gb, Bb, Db)
for pitch in [47, 49, 41, 43]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=4.5, end=4.5 + 0.375)
    piano.notes.append(note)

# Little Ray: Same pattern as before
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    for beat in range(4):
        time_beat = time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time_beat, end=time_beat + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time_beat, end=time_beat + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time_beat, end=time_beat + 0.125)
        drums.notes.append(note)

# Dante: Tenor sax
# Motif: F, Ab, G, Eb (Fm scale with a touch of tension)
# Start it, leave it hanging, come back and finish it
note = pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=1.5 + 0.375, end=1.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=47, start=1.5 + 1.125, end=1.5 + 1.5)
sax.notes.append(note)

# Repeat motif in bar 4 with variation
note = pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=4.5 + 0.375, end=4.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=40, start=4.5 + 0.75, end=4.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=47, start=4.5 + 1.125, end=4.5 + 1.5)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")

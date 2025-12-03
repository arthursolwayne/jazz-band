
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums

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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2), roots and fifths with chromatic approaches
# Fm7 -> Bbm7 -> Eb7 -> Am7
chords = ['Fm7', 'Bbm7', 'Eb7', 'Am7']
root_notes = [53, 48, 50, 45]  # F, Bb, Eb, A
fifth_notes = [58, 53, 55, 50]  # C, F, A, D
chromatic_approaches = [52, 47, 49, 44]  # Eb, Ab, Db, G

for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        # Root
        note = pretty_midi.Note(velocity=100, pitch=root_notes[bar - 2], start=time, end=time + 0.25)
        bass.notes.append(note)
        # Fifth
        note = pretty_midi.Note(velocity=100, pitch=fifth_notes[bar - 2], start=time + 0.25, end=time + 0.5)
        bass.notes.append(note)
        # Chromatic approach
        note = pretty_midi.Note(velocity=80, pitch=chromatic_approaches[bar - 2], start=time + 0.5, end=time + 0.75)
        bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Fm7, Bbm7, Eb7, Am7
# Bar 2: Fm7 -> Ab - C - F - D
# Bar 3: Bbm7 -> D - F - Bb - G
# Bar 4: Eb7 -> G - Bb - Eb - F
# Bar 5: Am7 -> C - E - A - G

for bar in range(2, 6):
    time = bar * 1.5
    if bar == 2:
        # Fm7: Ab, C, F, D
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 1.5))
    elif bar == 3:
        # Bbm7: D, F, Bb, G
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 1.5))
    elif bar == 4:
        # Eb7: G, Bb, Eb, F
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time, end=time + 1.5))
    elif bar == 5:
        # Am7: C, E, A, G
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=time, end=time + 1.5))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + 1.5))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Ab - Bb - C (bar 2), then F - Ab (bar 3), then Bb - C (bar 4)

# Bar 2: F - Ab - Bb - C
for i, note in enumerate([53, 55, 57, 58]):
    time = 1.5 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1875))

# Bar 3: F - Ab
for i, note in enumerate([53, 55]):
    time = 3.0 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1875))

# Bar 4: Bb - C
for i, note in enumerate([57, 58]):
    time = 4.5 + i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1875))

# Drums: Full quartet (bars 2-4)
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

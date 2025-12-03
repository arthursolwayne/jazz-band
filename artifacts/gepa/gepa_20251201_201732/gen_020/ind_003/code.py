
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

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        # Dm7 (D, F, A, C)
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=40, start=time + 0.375, end=time + 0.75)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=37, start=time + 0.375, end=time + 0.75)
        bass.notes.append(note)
    elif bar == 3:
        # G7 (G, B, D, F)
        note = pretty_midi.Note(velocity=100, pitch=43, start=time, end=time + 0.375)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=47, start=time, end=time + 0.375)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=45, start=time + 0.375, end=time + 0.75)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.375, end=time + 0.75)
        bass.notes.append(note)
    elif bar == 4:
        # Cmaj7 (C, E, G, B)
        note = pretty_midi.Note(velocity=100, pitch=40, start=time, end=time + 0.375)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=44, start=time, end=time + 0.375)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=47, start=time + 0.375, end=time + 0.75)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=49, start=time + 0.375, end=time + 0.75)
        bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        note = pretty_midi.Note(velocity=100, pitch=50, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=55, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=57, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=52, start=time, end=time + 0.75)
        piano.notes.append(note)
    elif bar == 3:
        # G7: G, B, D, F
        note = pretty_midi.Note(velocity=100, pitch=55, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=59, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=57, start=time, end=time + 0.75)
        piano.notes.append(note)
    elif bar == 4:
        # Cmaj7: C, E, G, B
        note = pretty_midi.Note(velocity=100, pitch=52, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=57, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.75)
        piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
time = 1.5
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)

# Bar 3: Leave it hanging
time = 3.0
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)

# Bar 4: Come back and finish it
time = 4.5
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=time + 0.75, end=time + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=time + 1.125, end=time + 1.5)
sax.notes.append(note)

# Drums: continue for bars 2-4
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    for beat in range(4):
        time_bar = time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time_bar, end=time_bar + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time_bar, end=time_bar + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time_bar + eighth * 0.1875, end=time_bar + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

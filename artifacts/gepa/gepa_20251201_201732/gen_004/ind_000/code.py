
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

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2, F#, A, Bb
# Bar 3: G2, Bb, C#, D
# Bar 4: D2, F#, A, Bb

# Bass
for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 2) * 1.5 + beat * 0.375
        if bar == 2:
            note = pretty_midi.Note(velocity=80, pitch=38 + beat, start=time, end=time + 0.25)
            bass.notes.append(note)
        elif bar == 3:
            note = pretty_midi.Note(velocity=80, pitch=43 + beat, start=time, end=time + 0.25)
            bass.notes.append(note)
        elif bar == 4:
            note = pretty_midi.Note(velocity=80, pitch=38 + beat, start=time, end=time + 0.25)
            bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Dm7 (D, F, A, C)
# Bar 4: G7 (G, B, D, F)

# Piano
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=time, end=time + 1.5))  # F
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=time, end=time + 1.5))  # A
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=time, end=time + 1.5))  # C
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=time, end=time + 1.5))  # E
    elif bar == 3:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=time, end=time + 1.5))  # D
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=time, end=time + 1.5))  # F
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=58, start=time, end=time + 1.5))  # A
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=60, start=time, end=time + 1.5))  # C
    elif bar == 4:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=time, end=time + 1.5))  # G
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=time, end=time + 1.5))  # B
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=time, end=time + 1.5))  # D
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=time, end=time + 1.5))  # F

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G#, Bb, F (F - G# - Bb - F) in 1st bar, then repeat with a slight variation in the last bar
# Bar 2
time = 1.5
note = pretty_midi.Note(velocity=100, pitch=53, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.75, end=time + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=53, start=time + 1.125, end=time + 1.5)
sax.notes.append(note)

# Bar 3 (repeat with variation)
time = 3.0
note = pretty_midi.Note(velocity=100, pitch=53, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.75, end=time + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=53, start=time + 1.125, end=time + 1.5)
sax.notes.append(note)

# Bar 4 (variation with a slight chromatic lead into the next bar)
time = 4.5
note = pretty_midi.Note(velocity=100, pitch=53, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=57, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=51, start=time + 0.75, end=time + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=53, start=time + 1.125, end=time + 1.5)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

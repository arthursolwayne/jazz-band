
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
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 (38)
note = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + 0.375)
bass.notes.append(note)
# Chromatic approach to G2 (43)
note = pretty_midi.Note(velocity=90, pitch=42, start=1.5 + 0.375, end=1.5 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 0.75, end=1.5 + 1.125)
bass.notes.append(note)

# Bar 3: G2 (43)
note = pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
bass.notes.append(note)
# Chromatic approach to C3 (48)
note = pretty_midi.Note(velocity=90, pitch=47, start=1.5 + 1.5 + 0.375, end=1.5 + 1.5 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=48, start=1.5 + 1.5 + 0.75, end=1.5 + 1.5 + 1.125)
bass.notes.append(note)

# Bar 4: C3 (48)
note = pretty_midi.Note(velocity=90, pitch=48, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
bass.notes.append(note)
# Chromatic approach to F3 (53)
note = pretty_midi.Note(velocity=90, pitch=52, start=1.5 + 3.0 + 0.375, end=1.5 + 3.0 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=53, start=1.5 + 3.0 + 0.75, end=1.5 + 3.0 + 1.125)
bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
note = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.75)
piano.notes.append(note)

# Bar 3: Gm7 (G, Bb, D, F)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 1.5, end=1.5 + 2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5 + 1.5, end=1.5 + 2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=53, start=1.5 + 1.5, end=1.5 + 2.25)
piano.notes.append(note)

# Bar 4: C7 (C, E, G, Bb)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.0, end=1.5 + 3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5 + 3.0, end=1.5 + 3.75)
piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Start with F (65), G (67), Bb (66), then leave it hanging on Bb (66)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5 + 3.0, end=1.5 + 3.375)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

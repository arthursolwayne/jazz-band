
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

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

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
# Bar 2: F (MIDI 45) -> C (MIDI 52) -> G (MIDI 55) -> D (MIDI 57)
# Bar 3: Bb (MIDI 49) -> F (MIDI 53) -> C (MIDI 58) -> G (MIDI 60)
# Bar 4: D (MIDI 50) -> A (MIDI 55) -> E (MIDI 59) -> B (MIDI 62)

# Bass
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if bar == 2:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=45, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=52, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=55, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=57, start=time, end=time + 0.25)
                bass.notes.append(note)
        elif bar == 3:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=49, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=53, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=58, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=60, start=time, end=time + 0.25)
                bass.notes.append(note)
        elif bar == 4:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=50, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=55, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=59, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=62, start=time, end=time + 0.25)
                bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
# Bar 4: Dm7 (D, F, A, C)

# Piano
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            if bar == 2:
                note = pretty_midi.Note(velocity=100, pitch=45, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=52, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=57, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.25)
                piano.notes.append(note)
            elif bar == 3:
                note = pretty_midi.Note(velocity=100, pitch=49, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=55, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=57, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.25)
                piano.notes.append(note)
            elif bar == 4:
                note = pretty_midi.Note(velocity=100, pitch=50, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=52, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=57, start=time, end=time + 0.25)
                piano.notes.append(note)
                note = pretty_midi.Note(velocity=100, pitch=60, start=time, end=time + 0.25)
                piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Bar 2: F (MIDI 45), C (MIDI 52), G (MIDI 55)
# Bar 3: Hold high G (MIDI 55)
# Bar 4: D (MIDI 57), C (MIDI 52), F (MIDI 45)

# Sax
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if bar == 2:
            if beat == 0:
                note = pretty_midi.Note(velocity=110, pitch=45, start=time, end=time + 0.25)
                sax.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=110, pitch=52, start=time, end=time + 0.25)
                sax.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=110, pitch=55, start=time, end=time + 0.25)
                sax.notes.append(note)
        elif bar == 3:
            if beat == 0:
                note = pretty_midi.Note(velocity=110, pitch=55, start=time, end=time + 0.25)
                sax.notes.append(note)
        elif bar == 4:
            if beat == 0:
                note = pretty_midi.Note(velocity=110, pitch=57, start=time, end=time + 0.25)
                sax.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=110, pitch=52, start=time, end=time + 0.25)
                sax.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=110, pitch=45, start=time, end=time + 0.25)
                sax.notes.append(note)

# Drums continue for bars 2-4
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

midi.write("jazz_intro.mid")

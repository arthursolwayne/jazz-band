
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
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Dm7 (D, A, F, C)
# Bar 3: G7 (G, D, B, F)
# Bar 4: Cmaj7 (C, E, G, B)
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        # Dm7 root motion: D -> F -> A -> D
        bass_note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.25)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=41, start=time + 0.5, end=time + 0.75)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=45, start=time + 1.0, end=time + 1.25)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=38, start=time + 1.5, end=time + 1.75)
        bass.notes.append(bass_note)
    elif bar == 3:
        # G7 root motion: G -> Bb -> D -> G
        bass_note = pretty_midi.Note(velocity=80, pitch=43, start=time, end=time + 0.25)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=44, start=time + 0.5, end=time + 0.75)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=47, start=time + 1.0, end=time + 1.25)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=43, start=time + 1.5, end=time + 1.75)
        bass.notes.append(bass_note)
    elif bar == 4:
        # Cmaj7 root motion: C -> E -> G -> C
        bass_note = pretty_midi.Note(velocity=80, pitch=40, start=time, end=time + 0.25)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=43, start=time + 0.5, end=time + 0.75)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=45, start=time + 1.0, end=time + 1.25)
        bass.notes.append(bass_note)
        bass_note = pretty_midi.Note(velocity=80, pitch=40, start=time + 1.5, end=time + 1.75)
        bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Cmaj7 (C, E, G, B)
for bar in range(2, 5):
    time = (bar - 2) * 1.5
    if bar == 2:
        piano_note = pretty_midi.Note(velocity=80, pitch=62, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=64, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=67, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=60, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
    elif bar == 3:
        piano_note = pretty_midi.Note(velocity=80, pitch=67, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=71, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=67, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=65, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
    elif bar == 4:
        piano_note = pretty_midi.Note(velocity=80, pitch=60, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=64, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=67, start=time, end=time + 1.5)
        piano.notes.append(piano_note)
        piano_note = pretty_midi.Note(velocity=80, pitch=71, start=time, end=time + 1.5)
        piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time_beat + eighth * 0.1875, end=time_beat + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Dante: Tenor sax motif - short, singable, leave it hanging
# Motif: D (62), F (64), G (65), D (62) - start, leave it hanging
# Play the first two notes, then rest, then come back and finish

# Bar 2: First two notes of the motif
time = 1.5
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=time, end=time + 0.5)
sax.notes.append(note)

# Bar 4: Finish the motif
time = 4.5
note = pretty_midi.Note(velocity=110, pitch=65, start=time, end=time + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.5)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")

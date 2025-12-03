
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

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
bass_chords = [
    # Bar 2: Dm7 (D, F, A, C)
    [38, 41, 46, 49],  # D, F, A, C
    # Bar 3: G7 (G, B, D, F)
    [43, 47, 50, 52],  # G, B, D, F
    # Bar 4: Cmaj7 (C, E, G, B)
    [49, 53, 57, 60],  # C, E, G, B
]

# Walking bass line with chromatic approaches
for bar in range(2, 5):
    time_start = (bar - 2) * 1.5
    for beat in range(4):
        time = time_start + beat * 0.375
        if bar == 2:
            if beat == 0:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=38, start=time, end=time + 0.125))
            elif beat == 1:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=39, start=time, end=time + 0.125))
            elif beat == 2:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=40, start=time, end=time + 0.125))
            elif beat == 3:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=43, start=time, end=time + 0.125))
        elif bar == 3:
            if beat == 0:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=43, start=time, end=time + 0.125))
            elif beat == 1:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=44, start=time, end=time + 0.125))
            elif beat == 2:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=45, start=time, end=time + 0.125))
            elif beat == 3:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=47, start=time, end=time + 0.125))
        elif bar == 4:
            if beat == 0:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=47, start=time, end=time + 0.125))
            elif beat == 1:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=48, start=time, end=time + 0.125))
            elif beat == 2:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=49, start=time, end=time + 0.125))
            elif beat == 3:
                bass_notes.append(pretty_midi.Note(velocity=75, pitch=52, start=time, end=time + 0.125))

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
for bar in range(2, 5):
    time_start = (bar - 2) * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=49, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=52, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=55, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=57, start=time_start, end=time_start + 0.125))
    elif bar == 3:
        # G7: G, B, D, F
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=50, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=55, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=52, start=time_start, end=time_start + 0.125))
    elif bar == 4:
        # Cmaj7: C, E, G, B
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=48, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=51, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=55, start=time_start, end=time_start + 0.125))
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=57, start=time_start, end=time_start + 0.125))

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
bar = 2
time_start = (bar - 2) * 1.5

# Melody: D (E4), B (D5), F (F4), G (G4), rest, D (E4), B (D5), F (F4), G (G4)
notes = [62, 67, 66, 67, 62, 67, 66, 67]
durations = [0.125] * 8
for i, pitch in enumerate(notes):
    time = time_start + i * 0.125
    sax_notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + durations[i]))

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled

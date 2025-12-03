
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
for bar in range(2, 5):
    start_time = bar * 1.5
    if bar == 2:
        # Dm7 -> G7 -> Cmaj7 -> F7
        # Root: D (38), G (43), C (48), F (53)
        # Root and fifth with chromatic approach
        # Bar 2: Dm7 (D, A, F, C)
        # Start on D (38), approach from Eb (39)
        note = pretty_midi.Note(velocity=100, pitch=39, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=38, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=43, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=48, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
    elif bar == 3:
        # G7 (G, D, B, F)
        note = pretty_midi.Note(velocity=100, pitch=43, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=44, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=47, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=53, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
    elif bar == 4:
        # Cmaj7 (C, G, E, B)
        note = pretty_midi.Note(velocity=100, pitch=48, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=49, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=51, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=57, start=start_time, end=start_time + 0.25)
        bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
for bar in range(2, 5):
    start_time = bar * 1.5
    if bar == 2:
        # Dm7: D, F, A, C
        note = pretty_midi.Note(velocity=100, pitch=50, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=52, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=55, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=60, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
    elif bar == 3:
        # G7: G, B, D, F
        note = pretty_midi.Note(velocity=100, pitch=55, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=57, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=59, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=65, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
    elif bar == 4:
        # Cmaj7: C, E, G, B
        note = pretty_midi.Note(velocity=100, pitch=60, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=64, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=67, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=71, start=start_time, end=start_time + 0.25)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
for bar in range(2, 5):
    start_time = bar * 1.5
    if bar == 2:
        # D (62), F (65), G (67)
        note = pretty_midi.Note(velocity=110, pitch=62, start=start_time, end=start_time + 0.375)
        sax.notes.append(note)
        note = pretty_midi.Note(velocity=110, pitch=65, start=start_time + 0.375, end=start_time + 0.75)
        sax.notes.append(note)
        note = pretty_midi.Note(velocity=110, pitch=67, start=start_time + 0.75, end=start_time + 1.125)
        sax.notes.append(note)
    elif bar == 3:
        # G (67), A (69), D (62)
        note = pretty_midi.Note(velocity=110, pitch=67, start=start_time, end=start_time + 0.375)
        sax.notes.append(note)
        note = pretty_midi.Note(velocity=110, pitch=69, start=start_time + 0.375, end=start_time + 0.75)
        sax.notes.append(note)
        note = pretty_midi.Note(velocity=110, pitch=62, start=start_time + 0.75, end=start_time + 1.125)
        sax.notes.append(note)
    elif bar == 4:
        # D (62), F (65), G (67)
        note = pretty_midi.Note(velocity=110, pitch=62, start=start_time, end=start_time + 0.375)
        sax.notes.append(note)
        note = pretty_midi.Note(velocity=110, pitch=65, start=start_time + 0.375, end=start_time + 0.75)
        sax.notes.append(note)
        note = pretty_midi.Note(velocity=110, pitch=67, start=start_time + 0.75, end=start_time + 1.125)
        sax.notes.append(note)

# Drums: Continue for bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    for beat in range(4):
        time = start_time + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')

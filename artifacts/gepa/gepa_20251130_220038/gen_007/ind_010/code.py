
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
# Bar 2: Start of the melody, sax takes the lead
# Melody: F7, Ab7, Bb7, C7 (intervallic motif, not scale)
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        # Bass line: walking, chromatic approaches
        if bar == 2:
            if beat == 0:
                note = pretty_midi.Note(velocity=90, pitch=48, start=time, end=time + 0.375)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=90, pitch=49, start=time, end=time + 0.375)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=90, pitch=50, start=time, end=time + 0.375)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=90, pitch=51, start=time, end=time + 0.375)
                bass.notes.append(note)
        # Piano: 7th chords, comp on 2 and 4
        if bar == 2 and beat == 1:
            for pitch in [64, 67, 69, 71]:  # F7
                note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
                piano.notes.append(note)
        elif bar == 2 and beat == 3:
            for pitch in [66, 69, 71, 73]:  # Ab7
                note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
                piano.notes.append(note)
        # Sax: motif starts
        if bar == 2 and beat == 0:
            note = pretty_midi.Note(velocity=110, pitch=64, start=time, end=time + 0.375)
            sax.notes.append(note)
        elif bar == 2 and beat == 1:
            note = pretty_midi.Note(velocity=110, pitch=67, start=time, end=time + 0.375)
            sax.notes.append(note)
        elif bar == 2 and beat == 2:
            note = pretty_midi.Note(velocity=110, pitch=69, start=time, end=time + 0.375)
            sax.notes.append(note)
        elif bar == 2 and beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.375)
            sax.notes.append(note)
        # Drums continue
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 3: Piano plays Bb7, sax continues motif
for beat in range(4):
    time = 3 * 1.5 + beat * 0.375
    if beat == 1:
        for pitch in [65, 68, 70, 72]:  # Bb7
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
            piano.notes.append(note)
    elif beat == 3:
        for pitch in [67, 70, 72, 74]:  # C7
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
            piano.notes.append(note)
    # Sax continues motif
    if beat == 0:
        note = pretty_midi.Note(velocity=110, pitch=64, start=time, end=time + 0.375)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=110, pitch=67, start=time, end=time + 0.375)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=110, pitch=69, start=time, end=time + 0.375)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.375)
        sax.notes.append(note)

# Bar 4: Sax finishes motif, piano resolves
for beat in range(4):
    time = 4 * 1.5 + beat * 0.375
    if beat == 0:
        note = pretty_midi.Note(velocity=110, pitch=64, start=time, end=time + 0.375)
        sax.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(velocity=110, pitch=67, start=time, end=time + 0.375)
        sax.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(velocity=110, pitch=69, start=time, end=time + 0.375)
        sax.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.375)
        sax.notes.append(note)
    if beat == 3:
        for pitch in [64, 67, 69, 71]:  # F7 resolution
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
            piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")


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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Roots and fifths with chromatic approaches, MIDI 38-43
# Bar 2: F (38) -> G (40) -> E (41) -> C (36)
# Bar 3: A (45) -> B (47) -> G (40) -> D (43)
# Bar 4: C (36) -> D (43) -> B (47) -> G (40)
for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 2) * 1.5 + beat * 0.375
        if bar == 2:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=40, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=41, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.25)
                bass.notes.append(note)
        elif bar == 3:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=45, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=47, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=40, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=43, start=time, end=time + 0.25)
                bass.notes.append(note)
        elif bar == 4:
            if beat == 0:
                note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 1:
                note = pretty_midi.Note(velocity=80, pitch=43, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 2:
                note = pretty_midi.Note(velocity=80, pitch=47, start=time, end=time + 0.25)
                bass.notes.append(note)
            elif beat == 3:
                note = pretty_midi.Note(velocity=80, pitch=40, start=time, end=time + 0.25)
                bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: A7 (A, C#, E, G)
# Bar 4: C7 (C, E, G, B)
for bar in range(2, 5):
    for beat in range(2, 4, 2):  # comp on 2 and 4
        time = (bar - 2) * 1.5 + beat * 0.375
        if bar == 2:
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)  # F
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)  # A
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.25)  # C
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=74, start=time, end=time + 0.25)  # E
            piano.notes.append(note)
        elif bar == 3:
            note = pretty_midi.Note(velocity=90, pitch=76, start=time, end=time + 0.25)  # A
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=81, start=time, end=time + 0.25)  # C#
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=74, start=time, end=time + 0.25)  # E
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)  # G
            piano.notes.append(note)
        elif bar == 4:
            note = pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.25)  # C
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=74, start=time, end=time + 0.25)  # E
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.25)  # G
            piano.notes.append(note)
            note = pretty_midi.Note(velocity=90, pitch=77, start=time, end=time + 0.25)  # B
            piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (69) -> G (71) -> E (74) -> D (72)
# First note on bar 2, beat 1; second note on bar 2, beat 3; third note on bar 3, beat 1; final note on bar 3, beat 3
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.375 * 1, end=1.5 + 0.375 * 1 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 0.375 * 3, end=1.5 + 0.375 * 3 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=3.0 + 0.375 * 1, end=3.0 + 0.375 * 1 + 0.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.0 + 0.375 * 3, end=3.0 + 0.375 * 3 + 0.25)
sax.notes.append(note)

# Drums continue in bars 2-4
for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 2) * 1.5 + beat * 0.375
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


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
    # Kick on 1 and 3
    kick_time = bar * 1.5 + 0.0
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)
    
    kick_time = bar * 1.5 + 0.75
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

    # Snare on 2 and 4
    snare_time = bar * 1.5 + 0.375
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

    snare_time = bar * 1.5 + 0.75 * 3
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

    # Hi-hat on every eighth
    for i in range(8):
        hihat_time = bar * 1.5 + i * 0.375
        hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone: short motif, start on D (62), Bb (60), F# (66), D (62)
note_durations = [0.5, 0.5, 0.5, 0.5]
note_pitches = [62, 60, 66, 62]

for i, pitch in enumerate(note_pitches):
    start = 1.5 + i * note_durations[i]
    end = start + note_durations[i]
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bass: walking line, chromatic approaches, no repeated notes
# D - Eb - E - F - F# - G - G# - A
bass_notes = [62, 63, 64, 65, 66, 67, 68, 69]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
# G7 = G, B, D, F
# C7 = C, E, G, B
# F7 = F, A, C, E

# Bar 2 (1.5 - 3.0)
# Comp on 2 and 4 (beat 2 and 4)
# D7 on 2, G7 on 4
for i in [1, 3]:
    start = 1.5 + i * 0.375
    end = start + 0.1
    for pitch in [62, 66, 69, 60]:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
        piano.notes.append(note)

# Bar 3 (3.0 - 4.5)
# Comp on 2 and 4
# C7 on 2, F7 on 4
for i in [1, 3]:
    start = 3.0 + i * 0.375
    end = start + 0.1
    for pitch in [60, 64, 67, 69]:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
        piano.notes.append(note)

# Bar 4 (4.5 - 6.0)
# Comp on 2 and 4
# G7 on 2, D7 on 4
for i in [1, 3]:
    start = 4.5 + i * 0.375
    end = start + 0.1
    for pitch in [67, 71, 69, 65]:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
        piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    # Kick on 1 and 3
    kick_time = bar * 1.5 + 0.0
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)
    
    kick_time = bar * 1.5 + 0.75
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

    # Snare on 2 and 4
    snare_time = bar * 1.5 + 0.375
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

    snare_time = bar * 1.5 + 0.75 * 3
    snare_note = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

    # Hi-hat on every eighth
    for i in range(8):
        hihat_time = bar * 1.5 + i * 0.375
        hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")

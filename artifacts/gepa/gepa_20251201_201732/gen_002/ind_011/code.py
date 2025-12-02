
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums

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
# Bar 2 (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 50, 60),   # D2 (root)
    (1.875, 51, 60), # Eb2 (chromatic approach)
    (2.25, 52, 60),  # E2 (fifth)
    (2.625, 50, 60), # D2 (root)
]
for time, velocity, pitch in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (1.5, 100, 62), (1.5, 100, 64), (1.5, 100, 67), (1.5, 100, 69),
    # Bar 2: Bb7 (Bb, D, F, Ab)
    (2.25, 100, 60), (2.25, 100, 64), (2.25, 100, 67), (2.25, 100, 70),
    # Bar 3: G7 (G, B, D, F)
    (3.0, 100, 67), (3.0, 100, 71), (3.0, 100, 69), (3.0, 100, 67),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.75, 100, 60), (3.75, 100, 64), (3.75, 100, 67), (3.75, 100, 70),
]
for time, velocity, pitch in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - G - D (Dm melody)
sax_notes = [
    (1.5, 100, 62), (1.5, 100, 64), (1.5, 100, 67), (1.5, 100, 62),  # D - F - G - D
    (2.25, 100, 62), (2.25, 100, 64), (2.25, 100, 67), (2.25, 100, 62)  # Repeat
]
for time, velocity, pitch in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
    for beat in range(4):
        time = bar_start + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')

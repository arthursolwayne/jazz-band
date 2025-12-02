
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line (roots and fifths with chromatic approaches)
# F7, Bb7, C7, D7
bass_notes = [
    (1, 38, 0.0),    # F2 (root)
    (0, 37, 0.125),  # E2 (chromatic approach)
    (2, 43, 0.25),   # C3 (fifth of F7)
    (3, 41, 0.375),  # A2 (chromatic approach)
    (4, 40, 0.5),    # Bb2 (root of Bb7)
    (3, 39, 0.625),  # A2 (chromatic approach)
    (6, 44, 0.75),   # D3 (fifth of Bb7)
    (5, 42, 0.875),  # C3 (chromatic approach)
    (7, 42, 1.0),    # C3 (root of C7)
    (6, 41, 1.125),  # B2 (chromatic approach)
    (9, 46, 1.25),   # E3 (fifth of C7)
    (8, 44, 1.375),  # D3 (chromatic approach)
    (10, 44, 1.5),   # D3 (root of D7)
    (9, 43, 1.625),  # C3 (chromatic approach)
    (12, 47, 1.75),  # F3 (fifth of D7)
    (11, 45, 1.875)  # E3 (chromatic approach)
]
for note in bass_notes:
    time = note[2] + 1.5
    n = pretty_midi.Note(velocity=100, pitch=note[1], start=time, end=time + 0.1)
    bass.notes.append(n)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: F7 (F, A, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: C7 (C, E, G, Bb)
# Bar 5: D7 (D, F#, A, C)
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (1, 65, 1.5), (1, 74, 1.5), (1, 76, 1.5), (1, 71, 1.5),  # F7
    # Bar 3 (2.0 - 2.5s)
    (1, 62, 2.0), (1, 67, 2.0), (1, 65, 2.0), (1, 68, 2.0),  # Bb7
    # Bar 4 (2.5 - 3.0s)
    (1, 60, 2.5), (1, 64, 2.5), (1, 67, 2.5), (1, 62, 2.5),  # C7
    # Bar 5 (3.0 - 3.5s)
    (1, 62, 3.0), (1, 67, 3.0), (1, 69, 3.0), (1, 60, 3.0),  # D7
    # Bar 6 (3.5 - 4.0s)
    # Bar 7 (4.0 - 4.5s)
    # Bar 8 (4.5 - 5.0s)
    # Bar 9 (5.0 - 5.5s)
    # Bar 10 (5.5 - 6.0s)
]
for note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note[1], start=note[2], end=note[2] + 0.1)
    piano.notes.append(n)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, F (melodic idea)
sax_notes = [
    (1, 76, 1.5),  # F
    (1, 69, 1.75), # Bb
    (1, 72, 2.0),  # C
    (1, 76, 2.5),  # F
    (1, 72, 2.75), # C
    (1, 69, 3.0),  # Bb
    (1, 76, 3.5),  # F
    (1, 76, 4.0)   # F
]
for note in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note[1], start=note[2], end=note[2] + 0.1)
    sax.notes.append(n)

# Drums for Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')

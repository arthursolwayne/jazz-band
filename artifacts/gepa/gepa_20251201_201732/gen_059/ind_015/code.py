
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
bar_length = 1.5
for note_time in [0.0, 0.75, 1.5]:  # Kick on 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=note_time, end=note_time + 0.1)
    drums.notes.append(note)
for note_time in [0.375, 1.125]:  # Snare on 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=note_time, end=note_time + 0.1)
    drums.notes.append(note)
for note_time in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:  # Hihat on every eighth
    note = pretty_midi.Note(velocity=100, pitch=42, start=note_time, end=note_time + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5),   # D2
    (40, 1.875), # F2
    (38, 2.25),  # D2
    (41, 2.625), # G2
    (43, 2.875), # Bb2 (chromatic approach)
    (41, 3.25),  # G2
    (38, 3.625), # D2
    (40, 4.0),   # F2
    (38, 4.375), # D2
    (41, 4.75),  # G2
    (43, 5.0),   # Bb2 (chromatic approach)
    (41, 5.375), # G2
    (38, 5.75),  # D2
]
for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Chords: Dm7 (bar 2), G7 (bar 3), Cm7 (bar 4)
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
chords = [
    [50, 53, 57, 60],  # Dm7 (D, F, A, C)
    [67, 71, 69, 65],  # G7 (G, B, D, F)
    [60, 63, 67, 71],  # Cm7 (C, Eb, G, Bb)
]
for bar_idx, chord in enumerate(chords):
    start = 1.5 + bar_idx * 1.5
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 1.5)
        piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (D4), F (F4), Bb (Bb4), D (D4)
sax_notes = [
    (62, 1.5),     # D4
    (65, 1.625),   # F4
    (69, 1.75),    # Bb4
    (62, 2.0),     # D4
    (69, 3.0),     # Bb4
    (65, 3.125),   # F4
    (62, 3.25)     # D4
]
for pitch, start in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
